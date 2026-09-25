# 7. First adoption

## Status

Proposed (2026-09-25). This record replaces decision 0004. It starts to apply when a person changes this status to Accepted and sets the `status` of the adopted clauses to `adopted`.

## Context

Decision 0004 proposed four clauses. Since then, decision 0006 withdrew P-002, and R-004 was added. No prescription of the guidebook is in effect, and [guides/new-project.md](../guides/new-project.md) cites only proposals.

## Decision

| Clause | Certainty | Entry condition ([DESIGN.md](../DESIGN.md) §2) | Proposal |
|---|---|---|---|
| P-001 Context files grow mainly by addition | moderate | Met: two different direct studies [1] [6], and one indirect study [9] | Adopt |
| R-001 Give a reason for each instruction | low | Met: a falsification criterion and a review date | Adopt |
| R-002 Keep only the conventions of the repository in context files | low | Met | Adopt |
| R-004 Name the reader of each document, and test the document with that reader | very low | Met | Adopt. One repository recorded a reader test in two runs ([snapshot 2026-09-25](../snapshots/2026-09-25-reader-test/README.md)) |

## Alternatives considered

- **Keep R-004 proposed.** Rejected: the condition was one recorded reader test, and the snapshot of 2026-09-25 records one in two runs. The test found three real defects: two in the context file and one in the code that it describes. After the fix, both readers met all criteria. The certainty stays very low, and the clause states it.
- **Adopt only clauses with the certainty moderate or higher.** Rejected: the practice layer accepts a low certainty. Without the low clauses, R-001 and R-002 have no effect, and they are the core of the guide.

## Consequences

- If a person accepts this decision, set `status: adopted` in P-001, R-001, R-002 and R-004.
- R-001 and R-002 keep their review date, 2027-03-24.
