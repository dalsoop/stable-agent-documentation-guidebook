---
id: P-001
layer: principle
status: proposed
certainty: moderate
downgraded-for: [risk-of-bias]
falsified-if: "A large sample from a different population shows that most changes to instruction files are deletions, not additions"
references: [1, 6, 9]
superseded-by: null
---

# Instruction files grow mainly by addition

## Clause

Instruction files grow mainly because people add instructions. People delete old instructions less frequently than new instructions. Thus instruction files collect sediment.

## Evidence

- A study of instruction lifetimes in 1,867 repositories found that instruction files grew much. Old instructions had a lower risk of deletion [1]. A manual sample validated the rules that extract instructions.
- 2,303 instruction files in 1,925 repositories changed through frequent small additions [6].
- Extensions and reinforcements were the most frequent types of rule change [9].

## Rebuttals

- **Counter-evidence:** [1] has one author and no peer review. Most projects in [9] are small and have one developer.
  **Judgement:** the three studies have different authors, populations and methods, but they show the same direction. Thus the certainty is not lower for inconsistency. It is one level lower for risk of bias.
- **Counter-evidence:** the clause does not show that growth causes harm.
  **Judgement:** the clause states the phenomenon only. Practices decide if growth must stop.
