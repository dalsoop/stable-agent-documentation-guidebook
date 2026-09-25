# 12. Revise the setup guide after a simulation

## Status

Proposed (2026-09-25). An agent wrote this record. It applies when the owner changes this status to Accepted and merges the change that adds it.

## Context

[Snapshot 2026-09-25](../snapshots/2026-09-25-setup-simulation/README.md) ran the procedures of guides/new-repository.md and guides/notes.md in a simulation. Each cell had three runs or fewer, one model and one toy repository. Thus the sample integrity invariant (DESIGN.md §3) forbids conclusions for a clause. The snapshot shows these observations:

- Overlapping tasks all merged only when each worker updated its branch from the fetched default branch, ran the checks again and retried. Worktrees without that update merged fewer tasks than a shared checkout.
- Protection with no documented change path blocked a needed fix in each run. A documented change path kept each fix on the change path, with or without protection.
- The bare layout showed no effect over a normal checkout with protection.
- A separate normalizer showed no difference in quality from the author, and it cost less.
- A reader test found three gaps. The guide did not tell where worktrees go or how to verify step 4. It also did not tell how a change request and an approval work.

## Decision

- Step 7 adds the update from the fetched default branch and the second run of the checks. Step 8 adds merges one at a time, with an update and a retry after a conflict or a failed check.
- New step 11 writes the change path in the context file or in CONTRIBUTING. Step 3 refers to it.
- Step 6 tells where a worktree goes. Step 4 tells how to verify the approval rule. Step 9 removes the worktree right after the merge.
- Step 5 states that the snapshot showed no effect of the bare layout. Step 5 of guides/notes.md states that a separate normalizer showed no gain in quality.
- The guides cite the snapshot as an observation. No clause is proposed.

## Alternatives considered

- **Propose a practice from the snapshot.** Rejected: three runs, one model and a toy repository do not meet the sample integrity invariant.
- **Delete the bare layout from step 5.** Rejected: readers copy and link the published steps (DESIGN.md §13). No effect is not a harm, and the bare layout still keeps no worktree on the default branch.
- **Delete the separate normalizer from guides/notes.md.** Rejected: it was not worse, and it cost less. The owner keeps the maker and the checker apart.
- **Insert the update as a new step between steps 7 and 8.** Rejected: that renumbers published steps. Sentences in steps 7 and 8 keep the numbers.
- **Write the change path in step 3.** Rejected: step 3 sets the rule on the code host. The change path is a convention for agents, so it goes in a document (R-002).

## Consequences

- **Counter-evidence:** in the snapshot, the update, the retry and the change requests that each worker sent are mixed with the worktree layout.
  **Judgment:** the guide adds the update as its own sentence, with no clause. It claims no effect of the layout alone.
- **Counter-evidence:** worktrees without the update merged fewer overlapping tasks than a shared checkout.
  **Judgment:** the shared checkout merged more because its workers stacked their changes by accident, and it mixed other tasks into branches. The guide keeps worktrees and adds the update.
- **Counter-evidence:** the reader test found gaps that the revision does not close. The guide still does not tell how to make a change request on a given code host.
  **Judgment:** that depends on the code host, and the guide stays abstract. Step 11 makes each repository write its own change path.
- A second reader test of the revised guide is not done.
