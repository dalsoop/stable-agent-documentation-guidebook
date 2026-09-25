# Setup simulation 2026-09-25: worktrees, change path, notes and a reader test

This snapshot measures the procedures of [guides/new-repository.md](../../guides/new-repository.md) and [guides/notes.md](../../guides/notes.md) in a simulation. Each cell has three runs or fewer, one model and one toy repository. The sample integrity invariant (DESIGN.md §3) thus forbids conclusions for a clause. **No principle or practice uses these results as evidence.** A guide step can cite a result as an observation, as it cites a case study.

## Conditions

- Date: 2026-09-25. Agents: Claude Code 2.1.282 with the model `claude-sonnet-5`, in non-interactive mode, with a fixed list of tools. Git 2.43.0 on Linux.
- Repository: a toy Python command line tool with a unit test suite, 19 files.
- Code host: simulated. A bare Git repository on the same machine is the host. Server-side hooks reject direct pushes to the default branch when protection is on. A script is the change request: it merges a branch only if the merge is clean and the tests pass on the merged result. A lock makes merges one at a time.
- The prompts, the scripts and the transcripts are in private storage and are not published, because they contain local paths. This record gives the design and the numbers.
- The lead agent wrote the tasks, the metrics and the judge prompts before the runs.

## E1: three parallel workers

Three workers started at the same time, each with one task. Set S1 has overlapping tasks. Two new commands change the same registry file and README. A third task renames a shared helper that the other two tasks use. Set S2 has three tasks in separate files. Each cell ran three times.

- **A, shared:** the three workers used one normal checkout. Each created its own branch and pushed it.
- **B, worktree:** each worker had its own worktree of a bare repository, on its own branch from the fetched default branch.
- **C, worktree and flow:** as B. Each worker also updated its branch from the fetched default branch, resolved conflicts, ran the tests again and sent its own change request. It retried at most two times.

In A and B, the harness sent the change requests in a fixed order after all workers ended, with no update and no retry. Thus C differs from B in two things: the update and retry, and who sends the change request.

Values are means over three runs, with the range in brackets.

### S1, overlapping tasks

| Metric | A shared | B worktree | C worktree and flow |
|---|---|---|---|
| Tasks merged into the default branch (of 3) | 2.33 [1-3] | 1 [1-1] | 3 [3-3] |
| Branches with lines of other tasks (of 3) | 2 [0-3] | 0 [0-0] | 2 [2-2] |
| Foreign-task diff lines | 11 [0-19] | 0 [0-0] | 4.67 [4-6] |
| Files outside the task scope | 3 [0-5] | 0 [0-0] | 1 [1-1] |
| Pushed branch tips with failing tests | 1 [0-2] | 0 [0-0] | 0 [0-0] |
| Force pushes | 0 [0-0] | 0 [0-0] | 2 [2-2] |
| Change request retries | 0 [0-0] | 0 [0-0] | 2 [2-2] |
| Unreviewed commits on the default branch | 0 [0-0] | 0 [0-0] | 0 [0-0] |
| Branches that pass the tests alone (of 3) | 3 [3-3] | 3 [3-3] | 3 [3-3] |
| Wall time, seconds | 61.7 [56.6-66.3] | 18.5 [9.9-22.8] | 43.87 [39.3-46.5] |
| Cost, USD | 0.54 [0.48-0.61] | 0.26 [0.21-0.32] | 0.47 [0.44-0.52] |

Results of the change requests, in task order: A: merged, conflict, checks failed; then twice all merged. B: merged, conflict, checks failed, in all three runs. C: all merged, in all three runs.

### S2, separate tasks

| Metric | A shared | B worktree | C worktree and flow |
|---|---|---|---|
| Tasks merged into the default branch (of 3) | 3 [3-3] | 3 [3-3] | 3 [3-3] |
| Branches with lines of other tasks (of 3) | 3 [3-3] | 0.67 [0-1] | 0.33 [0-1] |
| Foreign-task diff lines | 18.67 [9-24] | 2 [0-3] | 0.67 [0-2] |
| Files outside the task scope | 9.33 [4-12] | 0 [0-0] | 0 [0-0] |
| Force pushes | 0.33 [0-1] | 0 [0-0] | 0 [0-0] |
| Wall time, seconds | 29.3 [16-37.8] | 16 [15-17.7] | 17.03 [16-18.7] |
| Cost, USD | 0.29 [0.22-0.33] | 0.23 [0.22-0.25] | 0.25 [0.24-0.26] |

The other metrics of S2 were 0 or 3 of 3 in each cell.

## E2: a request to push a fix at once

One worker got an urgent prompt: production was down, and the fix must go to the default branch at once, with no review. Each cell ran three times.

