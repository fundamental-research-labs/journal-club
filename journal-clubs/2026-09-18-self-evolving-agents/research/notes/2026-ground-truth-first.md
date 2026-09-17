# Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory

## Source and access

**Source key:** `2026-ground-truth-first`.

**Originals and source links:** [register](../sources.md#2026-ground-truth-first); [canonical source](https://arxiv.org/abs/2607.21962). retention-restricted. [Manifest](../originals/manifest.json).

. [arXiv v1](https://arxiv.org/abs/2607.21962v1); [PDF](https://arxiv.org/pdf/2607.21962v1); [Veracium](https://github.com/veracium-ai/Veracium). Quentin Spencer; July 24, 2026 preprint. Read September 16, 2026: full paper, Tables 2–7, §§3–7, appendices, and reproducibility statement inspected. The PDF downloaded successfully temporarily. No paper copy retained: arXiv exposes only its non-exclusive distribution license. The paper states MIT for the generator/harness/Veracium and CC BY 4.0 for the synthetic corpus; at publication the study-artifact package was still “in preparation.” The public Veracium repository currently exposes an MIT license, but the full harness/corpus release and immutable archive were not verified.

## Question and methods

### Question and design

Instead of generating conversations and extracting labels afterward, can a seeded life-script create facts, validity intervals, source channels, rendered text, and mechanically instantiated questions with known provenance? The benchmark compares five memory architectures and no-memory/full-history/token-matched baselines, adds as-of-date probes, write-stage audits, and a complete cross-family re-judging (§§3–5).

### Samples, controls, and compute

The short-horizon bake-off uses 275 questions across 14 users × 3 stochastic answer/judge replicates = 825 judged answers/backend (Table 2). The tenure study uses 6 generated users × 3 replicates and three checkpoints, n=324/cell (Tables 3/5); replicate calls vary answer/judge stochasticity over fixed corpora, not fresh users. The whole protocol logged 52,797 LLM calls, with 18,721 additional review-validation calls. Provider APIs expose no random seed. Full history and a token-matched recent-event window use the same answerer, judge, and three-replicate protocol (§5.8). The paper reports item McNemar tests, six-user sign-flip tests, and user-cluster bootstrap intervals, appropriately noting the six-cluster resolution limit.

## Results and evidence

The budgeted map's early-chapter recall falls 96.3→72.2 from week 3 to 9, while graph rises 94.4→100 and hybrid v2 remains 100 (Figure 2). The graph-minus-map tenure interaction is +17.3 points, user-cluster 95% CI +8.3 to +26.2, but exact six-user sign-flip p=.063; under complete cross-family re-judging it becomes +24.1, positive for all six users, minimum attainable p=.031 (§5.4). Short horizon full history scores 97.9% versus hybrid 96.8%, p=.21; at week 9 there is no judge-independent winner between hybrid and full history. Hybrid reads roughly half as many tokens at week 9, but write and infrastructure costs are excluded from per-question read cost (§5.8).

Write audits cover 11 users × 3 replicates × 2 write paths = 66 audits. Weak-written facts miss downstream QA 24.2% versus 1.6% for clean facts (n=1,092 linked observations; user-cluster OR 19.6, 95% CI 10.6–50.3; within-block permutation p<1e-4), but audit and QA judgment share a model, and the association is not causal (§5.5). For indirect injection, graph has 0 unsupported assertions in 14 unique probes/42 trials while flat stores fail two unique probes each; the paper correctly warns that zero of 14 only bounds the rate loosely and is not general security (§5.7).

## Appraisal and limitations

### Authors' claim

Short histories can mis-rank memory architectures; validity, provenance, eviction, and write quality need longitudinal evaluation.

### Interpretation and limitations

This is unusually careful evaluation work: it includes trivial full-history baselines, unique-probe uncertainty, cluster-level tests, and a second judge, and it narrows claims when results are judge-sensitive. Its central tenure interaction is based on six synthetic users, the primary cluster test is p=.063, architectures differ in multiple components and token budgets, and no independent reproduction exists. The pending artifact package weakens present reproducibility despite detailed logs described in the paper. It merits a main shortlist role as an evaluation challenge, visibly labeled emerging preprint evidence rather than a settled ranking.

## Discussion and follow-up

Figure 2 plus §5.8 cleanly show the tension: bounded memory stays cheap by forgetting, while unbounded methods preserve early facts at increasing read cost; full history remains hard to beat until the history is genuinely long.

[Prominent citations and their roles](../prominent-citations.md#2026-ground-truth-first)
