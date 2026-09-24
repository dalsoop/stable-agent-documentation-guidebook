# Starting a project

The order for creating the repository documents of a new repository. It follows the guide layer rules in [DESIGN.md](../DESIGN.md) §2: each step cites the clauses and references it rests on, or says that it rests on none. Certainty and limits are in each clause and in [REFERENCES.md](../REFERENCES.md). A `proposed` clause is not yet adopted.

## 1. Documents

| Document | Holds | Leaves out | Skeleton |
|---|---|---|---|
| README | What it is in one paragraph, the first commands to run, links to the other documents | Structure, working rules | [templates/README.md](templates/README.md) |
| ARCHITECTURE | Purpose, folder layout, dependency direction, main flows, boundaries, when changing | Module internals, options, numbers, lists derived from code | [templates/ARCHITECTURE.md](templates/ARCHITECTURE.md) |
| Instruction file (AGENTS.md, CLAUDE.md, ...) | The repository's own conventions, each with a reason | Overviews, general language and tool conventions | [templates/AGENTS.md](templates/AGENTS.md) |
| CONTRIBUTING | Procedures for human contributors | Agent instructions | Create it when human contributors appear |

The ARCHITECTURE row rests on [22] and the instruction file row on R-002. The README and CONTRIBUTING rows are common convention and rest on no clause or reference.

## 2. Steps

1. **Keep the README short:** what it is, how to run it first, where everything else lives. Rests on no clause or reference.
   Done when the README holds no structure description and no working rule.
2. **Write only what rarely changes in ARCHITECTURE.** Leave out lists, versions and options, and name the command that queries them. [22]
   Done when ARCHITECTURE holds no list derived from code.
3. **Write the instruction file as the repository's own conventions, stated positively, each with a one-line reason.** R-001, R-002. Positive wording: DESIGN.md §5.
   Done when every rule has a reason and no rule restates the README or ARCHITECTURE.
4. **Generate any list a document needs, such as a version list in the README, and fail the check when the document and the generated output differ** (Cog's `--check`). Use it only for lists derived from code. [20]
   Done when a hand edit of the generated list fails the check.
5. **Force a re-read when code a document relies on changes.** Keep the target files few, and fail the check when their hash differs from the hash recorded in the document (the rust-analyzer approach). [21]
   Done when changing a target file fails the check until the recorded hash is updated.
6. **Report stale references as warnings for a person to review.** Stale references are common, but automatic detection (DOCER) has many false positives, so it does not fail the build. P-002, [8], [2]
   Done when the check runs on every pull request and never blocks it.
7. **List the rules no check enforces** in the "When changing" section of ARCHITECTURE, so a person knows what to verify by hand. Rests on no clause or reference; taken from the case.
   Done when every boundary rule is either enforced by a check or listed.
8. **Leave feature descriptions out of the instruction file.** Behaviour goes to the tool's help and reasons to a decision record; a feature description is not a repository convention. R-002, P-001
   Done when a feature change leaves the instruction file untouched unless a convention changed.
9. **Re-read every document on a fixed cycle,** deleting rules whose reason is gone and sentences that went stale. Instruction files accumulate sediment (P-001). [22]
   Done when the cycle and the date of the last re-read are written in ARCHITECTURE.

## Case

[case-swift-monorepo.md](case-swift-monorepo.md) applies this order to one monorepo.
