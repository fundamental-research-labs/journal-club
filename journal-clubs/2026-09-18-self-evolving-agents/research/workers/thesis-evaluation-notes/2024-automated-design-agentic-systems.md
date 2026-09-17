# Automated Design of Agentic Systems (ADAS)

## Research question

Can a meta-agent search code-defined agent architectures and outperform fixed hand-designed workflows, including on held-out domains and models? ADAS is foundational meta-agent design search, rather than an agent learning from a deployment task stream.

## Methods

Meta Agent Search uses GPT-4 as optimizer to iteratively write a `forward` function, evaluate it, and archive designs; evaluation uses GPT-3.5 executors. ARC uses 20 validation and 60 held-out test questions, 25 search iterations, and five test evaluations (HTML §§3–4.1, lines 89–110). Four other domains use 30 iterations and held-out tests (lines 121–128). Baselines include CoT, self-refine, debate, quality-diversity, and prompt optimization.

## Findings

On four domains, Meta Agent Search reports DROP F1 79.4±0.8, MGSM accuracy 53.4±3.5, MMLU 69.6±3.2, and GPQA 34.6±3.2, versus prompt optimization 69.1±0.9, 30.6±3.2, 67.6±3.2, and 32.9±3.2 (Table 1, lines 128–145). Authors report transfer to held-out domains/models (Section 4.3), and describe progressive combinations of archive “stepping stones” (lines 115–120).

## Thesis implication

ADAS shows within-search design improvement and some held-out transfer, challenging a blanket claim that gains are only fixed expertise. However, each domain search is separately optimized, so this is not evidence that one agent accumulates value across future production tasks. The relevant comparison is meta-search cost and strong static workflows, not reset versus persistent experience. It supports treating “learning to design” as a distinct mechanism family.

## Limitations

The optimizer is supplied a fixed framework and task-specific prompt text; the search budget is substantial and not compared to equal extra attempts. Transfer is benchmark/model transfer, not open-world task-stream transfer. Results use GPT-3.5 executors and reported bootstrap intervals, but no independent replication was inspected. The paper is CC BY 4.0; no copy retained.
