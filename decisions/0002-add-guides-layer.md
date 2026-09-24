# 2. Put the order of application in a guide layer

## Status

Accepted (2026-09-25).

## Context

Clauses tell why, and each clause has its own file. But no document told a person who starts a repository which documents to make, in which order and with which sections. Each reader had to make the order again from the clauses. Also, no document recorded an application to a real repository.

## Decision

Add `guides/` as a layer below practices. It contains the order (`new-project.md`), skeleton files (`templates/`) and cases. A guide makes no claim of its own. It cites clause ids and reference numbers, and it marks each step that has neither. A case is not evidence.

## Alternatives considered

- **Put the order in DESIGN.md.** Rejected: DESIGN.md tells how to make clauses. The order changes when clauses change, so it must be in a layer that changes more frequently.
- **Make the order a practice.** Rejected: no study gives a certainty for the order. As a clause, it would look like it has evidence.
- **Put cases in snapshots.** Rejected: snapshots contain measurements, and a case measures nothing.

## Consequences

- Adds `guides/new-project.md`, `guides/templates/` and `guides/case-swift-monorepo.md`.
- Adds the guide layer to the table in DESIGN.md §2.
- Adds reference [22] as the source of the ARCHITECTURE structure.
