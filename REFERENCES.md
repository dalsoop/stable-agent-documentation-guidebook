# References

Each entry tells what this repository takes from the source. It also gives the limits that the authors state or that this repository found. The limits change the certainty of clauses ([DESIGN.md](DESIGN.md) §4). Titles stay in their original words.

## Context files and repository documents

**[1]** K. Chakrabarti, "Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding," arXiv:2608.11095, 2026. https://arxiv.org/abs/2608.11095
- Takes: an analysis of the lifetime of 247,694 instructions in 1,867 repositories. Context files grow by addition, and people rarely delete old instructions. The prescription to give a reason with each instruction.
- Limits: one author and no peer review. The large effect sizes of the prescription come from synthetic experiments with two or three instructions. The effect on real prompts is smaller, and an LLM graded it.

**[2]** C. Treude, S. Baltes, "Context Rot in AI-Assisted Software Development: Repurposing Documentation Consistency for AI Configuration Artifacts," arXiv:2606.09090, 2026. https://arxiv.org/abs/2606.09090
- Takes: the use of available checkers of documentation consistency on context files, with no new tool.
- Limits: of 50 findings that a person examined, 36% were false positives or ambiguous. One person did the validation. The authors call their prevalence figures a possible signal only.

**[3]** T. Gloaguen, N. Mündler, M. Müller, V. Raychev, M. Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?," arXiv:2602.11988, 2026. https://arxiv.org/abs/2602.11988
- Takes: repository overviews did not help, and agents obeyed the instructions. The advice to put only non-standard conventions in files that people write.
- Limits: Python repositories only. Files that developers wrote had a positive effect, but the effect was not statistically significant.

**[4]** J. L. Lulla, S. Mohsenimofidi, M. Galster, J. M. Zhang, S. Baltes, C. Treude, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents," arXiv:2601.20404, 2026. https://arxiv.org/abs/2601.20404
- Takes: nothing. Only the scope decision in DESIGN.md §1 cites it.
- Limits: one agent, ten repositories and small tasks. The study did not measure correctness.

**[5]** P. Khatri, "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories," arXiv:2607.27250, 2026. https://arxiv.org/abs/2607.27250
- Takes: the study found no effect of the context strategy on correctness.
- Limits: one author, 17 tasks and 3 repositories. The study cannot exclude a medium effect.

**[6]** W. Chatlatanagulchai et al., "Agent READMEs: An Empirical Study of Context Files for Agentic Coding," arXiv:2511.12884, 2025 (revised 2026). https://arxiv.org/abs/2511.12884 · Dataset: https://github.com/woraamy/Agent-Context-File-Analysis
- Takes: 2,303 context files from 1,925 repositories. The files change through frequent small additions. This repository uses the dataset as its sample of context files.
- Limits: the population contains only repositories from AIDev with five or more stars.

**[7]** W. S. Tan, M. Wagner, C. Treude, "Detecting Outdated Code Element References in Software Repository Documentation," *Empirical Software Engineering* 29, article 5, 2024. https://link.springer.com/article/10.1007/s10664-023-10397-6 · arXiv:2212.01479
- Takes: the share of projects with at least one outdated code reference at the time of the study. It was 28.9% of 1,000 popular GitHub projects and 5.4% of 2,279 Google projects. The rate grew with project size.
- Limits: the detection uses regular expressions, and [2] found its false positives again. The abstract says that most projects had one at some time in their history. The two samples above show that the rate depends on the population.

**[8]** W. S. Tan et al., DOCER tool. https://github.com/wesleytanws/DOCER_tool · Paper: arXiv:2307.04291
- Takes: a GitHub Actions tool that finds outdated code references in each pull request.
- Limits: it has the false positives that [2] reports.

**[9]** G. Cai, R. Li, P. Liang, Z. Li, M. Shahin, "Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study," arXiv:2606.12231, 2026. https://arxiv.org/abs/2606.12231
- Takes: in 7,310 rules from 83 open source projects, the most frequent changes were context expansions (29.17%) and enrichments (26.59%). The rise of compliance after rule updates was used only by the withdrawn R-003, and this repository does not cite it now.
- Limits: the files are rules of AI IDEs, not context files, so their use for context files is indirect. Correlation, not cause. An LLM graded compliance. Most projects are small TypeScript web projects with one developer.

## Samples and evidence

**[10]** E. Kalliamvakou et al., "The Promises and Perils of Mining GitHub," MSR 2014. https://dl.acm.org/doi/10.1145/2597073.2597074
- Takes: the problems of samples from GitHub data.

**[11]** S. Baltes, P. Ralph, "Sampling in Software Engineering Research: A Critical Review and Guidelines," *Empirical Software Engineering*, 2022. https://arxiv.org/abs/2002.07764
- Takes: guidelines for samples.

**[12]** GRADE Working Group, GRADE Handbook and guidance series. https://book.gradepro.org/guideline/overview-of-the-grade-approach
- Takes: the four levels of certainty and the five domains that lower a certainty.
- Limits: GRADE is for clinical guidelines. This repository decided to apply it to research on software documentation.

