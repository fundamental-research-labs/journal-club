# The Cost of Dynamic Reasoning

- **Canonical:** https://arxiv.org/abs/2506.04301
- **Date/access:** 2025-06-04; arXiv HTML methods/results read 2026-09-16; no local copy retained.

The paper evaluates Llama-3.1 8B and 70B agent designs on Google Cloud hardware, measuring accuracy, latency, tokens, FLOPs, GPU energy, and serving power. LATS averages 71 LLM calls per request versus one for CoT (HTML lines 134–140). Prefix caching reduces end-to-end latency by 15.7% in agent workloads (lines 174–177). In HotpotQA, reported agent designs use 62.1–136.5× the GPU energy per query of single-turn inference (lines 275–297); results saturate as reasoning steps increase (lines 275–281).

This supplies the thesis’s economic counterfactual: extra inference can buy apparent quality, but its cost and diminishing returns must be compared against persistent updates. The study is transparent about system measures and Pareto tradeoffs. Limits include two model sizes, selected benchmarks, one cloud setup, and no continual-learning intervention; energy projections should not be generalized to all deployments. It supports full-budget accounting rather than a claim that test-time scaling always dominates learning.
