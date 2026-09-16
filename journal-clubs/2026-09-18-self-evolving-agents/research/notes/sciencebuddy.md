# ScienceBuddy

[Paper v1](https://arxiv.org/html/2609.17523v1); [code](https://github.com/Gen-Verse/ScienceBuddy/tree/454d11c6e0609de074f27391ef170ca748dfae37). Shuhan Xue et al.; September 15, 2026 preprint; PhAI release September 16. Accessed September 16; §§2, 4, 7.1–7.3 inspected. Family: ScienceBuddy (paper, preview, announcement, code).

**Question/method.** Alternate fixed-model harness refinement and fixed-harness GRPO. The auxiliary reflector stays fixed. Scientific inventory: 895 tasks across four families; standalone harness experiment has 288 adaptation conversations, not 288 independent evaluation tasks.

**Reported evidence.** §4.2/Figure 8 reports three cycles, each ten harness steps plus twenty RL updates; single-attempt test accuracy 42.2→73.3. Standalone harness comparison: 31.1→51.1 validation accuracy. Fixed-harness model experiment: pass@4 48.3→67.8. Evaluation denominators, repeated-run uncertainty, and full resource accounting were not established from reviewed sections; 895 is not a verified denominator for each result.

**Authors' claim.** Coupled procedural and parameter learning supports continual scientific assistance.

**Interpretation/limits.** Fresh, relevant cross-surface demonstration. Simulated procedural feedback in the experiment differs from real researcher case studies. Stronger fixed helper models assist harness changes. Different splits/metrics prevent adding the gains. §4.2 heading says two cycles while text/figure say three: flag this editorial discrepancy. No proof that the improver itself strengthens.

**Inspect/discuss.** Figures 8–10 and Appendix 7.2 information boundaries.
