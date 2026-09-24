# Case study: a Swift monorepo (2026-09)

This is a record of one repository that followed [new-project.md](new-project.md). The repository is private, so generic names replace its name and the names of its tools. The rules for guides in [DESIGN.md](../DESIGN.md) §2 tell how to use a case study.

## Repository

A Swift monorepo with several apps and shared packages. Several AI agents edit it at the same time. A root CLI (`./repo`) builds, tests, examines the structure (`doctor`) and examines the code (`lint`).

## Before

- Each feature change added sentences to the README, ARCHITECTURE and the context file. The same text was in three documents. No document described the folder layout.
- Each app also had its own context file, and these files repeated the same conventions.
- The instructions had no reasons. Thus nobody knew which rules were safe to delete.

## Changes

| Step | Clause or source | Change | Mechanical check |
|---|---|---|---|
| Context file | R-001, R-002 | One root file with four rules. Each rule ends with "(Reason: ...)". The file has 17 lines and cites R-001 and R-002 | `doctor` fails if a context file is outside the root |
| Context files of apps | R-002 | Six context files of apps were deleted. The usage of each app moved to its README | Same as above |
| ARCHITECTURE | [22] | New sections: purpose, folder layout, dependency direction, main flows, boundaries and rules for change. No list of apps or versions, but the query command `./repo status` | `doctor` verifies four required headings and the links in the document |
| Generated lists | [20] | The lists of versions and dependencies in the README are generated blocks. A lock file records their sources | `doctor` fails if a generated block is different from its source or the lock file. A commit hook does the same check on the staged content, not on the working tree |
| Rules with no check | Step 10 | The "Check status" section of ARCHITECTURE lists rules such as dependency order and template use | None: a person verifies them |
| Rules for change | P-001, R-002 | The rules for change in ARCHITECTURE tell people not to add sentences when a feature changes | None |

## Limits

- **No measurement of effect.** Nobody compared the growth rate or the ratio of rule deletions before and after. Thus this case study cannot test the falsification criteria of R-001 or R-002.
- **No readers and no reader test.** The case study named no reader for each document and did no reader test (R-004). Thus nobody knows if each document does its job for its reader.
- **One team and one language.** Several agents edit the repository, but only one person operates it. The code is Swift.
- **The check commands belong to the repository.** This guidebook makes no tools ([decision 0001](../decisions/0001-adopt-existing-methods.md)). Use the method of the checks, not the commands.
