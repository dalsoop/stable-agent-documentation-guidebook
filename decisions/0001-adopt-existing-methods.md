# 1. Use available research and tools, and make no new tools

## Status

Accepted (2026-09-24). This decision replaces design v1. Decision 0005 changed its language.

## Context

Design v1 defined its own metrics and gate thresholds: the relative rate of change, the direction of growth and the validity of references. It also planned a new tool for measurements. In the pilot, the reference check of v1 gave false positives. Also, a conclusion from a sample with mixed document roles changed direction when we divided the sample by role. Recent studies, public datasets and available tools already examined the same problems.

## Decision

The guidebook is a guide for application, not new research. Metrics, evidence assessment, samples, the format of decision records and check tools come from the sources in [REFERENCES.md](../REFERENCES.md). The sample integrity invariant stays. GRADE [12] and the guidelines for samples [10] [11] examine it.

## Alternatives considered

- **Make metrics and tools as in v1.** Rejected: the metrics would have no validation. Also, a comparison with studies of the same problem would not be possible.
- **Cite studies without a certainty.** Rejected: most sources had small samples, one ecosystem, synthetic experiments or no peer review. Without a certainty, a weak source looks like a principle.

## Consequences

- The metrics, gate thresholds and planned collector of v1 are removed.
- The pilot snapshot stays as a record, but the guidebook does not cite it as evidence.
- Each clause has a certainty, the domains that lowered it and a falsifier.
- If an available tool cannot do a check, a new decision record decides whether to make a tool.
