---
id: R-001
layer: practice
status: adopted
certainty: low
downgraded-for: [risk-of-bias, indirectness]
falsified-if: "In real repositories, context files with reasons and context files without reasons have the same growth rate and the same ratio of deletions"
review-by: 2027-03-24
references: [1]
superseded-by: null
---

# Give a reason for each instruction

## Clause

Give each instruction in a context file a reason of one line.

## Reason

People keep an instruction without a reason, because they cannot know if it is safe to delete it [1]. If the instruction has a reason, people can delete it when the reason goes away. This practice works against the growth by addition that P-001 describes.

## Refutations

- **Counter-evidence:** the large effect sizes come from synthetic experiments with two or three instructions. The effect on real prompts was smaller, and an LLM graded it [1].
  **Judgment:** this clause cites no effect size. The cost is one line, and no study reports a side effect. Thus the practice is worth a trial, and its certainty is low.
- **Counter-evidence:** reasons make the file longer.
  **Judgment:** no cited study connects file length and compliance. Each reason adds one line.

## Application

```markdown
- Run `./repo lint` after each change. (Reason: this file does not repeat the rules that the linter checks.)
```
