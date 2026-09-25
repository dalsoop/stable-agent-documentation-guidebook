---
id: P-001
layer: principle
status: adopted
certainty: moderate
downgraded-for: [risk-of-bias]
falsified-if: "A large sample from a different population shows that most changes to context files are deletions, not additions"
references: [1, 6, 9]
superseded-by: null
---

# Context files grow mainly by addition

## Clause

Context files grow mainly because people add instructions. People delete old instructions less frequently than new instructions. Thus context files become longer over time, and old instructions stay.

## Evidence

- A study of instruction lifetimes in 1,867 repositories found that context files grew much. Old instructions had a lower risk of deletion [1]. A manual sample validated the rules that extract instructions.
- 2,303 context files in 1,925 repositories changed through frequent small additions [6].
- In 7,310 rules of AI IDEs from 83 projects, context expansions and enrichments were the most frequent changes [9].

## Refutations

- **Counter-evidence:** [1] has one author and no peer review. Most projects in [9] are small and have one developer.
  **Judgment:** the three studies have different authors, populations and methods, but they show the same direction. Thus the certainty is not lower for inconsistency. It is one level lower for risk of bias.
- **Counter-evidence:** the clause does not show that growth causes harm.
  **Judgment:** the clause states the phenomenon only. Practices decide if growth must stop.
- **Counter-evidence:** [9] examined rules of AI IDEs, not context files.
  **Judgment:** this makes [9] indirect. [1] and [6] examined context files, have no author in common and use different methods. Thus two different direct studies remain, and the certainty does not go lower.
- **Counter-evidence:** the samples of [1] and [6] can overlap, because both come from public GitHub repositories.
  **Judgment:** an overlap would make the two results less independent. Nobody checked it, so this is one more reason for the downgrade for risk of bias.
