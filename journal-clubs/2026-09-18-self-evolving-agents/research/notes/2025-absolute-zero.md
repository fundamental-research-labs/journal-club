# Absolute Zero: Reinforced Self-play Reasoning with Zero Data

## Source and access

**Source key:** `2025-absolute-zero`.

**Originals and source links:** [register](../sources.md#2025-absolute-zero); [canonical source](https://arxiv.org/abs/2505.03335). Retained unmodified: [2025-absolute-zero-paper-v3.pdf](../originals/2025-absolute-zero/2025-absolute-zero-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Authors:** Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang. Yang Yue appears twice in the current arXiv citation metadata and PDF author list; this note preserves the primary metadata rather than guessing whether it is a duplicate-entry error.

**Canonical source:** https://arxiv.org/abs/2505.03335

**Version read:** arXiv v3, October 16, 2025; first posted May 6, 2025.

**Reading date / depth:** September 16, 2026; full primary PDF and appendices inspected.

## Question and methods

### Question and mechanism

Absolute Zero Reasoner (AZR) tests whether one pretrained model can both propose executable code-reasoning tasks and solve them without a curated downstream training set. It creates deduction, abduction, and induction tasks around program/input/output triples, filters them through execution, and updates proposer and solver roles jointly with verifiable rewards. “Zero data” means no external curated reasoning examples during this self-play stage; it does not mean zero pretrained data, zero hand-designed prompts/rewards, or zero initial task seeding. Appendix §3.3.1 initializes buffers with model-generated valid triplets (`B × 4`) before weight updates.

### Experimental setting

The principal models are Qwen2.5-7B and Qwen2.5-Coder-7B, with 3B, 14B, and Llama-3.1-8B follow-ups. Training uses batch size `64 × 6` (two roles × three task modes), learning rate 1e-6, 500 total steps, one rollout, six references, and eight samples to estimate task accuracy (Appendix Table 3). Runs lasted about 3–5 days on unspecified-size clusters of A800 GPUs, so total accelerator count and GPU-hours are not reported.

Evaluation uses greedy decoding. The OOD suite contains HumanEval+, MBPP+, LiveCodeBench v1–5, AIME 2024/2025, AMC 2023, MATH-500, Minerva, and OlympiadBench. Table 1 averages the three code tasks into CAvg and six math tasks into MAvg, then defines overall AVG as `(CAvg + MAvg)/2`; this gives the code and math groups equal weight rather than weighting all nine benchmarks equally. No run repeats, confidence intervals, or standard deviations are reported for the headline scores.

## Results and evidence

- Starting from Qwen2.5-7B-Base, AZR moves CAvg 52.0→55.2, MAvg 27.5→38.4, and overall AVG 39.8→46.8 (+7.0). HumanEval+ declines 73.2→71.3 while other aggregate components rise (Table 1).
- Starting from Qwen2.5-Coder-7B, CAvg moves 56.6→61.6, MAvg 23.9→39.1, and AVG 40.2→50.4 (+10.2). The rendered primary PDF shows MATH-500 54.0→72.6 but prints a green superscript `+22.6`; the arithmetic difference is **+18.6**, so the superscript is internally inconsistent and should not be quoted as a verified gain.
- The authors compare against curated-data “zero-style” reasoners with different base variants and training sets. AZR-Coder’s 50.4 overall average is 1.8 points above the strongest listed prior overall score (48.6), but this is a cross-system table rather than a matched-budget experiment (§4.2, Table 1 and Table 4).
- Pass@k curves in Figure 8 show AZR generally matches or exceeds the base at high k, except AIME 2024 at k=512. Exact confidence bands are absent.
- The appendix reports potentially consequential environment effects: removing comments/docstrings or global variables reduced performance, suggesting that task representation and information leakage channels materially affect the self-play curriculum (Appendix D.5).

## Appraisal and limitations

### Authors' claim

Verifiable self-play can generate its own curriculum and substantially improve math and coding reasoning without curated training examples.

### Evidence

Broad benchmark coverage, multiple model families/scales, executable rewards, ablations, public code, and fully specified core hyperparameters make this a consequential primary demonstration. However, there is no independent repeat uncertainty, total compute is incomplete, several comparisons are unmatched, and “zero data” obscures pretrained knowledge, model-generated seeding, hand-designed code environments, and fixed verifiers.

### Interpretation

AZR is a high-value case study of autonomous curriculum generation, not a demonstration of unbounded self-improvement. The strongest causal statement is that this particular self-play training procedure improves the listed base checkpoints under the paper’s evaluation protocol. Pair it with the later self-play dynamics analysis, which finds entropy collapse and large-k support limits, and with R-Zero, which separates challenger and solver but eventually collapses as pseudo-label quality declines.

## Discussion and follow-up

When does an executable verifier provide genuinely new learning signal, and when does it merely reinforce the pretrained model’s existing coverage?
