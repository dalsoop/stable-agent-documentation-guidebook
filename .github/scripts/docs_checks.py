#!/usr/bin/env python3
"""Checks of DESIGN.md §13 (decisions/0009). Python standard library and git only.

  docs_checks.py structure   [--base REV] [--head REV]
  docs_checks.py abstraction [--base REV] [--head REV]
  docs_checks.py notes       [--base REV] [--head REV]
  docs_checks.py cutoff      [--head REV]

--base: the change is compared with the merge base of REV and the head.
        Without --base, abstraction checks only the tree, and structure does nothing.
--head: a commit. Without it, the head is the working tree of the tracked files.
"""
import argparse
import os
import re
import subprocess
import sys

GLOSSARY = "GLOSSARY.md"
VALE_INI = ".vale.ini"
MARKER = re.compile(r"<!--\s*structure-change:\s*(\S+)\s*-->")
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
STEP = re.compile(r"^(\d+)\.\s+(.*)$")
BOLD = re.compile(r"^\*\*(.+?)\*\*")
REF = re.compile(r"^\*\*\[(\d+)\]\*\*")
CLAUSE_ID = re.compile(r"^id:\s*(\S+)", re.M)
CITATION = re.compile(r"\[\d+\]")
URL = re.compile(r"https?://\S+")
PATHS = [
    (re.compile(r"/home/[^/\s`]+/"), "/home/<user>/"),
    (re.compile(r"/Users/[^/\s`]+/"), "/Users/<user>/"),
    (re.compile(r"[A-Za-z]:\\+Users\\+"), "C:\\Users\\"),
]
# First person in Korean: uri, jeohui, na-neun, na-ui, na-reul, na-ege, nae-ga, jeo-neun, je-ga, jeo-ui.
KO_FIRST_PERSON = re.compile(
    r"(?<![\uac00-\ud7a3])(\uc6b0\ub9ac|\uc800\ud76c|\ub098\ub294|\ub098\uc758|\ub098\ub97c|\ub098\uc5d0\uac8c|\ub0b4\uac00|\uc800\ub294|\uc81c\uac00|\uc800\uc758)(?![\uac00-\ud7a3])"
    r"|(?<![\uac00-\ud7a3])(\uc6b0\ub9ac|\uc800\ud76c)(?=[\uac00-\ud7a3])")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True,
                          text=True).stdout


class Tree:
    """The Markdown files of one commit, or of the working tree when rev is None."""

    def __init__(self, rev):
        self.rev = rev
        if rev:
            names = git("ls-tree", "-r", "--name-only", rev).split("\n")
        else:
            names = git("ls-files").split("\n")
        self.files = [n for n in names if n]

    def read(self, path):
        if self.rev:
            return git("show", f"{self.rev}:{path}")
        with open(path, encoding="utf-8") as f:
            return f.read()

    def markdown(self):
        return [f for f in self.files if f.endswith(".md")]


def glob_regex(pattern):
    out, i = "", 0
    while i < len(pattern):
        c = pattern[i]
        if pattern.startswith("**", i):
            out, i = out + ".*", i + 2
            continue
        out += {"*": "[^/]*", "?": "[^/]", "{": "(", "}": ")", ",": "|"}.get(c, re.escape(c))
        i += 1
    return re.compile(out + r"\Z")


def abstract_scope(tree):
    """The files of the sections of .vale.ini that use the style Abstract, and their translations."""
    globs, current = [], None
    for line in tree.read(VALE_INI).splitlines():
        m = re.match(r"^\[(.+)\]\s*$", line)
        if m:
            current = m.group(1)
        elif current and re.match(r"^BasedOnStyles\s*=.*\bAbstract\b", line):
            globs.append(glob_regex(current))
    def in_scope(path):
        original = re.sub(r"\.ko\.md$", ".md", path)
        return any(g.match(original) for g in globs)
    return [f for f in tree.markdown() if in_scope(f)]


def concrete_terms(tree):
    """(pattern, concrete term, abstract term) from the table 'Concrete terms' in GLOSSARY.md."""
    terms, in_table = [], False
    for line in tree.read(GLOSSARY).splitlines():
        h = HEADING.match(line)
        if h:
            in_table = h.group(2).strip() == "Concrete terms"
            continue
        if not in_table or not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0] == "Concrete term":
            continue
        concrete, abstract = cells[0], cells[1]
        if concrete.startswith("`"):
            pattern = re.compile(re.escape(concrete))
        else:
            flags = 0 if re.search(r"[A-Z]", concrete) else re.I
            pattern = re.compile(r"(?<![\w/])" + re.escape(concrete) + r"(e?s)?(?![\w/])", flags)
        terms.append((pattern, concrete, abstract))
    if not terms:
        sys.exit(f"{GLOSSARY}: no table under the heading 'Concrete terms'")
    return terms