## Counter-evidence

**[13]** N. L. Schroeder, A. C. Kucera, "Refutation Text Facilitates Learning: A Meta-Analysis of Between-Subjects Experiments," *Educational Psychology Review*, 2022. https://pubmed.ncbi.nlm.nih.gov/35095236/
- Takes: texts that state a misconception and refute it help people learn (44 comparisons, g = 0.41).
- Limits: the study examined human learners. Its use for agent documents is indirect.

**[14]** D. J. O'Keefe, "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages," *Communication Yearbook* 22, 1999. https://academic.oup.com/anncom/article-pdf/22/1/209/61205855/anncom_22_1_209.pdf
- Takes: two-sided messages with a refutation are more credible and more persuasive. Two-sided messages without a refutation are less persuasive.
- Limits: an old study of human readers.

**[15]** C. J. Clark, P. E. Tetlock, Adversarial Collaboration Project. https://web.sas.upenn.edu/adcollabproject/publications/
- Takes: a procedure. State each disagreement so that a test can resolve it, and agree before the test to accept the result. This is the source of falsification criteria.

**[16]** Z. Zhou, T. Zhou, R. Jia, J. May, "How Language Models Process Negation," arXiv:2605.03052, 2026. https://arxiv.org/abs/2605.03052
- Takes: language models can process negation, but shortcuts frequently cause them to miss it. This is the reason for positive context files.
- Limits: the study did not test context files.

## Decision records

**[17]** M. Nygard, "Documenting Architecture Decisions," 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

**[18]** F. Nogueira, N. Silva, T. Conte, "One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption," arXiv:2604.27333, 2026. https://arxiv.org/abs/2604.27333
- Takes: in an experiment with students, the Nygard format had a higher total score than MADR.
- Limits: the participants were undergraduate students.

**[19]** N. Miccio Palermo, A. Tommasel, J. A. Diaz-Pace, "A Text Mining and Classification Approach for Analyzing Architecture Decision Records," arXiv:2609.07375, 2026. https://arxiv.org/abs/2609.07375
- Takes: in the decision records of approximately 550 repositories, alternatives and decision drivers were frequently absent.

## Tools, language and practitioner sources

**[20]** N. Batchelder, Cog. https://nedbatchelder.com/code/cog/index

**[21]** rust-analyzer, `check_lsp_extensions_docs` in `xtask/src/tidy.rs`. https://github.com/rust-lang/rust-analyzer/blob/master/xtask/src/tidy.rs

**[22]** A. Kladov (matklad), "ARCHITECTURE.md," 2021. https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- Takes: the structure of an ARCHITECTURE document, which is an overview, a codemap, invariants and boundaries. Write only information that changes rarely. Do not try to keep the document in sync with the code, but read it again a few times each year. Give names of files and types that a reader can search for, not links.
- Limits: an essay from a practitioner with no empirical evaluation. GRADE treats it as expert opinion.

**[23]** M. Pocock, "writing-great-skills," in *mattpocock/skills* (MIT). https://github.com/mattpocock/skills
- Takes: terms for the removal of unnecessary text from instructions, which are single source of truth, duplication, no-op and relevance. One main term for each concept.
- Limits: the author wrote it for agent skills, not for repository documents. It is guidance from a practitioner with no empirical evaluation.

**[24]** ASD, "ASD-STE100 Simplified Technical English," specification. https://www.asd-ste100.org/
- Takes: the style guide for English. Its rules for sentence length, verb forms, noun clusters and one meaning for each word.
- Limits: the specification is for technical manuals in aerospace. Its approved dictionary is not in this repository, so the check verifies only sentence length.

**[25]** snflkd, "fluent-korean," Claude Code output style (MIT). https://github.com/snflkd/fluent-korean
- Takes: the style guide for Korean. Complete sentences, no omitted particles or endings, precise Sino-Korean words, no metaphors in place of plain words, and no em dash.
- Limits: guidance from a practitioner with no empirical evaluation. The author wrote it for the output of an assistant for code. The check verifies only the em dash rule.

## README content and diagrams

**[26]** G. A. A. Prana, C. Treude, F. Thung, T. Atapattu, D. Lo, "Categorizing the Content of GitHub README Files," *Empirical Software Engineering* 24(3), 2019. https://arxiv.org/abs/1802.06997
- Takes: 4,226 README sections from 393 repositories. Sections about "what" and "how" are frequent. Many README files do not tell the purpose or the status of the repository.
- Limits: the sample is from 2017 and has no context files. The study classifies content and does not measure its effect on readers.

**[27]** T. Ho-Quang, R. Hebig, G. Robles, M. R. V. Chaudron, M. A. Fernandez, "Practices and Perceptions of UML Use in Open Source Projects," ICSE-SEIP 2017. https://ieeexplore.ieee.org/document/7965444/
- Takes: a survey with 485 answers from contributors of 458 open source projects. Collaboration was the most important reason to use diagrams, and diagrams helped new contributors.
- Limits: the answers are perceptions, not measurements. The study examined UML diagrams and human contributors, not README diagrams or agents.

