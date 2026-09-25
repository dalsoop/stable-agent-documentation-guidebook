# Start a project

Use this procedure to make the repository documents of a new repository. For a repository that already has documents, use §4. The procedure follows the rules for guides in [DESIGN.md](../DESIGN.md) §2. Each step cites its clauses, references and sections of DESIGN.md, or it states that it has none. Each clause and [REFERENCES.md](../REFERENCES.md) give the certainty and the limits. A clause with the status `proposed` is not adopted yet.

## 1. Readers

Each document has one reader and one reader task (R-004). Start from this table, and change it for your repository.

| Document | Reader | Reader task |
|---|---|---|
| README | A person or an agent that sees the repository for the first time | Tell what the repository is and why, run it once and find the next document |
| ARCHITECTURE | A contributor, human or agent, who will change the code | Find where a change goes and which boundary it must keep |
| Context file (AGENTS.md, CLAUDE.md) | An agent before each task | Make a change that obeys the conventions, with no question to a person |
| Decision records (`decisions/`) | A person or an agent that wants to change a decision | Tell why the decision was made and which alternatives failed |
| CONTRIBUTING | A human contributor | Send a change that passes the review |

The README and context file rows come from [30]. The reader task column comes from [31]. The other rows have no clause or reference.

## 2. Contents

| Document | Contents | Not in the document | Skeleton |
|---|---|---|---|
| README | The purpose (what and why), the first commands, links to the other documents. Diagrams of the parts and the main flow are optional | Details of the structure, rules for work | [templates/README.md](templates/README.md) |
| ARCHITECTURE | Purpose, folder layout, dependency direction, main flows, boundaries, rules for change with the readers | Internal details of modules, options, numbers, lists from code | [templates/ARCHITECTURE.md](templates/ARCHITECTURE.md) |
| Context file | The conventions of the repository, each with a reason | Overviews, general conventions of languages and tools | [templates/AGENTS.md](templates/AGENTS.md) |
| Decision records | The reason for each decision, and the alternatives | Descriptions of behavior | Use the format of [17] |
| CONTRIBUTING | Procedures for human contributors | Instructions for agents | Make it when human contributors come |

The README row comes from [26]. The ARCHITECTURE row comes from [22]. The context file row comes from R-002. The CONTRIBUTING row is a usual convention with no clause or reference.

## 3. Steps

1. **Name the reader and the reader task of each document.** Write them in a table in the rules for change of ARCHITECTURE. R-004, [30], [31].
   Done when: each document has one reader and one reader task in that table.
2. **Write the README for its reader.** State what the repository is and why it exists [26]. Give the first commands and the links to the other documents.
   Done when: the README states the purpose and the first commands.
3. **If a picture helps the reader, add one structure diagram and one flow diagram as Mermaid text.** A diff then shows each change, and GitHub shows the picture [28]. No clause: [27] only reports that contributors find diagrams useful for newcomers.
   Done when: each diagram is text, not an image file.
4. **Write only information that changes rarely in ARCHITECTURE.** Do not write lists, versions or options. Give the command that shows them. [22].
   Done when: ARCHITECTURE has no list from code.
5. **Write the conventions of the repository in the context file.** Give each rule a reason of one line. Write rules as positive instructions where you can. R-001, R-002, DESIGN.md §5.
   Done when: each rule has a reason, and no rule repeats the README or ARCHITECTURE.
6. **Keep one context file at the root.** R-002. A file in a subfolder is permitted only for rules that apply only in that folder. It adds rules and does not repeat or contradict the files above it. No clause or reference supports this permission.
   Done when: no context file repeats or contradicts a rule of a file above it.
7. **Keep decision records in the repository, in `decisions/`.** Do not keep the reasons for the structure only in an external wiki. [17].
   Done when: each decision about the structure has a record in `decisions/`.
8. **Generate each list that a document must show, for example the versions in the README.** Make the check fail when the document and the generated output are different (Cog `--check`). Use this only for lists from code. [20].
   Done when: a manual change to the generated list makes the check fail.
9. **Make a person read a document again when its code changes.** Select few target files, not ARCHITECTURE. Record their hash in the document, and make the check fail when the hash changes (the rust-analyzer method). [21].
   Done when: a change to a target file makes the check fail until you update the recorded hash.
10. **Report outdated references as warnings.** Automatic detection (DOCER) has many false positives [8] [2]. Make the check block a change only after a sample of its findings shows a precision that you accept. [7].
    Done when: the check runs on each pull request, and a record gives its measured precision.
11. **List the rules that no check verifies.** Put them in the rules for change of ARCHITECTURE. Then a person knows what to verify manually. No clause or reference: this step comes from the case study.
    Done when: each boundary rule has a check or is on the list.
12. **Do not add feature descriptions to the context file.** A feature description repeats what the code and the help show (R-002). Put behavior in the help of the tool, and reasons in a decision record.
    Done when: a feature change does not change the context file, unless a convention changes.
13. **Do a reader test for each document.** Give a new reader the repository, the document as the start, and the reader task. The reader can follow the links of the document. For an agent, use a new session with no other context. Run the test more than once. R-004, [3], [5].
    Done when: each document passed each run, and the readers table records the date.
14. **Read all documents again at a fixed interval.** Delete rules that have no reason now. Delete sentences that do not change what a reader does [23]. Context files grow by addition (P-001). [22].
    Done when: ARCHITECTURE gives the interval and the date of the last review.

## 4. A repository that already has documents

Do not rewrite everything. Do these five steps first, then continue with §3.

1. List the documents, and name the reader and the reader task of each one (step 1).
2. Remove one duplication: text that exists in the context file and in the README or ARCHITECTURE (R-002).
3. Do one reader test on the context file (step 13).
4. Add one check (step 8, 9 or 10).
5. Give each rule of the context file a reason (R-001).

Done when: the five steps are done, and the readers table records the result of the reader test.

## Case study

[case-swift-monorepo.md](case-swift-monorepo.md) applies this procedure to one monorepo.
