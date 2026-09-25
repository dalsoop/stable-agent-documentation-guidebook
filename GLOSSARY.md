# Glossary

This file gives the terms of this repository. All documents use these terms and no synonyms. Where the cited research has a term, this repository uses that term. The Source column shows where each term comes from. Numbers in brackets refer to [REFERENCES.md](REFERENCES.md).

| Term | Meaning | Source |
|---|---|---|
| repository document | A README, ARCHITECTURE, context file or CONTRIBUTING file | This repository |
| context file | A file that an agent reads before each task, for example AGENTS.md or CLAUDE.md | [3] [5] [6] |
| outdated reference | A reference to a code element that does not exist now | [7] [8] |
| duplication | The same meaning in more than one place | [23] |
| clause | A principle or a practice. Each clause has its own file | This repository |
| principle | An observed phenomenon. [DESIGN.md](DESIGN.md) §2 gives the entry condition | This repository |
| practice | A prescription. DESIGN.md §2 gives the entry condition | This repository |
| certainty | The certainty of evidence for a clause (DESIGN.md §4) | GRADE [12] |
| consistency | The agreement of the results of different studies. Its absence lowers the certainty | GRADE [12] |
| falsification criterion | The condition that shows a clause is wrong. The front matter field is `falsified-if` | [15] |
| refutation | One item of counter-evidence together with the judgment of this repository (DESIGN.md §5) | [13] [14] |
| sample integrity invariant | The top rule of this repository (DESIGN.md §3) | This repository |
| layer | One level of rules in this repository (DESIGN.md §2) | This repository |
| guide | A procedure that applies clauses (DESIGN.md §2) | This repository |
| case study | A record of one repository that followed a guide (DESIGN.md §2) | This repository |
| reader | The group of people or agents that a document is for | [30] [31] |
| reader task | What a reader must be able to do after reading a document | [31] |
| reader test | A check that gives a new reader the repository, one document as the start and its reader task. The reader can follow the links. The document passes if the reader does the task | R-004, [3] [5] |
| decision record | The reason for a change to the structure or to the status of a clause (DESIGN.md §2) | [17] |
| snapshot | A record of measurements (DESIGN.md §2) | This repository |
| style guide | The set of rules for text in one language (DESIGN.md §11) | This repository |
| original | An English file that a translation follows (DESIGN.md §11) | This repository |
| translation | A file in a different language that follows an original (DESIGN.md §11) | This repository |
| STE | ASD-STE100 Simplified Technical English, the style guide for English | [24] |
| worktree | A directory with the files of one branch or commit. One repository can have more than one worktree | Git [33] |
| bare repository | A repository with no worktree of its own | Git [33] |
| code host | The server that keeps the shared copy of a repository | This repository |
| default branch | The branch that receives the merged changes | [34] [35] |
| change request | A request to merge one branch into the default branch after a review | This repository, from [34] [35] |
| protection rule | A setting on the code host that controls who can push to a branch and how changes merge into it | This repository, from [34] [35] |
| abstract term | A term of this glossary that applies to each tool and each code host | This repository |
| concrete term | The name that one product or host uses for an abstract term. The table below lists them | This repository |
| note | A record of work in the words of its author: first person, real paths and product names (DESIGN.md §2) | This repository |
| normalization | The change of a note into a guide step, a clause or a template, with abstract terms | This repository |
| lead agent | The agent that plans a task, starts subagents, reviews their results and decides | This repository |
| subagent | An agent that a lead agent starts for one part of a task, in its own session | This repository |

## Concrete terms

This table is the only list of concrete terms. The `abstraction` check reads it (DESIGN.md §13). A term in backticks matches only as code. A term with a capital letter matches only with the same capitals. A term also matches with the ending "s" or "es".

| Concrete term | Abstract term |
|---|---|
| GitHub | code host |
| GitLab | code host |
| Bitbucket | code host |
| pull request | change request |
| merge request | change request |
| PR | change request |
| MR | change request |
| protected branch | protection rule |
| `main` | default branch |
| `master` | default branch |
| main branch | default branch |
| master branch | default branch |
| origin/main | default branch |
| origin/master | default branch |
