# Case: a Swift monorepo (2026-09)

A record of applying [new-project.md](new-project.md) to one existing repository. The repository is private, so its name and the names of its internal tools are replaced with generic ones. How a case may be used is set by the guide layer rules in [DESIGN.md](../DESIGN.md) §2.

## Repository

A Swift monorepo holding several apps and shared packages, edited by several AI agents at once. A root CLI (`./repo`) builds, tests, checks structure (`doctor`) and lints code (`lint`).

## Before

- Every feature change appended sentences to the README, ARCHITECTURE and the instruction file. The same content sat in three documents, and no document described the folder layout.
- Besides the root, each app had its own instruction file repeating the same conventions.
- Instructions had no reasons, so no one could tell which rules were safe to delete.

## What was applied

| Step | Clause or source | Change | Mechanical check |
|---|---|---|---|
| Instruction file | R-001, R-002 | One root file with four rules, each ending in "(Reason: ...)"; 17 lines. The file cites R-001 and R-002 as the source of its writing rules | `doctor` fails when an instruction file appears outside the root |
| Per-app instruction files | R-002 | Deleted six app-level instruction files; app usage moved to each app's README | Same as above |
| ARCHITECTURE | [22] | Rewritten as purpose, folder layout, dependency direction, main flows, boundaries, when changing. No app list or versions; the query command (`./repo status`) instead | `doctor` checks four required headings (boundaries, dependency direction, main flows, when changing) and the links in the document |
| Generated lists | [20] | The version and dependency lists in the README became generated blocks, with their sources pinned in a lock file | `doctor` fails when a generated block differs from its source or the lock file; a commit hook runs the same check on the staged content rather than the working tree |
| Unchecked rules | Step 7 | Rules such as dependency order and template use are collected under "Check status" in ARCHITECTURE | None; a person verifies them |
| Writing rules | P-001, R-002 | The "When changing" section of ARCHITECTURE says not to append sentences when a feature changes | None |

## Open

- **No effect was measured.** Growth rate and rule deletion ratio were not compared before and after, so this case cannot test the falsifiers of R-001 or R-002.
- **One team, one language.** Several agents edit the repository, but there is one human operator and the code is Swift.
- **The check commands are the repository's own.** This guidebook builds no tool ([decision 0001](../decisions/0001-adopt-existing-methods.md)); take the checking approach, not the commands.
