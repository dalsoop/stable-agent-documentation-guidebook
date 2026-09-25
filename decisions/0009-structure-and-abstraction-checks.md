# 9. Check stable structure and abstract terms

## Status

Proposed (2026-09-25). An agent wrote this record. It applies when the owner changes this status to Accepted and merges the change that adds it.

## Context

Readers copy the documents of this guidebook and link to their headings and steps. A renamed heading breaks each link to it. A renumbered step makes each copy cite the wrong step. The history of the default branch has such changes, for example the move to English and the withdrawal of clauses. No check found them.

The owner also wants documents that apply to each repository and each code host. Some documents contained first person, and one step named a product term where GLOSSARY.md has an abstract term.

[Decision 0001](0001-adopt-existing-methods.md) makes no new tools. It also says that a decision record decides when no available tool can do a check.

## Decision

- DESIGN.md §13 gives the rules. `.github/scripts/docs_checks.py` checks them, with the Python standard library and git only.
- `structure` compares the change with its merge base. It fails when a published heading, numbered step, table column, clause id, reference number or Markdown file goes away or changes its number. A decision record that the change adds can name each item with `<!-- structure-change: <item> -->`.
- `abstraction` reads the published layers: the files with the style `Abstract` in `.vale.ini`, and their translations. It fails on first person in translations, personal absolute paths and concrete terms. It also fails when a hunk replaces an abstract term with its concrete term.
- Vale does the first-person check for originals, with the new style `Abstract`.
- The table "Concrete terms" in GLOSSARY.md is the only list of concrete terms. Both parts of `abstraction` read it.
- `test_docs_checks.py` has one test for each type of failure. The workflow runs the checks and the tests.

## Alternatives considered

- **A link checker.** Rejected: it verifies links inside this repository. It cannot see links in copies outside it, and the stable structure protects those.
- **Vale for all abstraction rules.** Rejected for paths and concrete terms: Vale skips code, where paths and branch names occur. A Vale rule would also need a second list of concrete terms.
- **Ban concrete terms everywhere.** Rejected: records and REFERENCES.md name real studies and tools. A sentence that cites a reference reports a fact of that source, for example that one code host shows Mermaid.
- **Forbid all structure changes.** Rejected: withdrawals delete clause files (DESIGN.md §6). The marker keeps such a change possible and records it.

## Consequences

- The checks found three true findings in existing text. Two sentences in DESIGN.md used first person. Step 10 of guides/new-project.md used a product term. These sentences changed. No heading, step number or column changed.
- On the history of the default branch, `structure` finds items in four commits. Each item is a real rename or removal from before this rule, for example the move to English and the withdrawal of R-003.
- The checks cannot see meaning. A reviewer still verifies table cells, the Korean text and synonyms that are not in the table.
- The checkout of the workflow gets the full history, because `structure` needs the merge base.
