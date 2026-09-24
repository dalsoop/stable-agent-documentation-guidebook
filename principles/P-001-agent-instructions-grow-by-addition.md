---
id: P-001
layer: principle
status: proposed
certainty: moderate
downgraded-for: [risk-of-bias]
falsified-if: "A large sample from a different population shows instruction-file changes dominated by deletions rather than additions"
references: [1, 6, 9]
superseded-by: null
---

# Instruction files grow mainly by addition

## Clause

Instruction files grow over time mainly through added instructions, and the older an instruction is, the less likely it is to be deleted. They accumulate sediment.

## Evidence

- Tracking instruction lifetimes in 1,867 repositories, instruction files grew substantially and older instructions had a lower risk of deletion [1]. The instruction extraction rules were validated on a manual sample.
- 2,303 instruction files in 1,925 repositories evolved through frequent small additions [6].
- Among rule change events, extensions and reinforcements were the most common [9].

## Rebuttals

- **Counter-evidence:** [1] is a single-author preprint, and [9] consists mostly of small single-developer projects.
  **Judgement:** the three studies differ in authors, populations and methods, yet point the same way. No downgrade for inconsistency; one downgrade for risk of bias.
- **Counter-evidence:** the clause does not show that growth is harmful.
  **Judgement:** it states the phenomenon only. Whether to curb growth is decided by practices.
