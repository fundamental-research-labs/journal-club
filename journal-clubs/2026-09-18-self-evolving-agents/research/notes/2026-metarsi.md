# MetaRSI / RSI2

## Source and access

**Source key:** `metarsi`.

**Originals and source links:** [register](../sources.md#metarsi); [canonical source](https://arxiv.org/abs/2609.06396v2). Retained unmodified: [2026-metarsi-paper-v2.pdf](../originals/2026-metarsi/2026-metarsi-paper-v2.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

[Paper v2](https://arxiv.org/html/2609.06396v2). Zihan Tan et al.; September 6, revised September 9, 2026; preprint. Accessed September 16; §§3–5.2, Table 3, and Appendix F inspected; targeted code/artifact audit below, not a complete code review. Family: MetaRSI.

## Question and methods

How should data, harness, and weight updates be composed? Typed edit surfaces, refreshed evidence, scheduling, and cross-term meta policies; sealed evaluator stays outside writable state. Open-weight target Qwen3.5-35B-A3B; same target fills model roles, with external verification (§5.1).

## Results and evidence

### Reported evidence

Table 3: average gain +10.9 points versus frozen, +6.6 harness-only, +7.3 fixed composition; incremental difference +3.6 over fixed composition. Five outer seeds. Benchmark inventory: Terminal-Bench 89, SWE-bench Pro 731, GPQA hard subset 100, AIME 60. These inventories must not be silently treated as audited adaptation/sealed split counts. Table 3 gives means without intervals. Authors state matching of tokens, GPU-hours, time, candidates, and verifier queries; actual ledgers not reproduced.

### September 16 artifact audit

Appendix F specifies five outer seeds, single-decode pass@1, separate improvement/meta-training ledgers, fixed-base cumulative training, and a sealed split opened after freezing. It also supplies the 100 GPQA Record IDs (Table 10). These are accounting **conventions**, not released per-run realized costs. The [official project page](https://www.cosmosmind.top/research/metarsi-v1) is dated September 3, before the September 6 arXiv submission; record these as distinct events. Its GitHub link resolves to [RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness/tree/33c4f8dfac4359987f2e814e187de67c332498de), commit September 9 16:43 UTC. The repository exposes Pi-based Genome harness configuration, not an identifiable reproduction package for every Table 3 condition. Its 172-entry recursive tree had no paths matching split/ledger/result/benchmark/license; the README and linked project landing page did not establish published budget ledgers. This bounded search does not prove no release exists elsewhere.

## Appraisal and limitations

### Authors' claim

Scheduling contributes beyond individual update operators.

### Interpretation and limitations

Promising composition evidence under machine-checkable feedback. External verification remains supervision. Repeated terms receive renewed budgets, so later gains are not free acceleration. Novelty and evidential maturity differ.

## Discussion and follow-up

### Inspect/discuss

Tables 1–3; audit splits, budget ledgers, and multi-term controls before a strong causal slide.

### Status of open question

Not resolved by an inspectable empirical ledger. Cite matching as the authors' stated protocol; do not call it independently verified compute parity. Five outer seeds do not repair unspecified split membership or unreported intervals. The claim that composition causally dominates individual operators remains provisional.
