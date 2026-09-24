---
id: R-002
layer: practice
status: proposed
certainty: low
downgraded-for: [indirectness]
falsified-if: "Repositories that also keep overviews and structure in the context file have no more outdated references and no faster growth of that file than other repositories"
review-by: 2027-03-24
references: [1, 2, 3, 7]
superseded-by: null
---

# Keep only the conventions of the repository in context files

## Clause

A context file contains only the conventions and commands that the README and the code do not show. Overviews and structure are in README and ARCHITECTURE, and the context file refers to them.

## Reason

Overviews and structure contain many names of code elements, for example files, modules and commands. If the context file also contains them, the text exists in two places. When the code changes, people often correct only one copy, and outdated references stay. Outdated references are frequent (P-002), and text in a context file rarely goes away (P-001). One copy removes the second place where text becomes stale and grows.

No study gives a reason to put overviews in context files. Overviews did not change how fast agents found the related files [3]. That study measures task success, which is out of scope (DESIGN.md §1). Thus this clause cites only its null result.

## Refutations

- **Counter-evidence:** this practice comes from two principles by inference. No study compares repositories that moved overviews out of context files with repositories that did not.
  **Judgment:** the certainty is low because of indirectness. The falsification criterion states that comparison.
- **Counter-evidence:** in [3], context files that developers wrote had a positive effect.
  **Judgment:** the effect was not significant. Also, this practice moves overviews and does not delete them. The context file refers to their location.
- **Counter-evidence:** a repository with few documents can have no other place for an overview.
  **Judgment:** write the overview in the README first. Then refer to it from the context file.

## Application

```markdown
Read ARCHITECTURE.md first for structure and boundaries.

- Make apps only with `./repo new <app>`. (Reason: the scaffolder makes the necessary files.)
```
