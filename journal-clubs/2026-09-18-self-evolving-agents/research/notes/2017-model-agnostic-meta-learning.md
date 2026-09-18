# Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks

## Source and reading scope

Key: `2017-model-agnostic-meta-learning`. Chelsea Finn, Pieter Abbeel, Sergey Levine. [ICML 2017 proceedings](https://proceedings.mlr.press/v70/finn17a.html); peer-reviewed ICML 2017 proceedings paper, PMLR 70:1126–1135. Read September 18, 2026: §§1–2, Algorithm 1, §3 setting definitions and §4 distinction from learned update rules. Full text accessed; review limited to these sections. No original retained: redistribution permission was not established in this pass.

## Mechanism, interpretation and limits

The outer objective optimizes initial parameters for performance after inner gradient updates on a task. Held-out tasks assess adaptation; this is not a test of retaining all sequentially acquired abilities. MAML is a representative mechanism, not claimed as the origin of meta-learning. SEAL v2 §§2–3 independently describes its self-edit generation as meta-learning; its §5 separately acknowledges forgetting.

## Use and discussion

Introduction and meta-learning section: learning an initialization differs from editing an improver. Does experience improve the starting representation, the update data, or the procedure selecting updates?

[Citation/coverage scope](../thesis-coverage.md#scholarly-foundations-revision--september-18-2026). These targeted foundation readings do not extend the earlier 55-paper citation-network audit.
