# 10. Write notes first, then normalize them, then validate

## Status

Proposed (2026-09-25). An agent wrote this record. It applies when the owner changes this status to Accepted and merges the change that adds it.

## Context

Decision 0009 makes the published layers abstract. But an agent reports its work best in its own words: first person, real paths and product names. If each report must be abstract at once, the report loses facts, or the checks block it.

A person who reads a report later can have questions. The agent session that wrote it has the full context. Agent tools can delete old sessions, and a transcript can contain secrets and personal paths.

The owner also uses one lead agent that plans and reviews, and subagents that change files. A normalizer that did not write the note reads it as a new reader, as in the reader test of R-004. No study measures this for normalization.

## Decision

- Add the record type note in `notes/` (DESIGN.md §2). A note is free in perspective and terms, but it is English and follows the style guide of DESIGN.md §11. Only its `status` and `normalized-into` can change.
- Each note points to a private archive of the complete session record, with the SHA-256 of its manifest. The transcripts stay out of this repository.
- Add `guides/notes.md`. It has three stages: a subagent writes the note, a different subagent normalizes it, and the checks validate it. The lead agent changes no file. To discuss a note, fork the archived session, and do not add to the original.
- The `notes` check verifies the front matter, the hash format, the targets of `normalized-into` and the bodies of old notes. It rejects an archive in this repository. It cannot verify private storage.
- Add one example note about the trial of decision 0008.

## Alternatives considered

- **Put reports in `snapshots/`.** Rejected: a snapshot contains measurements, and a note does not.
- **Keep reports out of the repository.** Rejected: a normalized step then has no source that a person can find.
- **Put the transcripts in `notes/`.** Rejected: transcripts can contain secrets and personal paths, and this repository is public.
- **Resume the archived session itself.** Rejected: the transcript grows, and the hash in the note no longer matches.
- **Let the author normalize its own note.** Rejected by the owner: the maker is not the checker. No clause supports this, so the guide marks the step.
- **Add the rule for the lead agent to guides/templates/AGENTS.md.** Rejected: the template contains only rules that each repository needs. A repository that uses notes writes the rule in its own context file (R-002), as AGENTS.md of this guidebook does.

## Consequences

- The abstraction checks do not read `notes/`, `decisions/`, `snapshots/` or REFERENCES.md.
- Each step of the guide has no clause. A later decision can propose a clause when a study measures the effect.
- A note that was written before the end of its session has an incomplete archive. The guide tells the author to archive again and write a new note.
