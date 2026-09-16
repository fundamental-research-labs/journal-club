# Multi-Agent Reinforcement Learning in Sequential Social Dilemmas

**Authors:** Joel Z. Leibo, Vinicius Zambaldi, Marc Lanctot, Janusz Marecki, Thore Graepel
**arXiv:** 1702.03037
**Venue:** AAMAS 2017
**Date:** May 2017

## Problem
Classic matrix-game social dilemmas treat cooperation and defection as atomic simultaneous actions. Many real social dilemmas are sequential, partially observed, and require agents to learn policies that implement cooperative or defective intent. The paper asks how social dilemma structure changes when the agents must learn both what strategic stance to take and how to execute it over time.

## Method
The paper defines a sequential social dilemma (SSD) as a partially observable general-sum Markov game containing cooperative and defective policy sets whose empirical payoff matrix satisfies the usual social dilemma inequalities. It studies two gridworld SSDs: Gathering, where agents collect apples and can tag rivals with a beam, and Wolfpack, where two wolves can hunt prey alone or together for different rewards. Independent DQN agents learn from local observations while the authors vary environment and agent parameters, then use empirical game-theoretic analysis to classify the learned policy outcomes.

## Key Findings
- Gathering and Wolfpack can both induce prisoner-dilemma-like empirical payoff matrices, but their sequential implementations make different predictions about when cooperation or defection emerges.
- In Gathering, scarce apples and longer rival-removal windows lead to more aggressive beam use; plentiful resources lead to less aggressive policies.
- In Wolfpack, larger capture radius and stronger team capture reward increase the average number of wolves involved in captures, indicating more cooperative hunting.
- Agent parameters matter: greater patience tends to increase defection in both games, while larger network capacity has opposite qualitative effects in Gathering and Wolfpack because the harder-to-learn behavior differs by domain.
- The main modeling lesson is that cooperation and defection are policy-level properties, and their implementation complexity can change the expected social outcome even when the induced matrix game looks similar.

## Tags
`multi-agent-rl`, `sequential-social-dilemmas`, `markov-games`, `cooperation`, `social-dilemmas`, `empirical-game-theory`, `deep-q-networks`, `gridworld`

## Connections
- Useful foundation for later MARL social-dilemma work because it moves beyond repeated 2x2 matrix games to temporally extended policy learning.
- Complements **MADDPG_1706.02275** by using independent DQN agents descriptively to study emergent social behavior, rather than proposing centralized-training algorithms for continuous-control cooperation.
- Related to **EmergentMultiAgentCommunicationintheDeep_2006.02419** as an early deep-MARL study of emergent social behavior, though this paper focuses on cooperation and conflict rather than learned communication.
- Provides conceptual background for modern multi-agent agent-evaluation papers such as **CooperBench_2601.13295**, where coordination failures depend on how agents implement policies over time rather than on static payoff labels alone.
