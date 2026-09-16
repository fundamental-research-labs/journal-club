# MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning

**Authors:** Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman Ozdaglar, Kaiqing Zhang, Joo-Kyung Kim
**arXiv:** 2502.18439
**Venue:** Preprint
**Date:** July 2025

## Problem
Prompted multi-agent LLM systems can simulate collaboration, but they are not explicitly trained to coordinate. The paper argues that out-of-the-box collaboration and single-agent post-training can fail to induce useful cooperative behavior, especially when agents need to revise, persuade, or incorporate others' reasoning across multiple turns.

## Method
MAPoRL treats collaborative debate as a multi-agent reinforcement learning problem. Multiple LLM agents first answer independently, then debate over several turns while conditioning on their own and other agents' previous responses. A learned verifier scores each answer, and each agent is trained with multi-agent PPO to maximize rewards that include its current verifier score and its influence on future answers by itself and other agents. The paper also adds reward-shaping incentives for useful self-revision and influence on the group majority. Experiments use mostly small instruction models, including Phi-3-mini-128k-instruct, Qwen2.5-3B-instruct, and Llama-3-8B-instruct, with QLoRA adapters on GSM8K/TinyGSM and ANLI.

## Key Findings
- A simple game-theoretic model predicts why a single agent best-responding to a fixed, non-strategic opponent may avoid collaboration, while jointly optimized agents can coordinate when collaborative synergy is sufficiently valuable.
- In prompted debate, off-the-shelf Phi-3 agents do not reliably improve across turns; MAPoRL-trained agents improve over turns on GSM8K and ANLI and show more wrong-to-right revision behavior.
- A no-collaboration control reports similar single-question accuracy for off-the-shelf Phi-3 and MAPoRL-trained models, supporting the interpretation that gains come from interaction rather than only memorized task knowledge.
- Collaboration behavior transfers in the tested directions: ANLI-trained MAPoRL agents improve on GSM8K by later turns, and GSM8K-trained agents improve on ANLI.
- Verifier shaping helps but is not the whole effect: on the GSM8K ablation, MAPoRL without verifier rewards still improves over debate turns, while verifier rewards yield larger final accuracy.
- Naive SFT on selected high-quality debate trajectories underperforms the off-the-shelf model in the authors' setup, and heterogeneous model-pair experiments suggest co-training can help models with different strengths.

## Tags
`multi-agent-rl`, `llm-post-training`, `collaborative-reasoning`, `multi-agent-debate`, `verifier-rewards`, `ppo`, `qlora`, `gsm8k`, `anli`

## Connections
- Complements multi-agent debate work by asking how to train agents for collaboration instead of relying only on prompting.
- Relevant to **CooperBench** and other coordination-gap papers: MAPoRL is an attempt to make coordination a learned behavior rather than an assumed capability.
- Relevant to **CAID** as a different route to agent collaboration: CAID emphasizes software-engineering isolation and merge mechanics, while MAPoRL emphasizes RL co-training of the interacting models.
- Connects to self-correction and RLHF/RLAIF work because the verifier supplies outcome-style feedback over multi-turn reasoning, but the objective is explicitly multi-agent.
