# Design

This document gives the design of the guidebook. The guidebook tells how to write repository documents that stay correct when the code changes. It uses published research and available tools, and it makes no new metric or tool ([decision 0001](decisions/0001-adopt-existing-methods.md)). Numbers in brackets refer to [REFERENCES.md](REFERENCES.md). [CONTEXT.md](CONTEXT.md) gives the terms.

## 1. Scope

- **Documents:** README, ARCHITECTURE, instruction files and CONTRIBUTING.
- **In scope:** sediment and stale references in these documents, and the rules and checks that prevent them.
- **Out of scope:** the effect of instruction files on the task success of agents. Studies do not agree [3] [4] [5]. This repository only cites them.

## 2. Layers and records

A higher layer changes less frequently than a lower layer. A lower layer obeys the rules of the higher layers.

| Layer | Location | Entry condition |
|---|---|---|
| Sample integrity invariant | §3 | It does not change |
| Principle | `principles/` | The certainty is moderate or higher. At least two studies with samples that do not overlap show the same direction |
| Practice | `practices/` | The clause has a certainty, a falsifier and a review date |
| Guide | `guides/` | The guide cites only clause ids and reference numbers. It marks each step that has no clause or reference. A case is not evidence |

If two studies have the same authors or methods, their errors can overlap. Write this in a rebuttal, and use it when you set the certainty.

Two records are not layers. You can only add to them. To change a record, write a new record that replaces it.

| Record | Location | Content |
|---|---|---|
| Decision record | `decisions/` | The reason for a change to the structure or to the status of a clause |
| Snapshot | `snapshots/` | Measurements |

## 3. Sample integrity invariant

> If a sample does not have sufficient quality or directional coherence, do not adopt conclusions from it.

This invariant applies to our own measurements and to cited studies. Use these available methods to examine a sample:

- **Sample quality:** the known problems of GitHub data [10] and the guidelines for samples in software engineering research [11].
- **Directional coherence and weak points:** the five GRADE domains [12]. These are risk of bias, inconsistency, imprecision, indirectness and publication bias. Lower the certainty for risk of bias if all evidence comes from synthetic experiments. Lower it for inconsistency if the results do not agree. Lower it for imprecision if the samples are small. Lower it for indirectness if the studies use other languages or agents.

## 4. Certainty

Each clause has a GRADE certainty [12]. Each clause also lists the domains that lowered its certainty.

| Certainty | Meaning |
|---|---|
| high | More research will probably not change the conclusion |
| moderate | More research can change the conclusion |
| low | More research will probably change the conclusion |
| very low | The conclusion is very uncertain |

## 5. Counter-evidence

Put counter-evidence into a clause as rebuttals, not as a list. A two-sided message without a refutation persuades less than a one-sided message. A two-sided message with a refutation persuades more [14]. A text that states a misconception and refutes it helps people learn [13].

1. Put each item of counter-evidence together with the judgement of this repository. Tell what the clause took from it and what limit stays.
2. Give each clause a falsifier. This follows the procedure of adversarial collaboration [15].
3. Before you propose a clause, read the limits of each cited study. Also look for studies that disagree with it.
4. Do not put counter-evidence in instruction files. Language models frequently miss negation [16]. Thus an instruction file contains positive instructions, each with a reason of one line. Rebuttals go in clauses and decision records. This rule applies reader studies [13] [14] to agents, so it is indirect.

## 6. Clause format

```yaml
id: R-001                  # P- for principles, R- for practices
layer: practice            # principle | practice
status: proposed           # proposed | adopted | superseded
certainty: low             # high | moderate | low | very-low
downgraded-for: [indirectness, imprecision]   # risk-of-bias | inconsistency | imprecision | indirectness | publication-bias
falsified-if: "A replication with the same conditions does not show the same effect"
review-by: 2027-03-24      # practices only
references: [1]
superseded-by: null
```

The body contains the clause, the reason (the evidence, for a principle) and the rebuttals. A practice also contains its application. An agent can make a clause with the status `proposed`. Only a person changes a status, and the person writes a decision record for it. To withdraw a clause, delete its file and write the reason in a decision record. Keep the file only if a different clause replaces it. Then set `status: superseded` and `superseded-by`.

## 7. Decision record format

Use the format of Nygard, and add one section, Alternatives considered [17]. The short Nygard format had the best results for comprehension [18]. Real decision records omit alternatives more frequently than other sections [19].

```
# N. Title
## Status
## Context
## Decision
## Alternatives considered
## Consequences
```

## 8. Tools and data

Use available tools for document checks. [guides/new-project.md](guides/new-project.md) §2 gives their order and their limits. For measurements of instruction files, use the Agent Context File Analysis dataset [6].

## 9. Clauses

Principles are in [principles/](principles/), and practices are in [practices/](practices/). Each clause has its own file. This document does not list them.

Withdrawn clauses:

- "AGENTS.md is a file for efficiency" (a prescription of design v1, 2026-09-24). Its source [4] examined one agent and did not measure correctness. Also, its conditions were different from [3]. This clause is older than the decision records, so its reason stays here.
- R-003 "Change rules when the agent makes an error" (2026-09-25): [decision 0003](decisions/0003-withdraw-r003-p003.md).
- P-003 "No evidence shows that repository overviews increase the task success of agents" (2026-09-25): [decision 0003](decisions/0003-withdraw-r003-p003.md).

## 10. Pilot snapshot

`snapshots/2026-09-24-pilot/` contains measurements of metrics from design v1. This design does not use these metrics. Thus the guidebook does not cite the snapshot as evidence. The snapshot stays as an example: when we divided the sample, the conclusion changed direction. This example is the reason for §3.

## 11. Languages

Each language has one writing standard. A file follows the standard of its language, and it names only that standard.

| Language | Files | Writing standard | Mechanical check |
|---|---|---|---|
| English | All source files | ASD-STE100 Simplified Technical English [24] | No Hangul, and no sentence of more than 25 words |
| Korean | Translations with the name `<name>.ko.md` | fluent-korean [25] | No em dash |

A translation is a separate file next to its source file. If the two are different, the source file is correct. The first line of a translation records the SHA-256 hash of its source file. The check fails when the source file changes and the translation does not. This is the method of [21]. To add a language, add a row to this table and write a decision record.

## 12. Open questions

| Question | Recommendation |
|---|---|
| Population | For instruction files, use the population of [6]. Keep repositories of agent products as a different population |
| Review cycle | Every six months. Set the certainty again when new papers or datasets are available |
