#!/usr/bin/env python3
"""Fixture tests for docs_checks.py and the style Abstract (DESIGN.md §13).

Each test makes a small git repository with the configuration of this repository,
commits a base, makes one change and runs one check. VALE is the path of the Vale binary.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True, check=True).stdout.strip()
SCRIPT = os.path.join(ROOT, ".github", "scripts", "docs_checks.py")
VALE = os.path.abspath(os.environ.get("VALE") or shutil.which("vale") or os.path.join(ROOT, "vale"))
HASH = "0" * 64

GUIDE = """# Guide

## 1. Steps

1. **First step.** Open a change request.
   Done when: it exists.
2. **Second step.** Run the check.
   Done when: it passes.

| Step | Basis |
|---|---|
| 1 | none |
"""


def note(status="raw", into="[]", archive="~/archive/", body="I did it.\n",
         written="2026-09-25", cutoff="2026-06"):
    return f"""---
author: agent-x
date: 2026-09-25
repository: example
status: {status}
normalized-into: {into}
written-at: {written}
model: model-x
knowledge-cutoff: {cutoff}
session:
  tool: agent CLI
  id: session-1
  archive: {archive}
  sha256: {HASH}
---

# Note

{body}"""


class Fixture(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        for f in [".vale.ini", "GLOSSARY.md"]:
            shutil.copy(os.path.join(ROOT, f), self.dir)
        shutil.copytree(os.path.join(ROOT, ".github", "styles"), os.path.join(self.dir, ".github", "styles"))
        self.git("init", "-q", "-b", "main")
        self.write("guides/guide.md", GUIDE)
        self.write("notes/n.md", note())
        self.commit("base")

    def tearDown(self):
        shutil.rmtree(self.dir)

    def git(self, *args):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args],
                       cwd=self.dir, check=True, capture_output=True)

    def write(self, path, text):
        full = os.path.join(self.dir, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(text)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def run_check(self, check):
        r = subprocess.run([sys.executable, SCRIPT, check, "--base", "main"],
                           cwd=self.dir, capture_output=True, text=True)
        return r.returncode, r.stdout

    def change(self, path, text):
        self.git("checkout", "-q", "-b", "change")
        self.write(path, text)
        self.commit("change")

    def assertFails(self, check, expect):
        code, out = self.run_check(check)
        self.assertEqual(code, 1, out)
        self.assertIn(expect, out)

    def assertPasses(self, check):
        code, out = self.run_check(check)
        self.assertEqual(code, 0, out)

    # Baseline
    def test_base_passes(self):
        for c in ["structure", "abstraction", "notes", "cutoff"]:
            self.assertPasses(c)

    # Abstraction
    @unittest.skipUnless(os.path.exists(VALE), "Vale is not available")
    def test_first_person_in_original(self):
        self.write("guides/guide.md", GUIDE + "\nWe run the check.\n")
        r = subprocess.run([VALE, "--no-wrap", "--output=line", "guides/guide.md"],
                           cwd=self.dir, capture_output=True, text=True)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("Abstract.FirstPerson", r.stdout)

    @unittest.skipUnless(os.path.exists(VALE), "Vale is not available")
    def test_first_person_allowed_in_note(self):
        r = subprocess.run([VALE, "--no-wrap", "--output=line", "notes/n.md"],
                           cwd=self.dir, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_first_person_in_translation(self):
        self.change("guides/guide.ko.md", "# \uc548\ub0b4\n\n\uc6b0\ub9ac\ub294 \uac80\uc0ac\ub97c \ud569\ub2c8\ub2e4.\n")
        self.assertFails("abstraction", "first person")

    def test_personal_path(self):
        self.change("guides/guide.md", GUIDE + "\n```\ncd /home/x/repo\n```\n")
        self.assertFails("abstraction", "personal path")

    def test_concrete_term_in_step(self):
        self.change("guides/guide.md", GUIDE.replace("Run the check.", "Open a merge request."))
        self.assertFails("abstraction", "concrete term 'merge request'")

    def test_concrete_term_with_citation_passes(self):
        self.change("guides/guide.md", GUIDE + "\nGitHub shows Mermaid text as a picture [28].\n")
        self.assertPasses("abstraction")

    def test_concrete_term_in_note_passes(self):
        self.change("notes/n2.md", note(body="I opened a merge request on GitLab from /home/x/repo.\n"))
        self.assertPasses("abstraction")

    def test_deabstraction(self):
        self.change("guides/guide.md", GUIDE.replace("Open a change request.", "Open a pull request [34]."))
        self.assertFails("abstraction", "replaces 'change request' with 'pull request'")

    # Structure
    def test_heading_rename(self):
        self.change("guides/guide.md", GUIDE.replace("## 1. Steps", "## 1. Procedure"))
        self.assertFails("structure", "heading:guides/guide.md#1-steps")

    def test_step_renumber(self):
        text = GUIDE.replace("1. **First step.**", "1. **New step.** Do this.\n   Done when: done.\n2. **First step.**")
        text = text.replace("2. **Second step.**", "3. **Second step.**")
        self.change("guides/guide.md", text)
        self.assertFails("structure", "step:guides/guide.md#1-steps:1")

    def test_column_rename(self):
        self.change("guides/guide.md", GUIDE.replace("| Step | Basis |", "| Step | Source |"))
        self.assertFails("structure", "column:guides/guide.md#1-steps:Basis")

    def test_file_removal(self):
        self.git("checkout", "-q", "-b", "change")
        self.git("rm", "-q", "guides/guide.md")
        self.commit("remove")
        self.assertFails("structure", "file:guides/guide.md")

    def test_marker_in_new_decision_allows_change(self):
        self.git("checkout", "-q", "-b", "change")
        self.write("guides/guide.md", GUIDE.replace("## 1. Steps", "## 1. Procedure"))
        self.write("decisions/0001-rename.md", "# 1. Rename\n\n<!-- structure-change: heading:guides/guide.md#1-steps -->\n")
        self.commit("change")
        self.assertPasses("structure")

    def test_append_passes(self):
        self.change("guides/guide.md", GUIDE + "\n## 2. More\n\n1. **Other.** Text.\n   Done when: done.\n")
        self.assertPasses("structure")

    # Notes
    def test_normalized_note_with_missing_target(self):
        self.change("notes/n2.md", note("normalized", "[guides/guide.md#no-such-heading]"))
        self.assertFails("notes", "has no such heading")

    def test_normalized_note_with_target_passes(self):
        self.change("notes/n2.md", note("normalized", "[guides/guide.md#1-steps]"))
        self.assertPasses("notes")

    def test_note_body_change(self):
        self.change("notes/n.md", note(body="I did something else.\n"))
        self.assertFails("notes", "Only status and normalized-into can change")

    def test_note_status_change_passes(self):
        self.change("notes/n.md", note("normalized", "[guides/guide.md#1-steps]"))
        self.assertPasses("notes")

    def test_note_archive_in_repository(self):
        self.change("notes/n2.md", note(archive="notes/sessions/"))
        self.assertFails("notes", "session.archive is a relative path")

    def test_note_bad_hash(self):
        self.change("notes/n2.md", note().replace(HASH, "abc"))
        self.assertFails("notes", "session.sha256")

    def test_note_cutoff_after_writing(self):
        self.change("notes/n2.md", note(cutoff="2027-01"))
        self.assertFails("notes", "knowledge-cutoff is after written-at")

    def test_note_bad_written_at(self):
        self.change("notes/n2.md", note(written="yesterday"))
        self.assertFails("notes", "written-at is an ISO date")

    # Cutoff
    def test_latest_without_date(self):
        self.change("guides/guide.md", GUIDE + "\nThe latest release of the tool supports this.\n")
        self.assertFails("cutoff", "time-sensitive 'latest'")

    def test_version_without_date(self):
        self.change("guides/guide.md", GUIDE + "\nUse the tool 3.22 for this.\n")
        self.assertFails("cutoff", "time-sensitive '3.22'")

    def test_year_without_date(self):
        self.change("guides/guide.md", GUIDE + "\nIn 2025 most tools changed.\n")
        self.assertFails("cutoff", "time-sensitive '2025'")

    def test_korean_word_in_translation(self):
        self.change("guides/guide.ko.md", "# \uc548\ub0b4\n\n\ud604\uc7ac \ub3c4\uad6c\ub97c \uc501\ub2c8\ub2e4.\n")
        self.assertFails("cutoff", "time-sensitive")

    def test_dated_claim_passes(self):
        self.change("guides/guide.md", GUIDE + "\nAs of 2026-09-25, the latest release is 3.22.\n")
        self.assertPasses("cutoff")

    def test_cited_claim_passes(self):
        self.change("guides/guide.md", GUIDE + "\nThe latest release is 3.22 [29].\n")
        self.assertPasses("cutoff")

    def test_note_is_not_checked(self):
        self.change("notes/n2.md", note(body="I used the latest release, 3.22, in 2026.\n"))
        self.assertPasses("cutoff")


if __name__ == "__main__":
    unittest.main(verbosity=2)
