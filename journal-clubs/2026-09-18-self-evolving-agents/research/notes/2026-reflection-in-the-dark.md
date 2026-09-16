# Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization

## Source and access

**Source key:** `2026-reflection-in-the-dark`.

**Originals and source links:** [register](../sources.md#2026-reflection-in-the-dark); [canonical source](https://arxiv.org/abs/2603.18388). Retained unmodified: [2026-reflection-in-the-dark-paper-v2.pdf](../originals/2026-reflection-in-the-dark/2026-reflection-in-the-dark-paper-v2.pdf). Paper license: CC BY-NC-ND 4.0 (canonical arXiv license, coordinator verified). [Manifest](../originals/manifest.json).

. [arXiv v2](https://arxiv.org/abs/2603.18388v2); [PDF](https://arxiv.org/pdf/2603.18388v2). Shiyan Liu et al. First posted March 19, 2026; v2 June 8, 2026. Read September 16, 2026: full paper, main tables, appendices B–C, and optimization traces inspected. The PDF downloaded successfully for temporary inspection.

## Question and methods

### Question and method

Does reflective prompt optimization reliably diagnose why a prompt fails, or can its starting prompt silently constrain the hypothesis space? The paper constructs three seed conditions—GEPA's official GSM8K seed with an inverted JSON field order, a manually repaired version, and a minimal one-sentence seed—and compares no optimization, GEPA, and VISTA. VISTA separates hypothesis generation from rewriting, tests three hypotheses per round, records semantic labels, and adds random restart plus epsilon-greedy exploration (§§3–4).

### Splits, models, and compute

GSM8K uses 50 training and 50 validation examples sampled once from the official train set and the full 1,319-example official test set. AIME uses 50/50 working train/validation examples from 2022–2024 and the 30 AIME-2025 problems repeated five times (150 test instances, not 150 independent problems). All runs use minibatch 8, budget T=500 metric calls, random seed 0, and at most four workers (Appendix B). GSM8K uses Qwen3-4B base/Qwen3-8B reflector; AIME uses GPT-4.1-mini/GPT-4o-mini. Local inference ran on one RTX 4090. Reported API costs are $0.20 VISTA versus $0.12 GEPA for a GSM8K run with GPT-4o-mini reflection, and $4.1–6.0 versus $3.7–5.6 on AIME (Appendix C). Token counts and wall time are not reported.

## Results and evidence

Table 1: defective-seed GSM8K accuracy is 23.81 no optimization, 13.50 GEPA, and 87.57 VISTA. With the repaired seed, scores are 85.59/86.53/87.34; with the minimal seed, 20.67/21.68/85.67. On AIME the respective defective-seed scores are 38.67/44.00/46.00, with smaller VISTA advantages under repaired/minimal seeds. Table 2 changes reflectors and reports VISTA 87.64 with GPT-4o-mini versus GEPA 23.43; cross-model prompts give 86.05 versus 22.74. Table 3 shows the pre-specified heuristic set is the dominant component: GEPA 13.50; +restart 15.69; +parallel sampling 20.17; +heuristic-guided reflection 79.98. Removing exploitation collapses VISTA to 22.97. These are single configured runs; no independent optimization repeats, confidence intervals, or run-to-run variance are reported.

## Appraisal and limitations

### Authors' claim

GEPA-like reflection can be trapped by seed-imposed assumptions; explicit hypotheses and broader exploration can escape those traps.

### Interpretation and limitations

The degradation is a credible counterexample to monotonic reflective optimization under a real GEPA seed, not a population estimate of GEPA reliability. The field-order defect is constructed and severe, and VISTA's manually curated hypothesis categories contain the relevant failure class; the component ablation shows that prior is responsible for most of the recovery. Only math tasks, one sampled train/validation split, one random seed, and standard non-reasoning models are tested. VISTA is therefore a strong challenge companion if GEPA appears in the shortlist, but it does not displace AgentStream's broader method/stream comparison or Library Drift's repeated lifecycle ablations.

## Discussion and follow-up

Table 1 and the labeled optimization trees ask whether an optimizer is learning from feedback or merely searching within failure concepts its designer already supplied.
