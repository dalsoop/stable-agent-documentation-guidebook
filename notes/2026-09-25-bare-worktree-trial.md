---
author: agent-ad75e126f9fdb8296, a subagent of the lead session 23113130-bba2-4202-816c-c45c0893af66
date: 2026-09-25
repository: stable-agent-documentation-guidebook
status: normalized
normalized-into: [guides/new-repository.md#2-local-layout, guides/new-repository.md#3-change-flow]
session:
  tool: Claude Code
  id: agent-ad75e126f9fdb8296
  archive: ~/.local/share/agent-sessions/2026-09-25-23113130-bba2-4202-816c-c45c0893af66/
  sha256: 6e99f677c25bc095bd13e500a1d739f5a50192f36c2db09de85edc095bc79aca
---

# I tried a bare clone with one worktree for each task on a Linux machine

## What I did

I wrote the change for decision 0008 in a normal clone, made with `gh repo clone`, under `/tmp/claude-1000/<lead-session-folder>/scratchpad/guidebook`. So this change itself did not use a bare clone.

To test the commands of the new guide, I made a test repository `origin` with one empty commit on `main` in `/tmp/claude-1000/<lead-session-folder>/scratchpad/wt`. Then I ran these commands:

```
git clone --bare origin r.git
cd r.git
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
git fetch origin
git worktree list
git worktree add -b task1 ../task1 origin/main
git worktree list
git show origin/main:README
git worktree remove ../task1
git worktree list
```

## What I saw

- After the fetch, `git worktree list` showed only `.../wt/r.git  (bare)`.
- `git worktree add` made `.../wt/task1` on the branch `task1` at commit `e350934`.
- `git show origin/main:README` failed, because my test commit had no files. The command form worked.
- After `git worktree remove ../task1`, the list showed only the bare repository again.
- I did not test a clone without the fetch setting. The git-clone documentation says that a bare clone makes no remote-tracking branches.
- I did not test a direct push to a protected default branch, because my task was local only.

## My session record

The lead agent archived all transcripts of this session at 15:35 on 2026-09-25. I wrote this note after that time. `MANIFEST.sha256` in the archive lists the SHA-256 of each transcript, and the front matter gives the hash of that manifest. My transcript continued after 15:35, so the archive does not have the end of my session. At the end of the session, archive it again in a new folder, and write a new note with that folder and hash.

To discuss this note with me, verify the archive, then fork it. I did not test the fork command with a subagent id.

```
cd ~/.local/share/agent-sessions/2026-09-25-23113130-bba2-4202-816c-c45c0893af66/
sha256sum MANIFEST.sha256   # must equal session.sha256
sha256sum -c MANIFEST.sha256
claude --resume agent-ad75e126f9fdb8296 --fork-session
```

## Normalized into

- The bare clone and the fetch setting: [new-repository.md step 5](../guides/new-repository.md#2-local-layout).
- The worktree for each task, `git show` for the default branch, and the removal: [new-repository.md steps 6 and 9](../guides/new-repository.md#3-change-flow).
