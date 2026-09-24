---
id: R-004
layer: practice
status: proposed
certainty: very-low
downgraded-for: [risk-of-bias, indirectness, imprecision]
falsified-if: "In a comparison, readers do their reader task no more often with documents that name a reader and pass a reader test than with documents that do not"
review-by: 2027-03-25
references: [3, 5, 30, 31]
superseded-by: null
---

# Name the reader of each document, and test the document with that reader

## Clause

For each repository document, name its reader and its reader task. The reader task is what the reader must be able to do after reading. Then do a reader test: give a new reader the repository, the document as the start and the reader task, and examine the result. The reader can follow the links of the document.

## Reason

A document without a named reader has no criterion for success. Format checks, such as sentence length or outdated references, cannot show that a document does its job. The AGENTS.md format already separates readers: README files are for humans, and AGENTS.md is for agents [30]. Diátaxis selects the type of a document from what the reader tries to do [31]. Studies of context files measured agents that did tasks with and without the file [3] [5]. A reader test applies that method to one document in one repository.

A reader test checks one document for its own reader. It makes no general claim about task success, which stays out of scope ([DESIGN.md](../DESIGN.md) §1).

## Refutations

- **Counter-evidence:** [30] and [31] are practitioner sources with no evaluation. Also, [3] and [5] measured the effect of whole context files, not the effect of a named reader.
  **Judgment:** the evidence starts at low, and indirectness lowers it to very low (DESIGN.md §4). The clause stays proposed so that repositories can collect the comparison that the falsification criterion needs.
- **Counter-evidence:** a reader test with an agent does not always give the same result. One run can pass or fail by chance.
  **Judgment:** run the test more than once, and record each result. A document that fails one run needs work.
- **Counter-evidence:** a test with human readers costs time.
  **Judgment:** test human readers at each review cycle, not at each change. Agent readers cost less, so test them when the document changes.
- **Counter-evidence:** most documents link to other documents, so a test with only one file is not realistic.
  **Judgment:** the reader starts at the document and can follow its links, as a real reader does. A document that needs a link to do its task must contain that link.

## Application

[guides/new-project.md](../guides/new-project.md) §1 gives a table of readers and reader tasks, and step 13 gives the reader test.
