# 6. Withdraw P-002, define different studies, and adapt GRADE

## Status

Accepted (2026-09-25). The owner approved the plan after two external reviews.

## Context

Two reviewers, Grok (grok-4.7) and Codex (gpt-5.6-sol), read the guidebook on 2026-09-25 with the same instructions. Both found problems in P-002 "Repository documents frequently contain outdated references".

- Its two studies [2] [7] have an author in common, and [2] uses the type of check from [7]. The clause said that their samples do not overlap, but nobody checked the repositories.
- [7] found outdated references at the time of the study in 28.9% of popular projects and in 5.4% of Google projects. The word "frequently" and the phrase "most of approximately 3,000 projects" were too strong.

Codex also found that the certainties could not be reproduced. The guidebook said "GRADE certainty" but did not state a start level.

## Decision

- Withdraw P-002 and delete its file. R-002 and the guide cite [7] and [2] directly, with the rates above.
- Two studies are different if they have no author in common and use different methods (DESIGN.md §2). A possible overlap of samples goes into a refutation.
- DESIGN.md §4 gives the procedure: a start level, one level lower for each domain with a serious concern, and no rise. A principle starts at high, as GRADE does for evidence about how often an event occurs [32].

## Alternatives considered

- **Keep P-002 and look for an independent study.** Rejected for now: Aghajani et al. (ICSE 2019) is a candidate, but we could not verify its figures. A new principle can come back with a verified study.
- **Lower P-002 to low and keep it in `principles/`.** Rejected: the principle layer requires moderate or higher.
- **Keep the old definition of different studies.** Rejected: nobody can verify that two samples of public repositories do not overlap. Authors and methods can be verified.

## Consequences

- P-001 is the only principle. Its studies [1] and [6] meet the new definition, and a refutation states that their samples can overlap.
- R-002 adds imprecision to its downgrades, so the procedure of DESIGN.md §4 gives its certainty, low.
- Decision 0007 replaces the adoption proposal of decision 0004.
