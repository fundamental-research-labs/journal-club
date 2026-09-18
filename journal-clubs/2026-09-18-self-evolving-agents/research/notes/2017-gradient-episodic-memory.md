# Gradient Episodic Memory for Continual Learning

## Source and reading scope

Key: `2017-gradient-episodic-memory`. David Lopez-Paz, Marc’Aurelio Ranzato. [NIPS 2017 proceedings](https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf); peer-reviewed NIPS 2017 proceedings paper. Read September 18, 2026: §§1–3, equations 2–8, Algorithm 1 and §4.1 experimental setting. Full text accessed; review limited to these sections. No original retained: redistribution permission was not established in this pass.

## Mechanism, interpretation and limits

GEM constrains gradients using stored examples. §2 separates earlier-task changes from performance on future tasks before training, and describes denser evaluations for learning curves. Its integer task descriptors, supervised examples and finite memory differ from open-ended agent streams. The proposed frozen-copy evaluation and pretrained initial baseline are analyst adaptations, not GEM experiments. No benchmark numbers are imported.

## Use and discussion

Introduction and proposed tests: forward/backward transfer, performance matrix, episodic gradient constraints. Does an agent gain on new work while retaining prior abilities, or does its final average hide an exchange between them?

[Citation/coverage scope](../thesis-coverage.md#scholarly-foundations-revision--september-18-2026). These targeted foundation readings do not extend the earlier 55-paper citation-network audit.
