---
id: P-002
layer: principle
status: proposed
certainty: moderate
downgraded-for: [imprecision]
falsified-if: "A large sample, with false positives removed by a person, shows outdated references in few repositories"
references: [2, 7]
superseded-by: null
---

# Repository documents frequently contain outdated references

## Clause

Repository documents, which include context files, frequently keep references to code elements that do not exist now.

## Evidence

- Most of approximately 3,000 GitHub projects had an outdated reference at a time in their history [7].
- The same type of check found outdated references in the context files of many repositories [2].

## Refutations

- **Counter-evidence:** many findings that a person examined in [2] were false positives or ambiguous. The limits of [2] give the figure. The authors call their figures a possible signal only.
  **Judgment:** outdated references stay after the removal of false positives. Thus the clause accepts the phenomenon but cites no frequency. The certainty is lower for imprecision.
- **Counter-evidence:** the two studies have one author in common, and [2] uses the type of check from [7]. Thus they are not independent observations.
  **Judgment:** their samples do not overlap: [7] examined project documentation, and [2] examined context files. A shared method can cause false positives, and the previous refutation already lowered the certainty for imprecision. Thus the two studies meet the principle condition, and the certainty does not go lower. Examine the certainty again when an independent study with a different method is available.
