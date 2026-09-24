# 4. First adoption

## Status

Proposed (2026-09-25). This decision starts to apply when a person changes this status to Accepted. The person also sets the status of the four clauses to `adopted`.

## Context

The four clauses that stay all have the status `proposed`. Thus no prescription of the guidebook is in effect, and [guides/new-project.md](../guides/new-project.md) cites only proposals. In the same change, R-002 got a new reason and falsification criterion inside the scope: duplication and outdated references, not task success.

## Decision

| Clause | Certainty | Entry condition ([DESIGN.md](../DESIGN.md) §2) | Proposal |
|---|---|---|---|
| P-001 Context files grow mainly by addition | moderate | Met: three studies with samples that do not overlap [1] [6] [9] | Adopt |
| P-002 Repository documents frequently contain outdated references | moderate | Met: two studies with samples that do not overlap [2] [7]. A refutation states the common author and method | Adopt |
| R-001 Give a reason for each instruction | low | Met: a falsification criterion and a review date | Adopt |
| R-002 Keep only the conventions of the repository in context files | low | Met | Adopt |

## Alternatives considered

- **Adopt only clauses with the certainty moderate or higher.** Rejected: the practice layer accepts a low certainty. Without the low clauses, R-001 and R-002 have no effect, and they are the core of the guide. Each clause states its certainty, so readers can make their own decision.
- **Remove P-002 from the principles.** Rejected: the two samples do not overlap. One sample is approximately 3,000 sets of project documentation, and the other is context files. A shared method can cause false positives, and the certainty is already lower for imprecision.

## Consequences

- If a person accepts this decision, set `status: adopted` in P-001, P-002, R-001 and R-002.
- R-001 and R-002 keep their review date, 2027-03-24.
