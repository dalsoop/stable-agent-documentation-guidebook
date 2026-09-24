---
id: R-001
layer: practice
status: proposed
certainty: low
downgraded-for: [risk-of-bias, indirectness]
falsified-if: "In real repositories, instruction files with reasons and without reasons show no difference in growth rate or deletion ratio"
review-by: 2027-03-24
references: [1]
superseded-by: null
---

# State a reason for every instruction

## Clause

Give every instruction in an instruction file a one-line reason.

## Reason

An instruction without a reason stays, because no one can tell whether it is safe to delete [1]. With a reason, the instruction can go once the reason does. This is a practice against the sediment described in P-001.

## Rebuttals

- **Counter-evidence:** the large effect sizes come from synthetic experiments with two or three instructions; the effect on real prompts was smaller and graded by an LLM [1].
  **Judgement:** no effect size is cited. The cost is one line and no side effect is reported, so the practice is worth trying. Certainty low.
- **Counter-evidence:** reasons make the file longer.
  **Judgement:** no cited study links file length to compliance. The added length is one line per instruction.

## Application

```markdown
- Run `./repo lint` after every change. (Reason: rules the linter enforces are not restated here.)
```
