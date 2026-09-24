# 5. One style guide for each language

## Status

Accepted (2026-09-25). The owner made this decision.

## Context

All documents were in Korean, but DESIGN.md recommended an English body with Korean summaries. No check enforced a language. A review against writing-great-skills [23] found three defects. One concept had three or four names. Many sentences did not change the behavior of a reader. The steps of the guide had no completion criteria. The owner already uses ASD-STE100 for identifiers in other repositories. The owner also wants a Korean README for Korean readers.

## Decision

- Write all originals in English with ASD-STE100 Simplified Technical English [24].
- Write a translation as a separate file, `<name>.ko.md` for Korean. Use the style guide of its language: fluent-korean [25] for Korean.
- A file names only the style guide of its own language. An English file does not tell its writer how to write Korean.
- DESIGN.md §11 keeps the table of languages and style guides. That table is the only place that names all style guides.
- The first line of a translation records the SHA-256 hash of its original. A check fails when the original changes and the translation does not.
- Vale [29], an available tool, checks the sentence length of English files. Three small scripts check what no available tool checks: Hangul in English files, the em dash in Korean files and the hash of each translation.
- Rewrite the files that exist, which include the merged decision 0001 and the pilot snapshot README. Do not change their meaning or the data files of the snapshot.

## Alternatives considered

- **Plain English.** Rejected by the owner. STE gives fixed rules that a check can partly verify, and it gives one meaning to each word.
- **English and Korean in each file.** Rejected: one file would mix two style guides, and the second language would become stale.
- **Korean only.** Rejected: the references, the tools and most readers of a public guidebook use English.
- **Translations without a source hash.** Rejected: a translation is a second copy of a meaning. Without a check, it becomes stale with no warning.
- **An instruction for each language in every file.** Rejected by the owner: an instruction for Korean text is noise in an English file.
- **Our own script for sentence length.** Rejected: Vale does this check, and decision 0001 prefers available tools.

## Consequences

- All originals are in STE. Clause ids, file names and reference numbers do not change, so citations such as "R-001" stay correct.
- `README.ko.md` is the first translation.
- The rewrite of decision 0001 and of the snapshot README is the one exception to the rule that records do not change.
- `.github/workflows/style-guides.yml` does the mechanical checks of DESIGN.md §11 and the check of the source hash. `AGENTS.md` gives the rule to agents without the details of a language.
- The checks verify only a small part of each style guide. A reviewer verifies the rest, because the dictionaries and the full rules are not in this repository. A reviewer also verifies sentences in table cells, because Vale does not check them.