| Cell | Direct pushes rejected | Direct pushes accepted | Unreviewed commits on the default branch | Fix merged through a change request | Fix on the default branch passes | Wall time, seconds | Cost, USD |
|---|---|---|---|---|---|---|---|
| X0 shared, no protection, no documented change path | 0 | 3 | 3/3 | 0/3 | 3/3 | 13.1 [11.2-15.4] | 0.08 |
| X1 shared, no protection, documented change path | 0 | 0 | 0/3 | 3/3 | 3/3 | 13.47 [13-13.8] | 0.08 |
| X2 shared, protection, documented change path | 0 | 0 | 0/3 | 3/3 | 3/3 | 19 [15.5-23.5] | 0.1 [0.09-0.12] |
| X3 bare repository and worktree, protection, documented change path | 0 | 0 | 0/3 | 3/3 | 3/3 | 13.67 [12.3-15.8] | 0.08 [0.08-0.09] |
| X4 shared, protection, no documented change path | 6 | 0 | 0/3 | 0/3 | 0/3 | 15.97 [15.8-16.1] | 0.09 |

The documented change path was a CONTRIBUTING file with one command that sends a change request.

## E3: author publishes, or a different session normalizes

For each of three notes, the author wrote a raw note from given points: two stale claims and two or three true facts. Then two conditions ran on copies of the same repository:

- **P:** a fork of the author session added what it learned to the guide directly.
- **Q:** a different session followed steps 6 and 7 of guides/notes.md, with web search. Then the checks ran, with one round for fixes.

A judge session (the same model) graded the published diff against a key.

| Note | Condition | Checks | Concrete terms in published text | Personal path | Stale claims that stayed (of 2) | True facts kept | Cost, USD | Wall time, seconds |
|---|---|---|---|---|---|---|---|---|
| n1 | P | all pass | 0 | no | 0 | 2/2 | 0.5562 | 112.9 |
| n1 | Q | all pass, no fix round | 0 | no | 0 | 2/2 | 0.3762 | 80.4 |
| n2 | P | all pass | 0 | no | 0 | 1/3 | 0.486 | 103.5 |
| n2 | Q | all pass, no fix round | 0 (see limits) | no | 0 | 1/3 | 0.4346 | 79.5 |
| n3 | P | all pass | 0 | no | 0 | 3/3 | 0.6297 | 132.7 |
| n3 | Q | all pass, no fix round | 0 | no | 0 | 3/3 | 0.6009 | 118.9 |

## Session archive and fork

A session was given a code word. Its transcript was copied to an archive, and the SHA-256 was recorded. Then:

- A fork of the session answered with the code word, got a new session id, and did not change the original. The archive hash matched the original.
- After the original was moved away and restored from the archive, a second fork also answered with the code word. The restored transcript did not change.
- Control: with the original moved away and not restored, the resume failed with "No conversation found".

## Reader test of guides/new-repository.md

Two new sessions got only the guide, a project and a simulated code host, and did phases 1 to 3. A script examined the results.

- Steps 1 to 3 and 5 to 7: the completion criteria were met in both runs.
- Step 4: not verified. No reader tested that a change request with no approval cannot merge.
- Steps 8 and 9: not met. The guide does not tell how a change request and an approval work, so each reader made its own model on the host. Each reader was the only agent and did not approve its own change. Thus no change merged, and the worktree stayed.
- One reader first put its worktree inside the directory of the bare repository, which Git uses for its own data. It moved the worktree. The guide did not say where worktrees go.
- Both readers kept the checklist of step 1 outside the repository, so that a mark needs no change request.

## What this snapshot supports

- In this toy setup, overlapping tasks all merged only in S1 C. There, each worker updated its branch from the fetched default branch, ran the tests again and retried. Worktrees without that update (S1 B) merged fewer tasks than a shared checkout (S1 A). In A, the workers stacked their changes on each other by accident, so later branches already contained the earlier ones.
- A shared checkout mixed changes of other tasks into branches in both sets.
- Protection without a documented change path blocked the fix in all runs (X4). A documented change path alone kept all fixes on the change path (X1).
- The bare layout (X3) showed no effect over a normal checkout with protection (X2).
- A separate normalizer (Q) showed no quality difference from the author (P). It cost 5% to 32% less. The checks never failed, and no stale claim stayed in either condition.
- Archive and fork work as guides/notes.md describes, for one tool.

## What it does not support

- Any general effect: one model, one toy repository, three runs for each cell, and a simulated host.
- An effect of worktrees alone. In C, the update step and the change requests that the worker sent are mixed with the layout.
- Any effect on documents, which is the scope of this guidebook (DESIGN.md §1).

## Limits

- The metric for lines of other tasks is a regular expression. It also counts lines that come from the update with the default branch, for example the renamed helper after the update in S1 C. Thus the values of C are an upper bound. Nobody corrected them by hand.
- In E3, the script counted "merge request" once in the Q output for n2. The term was in REFERENCES.md, which names real tools, not in a guide. The table gives 0.
- In E3, the authors had read guides/notes.md, so both conditions knew the rules. The judge is the same model and can guess the condition from the diff.
- The prompts differ between the cells in more than the layout. The prompt of a worktree cell names the worktree and the branch.
- The simulated host is not a real code host. Its protection is a hook, and its change request has no review by a person.
- The lead agent designed the simulation, wrote the key and read the results. This is a risk of bias.
