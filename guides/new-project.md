# Start a project

Use this procedure to make the repository documents of a new repository. The procedure follows the rules for guides in [DESIGN.md](../DESIGN.md) §2. Each step cites its clauses and references, or it states that it has none. Each clause and [REFERENCES.md](../REFERENCES.md) give the certainty and the limits. A clause with the status `proposed` is not adopted yet.

## 1. Readers

Each document has one reader and one reader task (R-004). Start from this table, and change it for your repository.

| Document | Reader | Reader task |
|---|---|---|
| README | A person or an agent that sees the repository for the first time | Tell what the repository is and why, run it once and find the next document |
| ARCHITECTURE | A contributor, human or agent, who will change the code | Find where a change goes and which boundary it must keep |
| Context file (AGENTS.md, CLAUDE.md) | A coding agent before each task | Make a change that obeys the conventions, with no question to a person |
| Decision records (`decisions/`) | A person or an agent that wants to change a decision | Tell why the decision was made and which alternatives failed |
| CONTRIBUTING | A human contributor | Send a change that passes the review |

The README and context file rows come from [30]. The reader task column comes from [31]. The other rows have no clause or reference.

## 2. Contents

| Document | Contents | Not in the document | Skeleton |
|---|---|---|---|
| README | The purpose (what and why), one structure diagram, one flow diagram, the first commands, links to the other documents | Details of the structure, rules for work | [templates/README.md](templates/README.md) |
| ARCHITECTURE | Purpose, folder layout, dependency direction, main flows, boundaries, rules for change with the readers, references | Internal details of modules, options, numbers, lists from code | [templates/ARCHITECTURE.md](templates/ARCHITECTURE.md) |
| Context file | The conventions of the repository, each with a reason | Overviews, general conventions of languages and tools | [templates/AGENTS.md](templates/AGENTS.md) |
| Decision records | The reason for each decision, and the alternatives | Descriptions of behavior | Use the format of [17] |
| CONTRIBUTING | Procedures for human contributors | Instructions for agents | Make it when human contributors come |

The README row comes from [26], [27] and [28]. The ARCHITECTURE row comes from [22]. The context file row comes from R-002. The CONTRIBUTING row is a usual convention with no clause or reference.

## 3. Steps

1. **Name the reader and the reader task of each document.** Write them in a table in the rules for change of ARCHITECTURE. R-004, [30], [31].
   Done when: each document has one reader and one reader task in that table.
2. **Write the README for its reader.** State what the repository is and why it exists [26]. Show the parts in one structure diagram and the main flow in one flow diagram [27]. Write the diagrams as Mermaid text. Then a diff shows each change, and GitHub shows the diagrams [28]. Give the first commands and the links to the other documents.
   Done when: the README states the purpose and has one structure diagram and one flow diagram as text.
3. **Write only information that changes rarely in ARCHITECTURE.** Do not write lists, versions or options. Give the command that shows them. End the document with the references for its rules. [22].
   Done when: ARCHITECTURE has no list from code, and each rule for change has a source.
4. **Write the conventions of the repository in the context file.** Write each rule as a positive instruction with a reason of one line. R-001, R-002, DESIGN.md §5.
   Done when: each rule has a reason, and no rule repeats the README or ARCHITECTURE.
5. **Keep one context file at the root.** Add a context file in a subfolder only for rules that apply only in that folder. A file in a subfolder adds rules. It does not repeat or contradict the files above it. R-002.
   Done when: no context file repeats or contradicts a rule of a file above it.
6. **Keep decision records in the repository, in `decisions/`.** Do not keep the reasons for the structure only in an external wiki. [17].
   Done when: each decision about the structure has a record in `decisions/`.
7. **Generate each list that a document must show, for example the versions in the README.** Make the check fail when the document and the generated output are different (Cog `--check`). Use this only for lists from code. [20].
   Done when: a manual change to the generated list makes the check fail.
8. **Make a person read a document again when its code changes.** Select few target files. Record their hash in the document. Make the check fail when the hash changes (the rust-analyzer method). [21].
   Done when: a change to a target file makes the check fail until you update the recorded hash.
9. **Report outdated references as warnings for a person.** Outdated references are frequent, but automatic detection (DOCER) has many false positives. Thus the check must not stop a build. P-002, [8], [2].
   Done when: the check runs on each pull request and does not block it.
10. **List the rules that no check verifies.** Put them in the rules for change of ARCHITECTURE. Then a person knows what to verify manually. No clause or reference: this step comes from the case study.
    Done when: each boundary rule has a check or is on the list.
11. **Do not add feature descriptions to the context file.** Put behavior in the help of the tool. Put reasons in a decision record. A feature description is not a convention of the repository. R-002, P-001.
    Done when: a feature change does not change the context file, unless a convention changes.
12. **Do a reader test for each document.** Give a new reader only the document and its reader task. For an agent reader, use a new session with no other context. Run the test more than once. R-004, [3], [5].
    Done when: each document passed each run of its reader test, and the readers table records the date.
13. **Read all documents again at a fixed interval.** Delete rules that have no reason now. Delete sentences that do not change what a reader does [23]. Context files grow by addition (P-001). [22].
    Done when: ARCHITECTURE gives the interval and the date of the last review.

## Case study

[case-swift-monorepo.md](case-swift-monorepo.md) applies this procedure to one monorepo.
