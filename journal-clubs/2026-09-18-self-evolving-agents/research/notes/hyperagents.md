# Hyperagents

[Paper v1](https://arxiv.org/html/2603.19461v1). Jenny Zhang et al.; first submitted March 19, 2026; preprint. arXiv lists one version despite an August manuscript date in the initial session notes. Accessed September 16; §§3–5 read selectively. Family: DGM/Hyperagents; related systems are not independent replications.

**Question/method.** Can the process generating agent changes itself improve? Task and meta agents share editable code. Main experiments retain handcrafted parent selection (§3). Transfer experiments freeze the meta agent and measure improvement@50 (§5.2).

**Reported evidence.** Five coding runs, 80 iterations, 50 training tasks: full Polyglot performance 0.084→0.267 (reported CI 0.231–0.280; includes training tasks). In math grading after 200 iterations, transferred versus fresh initialization scores 0.640 (CI 0.550–0.720) versus 0.610 (0.510–0.680); authors explicitly report p>0.05 (§5.3). Interval construction was not audited.

**Authors' claim.** Meta-level strategies transfer and can accumulate across runs.

**Interpretation/limits.** More direct evidence about improving the improver than editing skills alone. Finite experiments do not establish unbounded acceleration. Initial zero scores in some domains reflect formatting failures; compare strong initialized controls. Full resource normalization and appendix statistics remain unreviewed.

**Inspect/discuss.** Figures 3–4: transferred improvement process versus ordinary task warm-start.
