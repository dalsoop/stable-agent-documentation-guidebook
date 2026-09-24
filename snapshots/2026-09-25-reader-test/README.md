# Reader test 2026-09-25: the context file of the case study repository

The first reader test (R-004). It tested the context file (AGENTS.md) of the repository in [the case study](../../guides/case-swift-monorepo.md), a private Swift monorepo. The repository is private, so this record gives a summary with generic names. The raw answers are not published.

## Conditions

- Reader: an agent before each task.
- Reader task: make a change that obeys the conventions, with no question to a person.
- Readers: Grok (grok-4.7) and Codex (gpt-5.6-sol). Each ran once in a new session through a job runner.
- Start: the context file at the repository root. The agent could follow its links.
- Task: add a new app named `text-counter`, a command line tool that prints the number of words in standard input.
- The agents gave a plan and did not change files. A check failed the job if a file changed. Both jobs passed that check.
- The lead wrote the rubric before reading any answer.

## Rubric and results

| # | Criterion | Source in the repository | Core | Grok | Codex |
|---|---|---|---|---|---|
| 1 | Look for an existing app first with the root CLI | ARCHITECTURE, main flows | no | yes | yes |
| 2 | Create the app with the scaffold command, not by hand | ARCHITECTURE, main flows and boundaries | yes | yes | yes |
| 3 | Build and test with the root CLI | ARCHITECTURE, main flows | no | yes | yes |
| 4 | Run the structure check and the lint after the change | Context file, rule 1 | yes | yes | yes |
| 5 | Put the version in the app's own version file | Context file, rule 3 | no | no | yes |
| 6 | Regenerate the generated blocks of the README | ARCHITECTURE, rules for change | no | yes | yes |
| 7 | Add no sentence about the app to ARCHITECTURE or the root README | Context file, rule 4 | yes | yes | yes |
| 8 | Do not sign, distribute or install from this repository | ARCHITECTURE, main flows | no | yes | yes |
| 9 | Ask no question | Reader task | yes | yes | yes |

Both agents met all core criteria, so the context file passed. Scores: Grok 8 of 9, Codex 9 of 9.

## Defects that the test found

1. **Version location.** Both agents named a root `Versions/<app>` file, which does not exist in this repository. The path comes from code that was copied from a different repository, not from the documents. Grok did not name the real version file. Fix: the context file gives the exact path of the version file.
2. **Scope of a rule.** Rule 4 of the context file puts behavior in the help of the root CLI. For an app, the behavior goes in the app's own README and usage file. One agent had to interpret this. Fix: rule 4 names its scope.

## Limits

- The job runner adds its own safety instructions to each prompt. They prescribe a build queue, so criterion 3 is not a pure test of the documents.
- Each agent also had global instructions from outside the repository.
- A plan is not a change. An agent that plans a step can still skip it in real work.
- Two runs of one task. The lead wrote the task, the rubric and the grades, which is a risk of bias.
