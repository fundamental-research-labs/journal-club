# Evo-Harness

## Source and access

**Source key:** `2026-evo-harness`.

**Originals and source links:** [register](../sources.md#2026-evo-harness); [canonical source](https://arxiv.org/abs/2608.15071). Retained unmodified: [2026-evo-harness-paper-v2.pdf](../originals/2026-evo-harness/2026-evo-harness-paper-v2.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Source/key:** `2026-evo-harness` — Tianxin Wei et al., *Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents*. [arXiv](https://arxiv.org/abs/2608.15071), [versioned PDF](https://arxiv.org/pdf/2608.15071v2). First submitted 2026-08-15; latest and read version **v2, 2026-08-30**, verified from the arXiv submission history and the PDF stamp `arXiv:2608.15071v2 [cs.AI] 30 Aug 2026`; arXiv comment says EMNLP 2026 Main. Read 2026-09-16: algorithm, §§4.1–4.6, Tables 1–5, transfer figure, Appendix A.

## Question and methods

Can a frozen solver compile one-shot execution contexts into local task-type skills and cross-task guidance during a stream? Main Opus 4.6 experiments cover CL-Bench (1,899), Terminal-Bench 2 (89), SWE-bench Lite (300), τ-bench (165), and WebArena-Infinity (80); environment verifiers or rubric judges supply feedback (Appendix A, Table 5).

## Results and evidence

Versus no evolution, pass/success rates are 34.02 vs 29.54 on CL-Bench, 73.03 vs 62.92 on Terminal-Bench, 67.00 vs 63.67 on SWE-bench Lite, 76.97 vs 72.73 on τ-bench, and 76.25 vs 72.50 on WebArena (Table 1). Every one of five CL-Bench solver models improves overall, by +0.8 to +4.5 points, although some categories regress (Table 2). On SWE-bench Lite, a Sonnet-4.5-evolved harness transferred to Opus 4.7 on the held-out test split gives 73.4 versus 68.8 with no evolution; online updating gives 75.0 (§4.5, Figure 5). Self-generated feedback regresses CL-Bench 29.54→27.96 and SWE-bench Lite 63.67→61.67; grounded minimal/standard feedback recovers or improves performance (Table 4).

## Appraisal and limitations

### Interpretation

Breadth and the explicit train-split transfer test make this a strong recent source. The negative feedback ablation supports a qualified lesson: persistent guidance helps when grounded by external evidence and matched to solver capability; it can also make the solver worse.

### Limitations

Main results are sequential online streams, so adaptation and later evaluation share a task distribution and depend on order. The paper does not report repeated independent stream runs, uncertainty intervals, or a complete token/dollar budget. The train/test counts for the transfer figure are not stated next to the result.

## Discussion and follow-up

How much of the gain survives replacing oracle feedback with self-generated feedback on held-out tasks?

[Prominent citations and their roles](../prominent-citations.md#2026-evo-harness)
