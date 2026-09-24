# Pilot snapshot 2026-09-24

An exploratory measurement made with shell commands and `git` before measurement model v1 was settled. It did not pass the sample integrity gate, so **its results are not used as evidence for any practice or principle.** It serves only as input for refining measurement model v1.

Translated into English by [decision 0005](../../decisions/0005-english-only.md); the content and the data files are unchanged.

## Conditions

- Panel: the 26 repositories in `panel.txt`, chosen by name before gate 1 (quality).
- Reference dates: 2026-09-24 and 2025-09-24 (retroactive). The commit measured at each date is in `heads.tsv`.
- Observation window: the 365 days before each reference date.
- Commit counts: with `--no-merges`.
- Role detection: find files by naming rules, then follow symlinks and one-line `@file` pointers and measure the single canonical file.

## `records.tsv` columns

| # | Column | Meaning |
|---|---|---|
| 1 | as_of | Reference date |
| 2 | repo | Repository |
| 3 | role | intro · arch · agent · contrib |
| 4 | path | File found for the role |
| 5 | canonical | Canonical file after following aliases |
| 6 | lines | Line count of the canonical file |
| 7 | doc_commits | Commits that changed the canonical file in the window |
| 8 | repo_commits | All commits in the repository in the window |
| 9 | lines_added | Lines added in the window |
| 10 | lines_deleted | Lines deleted in the window |
| 11 | code_lines | Lines inside code blocks |
| 12 | command_lines | Lines inside code blocks that start with a command |
| 13 | numeric_tokens | Version or number-with-unit tokens outside code blocks |
| 14 | headings | Heading lines |
| 15 | links | Markdown links |
| 16 | backtick_refs | Path-like tokens inside backticks (uncorrected) |
| 17 | backtick_refs_valid | Of those, tokens present in the tree at the reference date (uncorrected) |

`repo-references-2026.tsv` holds corrected values for columns 16 and 17: only tokens whose first path segment exists at the repository root count as repository references.

## Known defects

- Command detection looks only inside code blocks and misses commands in inline backticks.
- Columns 16 and 17 count runtime paths and example file names as references.
- Role detection depends on file naming rules and misses structure descriptions under `docs/` with other names.
