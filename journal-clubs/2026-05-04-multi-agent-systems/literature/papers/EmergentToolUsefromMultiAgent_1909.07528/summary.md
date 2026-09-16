# Emergent Tool Use from Multi-Agent Autocurricula

**Authors:** Bowen Baker, Ingmar Kanitscheider, Todor Markov, Yi Wu, Glenn Powell, Bob McGrew, Igor Mordatch
**arXiv:** 1909.07528
**Venue:** ICLR 2020
**Date:** February 2020

## Problem
Directly specifying rewards or demonstrations for rich embodied skills is costly, and intrinsic-motivation exploration can become poorly targeted in complex environments. The paper asks whether multi-agent competition can create a self-supervised autocurriculum that keeps generating new, physically grounded challenges for agents.

## Method
The authors build a MuJoCo hide-and-seek world with hider and seeker teams, movable boxes, ramps, randomly generated walls/rooms, partial observability, object grabbing, and team-based object locking. Agents receive only the hide-and-seek visibility reward, with no explicit reward for tool use or exploration. Policies are trained with PPO self-play using decentralized execution, a centralized omniscient critic, entity-centric observations, self-attention over agents/objects, and an LSTM. The paper also compares against intrinsic-motivation baselines and proposes transfer/fine-tuning on five domain-specific intelligence tests.

## Key Findings
- Self-play produced a six-stage strategy progression: running/chasing, fort building, ramp use, ramp defense, box surfing, and surf defense.
- Several phases require tool use and coordination: hiders build shelters from boxes, seekers use ramps to enter shelters, seekers later surf boxes from locked ramps, and hiders respond by locking unused boxes before building.
- The autocurriculum is scale- and environment-sensitive: the default setup reached ramp defense only after very large-scale training, smaller batch sizes failed to converge in the reported experiments, and reduced environment randomization produced fewer stages.
- Larger hider teams show useful division of labor; during surf-defense behavior, two- and three-hider teams lock more boxes than a single hider team.
- Intrinsic-motivation baselines produce object interaction mainly when the count representation is hand-chosen to emphasize relevant low-dimensional state features; richer state representations reduce meaningful box movement.
- Transfer results are mixed but informative: hide-and-seek pretraining improves over scratch and count-based pretraining on 3 of 5 targeted tests, while object counting and shelter construction show limits of the learned representations.
- The authors frame the result as proof of concept, noting bounded strategy space, enormous sample complexity, and simulator/exploit artifacts.

## Tags
`multi-agent-rl`, `self-play`, `autocurriculum`, `emergent-tool-use`, `embodied-agents`, `PPO`, `centralized-training`, `transfer-evaluation`, `intrinsic-motivation`

## Connections
- Complements **MultiAgentReinforcementLearningin** as a concrete CTDE/self-play case where agent interaction creates the curriculum.
- Related to **EmergenceofGroundedCompositionalLanguage** and **EmergentMultiAgentCommunicationintheDeep** as evidence that multi-agent pressure can produce emergent behavior, but here the behavior is embodied tool use rather than communication.
- Useful contrast with LLM-agent coordination papers such as **CooperBench** and **CAID**: this paper studies implicit coordination from shared team rewards in simulation, not explicit message passing or repository workflows.
- Relevant to benchmark/evaluation work because it argues reward curves are insufficient for open-ended multi-agent learning and proposes transfer tasks as a capability probe.
