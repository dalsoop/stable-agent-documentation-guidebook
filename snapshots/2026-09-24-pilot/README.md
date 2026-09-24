# Pilot snapshot 2026-09-24

This is an exploratory measurement with shell commands and `git`. It was done before measurement model v1 was final. It did not go through the gate for sample integrity. Thus **no practice or principle uses its results as evidence.** It is only an input to improve measurement model v1.

[Decision 0005](../../decisions/0005-style-guide-per-language.md) changed its language. The content and the data files did not change.

## Conditions

- Panel: the 26 repositories in `panel.txt`. A person selected them by name before gate 1 (quality).
- Reference dates: 2026-09-24 and 2025-09-24 (retroactive). `heads.tsv` gives the commit at each date.
- Observation window: the 365 days before each reference date.
- Commit counts: with `--no-merges`.
- Role detection: find files by their name rules. Then follow symlinks and one-line `@file` pointers, and measure the one canonical file.

## Columns of `records.tsv`

| # | Column | Meaning |
|---|---|---|
| 1 | as_of | Reference date |
| 2 | repo | Repository |
| 3 | role | intro · arch · agent · contrib |
| 4 | path | File that the role detection found |
| 5 | canonical | Canonical file after the aliases |
| 6 | lines | Number of lines in the canonical file |
| 7 | doc_commits | Commits that changed the canonical file in the window |
| 8 | repo_commits | All commits of the repository in the window |
| 9 | lines_added | Lines added in the window |
| 10 | lines_deleted | Lines deleted in the window |
| 11 | code_lines | Lines in code blocks |
| 12 | command_lines | Lines in code blocks that start with a command |
| 13 | numeric_tokens | Tokens outside code blocks that are versions or numbers with units |
| 14 | headings | Heading lines |
| 15 | links | Markdown links |
| 16 | backtick_refs | Tokens in backticks that look like paths (not corrected) |
| 17 | backtick_refs_valid | Tokens from column 16 that exist in the tree at the reference date (not corrected) |

`repo-references-2026.tsv` contains corrected values for columns 16 and 17. A token counts as a repository reference only if its first path segment exists at the repository root.

## Known defects

- The command detection examines only code blocks. It does not find commands in inline backticks.
- Columns 16 and 17 count runtime paths and names of example files as references.
- The role detection uses file name rules. It does not find structure descriptions with other names under `docs/`.
