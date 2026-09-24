# References

Each entry states what this repository takes from the source and the limits its authors admit or this repository found. The limits feed the certainty of clauses ([DESIGN.md](DESIGN.md) §4).

## Instruction files and repository documents

**[1]** K. Chakrabarti, "Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding," arXiv:2608.11095, 2026. https://arxiv.org/abs/2608.11095
- Takes: a lifetime analysis of 247,694 instructions in 1,867 repositories. Instruction files grow by addition and old instructions are rarely deleted. The prescription to state a reason with each instruction.
- Limits: single author, not peer reviewed. The large effect sizes of the prescription come from synthetic experiments with two or three instructions; the effect on real prompts is smaller and was graded by an LLM.

**[2]** C. Treude, S. Baltes, "Context Rot in AI-Assisted Software Development: Repurposing Documentation Consistency for AI Configuration Artifacts," arXiv:2606.09090, 2026. https://arxiv.org/abs/2606.09090
- Takes: applying existing documentation consistency checkers unchanged to instruction files, without building a new tool.
- Limits: of 50 manually checked findings, 36% were false positives or ambiguous. One validator. The authors call their prevalence figures a possibility signal.

**[3]** T. Gloaguen, N. Mündler, M. Müller, V. Raychev, M. Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?," arXiv:2602.11988, 2026. https://arxiv.org/abs/2602.11988
- Takes: repository overviews did not help, and agents followed the instructions. The advice to put only non-standard conventions in human-written files.
- Limits: Python repositories only. Developer-written files had a positive effect that was not statistically significant.

**[4]** J. L. Lulla, S. Mohsenimofidi, M. Galster, J. M. Zhang, S. Baltes, C. Treude, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents," arXiv:2601.20404, 2026. https://arxiv.org/abs/2601.20404
- Takes: nothing. Cited only for the scope judgement in DESIGN.md §1.
- Limits: one agent, ten repositories, small tasks. Correctness was not measured.

**[5]** P. Khatri, "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories," arXiv:2607.27250, 2026. https://arxiv.org/abs/2607.27250
- Takes: no measured effect of context strategy on correctness.
- Limits: single author, 17 tasks, 3 repositories. A medium effect cannot be ruled out.

**[6]** W. Chatlatanagulchai et al., "Agent READMEs: An Empirical Study of Context Files for Agentic Coding," arXiv:2511.12884, 2025 (revised 2026). https://arxiv.org/abs/2511.12884 · Dataset: https://github.com/woraamy/Agent-Context-File-Analysis
- Takes: 2,303 instruction files from 1,925 repositories, evolving through frequent small additions. The instruction-file sample.
- Limits: the population is limited to AIDev-based repositories with at least five stars.

**[7]** W. S. Tan, M. Wagner, C. Treude, "Detecting Outdated Code Element References in Software Repository Documentation," *Empirical Software Engineering* 29(1), 2024. https://link.springer.com/article/10.1007/s10664-023-10397-6
- Takes: most of about 3,000 GitHub projects had an outdated code reference at some point in their history.
- Limits: the false positives of regex-based detection were confirmed again in [2].

**[8]** W. S. Tan et al., DOCER tool. https://github.com/wesleytanws/DOCER_tool · Paper: arXiv:2307.04291
- Takes: a GitHub Actions tool that finds outdated code references in each pull request.
- Limits: shares the false positives reported in [2].

**[9]** G. Cai, R. Li, P. Liang, Z. Li, M. Shahin, "Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study," arXiv:2606.12231, 2026. https://arxiv.org/abs/2606.12231
- Takes: rule changes were mostly extensions and reinforcements. The observation that compliance rose after rule fixes was used only by the withdrawn R-003 and is no longer cited.
- Limits: correlation, not cause. Compliance was graded by an LLM. Most projects are small, single-developer TypeScript web projects.

## Samples and evidence assessment

