# 4. First adoption

## Status

Proposed (2026-09-25). Takes effect when a person changes this status to Accepted and sets the `status` of the four clauses to `adopted`.

## Context

The four remaining clauses are all `proposed`, so the guidebook has no prescription in force and [guides/new-project.md](../guides/new-project.md) cites only proposals. In the same change, the reason and falsifier of R-002 moved inside the scope: duplication and stale references instead of task success.

## Decision

| Clause | Certainty | Entry condition ([DESIGN.md](../DESIGN.md) §2) | Proposal |
|---|---|---|---|
| P-001 Instruction files grow mainly by addition | moderate | Met: three studies with non-overlapping samples [1] [6] [9] | Adopt |
| P-002 Repository documents often hold stale references | moderate | Met: two studies with non-overlapping samples [2] [7]; the shared author and method are stated in a rebuttal | Adopt |
| R-001 State a reason for every instruction | low | Met: falsifier and review date | Adopt |
| R-002 Keep only the repository's own conventions in instruction files | low | Met | Adopt |

## Alternatives considered

- **Adopt only clauses with certainty moderate or higher.** Rejected: the practice layer accepts low certainty. Excluding low leaves R-001 and R-002, the core of the guide, without force. Each clause states its certainty, so readers can weigh it.
- **Move P-002 out of principles.** Rejected: the two samples (about 3,000 project documentation sets, and instruction files) do not overlap. The error a shared method can carry is false positives, already graded as imprecision.

## Consequences

- On acceptance, `status: adopted` is set in P-001, P-002, R-001 and R-002.
- R-001 and R-002 keep their review date, 2027-03-24.
