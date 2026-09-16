# HarnessDev

[Paper v1](https://arxiv.org/html/2609.01437v1). Yuhao Wu et al.; September 1, 2026 preprint. Accessed September 16; setup, §4.3, Tables 6–7, Appendix B inspected. Family: HarnessDev.

**Question/method.** Can models create runnable infrastructure and evolve it? Creation covers 2,207 unique downstream instances. Evolution uses 100 SWE-Pro + 89 Terminal-Bench feedback tasks, then 630 held-out SWE-Pro tasks; nine creator/runtime lineages (§4.3).

**Reported evidence.** Seventy-three versions yield 64 adjacent switches. Feedback and held-out score directions agree in 34/64 (53.1%); this is not “34 improvements generalize.” All five self-runtime declared versions improve held-out scores by 1.43–4.44 points. Fixed-Gemini runtime: one of four improves, three regress (Table 6). Each creator/runtime cell has one evolution trajectory; repeated-commit noise can reach about ±4.75 feedback-pair points.

**Authors' claim.** Evolution gains are unstable and runtime-dependent.

**Interpretation/limits.** Strong separation of visible feedback, declared selection, and post-freeze tests. Version switches are correlated, not 64 independent trials. Creation's human-engineered references use different model–harness pairs, sometimes external reported scores (Appendix B.2); avoid attributing their entire gap to harness engineering. Cost plots exclude creator/judge/probe tokens (B.4).

**Inspect/discuss.** Figure 8 and Table 6. How should an agent select a version when feedback is noisy?
