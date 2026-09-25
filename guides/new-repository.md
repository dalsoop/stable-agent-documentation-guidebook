# Set up a repository

Use this procedure when you make a new repository, before the first document. It decides where agents write and how changes reach the default branch. The procedure follows the rules for guides in [DESIGN.md](../DESIGN.md) §2. [Decision 0008](../decisions/0008-repository-setup.md) gives the reason and the limits. No study measures the effect of this setup on documents. Thus only step 10 has a clause.

Each step gives the steps that it needs, its basis and a completion criterion.

## Roadmap

Do phases 1, 2 and 4 one time. Do phase 3 for each task, also for each document of phase 4. When an agent reports its work on the setup, use [notes.md](notes.md).

```mermaid
flowchart LR
  P1["1. Code host and<br/>default branch"] --> P2["2. Local layout"]
  P2 --> P4["4. Documents"]
  P4 -->|each task| P3["3. Change flow"]
  P3 -->|next task| P3
```

Step 1 puts this checklist in one place. Mark each phase when the completion criteria of its steps are true.

- [ ] Phase 1, [code host and default branch](#1-code-host-and-default-branch): steps 1 to 4
- [ ] Phase 2, [local layout](#2-local-layout): step 5
- [ ] Phase 3, [change flow](#3-change-flow): steps 6 to 9, for the first task
- [ ] Phase 4, [documents](#4-documents): step 10

## 1. Code host and default branch

1. **Keep the checklist of the roadmap in one place.** Use one tracker item or one file for each repository. Other documents link to it and do not copy it.
   Needs: nothing.
   Basis: [23].
   Done when: one place holds the checklist, and no other document of the repository contains a copy.
2. **Make the repository on the code host with one commit on the default branch.**
   Needs: step 1.
   Basis: no clause or reference.
   Done when: the default branch exists on the code host.
3. **Protect the default branch.** Make a protection rule: no one can push to the default branch. A change reaches it only through a change request. The rule also applies to administrators.
   Needs: step 2.
   Basis: [34] [35].
   Done when: the code host rejects a direct push to the default branch, also from an administrator.
4. **Require an approval and the checks before a merge.** Add each new check to the protection rule when you add the check.
   Needs: step 3.
   Basis: [34] [35]. The checks come from steps 8 to 10 of [new-project.md](new-project.md).
   Done when: a change request with no approval cannot merge, and each check is required.

## 2. Local layout

5. **Clone the repository as a bare repository.** A bare repository has no worktree of its own. Thus no worktree is on the default branch. Run `git clone --bare <url> <name>.git`. A bare clone has no remote-tracking branches, so set them: `git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"`. Then run `git fetch origin`.
   Needs: step 2.
   Basis: [33]. [Note 2026-09-25](../notes/2026-09-25-bare-worktree-trial.md) records one trial.
   Done when: `git worktree list` shows only the bare repository, with the mark `(bare)`.

## 3. Change flow

6. **Start the task in a new worktree from the fetched default branch.** Run `git fetch origin`. Then run `git worktree add -b <branch> <path> origin/<default branch>`. To read the default branch, use `git show origin/<default branch>:<file>`.
   Needs: step 5.
   Basis: [33]. [Note 2026-09-25](../notes/2026-09-25-bare-worktree-trial.md) records one trial.
   Done when: `git worktree list` shows the new worktree on its branch, and no worktree on the default branch.
7. **Send the branch as a change request.**
   Needs: steps 3 and 6.
   Basis: [34] [35].
   Done when: the change request exists, and the required checks ran on it.
8. **Merge the change request after the checks pass and a reviewer approves.**
   Needs: steps 4 and 7.
   Basis: [34] [35].
   Done when: the default branch contains the change, and the change request records the approval.
9. **Remove the worktree.** Run `git worktree remove <path>`.
   Needs: step 8.
   Basis: [33]. [Note 2026-09-25](../notes/2026-09-25-bare-worktree-trial.md) records one trial.
   Done when: `git worktree list` shows no worktree for a merged branch.

## 4. Documents

10. **Write the documents with [new-project.md](new-project.md), one task at a time.** In its step 5, add one rule to the context file. The rule: start each task in a new worktree from the fetched default branch. Give the rule a reason. Nothing on the code host makes an agent start in a new worktree. Do not write the protection rule in the context file, because the code host enforces it.
    Needs: steps 4 and 5.
    Basis: R-001, R-002.
    Done when: the context file has the rule for worktrees with a reason. It does not state the protection rule.