def prose_lines(text):
    """(line number, line, in a fenced code block) for each line."""
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            fenced = not fenced
            yield n, line, True
            continue
        yield n, line, fenced


def sentences(line):
    return re.split(r"(?<=[.!?])\s+", line)


def check_tree(tree, scope, terms):
    errors = []
    for path in scope:
        for n, line, fenced in prose_lines(tree.read(path)):
            for pattern, shown in PATHS:
                if pattern.search(line):
                    errors.append(f"{path}:{n}: personal path {shown}. Use a placeholder such as <path>.")
            if path.endswith(".ko.md") and not fenced:
                m = KO_FIRST_PERSON.search(line)
                if m:
                    errors.append(f"{path}:{n}: first person '{m.group(0)}'. Name the repository, the reader or a role.")
            if fenced:
                continue
            for sentence in sentences(URL.sub("", line)):
                if CITATION.search(sentence):
                    continue  # The sentence reports a fact of a cited source.
                for pattern, concrete, abstract in terms:
                    if pattern.search(sentence):
                        errors.append(f"{path}:{n}: concrete term '{concrete}'. Use the abstract term '{abstract}' (GLOSSARY.md).")
    return errors


def check_deabstraction(base, head, scope, terms):
    """Fail when a hunk removes an abstract term and adds its concrete term."""
    errors = []
    args = ["diff", "-U0", "--no-color", base] + ([head.rev] if head.rev else []) + ["--"] + scope
    path, removed, added, start = None, [], [], 0

    def flush():
        for pattern, concrete, abstract in terms:
            a = re.compile(r"\b" + re.escape(abstract) + r"s?\b", re.I)
            count = lambda p, lines: sum(len(p.findall(l)) for l in lines)
            if (count(a, removed) > count(a, added)
                    and count(pattern, added) > count(pattern, removed)):
                errors.append(f"{path}:{start}: the change replaces '{abstract}' with '{concrete}'. Keep the abstract term.")

    for line in git(*args).splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else line[4:]
        elif line.startswith("@@"):
            if path:
                flush()
            removed, added = [], []
            start = int(re.search(r"\+(\d+)", line).group(1))
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:])
        elif line.startswith("+"):
            added.append(line[1:])
    if path:
        flush()
    return errors


def anchor(text):
    text = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return text.replace(" ", "-")


def structure(text):
    """Headings, numbered steps and table columns of one Markdown file."""
    headings, steps, columns = [], {}, {}
    section, seen, prev = "", {}, None
    for _, line, fenced in prose_lines(text):
        if fenced:
            prev = None
            continue
        h = HEADING.match(line)
        if h:
            a = anchor(h.group(2))
            k = seen.get(a, 0)
            seen[a] = k + 1
            section = a if k == 0 else f"{a}-{k}"
            headings.append(section)
        s = STEP.match(line)
        if s:
            b = BOLD.match(s.group(2))
            steps.setdefault(section, []).append((int(s.group(1)), (b.group(1) if b else s.group(2)).strip()))
        if re.match(r"^\|?\s*:?-{3,}", line) and prev and prev.startswith("|"):
            columns.setdefault(section, set()).update(c.strip() for c in prev.strip().strip("|").split("|"))
        prev = line
    return headings, steps, columns


def check_structure(base, head):
    items = []
    head_files = set(head.markdown())
    for path in base.markdown():
        if path not in head_files:
            items.append(f"file:{path}")
            continue
        old, new = base.read(path), head.read(path)
        oh, osteps, ocols = structure(old)
        nh, nsteps, ncols = structure(new)
        for a in oh:
            if a not in nh:
                items.append(f"heading:{path}#{a}")
        for section, ss in osteps.items():
            if section not in nh and section:
                continue  # The heading item covers it.
            now = nsteps.get(section, [])
            numbers = {num for num, _ in now}
            by_key = {key: num for num, key in now}
            for num, key in ss:
                if num not in numbers or by_key.get(key, num) != num:
                    items.append(f"step:{path}#{section}:{num}")
        for section, cols in ocols.items():
            for c in sorted(cols - ncols.get(section, set())):
                if section in nh or not section:
                    items.append(f"column:{path}#{section}:{c}")
        m_old, m_new = CLAUSE_ID.search(old), CLAUSE_ID.search(new)
        if path.startswith(("principles/", "practices/")) and m_old and (not m_new or m_new.group(1) != m_old.group(1)):
            items.append(f"id:{m_old.group(1)}")
        if path == "REFERENCES.md":
            refs = lambda t: {m.group(1) for l in t.splitlines() for m in [REF.match(l)] if m}
            for r in sorted(refs(old) - refs(new), key=int):
                items.append(f"ref:[{r}]")
    # A decision record that the change adds can name the items.
    waived = set()
    for path in head.markdown():
        if path.startswith("decisions/") and path not in base.files:
            waived.update(MARKER.findall(head.read(path)))
    items = list(dict.fromkeys(items))
    return [f"{i}: a published item changed. Keep it, or add a decision record with <!-- structure-change: {i} --> (DESIGN.md §13)."
            for i in items if i not in waived]


