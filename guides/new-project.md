# Start a project

Use this procedure to make the repository documents of a new repository. The procedure follows the rules for guides in [DESIGN.md](../DESIGN.md) §2. Each step cites its clauses and references, or it states that it has none. Each clause and [REFERENCES.md](../REFERENCES.md) give the certainty and the limits. A clause with the status `proposed` is not adopted yet.

## 1. Documents

| Document | Contents | Not in the document | Skeleton |
|---|---|---|---|
| README | What it is (one paragraph), the first commands, links to the other documents | Structure, rules for work | [templates/README.md](templates/README.md) |
| ARCHITECTURE | Purpose, folder layout, dependency direction, main flows, boundaries, rules for change | Internal details of modules, options, numbers, lists from code | [templates/ARCHITECTURE.md](templates/ARCHITECTURE.md) |
| Instruction file (AGENTS.md, CLAUDE.md) | The conventions of the repository, each with a reason | Overviews, general conventions of languages and tools | [templates/AGENTS.md](templates/AGENTS.md) |
| CONTRIBUTING | Procedures for human contributors | Instructions for agents | Make it when human contributors come |

The ARCHITECTURE row comes from [22]. The instruction file row comes from R-002. The README and CONTRIBUTING rows are usual conventions with no clause or reference.

## 2. Steps

1. **Keep the README short.** Write what it is, how to run it first, and where the other documents are. No clause or reference.
   Done when: the README has no structure description and no rules for work.
2. **Write only information that changes rarely in ARCHITECTURE.** Do not write lists, versions or options. Give the command that shows them. [22]
   Done when: ARCHITECTURE has no list from code.
3. **Write the conventions of the repository in the instruction file.** Write each rule as a positive instruction with a reason of one line. R-001, R-002, DESIGN.md §5.
   Done when: each rule has a reason, and no rule repeats the README or ARCHITECTURE.
4. **Generate each list that a document must show, for example the versions in the README.** Make the check fail when the document and the generated output are different (Cog `--check`). Use this only for lists from code. [20]
   Done when: a manual change to the generated list makes the check fail.
5. **Make a person read a document again when its code changes.** Select few target files. Record their hash in the document. Make the check fail when the hash changes (the rust-analyzer method). [21]
   Done when: a change to a target file makes the check fail until you update the recorded hash.
6. **Report stale references as warnings for a person.** Stale references are frequent, but automatic detection (DOCER) has many false positives. Thus the check must not stop a build. P-002, [8], [2]
   Done when: the check runs on each pull request and does not block it.
7. **List the rules that no check verifies.** Put them in the rules for change of ARCHITECTURE. Then a person knows what to verify manually. No clause or reference: this step comes from the case.
   Done when: each boundary rule has a check or is on the list.
8. **Do not add feature descriptions to the instruction file.** Put behavior in the help of the tool. Put reasons in a decision record. A feature description is not a convention of the repository. R-002, P-001
   Done when: a feature change does not change the instruction file, unless a convention changes.
9. **Read all documents again at a fixed interval.** Delete rules that have no reason now. Delete stale sentences. Instruction files collect sediment (P-001). [22]
   Done when: ARCHITECTURE gives the interval and the date of the last review.

## Case

[case-swift-monorepo.md](case-swift-monorepo.md) applies this procedure to one monorepo.
