# AFlow: Automating Agentic Workflow Generation

## Research question

Can code-represented workflows be searched automatically with execution feedback, and can the resulting workflow improve performance-cost tradeoffs across executor models? AFlow is fixed benchmark workflow search, distinct from continual self-improvement after deployment.

## Methods

AFlow uses Claude 3.5 Sonnet as optimizer and Monte Carlo Tree Search over code workflows. Each candidate is executed five times on validation data; experience records modifications, scores, and failures; search runs for 20 rounds with early stopping (HTML §4, lines 212–224; pseudocode lines 382–413). Six public datasets are split 1:4 validation/test. Baselines include IO, CoT, self-consistency, debate, Self-Refine, MedPrompt, and ADAS. Costs are tracked by token use (lines 218–224).

## Findings

Across six datasets, AFlow averages 80.3%, versus 75.3% MedPrompt and 67.2% ADAS; on Table 1 it scores HotpotQA 73.5, DROP 80.6, HumanEval 94.7, MBPP 83.4, GSM8K 93.5, and MATH 56.2 (lines 226–243). HumanEval cost analysis reports AFlow with GPT-4o-mini execution at 94.7% for $0.0513 versus GPT-4o IO 93.89% for $0.6371; cross-model transfer is mixed, with workflows discovered on one executor weaker on another (lines 249–256, 527–561).

## Thesis implication

AFlow is evidence that search over workflows can discover useful fixed artifacts and sometimes lower execution cost. It strengthens the extra-compute/static-design counterfactual: gains may come from spending an optimization budget once to produce a reusable workflow. The mixed cross-model result cautions against calling this general self-improvement. There is no deployment-time accumulation, old-task retention test, or successive-domain learning curve.

## Limitations

Validation feedback and test evaluation are benchmark-specific; transfer is across executor models and selected datasets, not held-out future task families. Reported averages use three test runs, while candidate evaluation uses five validation runs. Cost omits human review and optimizer labor. The arXiv v4 page carries a perpetual non-exclusive license; no copy retained.