NOTE_FIELDS = ["author", "date", "repository", "status", "normalized-into",
               "written-at", "model", "knowledge-cutoff",
               "session.tool", "session.id", "session.archive", "session.sha256"]
NOTE_CHANGEABLE = {"status", "normalized-into"}


def front_matter(text):
    """(fields, body) of a file that starts with a YAML front matter of simple keys."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return None, text
    fields, parent = {}, None
    for line in m.group(1).splitlines():
        k = re.match(r"^(\s*)([\w-]+):\s*(.*?)\s*(\s#.*)?$", line)
        if not k:
            continue
        if k.group(1) and parent:
            fields[f"{parent}.{k.group(2)}"] = k.group(3)
        else:
            parent = k.group(2) if not k.group(3) else None
            fields[k.group(2)] = k.group(3)
    return fields, m.group(2)


def archive_errors(path, archive):
    """The archive is private storage: not a path in this repository, not a URL of it.
    The check cannot verify the private storage itself."""
    a = archive.strip("\"'")
    if not a:
        return [f"{path}: session.archive is empty."]
    if re.match(r"^[a-z][a-z0-9+.-]*://", a, re.I) or re.match(r"^[\w.-]+@[\w.-]+:", a):
        remotes = [u.strip() for u in git("remote", "-v").split() if "/" in u or ":" in u]
        norm = lambda u: re.sub(r"(\.git)?/*$", "", re.sub(r"^\w+://|^[\w.-]+@", "", u)).replace(":", "/").lower()
        if any(norm(r) and norm(a).startswith(norm(r)) for r in remotes):
            return [f"{path}: session.archive is in this repository. Keep transcripts in private storage."]
        return []
    if not a.startswith(("~", "/")):
        return [f"{path}: session.archive is a relative path, so it is in this repository. Keep transcripts in private storage."]
    root = git("rev-parse", "--show-toplevel").strip()
    full = os.path.realpath(os.path.expanduser(a))
    if full == root or full.startswith(root + os.sep):
        return [f"{path}: session.archive is in this repository. Keep transcripts in private storage."]
    return []


def check_notes(base, head):
    """Notes (DESIGN.md §2): front matter, targets of normalized notes, and append-only bodies."""
    errors = []
    notes = [f for f in head.markdown() if f.startswith("notes/") and f != "notes/README.md"]
    for path in notes:
        fields, body = front_matter(head.read(path))
        if fields is None:
            errors.append(f"{path}: a note starts with a front matter ({', '.join(NOTE_FIELDS)}).")
            continue
        for k in NOTE_FIELDS:
            if k not in fields or (k != "normalized-into" and not fields[k]):
                errors.append(f"{path}: the front matter has no value for '{k}'.")
        if not re.fullmatch(r"[0-9a-f]{64}", fields.get("session.sha256", "")):
            errors.append(f"{path}: session.sha256 is 64 lowercase hexadecimal characters.")
        if "session.archive" in fields:
            errors += archive_errors(path, fields["session.archive"])
        written = fields.get("written-at", "")
        cutoff = fields.get("knowledge-cutoff", "")
        if written and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", written):
            errors.append(f"{path}: written-at is an ISO date, YYYY-MM-DD.")
        if cutoff and not re.fullmatch(r"unknown|\d{4}-\d{2}(-\d{2})?", cutoff):
            errors.append(f"{path}: knowledge-cutoff is YYYY-MM, YYYY-MM-DD or unknown.")
        elif cutoff not in ("", "unknown") and written and cutoff > written:
            errors.append(f"{path}: knowledge-cutoff is after written-at.")
        status = fields.get("status")
        if status not in ("raw", "normalized"):
            errors.append(f"{path}: status is raw or normalized, not '{status}'.")
        targets = re.findall(r"[^\s\[\],]+", fields.get("normalized-into", "") or "")
        targets = [t for t in targets if t != "null"]
        if status == "normalized" and not targets:
            errors.append(f"{path}: a normalized note gives each target in normalized-into.")
        for t in targets:
            target, _, a = t.partition("#")
            if target not in head.files:
                errors.append(f"{path}: normalized-into target {target} does not exist.")
            elif a and a not in structure(head.read(target))[0]:
                errors.append(f"{path}: normalized-into target {t} has no such heading.")
        if base and path in base.files:
            old_fields, old_body = front_matter(base.read(path))
            if old_body != body or {k: v for k, v in (old_fields or {}).items() if k not in NOTE_CHANGEABLE} != \
                    {k: v for k, v in fields.items() if k not in NOTE_CHANGEABLE}:
                errors.append(f"{path}: a note is a record. Only status and normalized-into can change. Write a new note.")
    if base:
        for path in base.markdown():
            if path.startswith("notes/") and path not in head.files:
                errors.append(f"{path}: a note is a record and stays.")
    return errors


DATED = re.compile(r"\b\d{4}-\d{2}(-\d{2})?\b")
VERSION = re.compile(r"(?<![\w.\u00a7])v?\d+\.\d+(\.\d+)*(?![\w%])(?!\.\d)")
YEAR = re.compile(r"(?<![\w-])(19|20)\d{2}(?![\w-])")
LINK_TARGET = re.compile(r"\]\([^)]*\)")
CODE_SPAN = re.compile(r"`[^`]*`")
FILE_NAME = re.compile(r"[\w./-]+\.md\b")


KO_TIME_WORDS = ["\ucd5c\uc2e0", "\ud604\uc7ac", "\uc9c0\uae08\uc740", "\uc694\uc998", "\ucd5c\uadfc", "\ub354 \uc774\uc0c1", "\ud3d0\uae30"]


def time_words(tree):
    """Patterns from the table 'Time-sensitive words' in GLOSSARY.md."""
    words, in_table = [], False
    for line in tree.read(GLOSSARY).splitlines():
        h = HEADING.match(line)
        if h:
            in_table = h.group(2).strip() == "Time-sensitive words"
            continue
        if not in_table or not line.startswith("|") or "---" in line:
            continue
        word = line.strip("|").split("|")[0].strip()
        if not word or word == "Word":
            continue
        if re.search(r"[\uac00-\ud7a3]", word):
            words.append((re.compile(re.escape(word)), word))
        else:
            words.append((re.compile(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", re.I), word))
    if not words:
        sys.exit(f"{GLOSSARY}: no table under the heading 'Time-sensitive words'")
    # Korean: choesin, hyeonjae, jigeumeun, yojeum, choegeun, deo isang, pyegi.
    # They are here because an original contains no Hangul (DESIGN.md \u00a711).
    for w in KO_TIME_WORDS:
        words.append((re.compile(re.escape(w)), w))
    return words


def check_cutoff(tree, scope):
    """A time-sensitive sentence in a published layer has a date or cites a reference."""
    errors, words = [], time_words(tree)
    for path in scope:
        text = tree.read(path)
        fields, _ = front_matter(text)
        skip = len(re.match(r"^---\n.*?\n---\n", text, re.S).group(0).splitlines()) if fields else 0
        for n, line, fenced in prose_lines(text):
            if fenced or n <= skip or line.startswith("<!--"):
                continue
            clean = FILE_NAME.sub("", CODE_SPAN.sub("", LINK_TARGET.sub("]", URL.sub("", line))))
            for sentence in (p for part in clean.split("|") for p in sentences(part)):
                if CITATION.search(sentence) or DATED.search(sentence):
                    continue
                found = [w for pat, w in words if pat.search(sentence)]
                m = VERSION.search(sentence) or YEAR.search(sentence)
                if m:
                    found.append(m.group(0))
                if found:
                    errors.append(f"{path}:{n}: time-sensitive '{found[0]}' with no date. Add 'as of YYYY-MM-DD' or cite a reference [n] (DESIGN.md §13).")
    return errors


def main():
    p = argparse.ArgumentParser()
    p.add_argument("check", choices=["structure", "abstraction", "notes", "cutoff"])
    p.add_argument("--base")
    p.add_argument("--head")
    o = p.parse_args()
    head = Tree(o.head)
    base = None
    if o.base:
        base_rev = git("merge-base", o.base, o.head or "HEAD").strip()
        base = Tree(base_rev)
    if o.check == "structure":
        errors = check_structure(base, head) if base else []
    elif o.check == "cutoff":
        errors = check_cutoff(head, abstract_scope(head))
    elif o.check == "notes":
        errors = check_notes(base, head)
    else:
        scope, terms = abstract_scope(head), concrete_terms(head)
        errors = check_tree(head, scope, terms)
        if base:
            errors += check_deabstraction(base.rev, head, scope, terms)
    for e in errors:
        print(e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
