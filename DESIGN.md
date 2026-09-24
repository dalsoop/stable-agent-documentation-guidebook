# Design

How to write repository documents that stay correct as the code changes, using published research and existing tools. This repository builds no new metric and no new tool ([decision 0001](decisions/0001-adopt-existing-methods.md)). Bracketed numbers point to [REFERENCES.md](REFERENCES.md); terms are defined in [CONTEXT.md](CONTEXT.md).

## 1. Scope

- **Documents:** README, ARCHITECTURE, instruction files, CONTRIBUTING.
- **In scope:** sediment and stale references in these documents, and the writing rules and checks that prevent them.
- **Out of scope:** whether instruction files raise agent task success. Studies disagree [3] [4] [5]; this repository only cites them.

## 2. Layers and records

Higher layers change less often; lower layers follow higher ones.

| Layer | Location | Entry condition |
|---|---|---|
| Sample integrity invariant | §3 | Never changes |
| Principle | `principles/` | Certainty moderate or higher, observed in the same direction by at least two studies whose samples do not overlap |
| Practice | `practices/` | A certainty, a falsifier and a review date |
| Guide | `guides/` | Cites clause ids and reference numbers only, and marks any step that rests on neither. A case is never evidence |

When two studies share authors or methods, their errors may overlap: say so in a rebuttal and weigh it in the certainty.

Two records sit outside the layers. Both are append-only; a record that must change is superseded by a new one.

| Record | Location | Holds |
|---|---|---|
| Decision record | `decisions/` | Why the structure or a clause status changed |
| Snapshot | `snapshots/` | Measurements |

## 3. Sample integrity invariant

> If a sample falls short on quality or directional coherence, conclusions drawn from it are not adopted.

The invariant applies equally to our own measurements and to cited studies, and is judged with existing methods:

- **Sample quality:** the known pitfalls of GitHub data [10] and sampling guidelines for software engineering research [11].
- **Directional coherence and weakness:** the five GRADE domains [12], namely risk of bias, inconsistency, imprecision, indirectness and publication bias. Synthetic experiments only lower a certainty for risk of bias, conflicting results for inconsistency, small samples for imprecision, and other languages or agents for indirectness.

## 4. Certainty

Every clause carries a GRADE certainty [12] and lists the domains it was downgraded for.

| Certainty | Meaning |
|---|---|
| high | Further research is unlikely to change the conclusion |
| moderate | Further research may change the conclusion |
| low | Further research is likely to change the conclusion |
| very low | The conclusion is very uncertain |

## 5. Counter-evidence

Counter-evidence goes in as rebuttals, not as a list. Two-sided messages without refutation persuade less than one-sided ones, while refutational messages persuade more [14]; texts that state a misconception and refute it improve learning [13].

1. Pair each piece of counter-evidence with this repository's judgement: what was taken in and what limit remains.
2. Give every clause a falsifier, following the adversarial collaboration procedure [15].
3. Before proposing a clause, read the limitations of each cited study and look for studies that contradict it.
4. Keep counter-evidence out of instruction files. Models often miss negation [16], so instruction files hold positive instructions with a one-line reason; rebuttals live in clauses and decision records. This carries reader studies [13] [14] over to agents, so it is indirect.

## 6. Clause format

```yaml
id: R-001                  # P- for principles, R- for practices
layer: practice            # principle | practice
status: proposed           # proposed | adopted | superseded
certainty: low             # high | moderate | low | very-low
downgraded-for: [indirectness, imprecision]   # risk-of-bias | inconsistency | imprecision | indirectness | publication-bias
falsified-if: "The same effect is not observed in a replication under the same conditions"
review-by: 2027-03-24      # practices only
references: [1]
superseded-by: null
```

The body holds the clause, its reason (evidence, for a principle) and its rebuttals; a practice adds its application. Agents may create `proposed` clauses. Only a person changes a status, through a decision record. To withdraw a clause, delete its file and record why in a decision record. Keep the file only when another clause replaces it: set `status: superseded` and `superseded-by`.

## 7. Decision record format

Nygard's format with one added section, Alternatives considered [17]. Nygard's short format scored best on comprehension [18], and alternatives are the section real records omit most often [19].

```
# N. Title
## Status
## Context
## Decision
## Alternatives considered
## Consequences
```

## 8. Tools and data

Document checks use existing tools; their order and caveats are in [guides/new-project.md](guides/new-project.md) §2. The instruction-file sample for measurement is the Agent Context File Analysis dataset [6].

## 9. Clauses

Principles live in [principles/](principles/) and practices in [practices/](practices/), one file per clause. This document does not list them.

Withdrawn:

- "AGENTS.md is a file for efficiency" (a design v1 prescription, 2026-09-24). Its source [4] covered one agent, did not measure correctness, and could not be compared with [3]. It predates decision records, so the reason stays here.
- R-003 "Change rules when the agent actually errs" (2026-09-25): [decision 0003](decisions/0003-withdraw-r003-p003.md).
- P-003 "There is no evidence that repository overviews raise agent task success" (2026-09-25): [decision 0003](decisions/0003-withdraw-r003-p003.md).

## 10. Pilot snapshot

`snapshots/2026-09-24-pilot/` measured metrics defined in design v1. This design does not use them, so the snapshot is never cited as evidence. It stays as the example of a split sample reversing a conclusion, which motivated §3.

## 11. Open questions

| Question | Recommendation |
|---|---|
| Population | Use the population of [6] for instruction files; keep agent product repositories as a separate population |
| Review cycle | Every six months; re-grade when new papers or datasets appear |