**[28]** GitHub Docs, "Creating diagrams." https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
- Takes: GitHub shows Mermaid text in a fenced code block with the `mermaid` identifier as a diagram.

**[29]** Vale, a linter for prose. https://vale.sh/ · https://github.com/errata-ai/vale
- Takes: sentence length checks for English files, with a configuration in `.vale.ini` and rules in `.github/styles/`.
- Limits: it does not check sentences in table cells.

## Readers of documents

**[30]** AGENTS.md, "A simple, open format for guiding coding agents." Agentic AI Foundation, Linux Foundation. https://agents.md/
- Takes: README files are for humans, and AGENTS.md is a README for agents. Each file has its own reader.
- Limits: a format specification from practitioners, with no empirical evaluation.

**[31]** D. Procida, "Diátaxis." https://diataxis.fr/
- Takes: the type of a document follows from what its reader tries to do: learn, do a task, look up a fact or understand.
- Limits: a framework from a practitioner, with no empirical evaluation. It was written for product documentation, not for context files.

**[32]** A. Iorio, F. A. Spencer, M. Falavigna et al., "Use of GRADE for assessment of evidence about prognosis: rating confidence in estimates of event rates in broad categories of patients," *BMJ* 350, h870, 2015. https://researchonline.lshtm.ac.uk/id/eprint/2131850/1/bmj.h870.full.pdf
- Takes: for evidence about how often an event occurs in a population, a body of observational studies starts at high certainty.
- Limits: written for clinical prognosis. Its use for phenomena in software repositories is this repository's judgment.

## Repository setup

**[33]** Git documentation, "git-worktree," "git-clone" and "githooks." https://git-scm.com/docs/git-worktree · https://git-scm.com/docs/git-clone · https://git-scm.com/docs/githooks
- Takes: a repository can have more than one worktree, and `git worktree add -b` makes a branch and its worktree. A branch cannot be in two worktrees. A bare clone makes no remote-tracking branches. `--no-verify` skips the pre-commit hook.
- Limits: tool documentation. It tells how the tool works, not what the setup changes.

**[34]** GitHub Docs, "About protected branches." https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Takes: a protected branch can require a pull request with approvals and passed status checks, and can restrict pushes. By default, administrators skip these rules. A separate setting applies them to administrators too.
- Limits: tool documentation for one code host.

**[35]** GitLab Docs, "Protected branches." https://docs.gitlab.com/user/project/repository/branches/protected/
- Takes: the default branch is protected by default. To prevent direct pushes, set "Allowed to push and merge" to "No one".
- Limits: tool documentation for one code host. A user who can change the protection can remove it.

**[36]** J. Geng, G. Neubig, "Effective Strategies for Asynchronous Software Engineering Agents," arXiv:2603.21489, 2026. https://arxiv.org/abs/2603.21489
- Takes: nothing for a guide step. Only decision 0008 cites it. With one model, agents in a worktree each scored higher than agents in one shared worktree. The scores were 63.3% and 55.5% on PaperBench, and 59.1% and 56.1% on Commit0-Lite.
- Limits: it measures task success, which is out of scope (DESIGN.md §1). Two authors, two benchmarks, one model for this comparison and no peer review.

**[37]** G. Xu, A. Subramanian, N. Karthik, "AI Agent Pull Requests on GitHub: Frequency, Structure, and Merge Conflict Rates," arXiv:2607.04697, 2026. https://arxiv.org/abs/2607.04697
- Takes: the study merged 747 pairs of agent pull requests that were open at the same time. Pairs from the same agent had a textual conflict in 19.8% of cases. Pairs from different agents had a conflict in 41.7%.
- Limits: the study does not examine worktrees. It replays merges and does not observe how the agents worked. No peer review.

**[38]** D. Ogenrwot, J. Businge, "AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub," AIware 2026. https://arxiv.org/abs/2604.03551
- Takes: 27.67% of more than 107,000 agent pull requests had a merge conflict in a merge simulation.
- Limits: the study does not examine worktrees. The pull requests come from separate branches, so the rate shows only that separate branches do not prevent conflicts.

**[39]** K. Wirth, "How to Run Coding Agents in Parallel with Git Worktrees," Nimbalyst, 2026. https://nimbalyst.com/blog/git-worktrees-for-ai-coding-agents-complete-guide/
- Takes: worktrees isolate files, not ports, databases or external accounts. Each worktree needs its own installed dependencies.
- Limits: a blog post from a vendor of a tool for worktrees, with no measurement.

**[40]** GitWorktree.org, "Git Bare Repository with Worktrees — Setup Guide." https://www.gitworktree.org/guides/bare-repo
- Takes: the layout of a bare repository with one worktree for each branch, and the fetch setting that a bare clone needs. Some tools expect a normal clone and do not recognize a bare repository.
- Limits: a practitioner guide with no author, no date and no measurement.