**[10]** E. Kalliamvakou et al., "The Promises and Perils of Mining GitHub," MSR 2014. https://dl.acm.org/doi/10.1145/2597073.2597074
- Takes: the pitfalls of sampling GitHub data.

**[11]** S. Baltes, P. Ralph, "Sampling in Software Engineering Research: A Critical Review and Guidelines," *Empirical Software Engineering*, 2022. https://arxiv.org/abs/2002.07764
- Takes: sampling guidelines.

**[12]** GRADE Working Group, GRADE Handbook and guidance series. https://book.gradepro.org/guideline/overview-of-the-grade-approach
- Takes: the four certainty levels and the five domains that lower them.
- Limits: built for clinical guidelines. Applying it to software documentation research is this repository's judgement.

## Writing counter-evidence

**[13]** N. L. Schroeder, A. C. Kucera, "Refutation Text Facilitates Learning: A Meta-Analysis of Between-Subjects Experiments," *Educational Psychology Review*, 2022. https://pubmed.ncbi.nlm.nih.gov/35095236/
- Takes: texts that state a misconception and refute it improve learning (44 comparisons, g = 0.41).
- Limits: human learners. Applying it to agent documents adds indirectness.

**[14]** D. J. O'Keefe, "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages," *Communication Yearbook* 22, 1999. https://academic.oup.com/anncom/article-pdf/22/1/209/61205855/anncom_22_1_209.pdf
- Takes: refutational two-sided messages are more credible and persuasive; two-sided messages without refutation are less persuasive.
- Limits: an old study of human readers.

**[15]** C. J. Clark, P. E. Tetlock, Adversarial Collaboration Project. https://web.sas.upenn.edu/adcollabproject/publications/
- Takes: stating disagreements so they can be tested, and committing in advance to update on the result. The source of falsifiers.

**[16]** Z. Zhou, T. Zhou, R. Jia, J. May, "How Language Models Process Negation," arXiv:2605.03052, 2026. https://arxiv.org/abs/2605.03052
- Takes: language models can process negation yet often miss it through shortcuts. The basis for writing instruction files positively.
- Limits: instruction files were not tested directly.

## Decision records

**[17]** M. Nygard, "Documenting Architecture Decisions," 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

**[18]** F. Nogueira, N. Silva, T. Conte, "One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption," arXiv:2604.27333, 2026. https://arxiv.org/abs/2604.27333
- Takes: in a student experiment, Nygard's format scored higher overall than MADR.
- Limits: undergraduate participants.

**[19]** N. Miccio Palermo, A. Tommasel, J. A. Diaz-Pace, "A Text Mining and Classification Approach for Analyzing Architecture Decision Records," arXiv:2609.07375, 2026. https://arxiv.org/abs/2609.07375
- Takes: in the decision records of about 550 repositories, alternatives and decision drivers were often missing.

## Tools and practitioner sources

**[20]** N. Batchelder, Cog. https://nedbatchelder.com/code/cog/index

**[21]** rust-analyzer, `check_lsp_extensions_docs` in `xtask/src/tidy.rs`. https://github.com/rust-lang/rust-analyzer/blob/master/xtask/src/tidy.rs

**[22]** A. Kladov (matklad), "ARCHITECTURE.md," 2021. https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- Takes: the structure of an ARCHITECTURE document (overview, codemap, invariants and boundaries). Write only what rarely changes, do not try to keep it in sync with the code, and revisit it a few times a year. Name files and types so they can be searched instead of linking them.
- Limits: a practitioner essay without empirical evaluation. GRADE treats it as expert opinion.

**[23]** M. Pocock, "writing-great-skills," in *mattpocock/skills* (MIT). https://github.com/mattpocock/skills
- Takes: the vocabulary for pruning written instructions (single source of truth, duplication, sediment, no-op, relevance) and the use of one leading term per concept.
- Limits: written for agent skills, not repository documents. Practitioner guidance without empirical evaluation.
