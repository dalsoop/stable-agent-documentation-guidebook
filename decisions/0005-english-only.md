# 5. Write everything in English

## Status

Accepted (2026-09-25). Decided by the owner.

## Context

Every document was Korean, while DESIGN.md §11 recommended an English body with Korean summaries. The mismatch sat among the open questions and nothing enforced either. A review against the writing-great-skills reference [23] found synonym drift (one concept under three or four names, worst where Korean prose surrounded English identifiers), no-op sentences, and guide steps without a completion criterion.

## Decision

Every file is written in English, with no exception. Existing files are translated, including the merged decision record 0001 and the pilot snapshot's README; their meaning does not change and the snapshot's data files are untouched. `CONTEXT.md` fixes one term per concept. A CI check fails when a tracked file contains Hangul.

## Alternatives considered

- **English body with Korean summaries** (the old recommendation). Rejected: two languages hold two copies of each meaning, and the summaries go stale.
- **Korean only.** Rejected: the references, the tools and the likely readers of a public guidebook work in English.
- **English for new files only.** Rejected by the owner: every file, without exception.

## Consequences

- All files are rewritten in English. Clause ids, file names and reference numbers are unchanged, so external citations such as "R-001" still resolve.
- Translating 0001 and the snapshot README is the one exception to append-only records, made here.
- `.github/workflows/english-only.yml` enforces the rule; `AGENTS.md` states it for agents.
- DESIGN.md §11 drops the language question.
