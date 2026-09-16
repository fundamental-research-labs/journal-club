# R-Zero: Self-Evolving Reasoning LLM from Zero Data

## Source and access

**Source key:** `2025-r-zero`.

**Originals and source links:** [register](../sources.md#2025-r-zero); [canonical source](https://arxiv.org/abs/2508.05004). Retained unmodified: [2025-r-zero-paper-v4.pdf](../originals/2025-r-zero/2025-r-zero-paper-v4.pdf). Paper license: http://creativecommons.org/licenses/by-nc-nd/4.0/. [Manifest](../originals/manifest.json).

**Authors:** Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, Dong Yu

**Canonical source:** https://arxiv.org/abs/2508.05004

**Version read:** arXiv v4, February 13, 2026; first posted August 7, 2025. The PDF identifies the work as an ICLR 2026 conference paper.

**Reading date / depth:** September 16, 2026; full primary PDF and appendices inspected.

## Question and methods

### Question and mechanism

R-Zero separates a Challenger that generates near-frontier math questions from a Solver that learns to answer them. The Challenger reward peaks near an estimated Solver accuracy of 50% and penalizes repeated questions. The Solver generates pseudo-labels by majority vote; difficulty filtering rejects questions that are too easy, too hard, or inconsistent. Challenger and Solver are updated in alternating iterations.

This is “zero external data” only for the generated curriculum. Both roles begin from pretrained models, use hand-designed prompts and reward/filtering rules, and depend on fixed benchmark evaluators; a GPT-4o oracle is used in the paper’s retrospective pseudo-label audit.

### Experimental setting

The main evaluation covers Qwen3-4B/8B-Base and OctoThinker-3B/8B. Solver stages use global batch 128, learning rate 1e-6, 15 steps, and five rollouts; Challenger stages use batch 128, learning rate 1e-6, five steps, and four rollouts (Appendix B.1). Tables report the checkpoint after 45 Solver steps, i.e. three co-evolution iterations. Hardware, wall-clock time, total generated-token count, and number of independent training seeds are not reported.

Math evaluation spans AMC, Minerva, MATH-500, GSM8K, OlympiadBench, AIME 2024, and AIME 2025. AMC and AIME use mean@32; the other math benchmarks use greedy accuracy. General reasoning uses greedy exact match on SuperGPQA, MMLU-Pro, and BBEH. The paper calls the sets held out, but does not supply uncertainty across training runs.

## Results and evidence

- For Qwen3-4B-Base, Table 1 reports math average 42.57→49.93 (+7.36); Table 2 reports general average 26.34→31.15 (+4.81). The abstract’s +6.49 math and +7.54 general figures are not the Table 1/Table 2 differences for this checkpoint/version.
- For Qwen3-8B-Base, rendered PDF Table 1 reports math 48.64→53.72 (+5.08), while the prose directly below reports 49.18→54.69 (+5.51). Rendered PDF Table 2 reports general 31.98→34.50 (+2.52), although the prose immediately below states +5.13. Visual inspection confirms these are source inconsistencies in v4, not PDF-to-text column grouping errors. They should be resolved from code/checkpoints before quoting the abstract or prose aggregates.
- Results are not uniform: Qwen3-4B AIME-2025 falls 10.30→9.60 even as its seven-benchmark average rises; OctoThinker-3B AIME-2024 remains 0.00; OctoThinker-8B AIME-2024 rises only 0.62→3.44 (Table 1).
- A matched ablation on Qwen3-4B reports R-Zero math/general averages 49.07/31.15, versus 45.76/28.73 without repetition penalty and 47.35/26.69 without filtering (Table 3). The differing 49.07 versus Table 1’s 49.93 is another version/aggregation detail to flag.
- For pseudo-label auditing, the authors sample 200 generated questions from each of steps 15, 30, and 45 and treat GPT-4o answers as ground truth. Estimated pseudo-label accuracy falls 79%→69%→63% (Table 5). A separate Gemini-labeled 500-question late-stage audit reports model-size-specific accuracies and shows no universal noise threshold for collapse (Appendix E, Table 7).
- Two-model R-Zero peaks at 49.12 after step 45 and drops to 46.52 at step 60; a single shared Challenger/Solver peaks at 47.31 after step 15 and falls to 43.89 by step 60 (Appendix Table 6). This is direct evidence against indefinite monotonic improvement.

## Appraisal and limitations

### Authors' claim

Co-evolving a specialized Challenger and Solver creates an autonomous curriculum that improves reasoning and transfers to general domains.

### Evidence

The paper tests four base checkpoints, includes matched ablations and a useful data-quality/failure analysis, and directly shows late-iteration collapse. Evidence strength is reduced by missing compute and repeat uncertainty, reliance on model judges for some correctness checks, and internally inconsistent aggregate numbers.

### Interpretation

R-Zero is useful because it exposes both the promise and instability of self-generated curricula. It should be taught as a positive result through iteration three plus a negative result at iteration four. It is in the AZR family and is partly redundant for a shortlist, but its role separation, explicit pseudo-label audit, and collapse result make it the better source for discussing error accumulation and when “self-evolution” stops improving.

## Discussion and follow-up

What stopping or validation rule would detect curriculum deterioration before benchmark performance falls?
