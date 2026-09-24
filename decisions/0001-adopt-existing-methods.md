# 1. Adopt existing research and tools instead of building new ones

## Status

Accepted (2026-09-24). Supersedes design v1. Translated into English by decision 0005.

## Context

Design v1 defined its own metrics (relative change rate, direction of growth, reference validity) and gate thresholds, and planned a new measurement tool. In the pilot, the home-made reference check produced false positives, and a conclusion drawn from mixed document roles reversed once the sample was split by role. Recent studies, public datasets and running tools already covered the same problems.

## Decision

The guidebook is an application guide, not new research. Metrics, evidence assessment, sampling, the decision record format and checking tools all come from the sources in [REFERENCES.md](../REFERENCES.md). The sample integrity invariant stays, judged with GRADE [12] and the sampling guidelines [10] [11].

## Alternatives considered

- **Build metrics and tools as in v1.** Rejected: the metrics would be unvalidated and could not be compared with studies of the same problem.
- **Cite studies without grading them.** Rejected: most sources had small samples, one ecosystem, synthetic experiments, or no peer review. Ungraded, a weak source reads like a principle.

## Consequences

- Home-made metrics, gate thresholds and the planned collector are removed.
- The pilot snapshot stays as a record and is never cited as evidence.
- Every clause carries a certainty, its downgrade domains and a falsifier.
- If a check cannot be done with an existing tool, a new decision record decides whether to build one.
