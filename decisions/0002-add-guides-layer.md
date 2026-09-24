# 2. Put the application order in a guide layer

## Status

Accepted (2026-09-25).

## Context

Clauses explain why, one file each, but nothing told someone starting a repository which documents to create, in what order, and with which sections. Each reader had to rebuild the order from the clauses. An application to a real repository was not recorded either.

## Decision

Add `guides/` as a layer below practices, holding the order (`new-project.md`), skeleton files (`templates/`) and cases. A guide makes no claim of its own: it cites clause ids and reference numbers and marks any step that rests on neither. A case is never evidence.

## Alternatives considered

- **Put the order in DESIGN.md.** Rejected: DESIGN.md covers how clauses are made. The order changes whenever clauses change, so it belongs in a layer that changes more often.
- **Make the order a practice.** Rejected: no study grades the order itself. As a clause it would look graded without evidence.
- **Put cases in snapshots.** Rejected: snapshots hold measurements, and a case measures nothing.

## Consequences

- Adds `guides/new-project.md`, `guides/templates/` and `guides/case-swift-monorepo.md`.
- Adds the guide layer to the layer table in DESIGN.md §2.
- Adds reference [22] as the source of the ARCHITECTURE structure.
