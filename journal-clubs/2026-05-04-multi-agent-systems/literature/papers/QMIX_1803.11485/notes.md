# Notes

## Why It Matters
QMIX is a core value-factorization paper for cooperative multi-agent reinforcement learning. Its main contribution is a practical compromise between fully centralized Q-learning and fully independent learners: use global state during training, but constrain the joint value function so decentralized greedy execution remains valid. This made monotonic mixing a standard baseline and reference point for later centralized-training/decentralized-execution work.

## When To Cite
Cite it for QMIX itself, value-decomposition methods after VDN, centralized training with decentralized execution, monotonic mixing networks, off-policy cooperative MARL, StarCraft II micromanagement experiments, or comparisons against IQL, VDN, and centralized-critic actor-critic approaches such as COMA.

## Key Terms
QMIX; monotonic value factorization; centralized training decentralized execution; `Qtot`; per-agent `Qa`; mixing network; hypernetwork; non-negative mixing weights; value decomposition networks; independent Q-learning; Dec-POMDP; StarCraft II micromanagement; heterogeneous agents.
