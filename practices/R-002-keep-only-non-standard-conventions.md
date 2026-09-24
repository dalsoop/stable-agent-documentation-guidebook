---
id: R-002
layer: practice
status: proposed
certainty: low
downgraded-for: [indirectness]
falsified-if: "Repositories that also keep overviews and structure in the instruction file show no more stale references and no faster growth in it than repositories that do not"
review-by: 2027-03-24
references: [1, 2, 3, 7]
superseded-by: null
---

# Keep only the repository's own conventions in instruction files

## Clause

An instruction file holds only the conventions and commands that the README and the code do not reveal. Overviews and structure live in README and ARCHITECTURE, and the instruction file points to them.

## Reason

Overviews and structure name many code elements: files, modules, commands. Kept in the instruction file as well, they exist twice, and when the code changes only one copy gets fixed, leaving stale references. Stale references are common (P-002), and what enters an instruction file rarely leaves (P-001). Keeping one copy removes the second place to go stale and to grow.

No study reports a reason to put overviews in instruction files: overviews did not change how fast agents found relevant files [3]. That study measures task success, which is out of scope (DESIGN.md §1), so only its null finding is cited here.

## Rebuttals

- **Counter-evidence:** the practice is inferred from two principles; no study compares repositories that moved overviews out with repositories that did not.
  **Judgement:** downgraded for indirectness to low. The falsifier states that comparison.
- **Counter-evidence:** in [3], developer-written instruction files had a positive effect.
  **Judgement:** it was not significant. The practice moves overviews rather than deleting them: the instruction file points to where they are.
- **Counter-evidence:** a repository with few documents may have nowhere else to keep an overview.
  **Judgement:** write the overview in the README first and point to it.

## Application

```markdown
Read ARCHITECTURE.md first for structure and boundaries.

- Create apps only with `./repo new <app>`. (Reason: the scaffolder creates the required files.)
```
