---
id: P-002
layer: principle
status: proposed
certainty: moderate
downgraded-for: [imprecision]
falsified-if: "A large sample with false positives removed by hand shows stale references in few repositories"
references: [2, 7]
superseded-by: null
---

# Repository documents often hold stale references

## Clause

Repository documents, instruction files included, often keep references to code elements that no longer exist.

## Evidence

- Most of about 3,000 GitHub projects had a stale reference at some point in their history [7].
- Applying the same family of checks to instruction files found stale references in many repositories [2].

## Rebuttals

- **Counter-evidence:** many of the findings checked by hand in [2] were false positives or ambiguous (the figure is in the limits of [2]). The authors call their figures a possibility signal.
  **Judgement:** stale references remain after the false positives are removed. The phenomenon is accepted, no frequency is cited, and the certainty is downgraded for imprecision.
- **Counter-evidence:** the two studies share an author, and [2] reuses the family of checks from [7], so they are not independent observations.
  **Judgement:** their samples do not overlap ([7] project documentation, [2] instruction files). The error a shared method can carry is false positives, already graded as imprecision above. The principle condition of two studies is met and there is no further downgrade. Re-grade when an independent study with a different method appears.
