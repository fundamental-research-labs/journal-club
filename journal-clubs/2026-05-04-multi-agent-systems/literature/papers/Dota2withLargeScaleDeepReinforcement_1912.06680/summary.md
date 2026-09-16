# Dota 2 with Large Scale Deep Reinforcement Learning

**Authors:** OpenAI; Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemyslaw "Psyho" Debiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, Rafal Jozefowicz, Scott Gray, Catherine Olsson, Jakub Pachocki, Michael Petrov, Henrique Ponde de Oliveira Pinto, Jonathan Raiman, Tim Salimans, Jeremy Schlatter, Jonas Schneider, Szymon Sidor, Ilya Sutskever, Jie Tang, Filip Wolski, Susan Zhang
**arXiv:** 1912.06680
**Venue:** Preprint
**Date:** March 10, 2021 (arXiv v1: December 13, 2019)

## Problem
Dota 2 stresses reinforcement learning with long real-time games, partial observability, high-dimensional observations, and very large discrete action spaces. The paper asks whether scaled self-play RL can reach world-class performance in this multi-agent esport setting, despite a changing game environment and practical engineering constraints.

## Method
OpenAI Five controls five Dota 2 heroes using replicas of a shared recurrent policy with a 4096-unit LSTM core and about 159 million parameters. The policy is trained with PPO and GAE from self-play experience, using semantic game-state observations rather than pixels, 80% current-policy self-play and 20% games against older policies. A distributed training system separates rollout CPU workers, forward-pass GPUs, optimizer GPUs, and a controller, pushing fresh experience continuously. The project also introduces "surgery" tools to continue a long training run across model, observation, action-space, and Dota-version changes without restarting from scratch.

## Key Findings
- OpenAI Five defeated OG, the reigning Dota 2 world champion team, 2-0 on April 13, 2019, and won 99.4% of 7,257 public Arena games.
- The final system was not a new RL algorithm so much as a large-scale PPO self-play system: batches reached roughly 1-3 million timesteps, training lasted 180 training days spread across 10 months, and the paper estimates 770 +/- 50 PFlops/s-days of optimization compute by the world-champion match.
- Continual-transfer surgery enabled more than twenty successful changes during training, including game-version, observation, action, item, and LSTM-size changes; a later from-scratch Rerun validated the final environment but also showed surgery was imperfect.
- Data freshness mattered strongly: stale rollout data and sample reuse slowed learning in early-training ablations, motivating the final system's tight rollout-to-optimization loop.
- Longer reward horizons improved a trained agent up to the 6-12 minute range tested, suggesting long-term credit assignment was useful in high-skill Dota 2 play.
- Scope is restricted: OpenAI Five played a 17-hero subset, excluded items requiring temporary multi-unit control, used scripted logic for some mechanics, and trained from structured observations rather than rendered pixels.

## Tags
`deep-rl`, `self-play`, `multi-agent-rl`, `distributed-training`, `ppo`, `lstm`, `continual-training`, `esports`, `dota-2`, `openai-five`

## Connections
- Complements **AlphaStar** as another large-scale real-time esport result, but emphasizes pure self-play, Dota 2 team coordination, and continual surgery during a changing environment.
- Useful background for **MAPPO**, **QMIX**, **MADDPG**, and other multi-agent RL papers as a high-compute applied system rather than a compact algorithmic benchmark.
- Connects to **AgentScalingDiversity** and multi-agent coordination work by showing that a homogeneous shared policy can coordinate five agents through self-play, shaped rewards, and team-spirit tuning.
- Relevant to infrastructure-focused agent papers because many lessons are systems lessons: data freshness, batch scaling, distributed rollout pipelines, and preserving progress across iterative environment changes.
