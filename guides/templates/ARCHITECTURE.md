<!-- Skeleton: fill in the angle brackets, then delete this comment. Write only what rarely changes. Leave out lists, versions, options and numbers. -->
# Architecture

<What this repository is for, in one paragraph: who uses it and what it contains.>

## Folder layout

```
<repository>/
├── <folder>/   <role in one line>
└── <folder>/   <role in one line>
```

<Conventions inside the folders, for example "one folder is one app". Do not list what changes often; name the command that lists it.>

## Dependency direction

<What uses what, that the reverse direction is not allowed, and which files hold the actual dependencies.>

## Main flows

<The order of work when adding a feature, and the command used at each step.>

## Boundaries

<Rules that keep the structure: what must not use what, and which tool must not hold which feature.>

## When changing

Rules for agents and people who edit this document or the README. Source: `guides/new-project.md` §2 in https://github.com/dalsoop/stable-agent-documentation-guidebook. Copy the list again when the guidebook changes.

### Writing rules

1. **Write only what rarely changes.** Only the five sections above; behaviour belongs in the tool's help.
2. **Do not append sentences when a feature changes.** Behaviour goes to the help, reasons to a decision record.
3. **Name code elements so they can be searched.** Link only what a check verifies exists.
4. **Keep lists derived from code out of this document and name the command that queries them.** Where another document needs a list, generate it and fail the check when the two differ.
5. **Re-read from the start every <cycle>, and delete stale sentences.** Last re-read: <date>.

### Check status

- `<check command>` verifies: <required headings, links, generated blocks, ...>
- Not checked, verify by hand: <rules>

## References

<The sources these writing rules rest on.>
