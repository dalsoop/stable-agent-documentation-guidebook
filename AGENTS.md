# Rules for agents

Read [DESIGN.md](DESIGN.md) for the layers and [CONTEXT.md](CONTEXT.md) for the terms before you edit.

- Write each file in the writing standard of its language. DESIGN.md §11 gives the standards. (Reason: [decision 0005](decisions/0005-writing-standard-per-language.md). The `writing-standards` check verifies a part of each standard.)
- Change the source file first. Then update each translation and the source hash in its first line. (Reason: the check fails when a translation does not follow its source file.)
- Use the terms in CONTEXT.md and no synonyms. (Reason: one term for one concept keeps clauses easy to compare and find.)
- Write each meaning in one place, and link to it from other places. (Reason: duplication was the most frequent defect in the review of 2026-09-25.)
