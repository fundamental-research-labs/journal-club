# Huxley–Gödel Machine

## Source and access

**Source key:** `2025-huxley-godel-machine`.

**Originals and source links:** [register](../sources.md#2025-huxley-godel-machine); [canonical source](https://arxiv.org/abs/2510.21614). Retained unmodified: [2025-huxley-godel-machine-paper-v3.pdf](../originals/2025-huxley-godel-machine/2025-huxley-godel-machine-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by-nc-sa/4.0/. [Manifest](../originals/manifest.json).

**Source/key:** `2025-huxley-godel-machine` — Wenyi Wang et al., *Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine*. [arXiv](https://arxiv.org/abs/2510.21614), [versioned PDF](https://arxiv.org/pdf/2510.21614v3). First submitted 2025-10-24; latest and read version **v3, 2025-10-29**, verified from the arXiv submission history and the PDF stamp `arXiv:2510.21614v3 [cs.AI] 29 Oct 2025`; ICLR 2026 paper. Read 2026-09-16: §§3–4, Tables 1–4, appendices on setup.

## Question and methods

HGM asks whether a selection score should estimate a node's future descendant productivity rather than its current benchmark score. Its clade metaproductivity (CMP) is estimated from descendant performance and used with asynchronous expansion/evaluation. Controlled comparisons use matched ancestors and 800 task evaluations: GPT-5/GPT-5-mini on SWE-Verified-60 and Qwen3-Coder 480B/30B on Polyglot (§4.2).

## Results and evidence

CMP correlates more strongly with empirical future clade performance than SICA/DGM scores: weighted Pearson 0.778 versus 0.444/0.285 on SWE-Verified-60 and 0.626 versus 0.274/0.383 on Polyglot (Table 1). At 800 evaluations, HGM/DGM/SICA reach 56.7/53.3/50.0% on SWE-Verified-60 and 30.5/27.1/25.4% on Polyglot. Allocated CPU-hours are 517/1,231/infinite-loop on SWE and 347/2,385/572 on Polyglot (Table 2). Scaling to 8,000 evaluations on full SWE-Verified moves a stronger 53.2% ancestor to 61.4%. On SWE-Lite, excluding 93 overlaps leaves 207 unseen tasks: the evolved agent scores 40.1% versus its ancestor's 34.8%; on all 300 tasks it scores 49.0% versus 44.0% (Table 3).

## Appraisal and limitations

### Interpretation

HGM is the best resource-accounted continuation of DGM in this lane and directly tests the fitness-proxy problem. The completely nonoverlapping SWE-Lite result is the cleanest task-transfer result in the family, though modest in size.

### Limitations

One run per method and no uncertainty intervals. HGM changes both parent selection and execution scheduling, so Table 2 does not isolate CMP's causal contribution. “Allocated CPU-hours” is a scheduling measure, not dollars, tokens, or energy. The empirical CMP target is computed post hoc from each completed tree and depends on observed descendants.

## Discussion and follow-up

Does a better parent-selection score still help when total compute and execution scheduling are matched?
