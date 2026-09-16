# Value-Decomposition Networks For Cooperative Multi-Agent Learning

**Authors:** Peter Sunehag, Guy Lever, Audrunas Gruslys, Wojciech Marian Czarnecki, Vinicius Zambaldi, Max Jaderberg, Marc Lanctot, Nicolas Sonnerat, Joel Z. Leibo, Karl Tuyls, Thore Graepel
**arXiv:** 1706.05296
**Venue:** Preprint
**Date:** June 2017

## Problem
Cooperative multi-agent reinforcement learning with one shared team reward is hard under partial observability: independent learners receive non-stationary and often spurious reward signals, while fully centralized Q-learning faces a combinatorial joint action space and can learn "lazy agent" policies where one agent does the useful work and another avoids exploration.

## Method
VDN assumes the joint action-value function can be approximated as an additive sum of per-agent value functions, `Q_tot(h, a) ~= sum_i Q_i(h_i, a_i)`. Training backpropagates the team-reward Q-learning loss through this summation into recurrent DQN-style agent networks; execution is decentralized because each agent acts greedily from its own local value output. The paper evaluates VDN variants with shared weights, role identifiers, and low- or high-level information channels against independent learners and centralized baselines.

## Key Findings
- Across seven two-agent gridworld tasks built from Switch, Fetch, and Checkers variants, value-decomposition architectures outperform independent learners and centralized baselines in normalized training AUC and final performance.
- The learned decomposition can assign value spikes to the agent whose pickup or drop-off event is imminent even though the environment provides only a team reward.
- Weight sharing helps avoid a lazy-agent failure in the difficult one-corridor Fetch task, but it can hurt when agents need asymmetric roles or value scales, as in Checkers.
- Role information and information channels are useful enhancements in some tasks, with low-level communication learning faster than higher-level communication in the reported experiments.
- The experiments are limited to small, two-agent, partially observable gridworlds, so the paper frames scaling to larger teams and nonlinear value aggregation as future work.

## Tags
`multi-agent-rl`, `cooperative-marl`, `value-decomposition`, `value-factorization`, `centralized-training-decentralized-execution`, `deep-q-learning`, `credit-assignment`, `partial-observability`

## Connections
- Direct predecessor to **QMIX**, which generalizes VDN's fixed additive factorization with a learned monotonic mixing network.
- Related to **COMA** as an early deep cooperative MARL method addressing credit assignment from a shared team reward, but VDN is value-based while COMA is actor-critic with a counterfactual baseline.
- Complements **MADDPG** and **MAPPO** as another centralized-training/decentralized-execution pattern: VDN centralizes the training target through value summation rather than a centralized critic.
- Provides a baseline family later used in **SMAC** and PyMARL-style cooperative MARL benchmarks.
- Historically adjacent to **RIAL/DIAL** because both exploit centralized learning signals while preserving decentralized execution in partially observable cooperative tasks.
