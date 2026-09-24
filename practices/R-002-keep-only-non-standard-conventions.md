---
id: R-002
layer: practice
status: proposed
certainty: low
downgraded-for: [indirectness, imprecision]
falsified-if: "Repositories that also keep overviews and structure in the context file have no more outdated references and no faster growth of that file than other repositories"
review-by: 2027-03-24
references: [1, 2, 3, 7]
superseded-by: null
---

# Keep only the conventions of the repository in context files

## Clause

A context file contains only the conventions and commands that the README and the code do not show. Overviews and structure are in README and ARCHITECTURE, and the context file refers to them.

## Reason

Overviews and structure contain many names of code elements, for example files, modules and commands. If the context file also contains them, the text exists in two places. When the code changes, people often correct only one copy, and outdated references stay. Outdated references occur in project documentation [7] and in context files [2]. Also, text in a context file rarely goes away (P-001). One copy removes the second place where text becomes stale and grows.

In [3], context files did not reduce the steps that agents needed to reach the related files. That study measures task success, which is out of scope (DESIGN.md §1). Thus this clause cites only that result.

## Refutations

- **Counter-evidence:** in [3], when the authors removed all other documentation, context files that an LLM wrote increased performance by 2.7% on average.
  **Judgment:** a context file helps when it is the only documentation. This practice moves overviews to the README and does not delete them, so the overview stays available.
- **Counter-evidence:** this practice comes from a principle and two studies by inference. No study compares repositories that moved overviews out of context files with repositories that did not.
  **Judgment:** the certainty is low because of indirectness and imprecision. The falsification criterion states that comparison.
- **Counter-evidence:** in [3], context files that developers wrote had a positive effect.
  **Judgment:** the effect was not significant. Also, this practice moves overviews and does not delete them. The context file refers to their location.
- **Counter-evidence:** a repository with few documents can have no other place for an overview.
  **Judgment:** write the overview in the README first. Then refer to it from the context file.

## Application

```markdown
Read ARCHITECTURE.md first for structure and boundaries.

- Make apps only with `./repo new <app>`. (Reason: the scaffolder makes the necessary files.)
```
