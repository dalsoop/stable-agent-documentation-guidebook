# 8. Add the setup of a repository to the scope as a guide

## Status

Proposed (2026-09-25). An agent wrote this record. It applies when the owner changes this status to Accepted and merges the change that adds it.

## Context

[DESIGN.md](../DESIGN.md) §1 limits the scope to repository documents. The owner sets up each new repository with two conventions:

- No worktree is on the default branch. Each task has its own worktree from the latest default branch.
- No one pushes or merges to the default branch directly. Each change goes through a change request with a review.

The reason of the owner: each change goes through the path of the change request, with a review, the checks and a record.

Two parts of this setup decide if [guides/new-project.md](../guides/new-project.md) has an effect:

- **The version that an agent reads.** A worktree on the default branch becomes old when nobody updates it. An agent that starts a task there reads an old context file. The reader test of step 13 has the same problem.
- **The checks.** Steps 8 to 10 make checks fail. A direct push to the default branch skips these checks. A local hook does not stop it, because `--no-verify` skips the pre-commit hook [33].

Several practitioner sources recommend a worktree for each task and a bare repository [39] [40]. They give no measurement. One experiment compared agents in one shared worktree with agents in a worktree each. The agents with separate worktrees had better task results [36]. That study measures task success, which §1 puts out of scope. We found no study of the effect of the setup on documents.

## Decision

- Add to the scope in DESIGN.md §1: the setup of a repository that decides where agents write and how changes reach the default branch. Only its effect on the documents that agents read and on the checks is in scope.
- Add the guide `guides/new-repository.md`. A reader uses it before `guides/new-project.md`. It has four phases in a fixed order, a roadmap and a checklist. Each repository keeps the checklist in one place. Its steps cite only the documentation of the tools [33] [34] [35], and R-001 and R-002 for the context file.
- The README gives the order of the guides, because its reader task is to find the next document.
- The guide uses terms that apply to each code host: change request, protection rule and default branch. GLOSSARY.md gives the names on each host.
- Cite [36] only for this decision, as DESIGN.md §1 does for [4].

## Alternatives considered

- **Add a step to guides/new-project.md.** Rejected: that guide makes documents. The setup must be complete before step 1 of that guide, and it has more than one step.
- **Keep the setup in a different repository.** Rejected: the setup matters here only because of the checks and the reader test of `guides/new-project.md`. A different repository would keep the same reason in two places.
- **Use local hooks that block commits on the default branch.** Rejected: `--no-verify` skips the pre-commit hook [33], and each clone needs its own hook. A protection rule on the code host applies to all clones.
- **Make the setup a practice with the certainty very low.** Rejected: no source measures the in-scope effect, and [36] measures task success. As a clause, the setup would look like it has evidence. [Decision 0002](0002-add-guides-layer.md) rejected a practice for the same reason.
- **Add a rule to guides/templates/AGENTS.md.** Rejected: the template contains only rules that each repository needs. Step 10 of the new guide tells the reader to write the rule.
- **Give the order of the guides in a new file, `guides/README.md`.** Rejected: that file would need its own reader and reader test (R-004). The README already names each guide and its reader.

## Consequences

- DESIGN.md §1 and §11, `.vale.ini`, guides/new-project.md, GLOSSARY.md, REFERENCES.md, README.md and README.ko.md change. The limit of 20 words for procedure sentences also applies to the new guide.
- The refutations below stay in this record, because the guide has no clause for the setup (DESIGN.md §5).
- **Counter-evidence:** separate branches do not prevent merge conflicts. 27.67% of agent pull requests had a conflict [38]. Pairs of pull requests from the same agent had a conflict in 19.8% of cases [37].
  **Judgment:** the setup does not claim to prevent conflicts. It keeps changes apart until the change request, where the checks run.
- **Counter-evidence:** a worktree isolates files, not ports, databases or external accounts. Each worktree needs its own installed dependencies [39].
  **Judgment:** this is outside the scope of the guidebook. A repository that needs more isolation adds its own rules.
- **Counter-evidence:** some tools expect a normal clone and do not recognize a bare repository [40].
  **Judgment:** a repository with such a tool writes an exception in the rules for change of ARCHITECTURE.
- **Counter-evidence:** a protection rule can have exceptions. On one code host, administrators skip the rule by default [34]. On another, a user who can change the rule can remove it [35].
  **Judgment:** step 3 applies the rule to administrators too. Its completion criterion tests a direct push.
- If a study measures the effect of the setup on the documents that agents read, a new decision record can propose a clause.
