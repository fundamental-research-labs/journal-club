# TTRL: Test-Time Reinforcement Learning

## Source and access

**Source key:** `2025-test-time-reinforcement-learning`.

**Originals and source links:** [register](../sources.md#2025-test-time-reinforcement-learning); [canonical source](https://arxiv.org/abs/2504.16084). Retained unmodified: [2025-test-time-reinforcement-learning-paper-v3.pdf](../originals/2025-test-time-reinforcement-learning/2025-test-time-reinforcement-learning-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Authors:** Yuxin Zuo, Kaiyan Zhang, Li Sheng, Shang Qu, Ganqu Cui, Xuekai Zhu, Haozhan Li, Yuchen Zhang, Xinwei Long, Ermo Hua, Biqing Qi, Youbang Sun, Zhiyuan Ma, Lifan Yuan, Ning Ding, Bowen Zhou

**Canonical source:** https://arxiv.org/abs/2504.16084

**Version read:** arXiv v3, June 30, 2025; first posted April 22, 2025.

**Reading date / depth:** September 16, 2026; full primary PDF and appendices inspected.

## Question and methods

### Question and mechanism

TTRL performs benchmark-specific reinforcement learning directly on the unlabeled test inputs. For each prompt it samples 64 responses, uses their majority answer as a pseudo-label, then downsamples 32 responses for GRPO updates. The same test set is used for adaptation and evaluation, while ground-truth labels remain hidden from the update process. This is transductive test-set adaptation rather than evaluation on unseen examples after adaptation.

### Experimental setting

Main tasks are AIME 2024, AMC, MATH-500, and GPQA-Diamond. TTRL is run separately for each benchmark. The paper uses 10, 30, and 80 episodes for MATH-500, AMC, and AIME respectively, with peak learning rate 5e-7. Training used 8×A100 80GB GPUs; wall-clock time, token count, and hyperparameter-search cost are not reported (§3.1).

For main results, the authors sample 16 answers per question (four for the 32k-context Qwen3 condition) at temperature 0.6/top-p 0.95 and average correctness to estimate pass@1. Several appendix analyses instead use greedy decoding. No confidence intervals, standard deviations, or independent training repeats are reported. AIME 2024 has 30 problems, MATH-500 has 500, and GPQA-Diamond has 198; the exact AMC subset denominator is not stated in the paper section inspected.

## Results and evidence

- Qwen2.5-Math-7B rises on AIME 2024 from 12.9 to 40.2 pass@1: +27.3 percentage points, or +211.6% relative (Table 1). Calling this “211% improvement” without the 30-question benchmark and 16-sample estimator is misleadingly precise.
- The same model rises 35.6→68.1 on AMC and 46.7→83.4 on MATH-500, but falls 29.1→27.7 on GPQA-Diamond. The four-task unweighted average rises 31.1→54.9 (Table 1).
- Qwen2.5-Math-1.5B rises 32.7→73.0 on MATH-500 (+40.3 points), while Mistral-Nemo-Instruct falls 0.8→0 on AIME even as it improves on AMC and MATH-500 (Tables 1–2). The method is therefore not uniformly beneficial.
- Figure 7 reports that the adapted Qwen2.5-Math-7B’s avg@64 exceeds the initial model’s maj@64 on all three math benchmarks. Figure 8 compares TTRL with label-leaking RL on MATH-500; it is an illustrative upper-bound comparison, not an unseen-test generalization result.
- Figure 9 shows that pseudo-label accuracy can remain low while the per-sample reward agrees with correctness more often because some sampled responses hit the pseudo-label; this is the paper’s proposed explanation for learning despite wrong majority labels.

## Appraisal and limitations

### Authors' claim

Majority-vote pseudo-rewards can support substantial self-improvement on unlabeled test inputs and approach direct labeled-test RL.

### Evidence

The study spans many model families and includes useful mechanism probes and negative cells. Yet it adapts and scores on the same finite benchmark inputs, reports no independent repeats, gives incomplete total resource accounting, and offers limited ablation of prior knowledge or benchmark contamination. The phrase “unbounded lifelong learning” in §4.1 is unsupported by these finite per-benchmark runs.

### Interpretation

TTRL is strong evidence that repeated sampling plus RL can exploit an unlabeled batch distribution. It is weak evidence for durable general-purpose agent evolution because transfer to future held-out inputs is not the primary endpoint. Treat it as a bridge between test-time compute and parameter learning, and pair it with explicit warnings about transductive evaluation, consensus error, benchmark-specific compute, and the observed GPQA regression.

## Discussion and follow-up

What evidence would distinguish adaptation to a fixed test batch from learning that transfers to future unseen inputs?

[Prominent citations and their roles](../prominent-citations.md#2025-test-time-reinforcement-learning)
