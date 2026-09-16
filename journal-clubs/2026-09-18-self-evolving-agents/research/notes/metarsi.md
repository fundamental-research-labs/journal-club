# MetaRSI / RSI2

[Paper v2](https://arxiv.org/html/2609.06396v2). Zihan Tan et al.; September 6, revised September 9, 2026; preprint. Accessed September 16; §§3–5.2 and Table 3 inspected, not a complete appendix/code audit. Family: MetaRSI.

**Question/method.** How should data, harness, and weight updates be composed? Typed edit surfaces, refreshed evidence, scheduling, and cross-term meta policies; sealed evaluator stays outside writable state. Open-weight target Qwen3.5-35B-A3B; same target fills model roles, with external verification (§5.1).

**Reported evidence.** Table 3: average gain +10.9 points versus frozen, +6.6 harness-only, +7.3 fixed composition; incremental difference +3.6 over fixed composition. Five outer seeds. Benchmark inventory: Terminal-Bench 89, SWE-bench Pro 731, GPQA hard subset 100, AIME 60. These inventories must not be silently treated as audited adaptation/sealed split counts. Table 3 gives means without intervals. Authors state matching of tokens, GPU-hours, time, candidates, and verifier queries; actual ledgers not reproduced.

**Authors' claim.** Scheduling contributes beyond individual update operators.

**Interpretation/limits.** Promising composition evidence under machine-checkable feedback. External verification remains supervision. Repeated terms receive renewed budgets, so later gains are not free acceleration. Novelty and evidential maturity differ.

**Inspect/discuss.** Tables 1–3; audit splits, budget ledgers, and multi-term controls before a strong causal slide.
