# Turn a note into guidance

Use this procedure when a report of work can change a guide, a clause or a template. The procedure follows the rules for guides in [DESIGN.md](../DESIGN.md) §2. [Decision 0010](../decisions/0010-notes-and-stages.md) gives the reason and the limits. No clause supports this procedure.

Each step gives the steps that it needs, its basis and a completion criterion.

## Roadmap

Roles: the lead agent plans, starts subagents, reviews and decides. It changes no file. A subagent writes the note. A different subagent normalizes the note and makes each fix. The checks validate.

1. [Write the note](#1-write-the-note): the author writes freely, in its own words.
2. [Normalize](#2-normalize): a different session changes the note into the published structure.
3. [Validate](#3-validate): the checks run on the published layers.
4. [Change request](#4-change-request): the note and its normalization merge together.
5. [Discuss a note](#5-discuss-a-note): later, a person forks the session of the author.

## 1. Write the note

1. **Let a subagent write the note in `notes/`.** Use first person, real paths and product names. Tell what the author did and saw. Do not write secrets. Give the front matter of DESIGN.md §2 with `status: raw`.
   Needs: nothing.
   Basis: DESIGN.md §2.
   Done when: the note tells what the author did and what the author saw.
2. **Archive the complete session record of the author.** Copy each transcript file, and do not move it. The agent tool can delete old sessions automatically. Keep the archive in private storage, not in this repository, because a transcript can contain secrets and personal paths.
   Needs: step 1.
   Basis: no clause or reference.
   Done when: the private archive has a copy of each transcript file of the session.
3. **Record the pointer and the hash in the note.** Make a manifest with the SHA-256 of each transcript file. Write the tool, the session id, the archive location and the SHA-256 of the manifest in `session`.
   Needs: step 2.
   Basis: DESIGN.md §2.
   Done when: the `notes` check passes. It cannot verify the private storage.
4. **Archive again if the session continues after the note.** Use a new location, and do not change the first archive. Write a new note with the new location and hash.
   Needs: step 3.
   Basis: no clause or reference.
   Done when: each archive has one note that gives its hash.

## 2. Normalize

5. **Start a different subagent to normalize the note.** The lead agent reviews the result and changes no file.
   Needs: step 3.
   Basis: no clause or reference.
   Done when: the normalizer is not the author. The session record of the lead agent has no change to a file.
6. **Put each fact of the note into the structure that exists.** Add to a guide step, a clause or a template. Use the abstract terms of GLOSSARY.md. Add, and do not rename or renumber (DESIGN.md §13). Link each changed step to the note.
   Needs: step 5.
   Basis: DESIGN.md §2 and §13.
   Done when: each fact is in a published document or is left out on purpose. Each changed step links to the note.
7. **Set the status of the note to `normalized`.** Write each target heading in `normalized-into`. Do not change the body of the note.
   Needs: step 6.
   Basis: DESIGN.md §2.
   Done when: the `notes` check passes.

## 3. Validate

8. **Run the checks.** They are the checks of DESIGN.md §11 and §13, and the `notes` check. The abstraction checks do not read `notes/`.
   Needs: step 7.
   Basis: DESIGN.md §11 and §13.
   Done when: each check passes.

## 4. Change request

9. **Send the note and its normalization in one change request.** Use steps 6 to 8 of [new-repository.md](new-repository.md).
   Needs: step 8.
   Basis: no clause or reference.
   Done when: the default branch contains the note and the normalization.

## 5. Discuss a note

10. **Verify the archive before a fork.** Calculate the SHA-256 of the manifest, and compare it with `session.sha256`. Then verify each transcript against the manifest.
    Needs: step 3.
    Basis: no clause or reference.
    Done when: both hashes are equal, and each transcript matches the manifest.
11. **Fork the archived session, and discuss the note in the fork.** Resume a copy with a new session id. Do not add to the archived original, so that the source of the note stays fixed.
    Needs: step 10.
    Basis: no clause or reference.
    Done when: after the discussion, the SHA-256 of the manifest is still equal to `session.sha256`.
