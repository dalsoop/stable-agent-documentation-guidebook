# 11. Date each time-sensitive claim

## Status

Proposed (2026-09-25). An agent wrote this record. It applies when the owner changes this status to Accepted and merges the change that adds it.

## Context

An agent knows the world only up to its knowledge cutoff. It can state an old version or an old "latest" tool as a fact of today. The effective cutoff of a model is often different from its reported cutoff [41]. In code completion, 7 models used deprecated APIs at rates of 25% to 38% [42]. A fork of an archived session starts even further in the past than a new session.

These two studies do not examine documents or coding agents. No study measures time-sensitive claims in repository documents. Thus this decision adds no clause.

## Decision

- A note gives `written-at`, `model` and `knowledge-cutoff` (DESIGN.md §2). The `notes` check verifies their format, and that the cutoff is not after the date of writing.
- In a published layer, a time-sensitive claim has a date or cites a reference (DESIGN.md §13). The `cutoff` check finds versions, calendar years and the words of the table "Time-sensitive words" in GLOSSARY.md. The Korean words are in `docs_checks.py`, because an original contains no Hangul.
- Step 6 of guides/notes.md makes the normalizer verify each time-sensitive claim of a note again, with the date of access. Step 11 makes the first message to a fork state today's date and the date of the note.
- From [33], REFERENCES.md gives the date of access of each source.

## Alternatives considered

- **Trust the model.** Rejected: the reported cutoff is often not the effective cutoff [41], and models repeat deprecated APIs [42].
- **Block all version numbers.** Rejected: a guide must name versions sometimes, for example of a tool that it cites. A date or a reference makes the claim verifiable.
- **Use only review dates.** Rejected: a review date applies to a whole clause. A guide step has no review date, and a note has none.
- **Put "new", "now", "recent" and "current" in the table.** Rejected: in the procedures of this repository they refer to the time of reading. With them, the check found 26 sentences, and none was a claim about the world.

## Consequences

- The check found two true findings. The Korean README added "current" to "available tools", and guides/new-repository.md said "the latest default branch" twice. The translation now follows the original, and the guide says "the fetched default branch".
- **Counter-evidence:** a regular expression misses implicit claims, for example "the tool supports this option".
  **Judgment:** the check finds only the explicit forms. A reviewer and the review date of each practice cover the rest.
- **Counter-evidence:** a date also becomes old. "As of 2026-09-25" can be wrong one year later.
  **Judgment:** a date tells the reader how old the claim is. The review cycle of DESIGN.md §12 reads the claims again.
- **Counter-evidence:** the reported cutoff in a note can be wrong [41].
  **Judgment:** the note records the reported value. The normalizer verifies each claim against a source and does not rely on the cutoff.
- The entries [1] to [32] have no date of access. Nobody knows when they were read.
