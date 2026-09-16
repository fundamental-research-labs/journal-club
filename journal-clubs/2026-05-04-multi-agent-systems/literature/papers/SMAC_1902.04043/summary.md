# The StarCraft Multi-Agent Challenge (SMAC)

**Authors:** Mikayel Samvelyan, Tabish Rashid, Christian Schroeder de Witt, Gregory Farquhar, Nantas Nardelli, Tim G. J. Rudner, Chia-Man Hung, Philip H. S. Torr, Jakob Foerster, Shimon Whiteson
**arXiv:** 1902.04043
**Venue:** NeurIPS 2019 Deep Reinforcement Learning Workshop
**Date:** December 2019

## Problem
Cooperative multi-agent reinforcement learning lacked a standard, challenging benchmark analogous to ALE or MuJoCo for single-agent RL. Existing work often used one-off toy domains, making progress hard to compare, especially for partially observable tasks requiring decentralized execution.

## Method
SMAC turns StarCraft II micromanagement into a cooperative Dec-POMDP benchmark. Each allied unit is controlled by an independent learning agent that acts from local observations and a limited field of view, while enemy units are controlled by the built-in StarCraft II AI. The benchmark supplies 14 combat scenarios spanning symmetric battles, asymmetric battles, and micro-trick tasks such as kiting and terrain use. Training may use global state under centralized training, but evaluation requires decentralized execution. The paper also releases PyMARL, a PyTorch framework with implementations of IQL, VDN, COMA, QMIX, and QTRAN-style baselines.

## Key Findings
- SMAC is designed to test partial observability, high-dimensional unit features, large joint action spaces, and coordination skills such as focus fire, avoiding overkill, kiting, and choke-point control.
- The authors recommend standardized evaluation: fixed environment settings, decentralized test-time policies, win-rate curves over environment steps, multiple independent runs, median performance, and reporting compute resources.
- A simple focus-fire heuristic performs poorly on many scenarios, indicating that the suite requires richer coordination than attacking the nearest enemy.
- In the reported experiments, QMIX has the strongest overall performance among the tested methods and value-based methods generally outperform COMA on sample efficiency.
- Several scenarios remain hard or super-hard for all tested algorithms, motivating work on exploration, coordination, and history-dependent policies.

## Tags
`multi-agent-rl`, `benchmark`, `StarCraft-II`, `SMAC`, `PyMARL`, `centralized-training-decentralized-execution`, `Dec-POMDP`, `partial-observability`, `micromanagement`

## Connections
- Follows the benchmark role of ALE and MuJoCo, but targets cooperative MARL rather than single-agent control.
- Provides the standard evaluation environment used by later value-factorization and CTDE methods, especially QMIX-style work.
- Builds on SC2LE while changing the task from full-game StarCraft II control to decentralized cooperative micromanagement.
- Closely related to COMA, QMIX, VDN, IQL, and QTRAN as baseline families evaluated through PyMARL.
