# Agentic Harness Engineering

## Source and access

**Source key:** `2026-agentic-harness-engineering`.

**Originals and source links:** [register](../sources.md#2026-agentic-harness-engineering); [canonical source](https://arxiv.org/abs/2604.25850). retention-restricted. [Manifest](../originals/manifest.json).

**Source/key:** `2026-agentic-harness-engineering` — Jiahang Lin et al., *Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses*. [arXiv](https://arxiv.org/abs/2604.25850), [versioned PDF](https://arxiv.org/pdf/2604.25850v4). First submitted 2026-04-28; latest and read version **v4, 2026-05-18**, verified from the arXiv submission history and the PDF stamp `arXiv:2604.25850v4 [cs.CL] 18 May 2026`. Read 2026-09-16: methods, §§4.1–4.4, Tables 1–3, Figures 3–4, limitations. Temporary PDF inspected; no repository copy retained because the paper's redistribution license was not verified. Code link not located.

## Question and methods

Can an agent improve a minimal coding harness by turning traces into component-, experience-, and decision-level evidence, then editing prompt, tools, middleware, and long-term memory? A single GPT-5.4-high campaign runs ten iterations on all 89 Terminal-Bench 2 tasks (4 easy, 55 medium, 30 hard), at least two rollouts per task, one-hour timeout, and file-level rollback. All three roles use the same base model. The campaign takes roughly 32 hours (§§3–4.2).

## Results and evidence

Terminal-Bench pass@1 rises from 69.7% to 77.0%; ACE reaches 68.9% and Training-Free GRPO 72.3% from the same seed (Table 1). Frozen transfer to all 500 SWE-bench Verified tasks gives AHE 75.6% versus seed 75.2%, ACE 74.6%, and TF-GRPO 74.2%; mean tokens/trial are 461k, 526k, 679k, and 582k respectively (Table 2). Five alternate bases gain +2.3 to +10.1 points over the seed on the 89 Terminal-Bench tasks (Figure 3). Isolated memory/tool/middleware swaps score 75.3/73.0/71.9 versus 69.7 seed, while prompt-only regresses to 67.4 (Table 3). Predicted fixes have 33.7% precision and 51.4% recall; predicted regressions only 11.8%/11.1% (Figure 4).

## Appraisal and limitations

### Interpretation

This is unusually direct evidence that executable harness components can carry reusable behavior and reduce inference tokens. The cross-benchmark success difference is only 0.4 points (two of 500 tasks), and AHE regresses on three small repositories; do not present it as a large generalization gain. The token reduction and consistent model-transfer direction are stronger signals.

### Limitations

One evolution campaign, no repeated-run interval, repeated selection on the same 89 tasks, and timeouts excluded from token means. The step/time operating point was fitted to GPT-5.4 high. Component effects are nonadditive and regression prediction is poor. No total token or dollar ledger for evolution is reported.

## Discussion and follow-up

Would the evolved components remain useful on unseen repositories under a matched total budget?

[Prominent citations and their roles](../prominent-citations.md#2026-agentic-harness-engineering)
