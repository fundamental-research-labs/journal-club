# Notes

## Why It Matters
MAPPO is a useful corrective to the idea that cooperative MARL should default to off-policy value-decomposition methods. Its main contribution is not a novel algorithmic trick, but a broad empirical case that standard PPO, with CTDE-style critic inputs and careful implementation details, is a serious baseline on widely used cooperative benchmarks.

## When To Cite
Cite it when discussing PPO in multi-agent reinforcement learning, cooperative MARL baselines, centralized-training/decentralized-execution actor-critic methods, sample-efficiency comparisons against QMix/MADDPG-style methods, or practical implementation choices for SMAC, MPE, GRF, and Hanabi experiments.

## Key Terms
MAPPO; IPPO; proximal policy optimization; cooperative MARL; centralized training decentralized execution; centralized critic; decentralized execution; parameter sharing; value normalization; agent-specific global state; feature-pruned critic input; training epochs; mini-batching; PPO clipping; batch size; death masking; MPE; SMAC; Google Research Football; Hanabi.
