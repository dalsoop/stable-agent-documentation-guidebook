# 5. One writing standard for each language

## Status

Accepted (2026-09-25). The owner made this decision.

## Context

All documents were in Korean, but DESIGN.md recommended an English body with Korean summaries. No check enforced a language. A review against writing-great-skills [23] found three defects. One concept had three or four names. Many sentences did not change the behavior of a reader. The steps of the guide had no completion criteria. The owner already uses ASD-STE100 for identifiers in other repositories. The owner also wants a Korean README for Korean readers.

## Decision

- Write all source files in English with ASD-STE100 Simplified Technical English [24].
- Write a translation as a separate file, `<name>.ko.md` for Korean. Use the writing standard of its language: fluent-korean [25] for Korean.
- A file names only the writing standard of its own language. An English file does not tell its writer how to write Korean.
- DESIGN.md §11 keeps the table of languages and standards. That table is the only place that names all standards.
- The first line of a translation records the SHA-256 hash of its source file. A check fails when the source file changes and the translation does not.
- Rewrite the files that exist, which include the merged decision 0001 and the pilot snapshot README. Do not change their meaning or the data files of the snapshot.

## Alternatives considered

- **Plain English.** Rejected by the owner. STE gives fixed rules that a check can partly verify, and it gives one meaning to each word.
- **English and Korean in each file.** Rejected: one file would mix two standards, and the second language would become stale.
- **Korean only.** Rejected: the references, the tools and most readers of a public guidebook use English.
- **Translations without a source hash.** Rejected: a translation is a second copy of a meaning. Without a check, it becomes stale with no warning.
- **A writing instruction for each language in every file.** Rejected by the owner: an instruction for Korean text is noise in an English file.

## Consequences

- All source files are in STE. Clause ids, file names and reference numbers do not change, so citations such as "R-001" stay correct.
- `README.ko.md` is the first translation.
- The rewrite of decision 0001 and of the snapshot README is the one exception to the rule that records do not change.
- `.github/workflows/writing-standards.yml` does the mechanical checks of DESIGN.md §11 and the check of the source hash. `AGENTS.md` gives the rule to agents without the details of a language.
- The checks verify only a small part of each standard. A reviewer verifies the rest, because the dictionaries and style rules are not in this repository.
