# 참고 문헌

항목마다 이 저장소가 가져다 쓰는 것과, 저자가 인정했거나 이 저장소가 확인한 한계를 함께 적는다. 한계는 [DESIGN.md](DESIGN.md) 3절의 근거 등급을 매기는 입력이다.

## 에이전트 지시 파일과 저장소 문서

**[1]** K. Chakrabarti, "Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding," arXiv:2608.11095, 2026. https://arxiv.org/abs/2608.11095
- 가져다 쓰는 것: 저장소 1,867개, 지시 247,694개의 수명 분석. 지시 파일은 추가로 커지고 오래된 지시는 잘 지워지지 않는다. 지시에 이유를 함께 적으라는 처방
- 한계: 단독 저자, 동료 심사 전. 처방의 큰 효과 수치는 지시 2~3개짜리 합성 실험에서 나왔고, 실제 프롬프트 적용 결과는 더 작으며 LLM이 채점했다

**[2]** C. Treude, S. Baltes, "Context Rot in AI-Assisted Software Development: Repurposing Documentation Consistency for AI Configuration Artifacts," arXiv:2606.09090, 2026. https://arxiv.org/abs/2606.09090
- 가져다 쓰는 것: 기존 문서 일관성 검사 도구를 에이전트 지시 파일에 그대로 적용하는 방법. 새 도구를 만들지 않는다는 접근
- 한계: 수작업으로 확인한 50건 중 36%가 오탐이거나 애매했다. 검증자 1명. 저자 스스로 유병률 수치를 가능성 신호로 규정했다

**[3]** T. Gloaguen, N. Mündler, M. Müller, V. Raychev, M. Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?," arXiv:2602.11988, 2026. https://arxiv.org/abs/2602.11988
- 가져다 쓰는 것: 저장소 개요는 도움이 되지 않았고, 지시는 에이전트가 따랐다. 사람이 쓰는 파일에는 표준이 아닌 관례만 담으라는 권고
- 한계: Python 저장소만 다뤘다. 개발자가 쓴 파일의 효과는 통계적으로 유의하지 않았지만 방향은 양수였다

**[4]** J. L. Lulla, S. Mohsenimofidi, M. Galster, J. M. Zhang, S. Baltes, C. Treude, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents," arXiv:2601.20404, 2026. https://arxiv.org/abs/2601.20404
- 가져다 쓰는 것: 없음. 1절의 범위 판단에만 인용한다
- 한계: 에이전트 하나, 저장소 10개, 작은 작업만 다뤘다. 정확성을 측정하지 않았다

**[5]** P. Khatri, "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories," arXiv:2607.27250, 2026. https://arxiv.org/abs/2607.27250
- 가져다 쓰는 것: 컨텍스트 전략이 정확성에 미친 효과가 측정되지 않았다는 결과
- 한계: 단독 저자, 과제 17개, 저장소 3개. 중간 크기의 효과는 배제하지 못한다

**[6]** W. Chatlatanagulchai et al., "Agent READMEs: An Empirical Study of Context Files for Agentic Coding," arXiv:2511.12884, 2025 (2026 개정). https://arxiv.org/abs/2511.12884 · 공개 데이터: https://github.com/woraamy/Agent-Context-File-Analysis
- 가져다 쓰는 것: 저장소 1,925개의 에이전트 지시 파일 2,303개. 이 파일들이 잦고 작은 추가로 진화한다는 관찰. 에이전트 지시 파일 표본
- 한계: AIDev 기반이고 별 5개 이상인 저장소로 모집단이 한정된다

**[7]** W. S. Tan, M. Wagner, C. Treude, "Detecting Outdated Code Element References in Software Repository Documentation," *Empirical Software Engineering* 29(1), 2024. https://link.springer.com/article/10.1007/s10664-023-10397-6
- 가져다 쓰는 것: GitHub 프로젝트 3,000여 개 가운데 대부분이 이력 중 한 번은 낡은 코드 참조를 가졌다는 관찰
- 한계: 정규식 기반 탐지의 오탐 문제는 [2]에서 다시 확인되었다

**[8]** W. S. Tan et al., DOCER tool. https://github.com/wesleytanws/DOCER_tool · 관련 논문 arXiv:2307.04291
- 가져다 쓰는 것: 풀 리퀘스트마다 낡은 코드 참조를 찾는 GitHub Actions 도구
- 한계: [2]의 오탐 문제를 그대로 가진다

**[9]** G. Cai, R. Li, P. Liang, Z. Li, M. Shahin, "Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study," arXiv:2606.12231, 2026. https://arxiv.org/abs/2606.12231
- 가져다 쓰는 것: 규칙 변경은 확장과 보강이 대부분이었다. 에이전트의 실수를 고치려고 규칙을 수정한 뒤 준수율이 올랐다
- 한계: 인과가 아닌 상관. 준수 여부를 LLM이 채점했다. 프로젝트 대부분이 소규모, 1인 개발, TypeScript 웹이다

