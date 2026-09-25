# Rules for agents

Read [DESIGN.md](DESIGN.md) for the layers and [GLOSSARY.md](GLOSSARY.md) for the terms before you edit.

- Write each file in the style guide of its language. DESIGN.md §11 gives the style guides. (Reason: [decision 0005](decisions/0005-style-guide-per-language.md). The `style-guides` check verifies a part of each style guide.)
- Change the original first. Then update each translation, and put the output of `shasum -a 256 <original>` in its first line. (Reason: the check fails when the original changed after the hash in the translation. It cannot compare the text, so a person compares it.)
- Use the terms in GLOSSARY.md and no synonyms. For a new term, use the term of the cited research, and add it with its source. (Reason: readers can then search the research for the same term.)
- Write each meaning in one place, and link to it from other places. (Reason: duplication was the most frequent defect in the review of 2026-09-25.)
- Delete each sentence that does not change what a reader does. (Reason: such a sentence costs time to read and adds nothing [23].)
