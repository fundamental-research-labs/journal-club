# WikiSkill

## Source and access

**Source key:** `wikiskill`.

**Originals and source links:** [register](../sources.md#wikiskill); [canonical source](https://arxiv.org/abs/2608.27454v1). Retained unmodified: [2026-wikiskill-paper-v1.pdf](../originals/2026-wikiskill/2026-wikiskill-paper-v1.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

[Paper v1](https://arxiv.org/html/2608.27454v1). Liyan Tang et al.; August 27, 2026 preprint. Accessed September 16; methods, results, and relevant appendices read, not every prompt. Family: WikiSkill.

## Question and methods

Does a persistent knowledge layer improve reusable skill evolution? Separate traces, wiki, and skills; retain the wiki after rejected skill edits. Compare no skills, Trace2Skill, EvoSkill, and SkillOpt across five models and benchmarks (§§3–4).

## Results and evidence

Qwen-3.5-9B macro accuracy rises from 29.9 to 47.4, +17.5 percentage points (Table 1). Qwen-3.5-4B OfficeQA declines from 30.2 to 28.5. Appendix B, Table 6 gives train/validation/test counts: LiveMath 35/18/124; SealQA 16/10/85; SpreadsheetBench 80/40/280; OfficeQA 50/24/172; ALFWorld 39/18/134. Three evolution runs; Appendix C uses 1,000 paired bootstrap resamples and equal benchmark weighting. Table 1 supplies no numerical confidence intervals. Appendix D compares optimizer-call complexity, not end-to-end dollar parity.

## Appraisal and limitations

### Authors' claim

Persistent knowledge supports transferable skills.

### Interpretation and limitations

Useful controlled positive evidence with regressions. Small validation sets risk noisy acceptance; full skill injection bypasses retrieval failures. Oracle reference pages assist OfficeQA. Benchmark transfer is not unlimited deployment learning. No reproduction here.

## Discussion and follow-up

Figure 2; Tables 1, 3, 6. Should an unvalidated wiki persist when a skill is rejected?