## 표본과 근거 평가

**[10]** E. Kalliamvakou et al., "The Promises and Perils of Mining GitHub," MSR 2014. https://dl.acm.org/doi/10.1145/2597073.2597074
- 가져다 쓰는 것: GitHub 데이터 표집의 함정 목록

**[11]** S. Baltes, P. Ralph, "Sampling in Software Engineering Research: A Critical Review and Guidelines," *Empirical Software Engineering*, 2022. https://arxiv.org/abs/2002.07764
- 가져다 쓰는 것: 표집 방법 지침

**[12]** GRADE Working Group, GRADE Handbook and guidance series. https://book.gradepro.org/guideline/overview-of-the-grade-approach
- 가져다 쓰는 것: 근거 확실성의 네 등급과, 등급을 낮추는 다섯 영역
- 한계: 의학 진료지침용으로 만들어졌다. 소프트웨어 문서 연구에 적용하는 것은 이 저장소의 판단이다

## 반대 근거를 쓰는 방식

**[13]** N. L. Schroeder, A. C. Kucera, "Refutation Text Facilitates Learning: A Meta-Analysis of Between-Subjects Experiments," *Educational Psychology Review*, 2022. https://pubmed.ncbi.nlm.nih.gov/35095236/
- 가져다 쓰는 것: 오해를 제시하고 반박하는 글의 학습 효과 (44개 비교, g = 0.41)
- 한계: 사람 학습자 대상이다. 에이전트 문서에 적용하면 비직접성이 생긴다

**[14]** D. J. O'Keefe, "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages," *Communication Yearbook* 22, 1999. https://academic.oup.com/anncom/article-pdf/22/1/209/61205855/anncom_22_1_209.pdf
- 가져다 쓰는 것: 반박형 양면 메시지는 신뢰도와 설득력이 높고, 반박 없는 양면 메시지는 설득력이 낮다
- 한계: 오래된 연구이고 사람 독자 대상이다

**[15]** C. J. Clark, P. E. Tetlock, Adversarial Collaboration Project. https://web.sas.upenn.edu/adcollabproject/publications/
- 가져다 쓰는 것: 불일치를 검증 가능하게 명시하고, 결과에 따라 믿음을 바꾸기로 미리 약속하는 절차. 반증 조건을 적는 방식의 출처

**[16]** Z. Zhou, T. Zhou, R. Jia, J. May, "How Language Models Process Negation," arXiv:2605.03052, 2026. https://arxiv.org/abs/2605.03052
- 가져다 쓰는 것: LLM이 부정문을 처리할 능력이 있으면서도 지름길 때문에 자주 놓친다는 결과. 에이전트 지시 파일을 긍정형으로 쓰는 근거
- 한계: 에이전트 지시 파일을 직접 실험하지 않았다

## 결정 기록

**[17]** M. Nygard, "Documenting Architecture Decisions," 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

**[18]** F. Nogueira, N. Silva, T. Conte, "One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption," arXiv:2604.27333, 2026. https://arxiv.org/abs/2604.27333
- 가져다 쓰는 것: 학생 실험에서 Nygard 양식이 MADR보다 종합 점수가 높았다
- 한계: 참가자가 학부생이다

**[19]** N. Miccio Palermo, A. Tommasel, J. A. Diaz-Pace, "A Text Mining and Classification Approach for Analyzing Architecture Decision Records," arXiv:2609.07375, 2026. https://arxiv.org/abs/2609.07375
- 가져다 쓰는 것: 저장소 약 550개의 결정 기록에서 대안과 결정 동인이 자주 빠져 있었다

## 운영 중인 도구와 사례

**[20]** N. Batchelder, Cog. https://nedbatchelder.com/code/cog/index

**[21]** rust-analyzer, `xtask/src/tidy.rs`의 `check_lsp_extensions_docs`. https://github.com/rust-lang/rust-analyzer/blob/master/xtask/src/tidy.rs

**[22]** A. Kladov (matklad), "ARCHITECTURE.md," 2021. https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- 가져다 쓰는 것: ARCHITECTURE 문서의 구성(개요, 코드 지도, 불변식과 경계). 자주 바뀌지 않는 것만 쓰고 코드와 동기화하려 하지 않으며, 대신 한 해에 몇 번 다시 읽는다는 운영 방식. 파일과 타입은 링크 대신 검색할 수 있는 이름으로 부른다는 방식
- 한계: 실무자의 글이며 실증 평가가 없다. GRADE로는 전문가 의견에 해당한다
