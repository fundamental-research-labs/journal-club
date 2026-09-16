# TarMAC: Targeted Multi-Agent Communication

**Authors:** Abhishek Das, Theophile Gervet, Joshua Romoff, Dhruv Batra, Devi Parikh, Michael Rabbat, Joelle Pineau
**arXiv:** 1810.11187
**Venue:** Proceedings of the 36th International Conference on Machine Learning (ICML 2019)
**Date:** June 2019 (ICML); arXiv first posted October 2018; local PDF is arXiv v2 dated February 2020

## Problem
Cooperative multi-agent reinforcement learning often needs communication because each agent sees only a local, partial observation. Prior learned-communication systems commonly broadcast or average messages, making every recipient receive the same information and making it hard to inspect who is using which message. The paper asks whether agents can learn what to say, whom to address, and whether multiple communication rounds before acting help, using only downstream task reward.

## Method
TarMAC uses a centralized-training/decentralized-execution actor-critic setup with recurrent agent policies. Each agent receives its local observation plus an aggregated incoming message, then outputs both an environment action and a continuous message. The message is split into a sender signature/key and a value; each receiver predicts a query from its hidden state, computes soft attention over sender signatures, and receives an attention-weighted combination of message values. The same mechanism can be repeated for multiple communication rounds before the final action. Experiments cover SHAPES navigation, traffic junction control, House3D first-person navigation, and an IC3Net hybrid for Predator-Prey.

## Key Findings
- TarMAC combines decentralized execution, targeted communication, multi-round decisions, and actor-critic reinforcement learning, a combination the paper contrasts with DIAL, CommNet, VAIN, ATOC, and IC3Net.
- In SHAPES, communication helps most as the task becomes more complex: on the 50x50 mixed-goal setting, TarMAC reports 85.8% success versus 82.4% for mean-pooled communication and 69.1% for no communication.
- On the hard traffic junction task, 2-round TarMAC reports 97.1% success, above 1-round TarMAC at 84.6% and CommNet at 78.9%; the paper argues extra rounds help more than simply increasing message size.
- Attention patterns are interpretable in the paper's diagnostics: SHAPES agents attend to agents observing relevant target attributes, while traffic agents attend to cars near sensitive internal-grid locations and adapt attention count as active team size changes.
- In House3D find-fireplace navigation, TarMAC reports the best success rate and average path length among the tested communication variants, using compact message vectors with high-dimensional visual observations.
- In mixed Predator-Prey, replacing IC3Net's message averaging with TarMAC attention improves convergence and final episode length, but the paper cautions that pure soft attention can leak information in competitive settings without a separate "when to communicate" gate.

## Tags
`multi-agent-rl`, `emergent-communication`, `targeted-communication`, `attention`, `centralized-training-decentralized-execution`, `actor-critic`, `Dec-POMDP`, `cooperative-navigation`, `traffic-junction`, `House3D`, `IC3Net`

## Connections
- Extends CommNet-style continuous communication by replacing uniform/mean message aggregation with sender-receiver attention.
- Complements IC3Net: IC3Net learns when to communicate, while TarMAC supplies a learned mechanism for whom a message should reach.
- Related to DIAL and other emergent-communication work, but focuses on continuous machine-to-machine messages rather than human-readable discrete language.
- Fits the centralized-training/decentralized-execution line of MARL, alongside centralized critic methods and value-factorization approaches such as QMIX, but uses communication rather than value decomposition as the main coordination channel.
- Useful background for later multi-agent agent systems because it frames communication as routing plus content, not just a shared broadcast channel.
