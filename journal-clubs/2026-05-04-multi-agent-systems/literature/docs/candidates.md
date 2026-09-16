# Candidate Papers (400-paper expansion)

Expanded candidate universe for selecting the final top 100 multi-agent papers. This file now treats `docs/seeds.md` as the 100-paper search instrument and adds 300 additional candidates/watchlist items from agent-curated batches plus local citation snowballing over `papers/*/source/*.bib`.

For the broader 1000-paper field map, see `docs/field-map-1000.md`, `docs/field-map-1000.csv`, and `docs/field-map-1000.yaml`. The 1000-paper map preserves these 400 curated rows as its base and adds 600 lower-confidence auto-expanded rows for landscape analysis rather than top-100 selection.

## Legend
- **Status**: `seed` (active expansion seed), `candidate` (eligible for scoring), `watchlist` (promising but needs identifier/quality cleanup), `top100` (selected later), `cut` (reviewed and excluded).
- **Role**: `core`, `trend`, `bridge`, `anchor`, or `survey`, following `docs/top100-methodology.md`.
- **Provenance**: `seed`, `agent-batch:<lane>`, `prior-candidate`, `manual-gap`, or `local-snowball:N`, where `N` is the number of distinct local paper source trees whose BibTeX references contained the paper.
- **Local refs**: distinct local `papers/*/source` trees that referenced the paper during the BibTeX snowball pass; this is a discovery signal, not a ranking score.

## Current Stats
- Total entries: 400
- By status: `candidate` 286, `seed` 100, `watchlist` 14
- By provenance family: `agent-batch` 244, `local-snowball` 49, `manual-gap` 7, `seed` 100
- Sub-area balance:
  - LLM Multi-Agent Frameworks and Coordination: 65
  - Debate, Reasoning, and Aggregation: 35
  - Agent Foundations and Infrastructure: 45
  - Benchmarks and Evaluation: 45
  - Software, Web, and Computer-Use Agents: 55
  - Scientific and Domain Agents: 35
  - Safety, Security, and Reliability: 35
  - MARL, Emergent Communication, and Social Behavior: 55
  - Surveys and Taxonomies: 20
  - Classical MAS and Game-Theoretic Foundations: 10

---

## 1. LLM Multi-Agent Frameworks and Coordination

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 1 | A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration (DyLAN) | Liu et al | 2023 | 2310.02170 | seed | core | seed | 1 | core; Dynamic agent networks |
| 2 | AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors | Chen et al | 2023 | 2308.10848 | seed | core | seed | 1 | core; Multi-agent frameworks |
| 3 | AutoAgents: A Framework for Automatic Agent Generation | Chen et al | 2023 | 2309.17288 | seed | core | seed | 1 | core; Automatic agent generation |
| 4 | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | Wu et al | 2023 | 2308.08155 | seed | core | seed | 1 | core; Multi-agent frameworks |
| 5 | CAMEL: Communicative Agents for "Mind" Exploration of LLM Society | Li et al | 2023 | 2303.17760 | seed | core | seed | 1 | core; Agent communication |
| 6 | Generative Agents: Interactive Simulacra of Human Behavior | Park et al | 2023 | 2304.03442 | seed | core | seed | 1 | core; Society of agents |
| 7 | War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars | Hua et al | 2023 | 2311.17227 | seed | core | seed | 1 | core; Historical/social simulation |
| 8 | ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration | Estornell et al | 2024 | 2411.00053 | seed | trend | seed | 1 | trend; Learned collaboration |
| 9 | AgentScope: A Flexible yet Robust Multi-Agent Platform | Gao et al | 2024 | 2402.14034 | seed | core | seed | 1 | core; Multi-agent platform |
| 10 | Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks | Fourney et al | 2024 | 2411.04468 | seed | core | seed | 2 | core; Generalist multi-agent system |
| 11 | Scaling Large Language Model-based Multi-Agent Collaboration | Qian et al | 2024 | 2406.07155 | seed | core | seed | 1 | core; Collaboration scaling |
| 12 | AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems | Yang et al | 2025 | 2504.00587 | seed | core | seed | 1 | core; Decentralized coordination |
| 13 | MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems | Ye et al | 2025 | 2503.03686 | seed | trend | seed | 1 | trend; Automated MAS construction |
| 14 | Multi-Agent Architecture Search via Agentic Supernet | Zhang et al | 2025 | 2502.04180 | seed | core | seed | 1 | core; Architecture search |
| 15 | Multi-Agent Collaboration via Evolving Orchestration | Dang et al | 2025 | 2505.19591 | seed | core | seed | 1 | core; Adaptive orchestration |
| 16 | OMAC: A Broad Optimization Framework for LLM-Based Multi-Agent Collaboration | Li et al | 2025 | 2505.11765 | seed | trend | seed | 0 | trend; Collaboration optimization |
| 17 | Why Do Multi-Agent LLM Systems Fail? | Cemri et al | 2025 | 2503.13657 | seed | core | seed | 1 | core; Failure analysis |
| 18 | Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity | Yang et al | 2026 | 2602.03794 | seed | core | seed | 1 | core; Scaling & diversity |
| 19 | Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | Zhang et al | 2025 | OpenReview:LkzuPorQ5L | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Communication pruning for economical MAS |
| 20 | Theory of Mind for Multi-Agent Collaboration via Large Language Models | Li et al | 2023 | 2310.10701 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | ToM prompts for collaborative agents |
| 21 | Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents | Talebirad & Nadiri | 2023 | 2306.03314 | watchlist | core | agent-batch:core-frameworks-reasoning | 1 | Early broad collaboration framing |
| 22 | Emergent Coordination in Multi-Agent Language Models | Riedl | 2025 | 2510.05174 | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Recent coordination-focused analysis |
| 23 | ChatLaw: A Multi-Agent Collaborative Legal Assistant with Knowledge Graph Enhanced Mixture-of-Experts Large Language Model | Cui et al | 2023 | 2306.16092 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Multi-agent legal assistant with KG/MoE |
| 24 | Multi-Agent Consensus Seeking via Large Language Models | Chen et al | 2023 | 2310.20151 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Consensus-seeking planner for multi-agent settings |
| 25 | Self-Adaptive Large Language Model (LLM)-Based Multiagent Systems | Nascimento et al | 2023 | ACSOS-C 2023 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Early self-adaptation framing for LLM-MAS |
| 26 | G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks | Zhang et al | 2024 | 2410.11782 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Learns communication graph designs |
| 27 | Multi-Agent Verification: Scaling Test-Time Compute with Goal Verifiers | Lifshitz et al | 2025 | OpenReview:H22e93wnMe | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Goal verifiers for test-time scaling |
| 28 | Multi-Agent Communication Meets Natural Language: Synergies Between Functional and Structural Language Learning | Lazaridou et al | 2020 | ACL 2020 | candidate | core | agent-batch:marl-emergent-classical | 2 | Human-language priors for emergent communication |
| 29 | GPT-in-the-Loop: Adaptive Decision-Making for Multiagent Systems | Nascimento et al | 2023 | 2308.10435 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Uses GPT inside adaptive MAS control loops |
| 30 | MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs | Yu et al | 2024 | 2403.19267 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Large-scale embodied interaction environment |
| 31 | VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft | Dong et al | 2024 | 2406.05720 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Graph-based Minecraft coordination |
| 32 | MetaAgents: Simulating Interactions of Human Behaviors for LLM-based Task-Oriented Coordination via Collaborative Generative Agents | Li et al | 2023 | 2310.06500 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Collaborative generative agents for coordination |
| 33 | Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration | Wang et al | 2023 | 2307.05300 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Multi-persona self-collaboration |
| 34 | RoCo: Dialectic Multi-Robot Collaboration with Large Language Models | Mandi et al | 2023 | 2307.04738 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Dialectic robot collaboration with LLMs |
| 35 | Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems? | Chen et al | 2023 | 2309.15943 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Centralized/decentralized robot collaboration |
| 36 | Learning when to Communicate at Scale in Multiagent Cooperative and Competitive Tasks | Singh et al | 2019 | 1812.09755 | candidate | core | agent-batch:marl-emergent-classical | 1 | IC3Net communication control |
| 37 | Co-NavGPT: Multi-Robot Cooperative Visual Semantic Navigation using Large Language Models | Yu et al | 2023 | 2310.07937 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Multi-robot navigation with LLM planning |
| 38 | MAVEN: Multi-Agent Variational Exploration | Mahajan et al | 2019 | 1910.07483 | candidate | core | agent-batch:marl-emergent-classical | 0 | Latent commitment for coordinated exploration |
| 39 | QPLEX: Duplex Dueling Multi-Agent Q-Learning | Wang et al | 2021 | 2008.01062 | candidate | core | agent-batch:marl-emergent-classical | 0 | Complete IGM factorization |
| 40 | RODE: Learning Roles to Decompose Multi-Agent Tasks | Wang et al | 2021 | 2010.01523 | candidate | core | agent-batch:marl-emergent-classical | 0 | Role-based decomposition and transfer |
| 41 | Commitments and Conventions: The Foundation of Coordination in Multi-Agent Systems | Jennings | 1993 | DOI:10.1017/S0269888900000205 | candidate | core | agent-batch:marl-emergent-classical | 0 | Commitments and conventions for coordination |
| 42 | Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory | Yuen et al | 2025 | 2508.08997 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 43 | Mirix: Multi-agent memory system for llm-based agents | Wang et al | 2025 | 2507.07957 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 44 | MAgIC: Investigation of Large Language Model Powered Multi-Agent in Cognition, Adaptability, Rationality and Collaboration | Xu et al | 2023 | 2311.08562 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 45 | AgentCoord: Coordination Strategies in Multi-Agent LLM Systems | Anderson et al | 2024 | 2404.11943 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 46 | Emergent Behaviors in Multi-Agent LLM Collaboration | Wang et al | 2024 | Artificial Intelligence Insights | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 47 | Llm harmony: Multi-agent communication for problem solving | Rasal | 2024 | 2401.01312 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 48 | MechAgents: Large language model multi-agent collaborations can solve mechanics problems, generate new data, and integrate knowledge | Ni et al | 2024 | Extreme Mechanics Letters | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 49 | Towards efficient llm grounding for embodied multi-agent collaboration | Zhang et al | 2024 | 2405.14314 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 50 | MegaAgent: A large-scale autonomous LLM-based multi-agent system without predefined SOPs | Wang et al | 2025 | Findings of the Association for Computational Linguistics: ACL 2025 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 51 | Parallelized Planning-Acting for Efficient LLM-based Multi-Agent Systems | Li et al | 2025 | 2503.03505 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 52 | Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems | Zhang et al | 2025 | 2505.00212 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 53 | HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face | Shen et al | 2023 | 2303.17580 | candidate | core | agent-batch:benchmarks-software-web | 0 | Early orchestration of external models as tools |
| 54 | TaskMatrix.AI: Completing Tasks by Connecting Foundation Models with Millions of APIs | Liang et al | 2023 | 2303.16434 | candidate | core | agent-batch:benchmarks-software-web | 0 | Large-scale API ecosystem vision for foundation-model agents |
| 55 | On the Utility of Learning about Humans for Human-AI Coordination | Carroll et al | 2019 | 1910.05789 | candidate | core | agent-batch:marl-emergent-classical | 0 | Overcooked human-aware agents |
| 56 | Enhancing diagnostic accuracy through multi-agent conversations: Using large language models to mitigate cognitive bias | Ke et al | 2024 | 2401.14589 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 57 | LLM-based Multi-Agent Systems: Techniques and Business Perspectives | Yang et al | 2024 | 2411.14033 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 58 | Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System | Chen et al | 2024 | 2410.08115 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 59 | Synthesizing post-training data for llms through multi-agent simulation | Tang et al | 2024 | 2410.14251 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 60 | Cooperative Multi-agent Bandits: Distributed Algorithms with Optimal Individual Regret and Constant Communication Costs | Yang et al | 2023 | 2308.04314 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 61 | DesignGPT: Multi-Agent Collaboration in Design | Ding et al | 2023 | 2311.11591 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 62 | Learning multi-agent communication from graph modeling perspective | Hu et al | 2024 | 2405.08550 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 63 | LongAgent: Scaling Language Models to 128k Context through Multi-Agent Collaboration | Zhao et al | 2024 | EMNLP | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 64 | Multi-agent design: Optimizing agents with better prompts and topologies | Zhou et al | 2025 | 2502.02533 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 65 | MAS-ProVe: Understanding the Process Verification of Multi-Agent Systems | Venkataramani et al | 2026 | 2602.03053 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |

## 2. Debate, Reasoning, and Aggregation

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 66 | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al | 2022 | 2210.03629 | seed | bridge | seed | 0 | bridge; Reasoning/action foundation |
| 67 | Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate | Liang et al | 2023 | 2305.19118 | seed | core | seed | 1 | core; Debate & reasoning |
| 68 | Improving Factuality and Reasoning through Multiagent Debate | Du et al | 2023 | 2305.14325 | seed | core | seed | 1 | core; Debate & reasoning |
| 69 | Mixture-of-Agents Enhances Large Language Model Capabilities | Wang et al | 2024 | 2406.04692 | seed | core | seed | 1 | core; Model aggregation/ensembles |
| 70 | More Agents Is All You Need | Li et al | 2024 | 2402.05120 | seed | core | seed | 1 | core; Scaling by agent sampling |
| 71 | MIRROR: Multi-agent Intra- and Inter-Reflection for Optimized Reasoning in Tool Learning | Guo et al | 2025 | 2505.20670 | seed | trend | seed | 0 | trend; Multi-agent reflection/tool use |
| 72 | Two Heads are Better Than One: Test-time Scaling of Multi-agent Collaborative Reasoning | Jin et al | 2025 | 2504.09772 | seed | trend | seed | 0 | trend; Test-time multi-agent scaling |
| 73 | MemMA: Coordinating Memory Cycle through Multi-Agent Reasoning | Lin et al | 2026 | 2603.18718 | seed | core | seed | 0 | core; Memory coordination |
| 74 | Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning | Tran et al | 2026 | 2604.02460 | seed | core | seed | 0 | core; Single vs. multi-agent reasoning |
| 75 | Should We Be Going MAD? A Look at Multi-Agent Debate Strategies for LLMs | Smit et al | 2023 | 2311.17371 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Compares debate design strategies |
| 76 | CoMM: Collaborative Multi-Agent, Multi-Reasoning-Path Prompting for Complex Problem Solving | Chen et al | 2024 | 2404.17729 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Combines multiple agent reasoning paths |
| 77 | MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems | Lei et al | 2024 | NeurIPS 2024 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Multi-agent condition mining for math |
| 78 | Examining Inter-Consistency of Large Language Models Collaboration: An In-depth Analysis via Debate | Xiong et al | 2023 | 2305.11595 | candidate | core | agent-batch:core-frameworks-reasoning | 1 | Studies consensus and imbalance in debate |
| 79 | ART: Automatic Multi-Step Reasoning and Tool-Use for Large Language Models | Paranjape et al | 2023 | 2303.09014 | candidate | core | agent-batch:benchmarks-software-web | 1 | Automatic retrieval and use of tool-augmented reasoning programs |
| 80 | Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models | Lu et al | 2023 | 2304.09842 | candidate | core | agent-batch:benchmarks-software-web | 0 | Plug-and-play tools/modules for compositional reasoning |
| 81 | ChatLLM Network: More Brains, More Intelligence | Hao et al | 2023 | 2304.12998 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Early networked LLM collaboration idea |
| 82 | LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion | Jiang et al | 2023 | 10.18653/v1/2023.acl-long.792 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Pairwise ranking plus generative fusion |
| 83 | ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs | Chen et al | 2023 | 2309.13007 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Round-table consensus among diverse models |
| 84 | Wider and Deeper LLM Networks Are Fairer LLM Evaluators | Zhang et al | 2023 | 2308.01862 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Multi-model evaluator network |
| 85 | Graph of Thoughts: Solving Elaborate Problems with Large Language Models | Besta et al | 2024 | 10.1609/aaai.v38i16.29720 | watchlist | core | agent-batch:core-frameworks-reasoning | 0 | Bridge item for graph-structured reasoning |
| 86 | Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? | Choi et al | 2025 | 2508.17536 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 87 | Single-agent vs. multi-agent LLM strategies for automated student reflection assessment | Li et al | 2025 | Pacific-Asia Conference on Knowledge Discovery and Data Mining | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |
| 88 | Corex: Pushing the Boundaries of Complex Reasoning through Multi-Model Collaboration | Sun et al | 2023 | 2310.00280 | candidate | core | agent-batch:core-frameworks-reasoning | 0 | Collaboration across multiple models |
| 89 | MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning | Karpas et al | 2022 | 2205.00445 | candidate | core | agent-batch:benchmarks-software-web | 0 | Pre-agent neuro-symbolic/tool-router architecture |
| 90 | ViperGPT: Visual Inference via Python Execution for Reasoning | Suris et al | 2023 | 2303.08128 | candidate | core | agent-batch:benchmarks-software-web | 0 | Uses generated Python to compose visual tools |
| 91 | Enabling Synergistic Knowledge Sharing and Reasoning in Large Language Models with Collaborative Multi-Agents | Das et al | 2023 | 2023 IEEE 9th International Conference on Collaboration and Internet Computing (CIC) | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 92 | Confidence Calibration and Rationalization for LLMs via Multi-Agent Deliberation | Yang et al | 2024 | 2404.09127 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 93 | DebateGPT: Fine-tuning Large Language Models with Multi-agent Debate Supervision | Subramaniam et al | 2024 | unknown | watchlist | core | local-snowball:1 | 1 | referenced by local seed corpus; identifier unresolved |
| 94 | Improving LLM Reasoning with Multi-Agent Tree-of-Thought Validator Agent | Haji et al | 2024 | 2409.11527 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 95 | Malt: Improving reasoning with multi-agent llm training | Motwani et al | 2024 | 2412.01928 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 96 | Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key? | Wang et al | 2024 | Annual Meeting of the Association for Computational Linguistics (ACL) | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 97 | Let models speak ciphers: Multiagent debate through embeddings | Pham et al | 2023 | 2310.06272 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 98 | Improving Multi-Agent Debate with Sparse Communication Topology | Li et al | 2024 | EMNLP Findings | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 99 | Learning to Break: Knowledge-Enhanced Reasoning in Multi-Agent Debate System | Wang et al | 2024 | arXiv preprint arXiv:2312.04854 | candidate | core | local-snowball:1 | 1 | referenced by local seed corpus |
| 100 | Materealize: a multi-agent deliberation system for end-to-end material design and synthesis | Kim et al | 2026 | 2601.15743 | candidate | trend | local-snowball:1 | 1 | referenced by local seed corpus |

## 3. Agent Foundations and Infrastructure

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 101 | MemGPT: Towards LLMs as Operating Systems | Packer et al | 2023 | 2310.08560 | seed | bridge | seed | 0 | bridge; Agent memory architecture |
| 102 | GPTSwarm: Language Agents as Optimizable Graphs | Zhuge et al | 2024 | 2402.16823 | seed | core | seed | 1 | core; Agent graph optimization |
| 103 | A-MEM: Agentic Memory for LLM Agents | Xu et al | 2025 | 2502.12110 | seed | bridge | seed | 1 | bridge; Agent memory |
| 104 | AutoAgent: A Fully-Automated and Zero-Code Framework for LLM Agents | Tang et al | 2025 | 2502.05957 | seed | trend | seed | 0 | trend; Agent framework automation |
| 105 | Adapting LLM Agents Through Communication | Wang et al | 2023 | 2310.01444 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Agent adaptation through message exchange |
| 106 | Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View | Zhang et al | 2023 | 2310.02124 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Social-psychology lens on collaboration patterns |
| 107 | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | Chen et al | 2024 | 2407.12784 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Red-teaming benchmark for memory and knowledge-base poisoning |
| 108 | Building Cooperative Embodied Agents Modularly with Large Language Models | Zhang et al | 2023 | 2307.02485 | candidate | bridge | agent-batch:core-frameworks-reasoning | 2 | Modular cooperative embodied agents |
| 109 | Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication | Yin et al | 2023 | 10.18653/v1/2023.emnlp-main.936 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Memory, report, relay, and debate modes |
| 110 | Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf | Xu et al | 2023 | 2309.04658 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Werewolf communication-game study |
| 111 | AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems | Zhang et al | 2023 | 2310.09233 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Collaborative learning among autonomous agents |
| 112 | Agents: An Open-source Framework for Autonomous Language Agents | Zhou et al | 2023 | 2309.07870 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Framework substrate used in early agent work |
| 113 | CompeteAI: Understanding the Competition Behaviors in Large Language Model-based Agents | Zhao et al | 2023 | 2310.17512 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Studies competition among LLM agents |
| 114 | Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game | Xu et al | 2023 | 2310.18940 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | RL-augmented language agents in Werewolf |
| 115 | OpenAgents: An Open Platform for Language Agents in the Wild | Xie et al | 2023 | 2310.10634 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Open platform for deployable language agents |
| 116 | ProAgent: Building Proactive Cooperative AI with Large Language Models | Zhang et al | 2023 | 2308.11339 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Proactive cooperative agent design |
| 117 | S3: Social-network Simulation System with Large Language Model-empowered Agents | Gao et al | 2023 | 2307.14984 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | LLM agents in social-network simulation |
| 118 | Controlling Large Language Model-based Agents for Large-Scale Decision-Making: An Actor-Critic Approach | Zhang et al | 2024 | 2311.13884 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Actor-critic control for agent populations |
| 119 | Are You in a Masquerade? Exploring the Behavior and Impact of Large Language Model Driven Social Bots in Online Social Networks | Li et al | 2023 | 2307.10337 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Social-bot behavior and impact |
| 120 | D-Bot: Database Diagnosis System using Large Language Models | Zhou et al | 2023 | 2312.01454 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Domain-specific diagnostic agent system |
| 121 | GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction | Yang et al | 2023 | 2305.18752 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Self-instruction for multimodal/tool-use capability |
| 122 | Gorilla: Large Language Model Connected with Massive APIs | Patil et al | 2023 | 2305.15334 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | API call generation; also anchors BFCL lineage |
| 123 | Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | Zhou et al | 2023 | 2310.04406 | watchlist | bridge | agent-batch:core-frameworks-reasoning | 1 | Bridge item for agent search |
| 124 | Large Language Models as Tool Makers | Cai et al | 2023 | 2305.17126 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Tool-making/tool-using division for cost-efficient problem solving |
| 125 | Quantifying the Impact of Large Language Models on Collective Opinion Dynamics | Li et al | 2023 | 2308.03313 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | LLM agents in collective opinion models |
| 126 | RestGPT: Connecting Large Language Models with Real-World RESTful APIs | Song et al | 2023 | 2306.06624 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Planning and API selection over RESTful services |
| 127 | AgentBank: Towards Generalized LLM Agents via Fine-Tuning on 50000+ Interaction Trajectories | Song et al | 2024 | 2410.07706 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Large interaction-trajectory corpus for generalized agents |
| 128 | AFlow: Automating Agentic Workflow Generation | Zhang et al | 2025 | OpenReview:z5uVAKwmjf | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Automates workflow design for agent systems |
| 129 | Automated Design of Agentic Systems | Hu et al | 2025 | OpenReview:t9U3LW7JVX | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Searches agentic systems automatically |
| 130 | GNNs as Predictors of Agentic Workflow Performances | Zhang et al | 2025 | 2503.11301 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Predicts workflow performance from graph structure |
| 131 | RecAgent: A Novel Simulation Paradigm for Recommender Systems | Wang et al | 2023 | 2306.02552 | candidate | bridge | agent-batch:core-frameworks-reasoning | 2 | User behavior simulation with agents |
| 132 | Toolformer: Language Models Can Teach Themselves to Use Tools | Schick et al | 2023 | 2302.04761 | candidate | bridge | agent-batch:benchmarks-software-web | 2 | Early self-supervised tool-use learning paper |
| 133 | Epidemic Modeling with Generative Agents | Williams et al | 2023 | 2307.04986 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Public-health simulation with generative agents |
| 134 | Generative Agent-Based Modeling: Unveiling Social System Dynamics through Coupling Mechanistic Models with Generative Artificial Intelligence | Ghaffarzadegan et al | 2023 | 2309.11456 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Couples generative agents with mechanistic ABM |
| 135 | Lyfe Agents: Generative Agents for Low-Cost Real-Time Social Interactions | Zhao et al | 2023 | 2310.02172 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Low-cost real-time generative agents |
| 136 | On Generative Agents in Recommendation | Zhang et al | 2023 | 2310.10108 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Generative agents for recommendation scenarios |
| 137 | Avalon's Game of Thoughts: Battle Against Deception through Recursive Contemplation | Wang et al | 2023 | 2310.01320 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Recursive contemplation in deception games |
| 138 | ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases | Tang et al | 2023 | 2306.05301 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Simulated tool-use cases for generalized tool learning |
| 139 | Deal or No Deal? End-to-End Learning of Negotiation Dialogues | Lewis et al | 2017 | EMNLP 2017 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Language drift in negotiation agents |
| 140 | Learning with Opponent-Learning Awareness | Foerster et al | 2018 | 1709.04326 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Agents shape other agents' updates |
| 141 | Countering Language Drift via Visual Grounding | Lee et al | 2019 | EMNLP-IJCNLP 2019 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Visual grounding to stabilize protocols |
| 142 | Social Simulacra: Creating Populated Prototypes for Social Computing Systems | Park et al | 2022 | 10.1145/3526113.3545616 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Precursor to generative-agent societies |
| 143 | MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents | Du et al | 2025 | 2512.20237 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |
| 144 | Memory-r1: Enhancing large language model agents to manage and utilize memories via reinforcement learning | Yan et al | 2025 | 2508.19828 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |
| 145 | SimpleMem: Efficient Lifelong Memory for LLM Agents | Liu et al | 2026 | 2601.02553 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |

## 4. Benchmarks and Evaluation

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 146 | Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG) | Lowe et al | 2017 | 1706.02275 | seed | anchor | seed | 1 | anchor; MARL actor-critic |
| 147 | The StarCraft Multi-Agent Challenge (SMAC) | Samvelyan et al | 2019 | 1902.04043 | seed | anchor | seed | 1 | anchor; MARL benchmark |
| 148 | AgentBench: Evaluating LLMs as Agents | Liu et al | 2023 | 2308.03688 | seed | bridge | seed | 1 | bridge; Agent evaluation |
| 149 | ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate | Chan et al | 2023 | 2308.07201 | seed | core | seed | 1 | core; Debate-based evaluation |
| 150 | GAIA: a benchmark for General AI Assistants | Mialon et al | 2023 | 2311.12983 | seed | bridge | seed | 0 | bridge; General assistant benchmark |
| 151 | SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents | Zhou et al | 2023 | 2310.11667 | seed | bridge | seed | 1 | bridge; Social interaction benchmark |
| 152 | AI Agents That Matter | Kapoor et al | 2024 | 2407.01502 | seed | bridge | seed | 2 | bridge; Agent evaluation methodology |
| 153 | AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents | Ma et al | 2024 | 2401.13178 | seed | bridge | seed | 1 | bridge; Agent evaluation |
| 154 | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Yao et al | 2024 | 2406.12045 | seed | bridge | seed | 1 | bridge; Tool/user interaction benchmark |
| 155 | AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs | Grotschla et al | 2025 | 2507.08616 | seed | core | seed | 0 | core; Topological reasoning benchmark |
| 156 | Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents | Sun et al | 2025 | 2502.20073 | seed | trend | seed | 0 | trend; Collaborative embodied benchmark |
| 157 | MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents | Zhu et al | 2025 | 2503.01935 | seed | core | seed | 1 | core; Multi-agent benchmark |
| 158 | LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in Large Language Models | Agashe et al | 2023 | 2310.03903 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Tests coordination ability directly |
| 159 | LLMArena: Assessing Capabilities of Large Language Models in Dynamic Multi-Agent Environments | Chen et al | 2024 | 10.18653/v1/2024.acl-long.705 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Multi-agent game environments and scoring |
| 160 | The Berkeley Function Calling Leaderboard: From Tool Use to Agentic Evaluation of Large Language Models | Yan et al | 2025 | openreview:2GmDdhBdDk | candidate | bridge | agent-batch:benchmarks-software-web | 0 | BFCL benchmark family for tool/function-calling models |
| 161 | BOLAA: Benchmarking and Orchestrating LLM-augmented Autonomous Agents | Liu et al | 2023 | 2308.05960 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Controller orchestrates labor agents by action type |
| 162 | ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities | Lu et al | 2024 | 2408.04682 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Stateful multi-turn tool execution benchmark |
| 163 | Benchmarking Multi-Agent Deep Reinforcement Learning Algorithms in Cooperative Tasks | Papoudakis et al | 2021 | 2006.07869 | candidate | bridge | agent-batch:marl-emergent-classical | 1 | EPyMARL and algorithm comparison |
| 164 | API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs | Li et al | 2023 | 2304.08244 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Tool-augmented LLM benchmark with API calls |
| 165 | From Text to Tactic: Evaluating LLMs Playing the Game of Avalon | Light et al | 2023 | 2310.05036 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Avalon social-deduction evaluation |
| 166 | AgentQuest: A Modular Benchmark Framework to Measure Progress and Improve LLM Agents | Zhou et al | 2024 | 2404.06411 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Modular benchmark framework worth tracking for eval infrastructure |
| 167 | DiscoveryBench: Towards Data-Driven Discovery with Large Language Models | Majumder et al | 2024 | 2407.01725 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Benchmark for hypothesis and discovery workflows over data |
| 168 | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code | Jain et al | 2024 | 2403.07974 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Continuously updated coding benchmark with repair and execution tasks |
| 169 | MIRAI: Evaluating LLM Agents for Event Forecasting | Ye et al | 2024 | 2407.01231 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Agentic event-forecasting benchmark with tools and GDELT data |
| 170 | Natural Language Does Not Emerge Naturally in Multi-Agent Dialog | Kottur et al | 2017 | 1706.08502 | candidate | bridge | agent-batch:marl-emergent-classical | 2 | Compositionality failure and pressure |
| 171 | AlphaRank: Multi-Agent Evaluation by Evolution | Omidshafiei et al | 2019 | 1903.01373 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Strategy ranking for many-agent games |
| 172 | Neural MMO: A Massively Multiagent Game Environment for Training and Evaluating Intelligent Agents | Suarez et al | 2019 | 1903.00784 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Persistent many-agent world |
| 173 | Scalable Evaluation of Multi-Agent Reinforcement Learning with Melting Pot | Leibo et al | 2021 | 2107.06857 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Generalization and social-interaction suite |
| 174 | SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning | Ellis et al | 2022 | 2212.07489 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Procedural generalization for SMAC |
| 175 | BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents | Wei et al | 2025 | 2504.12516 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Hard-to-find web information benchmark with simple automatic grading |
| 176 | ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs | Qin et al | 2023 | 2307.16789 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | ToolBench and ToolLLaMA benchmark/training line |
| 177 | AgentGym: Evolving Large Language Model-based Agents across Diverse Environments | Xi et al | 2024 | 2406.04151 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Unified environment suite for evaluating and training generalist agents |
| 178 | An LLM Agent for Automatic Geospatial Data Analysis | Chen et al | 2024 | 2410.18792 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | GeoAgent combines code, RAG, and MCTS for geospatial workflows |
| 179 | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering | Chan et al | 2024 | 2410.07095 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Kaggle-style machine-learning engineering benchmark |
| 180 | Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale | Bonatti et al | 2024 | 2409.08264 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Scalable Windows OS benchmark adapted from OSWorld ideas |
| 181 | Pommerman: A Multi-Agent Playground | Resnick et al | 2018 | 1809.07124 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Competitive/cooperative gridworld |
| 182 | SMARTS: Scalable Multi-Agent Reinforcement Learning Training School for Autonomous Driving | Zhou et al | 2020 | 2010.09776 | watchlist | bridge | agent-batch:marl-emergent-classical | 1 | Multi-agent traffic simulator |
| 183 | PettingZoo: Gym for Multi-Agent Reinforcement Learning | Terry et al | 2021 | 2009.14471 | candidate | bridge | agent-batch:marl-emergent-classical | 0 | Standard MARL environment API |
| 184 | Harnessing Language for Coordination: A Framework and Benchmark for LLM-Driven Multi-Agent Control | Anne et al | 2024 | 2412.11761 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |
| 185 | On the Importance of Task Complexity in Evaluating LLM-Based Multi-Agent Systems | Tang et al | 2025 | 2510.04311 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |
| 186 | CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | Ding et al | 2023 | 2310.11248 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Tests use of cross-file context across languages |
| 187 | Welfare Diplomacy: Benchmarking Language Model Cooperation | Mukobi et al | 2023 | 2310.08901 | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Diplomacy-style cooperation benchmark |
| 188 | On the Pitfalls of Measuring Emergent Communication | Lowe et al | 2019 | 1903.05168 | candidate | bridge | agent-batch:marl-emergent-classical | 2 | Causal and positive-signaling cautions |
| 189 | Mas-orchestra: Understanding and improving multi-agent reasoning through holistic orchestration and controlled benchmarks | Ke et al | 2026 | 2601.14652 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |
| 190 | ChatArena: Multi-Agent Language Game Environments for Large Language Models | Wu et al | 2023 | GitHub repository | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |

## 5. Software, Web, and Computer-Use Agents

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 191 | AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation | Huang et al | 2023 | 2312.13010 | seed | core | seed | 1 | core; Multi-agent code generation |
| 192 | ChatDev: Communicative Agents for Software Development | Qian et al | 2023 | 2307.07924 | seed | core | seed | 1 | core; Multi-agent software development |
| 193 | MetaGPT: Meta Programming for Multi-Agent Collaborative Framework | Hong et al | 2023 | 2308.00352 | seed | core | seed | 1 | core; Multi-agent software development |
| 194 | Mind2Web: Towards a Generalist Agent for the Web | Deng et al | 2023 | 2306.06070 | seed | bridge | seed | 2 | bridge; Web-agent dataset |
| 195 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Jimenez et al | 2023 | 2310.06770 | seed | bridge | seed | 2 | bridge; Software agent benchmark |
| 196 | WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al | 2023 | 2307.13854 | seed | bridge | seed | 2 | bridge; Web agent benchmark |
| 197 | Agentless: Demystifying LLM-based Software Engineering Agents | Xia et al | 2024 | 2407.01489 | seed | bridge | seed | 2 | bridge; Software-agent baseline |
| 198 | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | Rawles et al | 2024 | 2405.14573 | seed | bridge | seed | 1 | bridge; Mobile-device agent benchmark |
| 199 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | Xie et al | 2024 | 2404.07972 | seed | bridge | seed | 1 | bridge; Computer-use benchmark |
| 200 | OpenHands: An Open Platform for AI Software Developers as Generalist Agents | Wang et al | 2024 | 2407.16741 | seed | bridge | seed | 2 | bridge; Software agents/platforms |
| 201 | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | Yang et al | 2024 | 2405.15793 | seed | bridge | seed | 2 | bridge; Software agent interface |
| 202 | SWE-bench Verified | OpenAI et al | 2024 | benchmark subset | seed | bridge | seed | 0 | bridge; Software-agent benchmark |
| 203 | The BrowserGym Ecosystem for Web Agent Research | Chezelles et al | 2024 | 2412.05467 | seed | bridge | seed | 1 | bridge; Web-agent infrastructure |
| 204 | TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | Xu et al | 2024 | 2412.14161 | seed | bridge | seed | 1 | bridge; Workplace-agent benchmark |
| 205 | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al | 2024 | 2401.13649 | seed | bridge | seed | 2 | bridge; Multimodal web benchmark |
| 206 | WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | He et al | 2024 | 2401.13919 | seed | bridge | seed | 1 | bridge; Multimodal web agents |
| 207 | WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks? | Drouin et al | 2024 | 2403.07718 | seed | bridge | seed | 1 | bridge; Knowledge-work web agents |
| 208 | MASLab: A Unified and Comprehensive Codebase for LLM-based Multi-Agent Systems | Ye et al | 2025 | 2505.16988 | seed | trend | seed | 0 | trend; MAS benchmarking/codebase |
| 209 | Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving | Seed | 2025 | 2504.02605 | seed | bridge | seed | 1 | bridge; Multilingual SWE benchmark |
| 210 | SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution | Wei et al | 2025 | 2502.18449 | seed | bridge | seed | 0 | bridge; Software-agent RL |
| 211 | SWE-bench Goes Live! | Zhang et al | 2025 | 2505.23419 | seed | bridge | seed | 0 | bridge; Live software-agent evaluation |
| 212 | SWE-smith: Scaling Data for Software Engineering Agents | Yang et al | 2025 | 2504.21798 | seed | bridge | seed | 1 | bridge; Software-agent data generation |
| 213 | CooperBench: Why Coding Agents Cannot be Your Teammates Yet | Khatua et al | 2026 | 2601.13295 | seed | core | seed | 1 | core; Multi-agent coding benchmark |
| 214 | Effective Strategies for Asynchronous Software Engineering Agents | Geng et al | 2026 | 2603.21489 | seed | core | seed | 0 | core; Software agent coordination |
| 215 | SlopCodeBench: How Coding Agents Degrade Over Long-Horizon Tasks | Orlanski et al | 2026 | 2603.24755 | seed | bridge | seed | 0 | bridge; Long-horizon code quality |
| 216 | Self-organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization | Ishibashi & Nishimura | 2024 | 2404.02183 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Self-organized code-agent teams |
| 217 | Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration | Wang et al | 2024 | 2406.01014 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Explicit planning, decision, and reflection agents for mobile control |
| 218 | Self-Evolving Multi-Agent Networks for Software Development | Hu et al | 2025 | OpenReview:4R71pdPBZp | candidate | bridge | agent-batch:core-frameworks-reasoning | 0 | Evolves software-agent networks |
| 219 | GameGPT: Multi-agent Collaborative Framework for Game Development | Chen et al | 2023 | 2310.08067 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Multi-agent game development workflow |
| 220 | MapCoder: Multi-Agent Code Generation for Competitive Problem Solving | Islam et al | 2024 | 2405.11403 | candidate | bridge | agent-batch:core-frameworks-reasoning | 1 | Multi-agent competitive-programming code generation |
| 221 | ToolQA: A Dataset for LLM Question Answering with External Tools | Zhuang et al | 2023 | 2306.13304 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | QA benchmark designed to require external tools |
| 222 | Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents | Deng et al | 2024 | 2407.00993 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Mobile benchmark with API-assisted and multi-app tasks |
| 223 | SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution | Wei et al | 2025 | 2501.05040 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Open-source model training for GitHub issue resolution |
| 224 | AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents | Trivedi et al | 2024 | 2407.18901 | candidate | bridge | agent-batch:benchmarks-software-web | 2 | Simulated app ecosystem for coding agents that call APIs |
| 225 | AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks? | Yoran et al | 2024 | 2407.15711 | candidate | bridge | agent-batch:benchmarks-software-web | 2 | Realistic, time-consuming web tasks; strong gap signal for web agents |
| 226 | A3: Android Agent Arena for Mobile GUI Agents | Zhang et al | 2025 | 2501.01149 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Online Android GUI-agent evaluation platform |
| 227 | SWE-PolyBench: A Multi-Language Benchmark for Repository Level Evaluation of Coding Agents | Rashid et al | 2025 | 2504.08703 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Multi-language execution benchmark for coding agents |
| 228 | Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces | Phan et al | 2026 | 2601.11868 | watchlist | bridge | agent-batch:benchmarks-software-web | 1 | Recent hard CLI benchmark; promising but very new |
| 229 | AutoDroid: LLM-powered Task Automation in Android | Wen et al | 2023 | 2308.15272 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Android task automation with app-specific memory injection |
| 230 | Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs | You et al | 2024 | 2404.05719 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Mobile UI grounding and reasoning benchmark/model |
| 231 | MMInA: Benchmarking Multihop Multimodal Internet Agents | Zhang et al | 2024 | 2404.09992 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Multihop web tasks across evolving multimodal websites |
| 232 | OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web | Kapoor et al | 2024 | 2402.17553 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Multimodal executable-script benchmark for desktop and web tasks |
| 233 | SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? | Yang et al | 2024 | 2410.03859 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Extends SWE-bench to visual JavaScript/UI issues |
| 234 | WebCanvas: Benchmarking Web Agents in Online Environments | Pan et al | 2024 | 2406.12373 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Online evaluation framework and Mind2Web-Live dataset |
| 235 | Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents | Deng et al | 2025 | 2505.11891 | watchlist | bridge | agent-batch:benchmarks-software-web | 0 | Recent follow-up to Mobile-Bench; needs adoption check |
| 236 | Evaluating Large Language Models Trained on Code | Chen et al | 2021 | 2107.03374 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | HumanEval origin paper; still a baseline for coding agents |
| 237 | WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents | Yao et al | 2022 | 2207.01206 | candidate | bridge | agent-batch:benchmarks-software-web | 2 | E-commerce web environment preceding modern web-agent benchmarks |
| 238 | Skeleton-of-Thought: Large Language Models Can Do Parallel Decoding | Ning et al | 2024 | OpenReview:mqVgBbNCm9 | watchlist | bridge | agent-batch:core-frameworks-reasoning | 0 | Adjacent parallel decomposition pattern |
| 239 | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | Liu et al | 2023 | 2306.03091 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Early repository-level context benchmark for coding systems |
| 240 | BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions | Zhuo et al | 2024 | 2406.15877 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Practical code-generation tasks requiring library/tool calls |
| 241 | GUI Odyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices | Lu et al | 2024 | 2406.08451 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Cross-app mobile navigation dataset |
| 242 | HammerBench: Fine-Grained Function-Calling Evaluation in Real Mobile Device Scenarios | Lin et al | 2024 | 2412.16516 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Function-calling benchmark in realistic mobile dialogues |
| 243 | OS-Copilot: Towards Generalist Computer Agents with Self-Improvement | Wu et al | 2024 | 2402.07456 | candidate | bridge | agent-batch:benchmarks-software-web | 2 | FRIDAY generalist computer agent with self-improvement |
| 244 | SWE-bench-java: A GitHub Issue Resolving Benchmark for Java | Zan et al | 2024 | 2408.14354 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Java issue-resolution variant with execution harness |
| 245 | WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks | Boisvert et al | 2024 | 2407.05291 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Compositional extension of WorkArena |

## 6. Scientific and Domain Agents

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 246 | Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents | Li et al | 2024 | 2405.02957 | seed | trend | seed | 1 | trend; Medical agent society |
| 247 | The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | Lu et al | 2024 | 2408.06292 | seed | trend | seed | 2 | trend; Autonomous research agents |
| 248 | Agent Laboratory: Using LLM Agents as Research Assistants | Schmidgall et al | 2025 | 2501.04227 | seed | trend | seed | 1 | trend; Research agents |
| 249 | AgentRxiv: Towards Collaborative Autonomous Research | Schmidgall et al | 2025 | 2503.18102 | seed | trend | seed | 1 | trend; Collaborative research agents |
| 250 | Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents | Kon et al | 2025 | 2502.16069 | seed | trend | seed | 1 | trend; Scientific experimentation agents |
| 251 | InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification | Team et al | 2025 | 2505.16938 | seed | trend | seed | 0 | trend; Closed-loop research agents |
| 252 | MLGym: A New Framework and Benchmark for Advancing AI Research Agents | Nathani et al | 2025 | 2502.14499 | seed | bridge | seed | 1 | bridge; ML research-agent benchmark |
| 253 | PaperBench: Evaluating AI's Ability to Replicate AI Research | Starace et al | 2025 | 2504.01848 | seed | bridge | seed | 0 | bridge; Research replication benchmark |
| 254 | Towards a Science of Scaling Agent Systems | Kim et al | 2025 | 2512.08296 | seed | trend | seed | 1 | trend; Scaling principles |
| 255 | Towards an AI Co-Scientist | Gottweis et al | 2025 | 2502.18864 | seed | core | seed | 1 | core; Scientific discovery agents |
| 256 | AI Scientists Produce Results Without Reasoning Scientifically | Rios-Garcia et al | 2026 | 2604.18805 | seed | trend | seed | 0 | trend; Scientific reasoning |
| 257 | TradingAgents: Multi-Agents LLM Financial Trading Framework | Xiao et al | 2025 | OpenReview:4QPrXwMQt1 | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Financial trading agent team |
| 258 | A Multi-agent Large Language Model Framework to Automatically Assess Performance of a Clinical AI Triage Tool | Flanders et al | 2025 | 2510.26498 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | LLM ensemble evaluates clinical AI triage-tool performance |
| 259 | Enhancing Diagnostic Capability with Multi-Agents Conversational Large Language Models | Chen et al | 2025 | DOI:10.1038/s41746-025-01550-0 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | NPJ Digital Medicine rare-disease diagnosis MAC framework |
| 260 | MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM | Li et al | 2025 | 2509.20067 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Self-learning clinical diagnosis MAS with human collaboration variant |
| 261 | Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation | Elboardy et al | 2025 | 2509.17353 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Radiology report generation and evaluation via specialized agents |
| 262 | MedCoAct: Confidence-Aware Multi-Agent Collaboration for Complete Clinical Decision | Zheng et al | 2025 | 2510.10461 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Doctor and pharmacist agents for integrated diagnosis and medication workflows |
| 263 | PiFlow: Principle-aware Scientific Discovery with Multi-Agent Collaboration | Pu et al | 2025 | 2505.15047 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Information-theoretic MAS for uncertainty-reducing discovery |
| 264 | ClinicalAgent: Clinical Trial Multi-Agent System with Large Language Model-based Reasoning | Yue et al | 2024 | 2404.14777 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Multi-agent clinical-trial outcome reasoning |
| 265 | Development of a Large Language Model-based Multi-Agent Clinical Decision Support System for KTAS-Based Triage and Treatment Planning in Emergency Departments | Han & Choi | 2024 | 2408.07531 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Emergency-department role agents for triage and treatment planning |
| 266 | KG4Diagnosis: A Hierarchical Multi-Agent LLM Framework with Knowledge Graph Enhancement for Medical Diagnosis | Zuo et al | 2024 | 2412.16833 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Hierarchical GP and specialist-agent diagnosis framework |
| 267 | TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance | Li et al | 2023 | 2309.03736 | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Layered memory and role characters for trading |
| 268 | MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation | Huang et al | 2023 | 2310.03302 | candidate | trend | agent-batch:benchmarks-software-web | 2 | Early end-to-end ML experimentation benchmark for agents |
| 269 | SciAgents: Automating Scientific Discovery through Multi-Agent Intelligent Graph Reasoning | Ghafarollahi & Buehler | 2024 | 2409.05556 | candidate | trend | agent-batch:science-safety-surveys-trends | 1 | Explicit multi-agent graph-reasoning system for materials discovery |
| 270 | A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making | Wu et al | 2025 | 2509.14998 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | KAMAC dynamically recruits specialist medical agents |
| 271 | ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | Chen et al | 2024 | 2410.05080 | candidate | trend | agent-batch:benchmarks-software-web | 1 | Peer-paper-derived scientific coding tasks for agents |
| 272 | MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making | Kim et al | 2024 | 2404.15155 | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Adaptive medical-agent collaboration |
| 273 | Data Interpreter: An LLM Agent For Data Science | Hong et al | 2024 | 2402.18679 | candidate | trend | agent-batch:benchmarks-software-web | 2 | Agentic workflow system for data-science problem solving |
| 274 | ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models | Baek et al | 2024 | 2404.07738 | candidate | trend | agent-batch:science-safety-surveys-trends | 2 | Literature-grounded idea generator with reviewing agents |
| 275 | Large Language Models to Accelerate Organic Chemistry Synthesis | Zhang et al | 2025 | DOI:10.1038/s42256-025-01066-y | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Organic synthesis acceleration paper adjacent to autonomous labs |
| 276 | MM-Agent: LLM as Agents for Real-world Mathematical Modeling Problem | Liu et al | 2025 | 2505.14148 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Agent framework and benchmark for mathematical modeling |
| 277 | MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning | Tang et al | 2023 | 2311.10537 | candidate | trend | agent-batch:core-frameworks-reasoning | 1 | Multi-disciplinary medical agent discussion |
| 278 | Verification-first Autonomous Catalysis: Large Language Models as Infrastructure for Mechanism, Computation, and Experiment | Liu et al | 2026 | DOI:10.1038/s44387-026-00111-4 | watchlist | trend | agent-batch:science-safety-surveys-trends | 0 | Very recent verification-first perspective for autonomous catalysis |
| 279 | A Sober Look at LLMs for Material Discovery: Are They Actually Good for Bayesian Optimization Over Molecules? | Kristiadi et al | 2024 | 2402.05015 | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Useful cautionary material-discovery evaluation |
| 280 | An Automatic End-to-End Chemical Synthesis Development Platform Powered by Large Language Models | Ruan et al | 2024 | DOI:10.1038/s41467-024-54457-x | candidate | trend | agent-batch:science-safety-surveys-trends | 0 | Automated synthesis development with LLM orchestration |

## 7. Safety, Security, and Reliability

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 281 | Teams of LLM Agents can Exploit Zero-Day Vulnerabilities | Zhu et al | 2024 | 2406.01637 | seed | trend | seed | 0 | trend; Multi-agent cybersecurity |
| 282 | G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems | Wang et al | 2025 | 2502.11127 | seed | core | seed | 0 | core; Multi-agent safety/security |
| 283 | OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety | Vijayvargiya et al | 2025 | 2507.06134 | seed | bridge | seed | 0 | bridge; Agent safety evaluation |
| 284 | SafeArena: Evaluating the Safety of Autonomous Web Agents | Tur et al | 2025 | 2503.04957 | seed | bridge | seed | 1 | bridge; Web-agent safety benchmark |
| 285 | LLMs Corrupt Your Documents When You Delegate | Laban et al | 2026 | 2604.15597 | seed | core | seed | 0 | core; Delegation reliability |
| 286 | A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks | Hossain et al | 2025 | 2509.14285 | watchlist | bridge | agent-batch:science-safety-surveys-trends | 0 | Multi-agent defensive pipeline for prompt injection |
| 287 | AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents | Luo et al | 2025 | 2506.00641 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Memory-augmented LLM judge for agent safety and security traces |
| 288 | Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models | Yi et al | 2023 | 2312.14197 | candidate | bridge | agent-batch:science-safety-surveys-trends | 1 | BIPIA precursor for indirect prompt injection defenses |
| 289 | Agent-SafetyBench: Evaluating the Safety of LLM Agents | Zhang et al | 2024 | 2412.14470 | candidate | bridge | agent-batch:science-safety-surveys-trends | 1 | Large benchmark across interaction environments and risk types |
| 290 | AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents | Andriushchenko et al | 2024 | 2410.09024 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Malicious multi-step agent tasks; important red-team benchmark |
| 291 | InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | Zhan et al | 2024 | 2403.02691 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Directly targets indirect prompt injection in tool-integrated agents |
| 292 | R-Judge: Benchmarking Safety Risk Awareness for LLM Agents | Yuan et al | 2024 | 2401.10019 | candidate | bridge | agent-batch:science-safety-surveys-trends | 1 | Safety-risk awareness benchmark over agent interaction records |
| 293 | CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models | Bhatt et al | 2024 | 2404.13161 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Cyber capability evaluation bridge for agent-risk assessment |
| 294 | Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety | Bonagiri et al | 2025 | 2510.16492 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | ToolEmu-based safety mechanism for high-stakes agent uncertainty |
| 295 | Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution | Alizadeh et al | 2025 | 2506.01055 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Data-exfiltration analysis built around AgentDojo-style tasks |
| 296 | Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Greshake et al | 2023 | 2302.12173 | candidate | bridge | agent-batch:science-safety-surveys-trends | 1 | Foundational indirect prompt-injection attack taxonomy |
| 297 | AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | Debenedetti et al | 2024 | 2406.13352 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | Dynamic tool-agent environment with attack and defense cases |
| 298 | AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification | Zhang et al | 2026 | 2602.22724 | watchlist | bridge | agent-batch:science-safety-surveys-trends | 0 | Recent causal mitigation for multi-turn indirect prompt injection |
| 299 | OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents | Li | 2026 | 2603.11853 | watchlist | bridge | agent-batch:science-safety-surveys-trends | 0 | Runtime security layer proposal for tool-augmented agents |
| 300 | Alignment Faking in Large Language Models | Greenblatt et al | 2024 | 2412.14093 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Empirical alignment-faking demonstration relevant to agent oversight |
| 301 | BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents | Wang et al | 2024 | 2406.03007 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Backdoor threat model for fine-tuned tool-using agents |
| 302 | Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training | Hubinger et al | 2024 | 2401.05566 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Deception and backdoor persistence anchor for autonomous agents |
| 303 | The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions | Wallace et al | 2024 | 2404.13208 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Important instruction-priority defense for tool and browsing contexts |
| 304 | The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents | Jia et al | 2024 | 2412.16682 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Test-time task-alignment defense evaluated on AgentDojo |
| 305 | ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages | Ye et al | 2024 | 2402.10753 | candidate | bridge | agent-batch:benchmarks-software-web | 0 | Safety cases across input, execution, and output stages of tool use |
| 306 | Model Evaluation for Extreme Risks | Shevlane et al | 2023 | 2305.15324 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Dangerous-capability and alignment-evaluation governance anchor |
| 307 | Agent Safety Alignment via Reinforcement Learning | Sha et al | 2025 | 2507.08270 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | RL alignment framework for user and tool threat channels |
| 308 | PromptArmor: Simple yet Effective Prompt Injection Defenses | Shi et al | 2025 | 2507.15219 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | AgentDojo defense baseline for injected-prompt removal |
| 309 | Identifying the Risks of LM Agents with an LM-Emulated Sandbox | Ruan et al | 2023 | 2309.15817 | candidate | bridge | agent-batch:benchmarks-software-web | 1 | ToolEmu sandbox for scalable risk discovery in high-stakes tool use |
| 310 | Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks | Schmotz et al | 2026 | 2602.20156 | watchlist | bridge | agent-batch:science-safety-surveys-trends | 0 | Agent-skill supply-chain injection benchmark |
| 311 | AI Control: Improving Safety Despite Intentional Subversion | Greenblatt et al | 2023 | 2312.06942 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Control protocols with untrusted model monitoring and editing |
| 312 | Frontier AI Regulation: Managing Emerging Risks to Public Safety | Anderljung et al | 2023 | 2307.03718 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Governance anchor for pre-deployment risk assessment and scrutiny |
| 313 | Dynamic Safety Cases for Frontier AI | Carlan et al | 2024 | 2412.17618 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Continuously updated safety-case approach, including cyber-capability template |
| 314 | Safety Cases for Frontier AI | Buhl et al | 2024 | 2410.21572 | candidate | bridge | agent-batch:science-safety-surveys-trends | 0 | Structured assurance-case frame for frontier agent deployment |
| 315 | Psysafe: A comprehensive framework for psychological-based attack, defense, and evaluation of multi-agent system safety | Zhang et al | 2024 | 2401.11880 | candidate | bridge | local-snowball:1 | 1 | referenced by local seed corpus |

## 8. MARL, Emergent Communication, and Social Behavior

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 316 | Learning Multiagent Communication with Backpropagation (CommNet) | Sukhbaatar et al | 2016 | 1605.07736 | seed | anchor | seed | 0 | anchor; Learned communication |
| 317 | Learning to Communicate with Deep Multi-Agent RL (RIAL/DIAL) | Foerster et al | 2016 | 1605.06676 | seed | anchor | seed | 0 | anchor; Emergent communication |
| 318 | Multi-Agent Cooperation and the Emergence of (Natural) Language | Lazaridou et al | 2017 | 1612.07182 | seed | anchor | seed | 1 | anchor; Emergent language |
| 319 | Multi-Agent Reinforcement Learning in Sequential Social Dilemmas | Leibo et al | 2017 | 1702.03037 | seed | anchor | seed | 2 | anchor; Social dilemmas |
| 320 | Counterfactual Multi-Agent Policy Gradients (COMA) | Foerster et al | 2018 | 1705.08926 | seed | anchor | seed | 1 | anchor; MARL credit assignment |
| 321 | Emergence of Grounded Compositional Language in Multi-Agent Populations | Mordatch et al | 2018 | 1703.04908 | seed | anchor | seed | 2 | anchor; Emergent language |
| 322 | QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning | Rashid et al | 2018 | 1803.11485 | seed | anchor | seed | 1 | anchor; MARL value factorization |
| 323 | Value-Decomposition Networks for Cooperative Multi-Agent Learning (VDN) | Sunehag et al | 2018 | 1706.05296 | seed | anchor | seed | 0 | anchor; MARL value decomposition |
| 324 | Dota 2 with Large Scale Deep Reinforcement Learning (OpenAI Five) | OpenAI et al | 2019 | 1912.06680 | seed | anchor | seed | 0 | anchor; Population self-play |
| 325 | Grandmaster Level in StarCraft II using Multi-Agent Reinforcement Learning (AlphaStar) | Vinyals et al | 2019 | DOI:10.1038/s41586-019-1724-z | seed | anchor | seed | 1 | anchor; League-based MARL |
| 326 | TarMAC: Targeted Multi-Agent Communication | Das et al | 2019 | 1810.11187 | seed | anchor | seed | 1 | anchor; Targeted communication |
| 327 | Emergent Tool Use from Multi-Agent Autocurricula | Baker et al | 2020 | 1909.07528 | seed | anchor | seed | 1 | anchor; Emergent tool use |
| 328 | The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO) | Yu et al | 2022 | 2103.01955 | seed | anchor | seed | 0 | anchor; MARL policy optimization |
| 329 | MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | Park et al | 2025 | 2502.18439 | seed | trend | seed | 1 | trend; Collaborative LLM training |
| 330 | Biases for Emergent Communication in Multi-agent Reinforcement Learning | Eccles et al | 2019 | NeurIPS 2019 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Inductive biases for protocols |
| 331 | Deep Decentralized Multi-task Multi-Agent Reinforcement Learning under Partial Observability | Omidshafiei et al | 2017 | 1703.06182 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Decentralized recurrent policies across tasks |
| 332 | Multiagent Bidirectionally-Coordinated Nets for Learning to Play StarCraft Combat Games | Peng et al | 2017 | 1703.10069 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | BiCNet StarCraft coordination |
| 333 | Stabilising Experience Replay for Deep Multi-Agent Reinforcement Learning | Foerster et al | 2017 | 1702.08887 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Fingerprints and importance sampling for replay |
| 334 | Emergent Complexity via Multi-Agent Competition | Bansal et al | 2018 | 1710.03748 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Self-play curriculum in physics games |
| 335 | Is Independent Learning All You Need in the StarCraft Multi-Agent Challenge? | de Witt et al | 2020 | 2011.09533 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Reassesses IQL strength |
| 336 | Parameter Sharing is Surprisingly Useful for Multi-Agent Deep Reinforcement Learning | Terry et al | 2020 | 2005.13625 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Baseline lesson for scalable teams |
| 337 | Multi-agent Reinforcement Learning: Independent versus Cooperative Agents | Tan | 1993 | ICML 1993 | candidate | anchor | agent-batch:marl-emergent-classical | 2 | Early independent/cooperative comparison |
| 338 | Mean Field Multi-Agent Reinforcement Learning | Yang et al | 2018 | 1802.05438 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Mean-field approximation for large populations |
| 339 | Actor-Attention-Critic for Multi-Agent Reinforcement Learning | Iqbal & Sha | 2019 | 1810.02912 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Centralized attention over agents |
| 340 | Bayesian Action Decoder for Deep Multi-Agent Reinforcement Learning | Foerster et al | 2019 | 1811.01458 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Public belief from actions in Hanabi |
| 341 | QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning | Son et al | 2019 | 1905.05408 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | More general IGM factorization |
| 342 | Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning | Jaques et al | 2019 | 1810.08647 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Causal influence reward |
| 343 | Deep Multi-Agent Reinforcement Learning for Decentralized Continuous Cooperative Control | de Witt et al | 2020 | 2003.06709 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Multi-Agent MuJoCo, COMIX, and FACMAC |
| 344 | Learning Implicit Credit Assignment for Multi-Agent Actor-Critic | Liu et al | 2020 | 2007.02529 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Actor-critic credit assignment without explicit counters |
| 345 | Weighted QMIX: Expanding Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning | Rashid et al | 2020 | 2006.10800 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Analyzes and relaxes QMIX projection |
| 346 | DOP: Off-Policy Multi-Agent Decomposed Policy Gradients | Wang et al | 2021 | 2007.12322 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Decomposed critics for policy gradients |
| 347 | Multi-Agent Reinforcement Learning is a Sequence Modeling Problem | Wen et al | 2022 | 2205.14953 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Transformer formulation of joint action |
| 348 | Markov Games as a Framework for Multi-Agent Reinforcement Learning | Littman | 1994 | ICML 1994 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Stochastic-game bridge for MARL |
| 349 | An Algorithm for Distributed Reinforcement Learning in Cooperative Multi-Agent Systems | Lauer & Riedmiller | 2000 | ICML 2000 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Distributed team-learning foundation |
| 350 | Hysteretic Q-Learning: An Algorithm for Decentralized Reinforcement Learning in Cooperative Multi-Agent Teams | Matignon et al | 2007 | IROS 2007 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Early nonstationarity-tolerant Q-learning |
| 351 | Emergent Communication through Negotiation | Cao et al | 2018 | 1804.03980 | candidate | anchor | agent-batch:marl-emergent-classical | 2 | Mixed-motive negotiation protocols |
| 352 | On the Interaction Between Supervision and Self-Play in Emergent Communication | Lowe et al | 2020 | ICLR 2020 | candidate | anchor | agent-batch:marl-emergent-classical | 2 | Human-language alignment under self-play |
| 353 | Heterogeneous Group-Based Reinforcement Learning for LLM-based Multi-Agent Systems | Chen et al | 2025 | 2506.02718 | candidate | anchor | local-snowball:1 | 1 | referenced by local seed corpus |
| 354 | How Agents See Things: On Visual Representations in an Emergent Language Game | Bouchacourt & Baroni | 2018 | 1808.10696 | candidate | anchor | agent-batch:marl-emergent-classical | 2 | Representation alignment without human semantics |
| 355 | Emergence of Communication in an Interactive World with Consistent Speakers | Bogin et al | 2018 | 1809.00549 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Consistent-speaker interaction setting |
| 356 | Ease-of-Teaching and Language Structure from Emergent Communication | Li & Bowling | 2019 | 1906.02403 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Teachable protocols and language structure |
| 357 | Llm-based multi-agent reinforcement learning: Current and future directions | Sun et al | 2024 | 2405.11106 | candidate | anchor | local-snowball:1 | 1 | referenced by local seed corpus |
| 358 | Heterogeneous Multi-Agent Reinforcement Learning for Zero-Shot Scalable Collaboration | Guo et al | 2024 | 2404.03869 | candidate | anchor | local-snowball:1 | 1 | referenced by local seed corpus |
| 359 | Deep Reinforcement Learning from Self-Play in Imperfect-Information Games | Heinrich & Silver | 2016 | 1603.01121 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | NFSP equilibrium learning |
| 360 | Opponent Modeling in Deep Reinforcement Learning | He et al | 2016 | 1609.05559 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Deep opponent-aware policy learning |
| 361 | Population Based Training of Neural Networks | Jaderberg et al | 2017 | 1711.09846 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Hyperparameter and policy population method |
| 362 | Inequity Aversion Improves Cooperation in Intertemporal Social Dilemmas | Hughes et al | 2018 | 1803.08884 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Social preferences in sequential dilemmas |
| 363 | Human-level Performance in First-person Multiplayer Games with Population-based Deep Reinforcement Learning | Jaderberg et al | 2019 | 1807.01281 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Capture-the-Flag population league |
| 364 | OpenSpiel: A Framework for Reinforcement Learning in Games | Lanctot et al | 2019 | 1908.09453 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Game-theoretic RL testbed |
| 365 | Compositionality and Generalization in Emergent Languages | Chaabouni et al | 2020 | 2004.09124 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Systematicity diagnostics for protocols |
| 366 | Open-Ended Learning Leads to Generally Capable Agents | Open Ended Learning Team et al | 2021 | 2107.12808 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | XLand multi-agent task universe |
| 367 | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning | Liu et al | 2025 | 2506.24119 | candidate | anchor | local-snowball:1 | 1 | referenced by local seed corpus |
| 368 | Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm | Silver et al | 2018 | 1712.01815 | watchlist | anchor | agent-batch:marl-emergent-classical | 0 | AlphaZero; adjacent but central to self-play |
| 369 | Learning to schedule communication in multi-agent reinforcement learning | Kim et al | 2019 | Proceedings of ICLR | candidate | anchor | local-snowball:2 | 2 | referenced by local seed corpus |
| 370 | Multi-agent cooperation through learning-aware policy gradients | Meulemans et al | 2024 | 2410.18636 | candidate | anchor | local-snowball:1 | 1 | referenced by local seed corpus |

## 9. Surveys and Taxonomies

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 371 | Emergent Multi-Agent Communication in the Deep Learning Era | Lazaridou et al | 2020 | 2006.02419 | seed | survey | seed | 2 | survey; Emergent communication survey |
| 372 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Guo et al | 2024 | 2402.01680 | seed | survey | seed | 1 | survey; LLM multi-agent survey |
| 373 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Tran et al | 2025 | 2501.06322 | candidate | survey | agent-batch:core-frameworks-reasoning | 1 | Recent survey focused on collaboration mechanisms |
| 374 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Yan et al | 2025 | 2502.14321 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Communication-centric taxonomy including security and scalability issues |
| 375 | Creativity in LLM-based Multi-Agent Systems: A Survey | Lin et al | 2025 | 2505.21116 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Creativity and persona-design taxonomy for MAS workflows |
| 376 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | Aratchige & Ilmini | 2025 | 2504.01963 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Technology-oriented survey over architecture, memory, planning, and frameworks |
| 377 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Chen et al | 2024 | 2412.17481 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Broad application-focused LLM-MAS survey already missing from seeds |
| 378 | LLM Multi-Agent Systems: Challenges and Open Problems | Han et al | 2024 | 2402.03578 | candidate | survey | agent-batch:science-safety-surveys-trends | 1 | Short challenges paper on task allocation, context, memory, and blockchain |
| 379 | LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead | He et al | 2024 | 2404.04834 | candidate | survey | agent-batch:science-safety-surveys-trends | 1 | SE-oriented MAS review useful for trustworthy agent-system design |
| 380 | A Survey on Large Language Model based Autonomous Agents | Wang et al | 2023 | 2308.11432 | candidate | survey | agent-batch:science-safety-surveys-trends | 2 | General autonomous-agent survey with natural-science and evaluation sections |
| 381 | Large Language Models for Scientific Idea Generation: A Creativity-Centered Survey | Shahhosseini et al | 2025 | 2511.07448 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Survey includes multi-agent collaboration as an ideation method family |
| 382 | Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents | Ren et al | 2025 | 2503.24047 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Focused survey for scientific-agent architecture, benchmarks, and ethics |
| 383 | The Rise and Potential of Large Language Model Based Agents: A Survey | Xi et al | 2023 | 2309.07864 | candidate | survey | agent-batch:science-safety-surveys-trends | 1 | Agent and agent-society survey with multi-agent scenarios |
| 384 | A Survey and Critique of Multiagent Deep Reinforcement Learning | Hernandez-Leal et al | 2019 | 1810.05587 | candidate | survey | agent-batch:marl-emergent-classical | 1 | Deep MARL critique and taxonomy |
| 385 | Rethinking Chemical Research in the Age of Large Language Models | MacKnight et al | 2025 | DOI:10.1038/s43588-025-00811-y | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Domain roadmap for chemistry LLM agents and workflows |
| 386 | Scientific Hypothesis Generation and Validation: Methods, Datasets, and Future Directions | Kulkarni et al | 2025 | 2505.04651 | candidate | survey | agent-batch:science-safety-surveys-trends | 0 | Survey of LLM-driven hypothesis generation and validation |
| 387 | A Comprehensive Survey of Multi-Agent Reinforcement Learning | Busoniu et al | 2008 | DOI:10.1109/TSMCC.2007.913919 | candidate | survey | agent-batch:marl-emergent-classical | 1 | Classic MARL survey |
| 388 | Cooperative Multi-Agent Learning: The State of the Art | Panait & Luke | 2005 | DOI:10.1007/s10458-005-2631-2 | candidate | survey | agent-batch:marl-emergent-classical | 1 | Pre-deep cooperative learning map |
| 389 | Towards reasoning in large language models via multi-agent peer review collaboration | Xu et al | 2023 | 2311.08152 | candidate | survey | local-snowball:1 | 1 | referenced by local seed corpus |
| 390 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Li et al | 2024 | Vicinagearth | candidate | survey | local-snowball:1 | 1 | referenced by local seed corpus |

## 10. Classical MAS and Game-Theoretic Foundations

| # | Paper | Authors | Year | ID | Status | Role | Provenance | Local refs | Notes |
|---:|---|---|---:|---|---|---|---|---:|---|
| 391 | An Introduction to MultiAgent Systems | Wooldridge | 2002 | Wiley | candidate | anchor | manual-gap | 1 | classical MAS textbook |
| 392 | Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations | Shoham & Leyton-Brown | 2009 | Cambridge 2009 | candidate | anchor | manual-gap | 1 | game-theoretic MAS textbook |
| 393 | Alympics: Language Agents Meet Game Theory | Mao et al | 2023 | 2311.03220 | candidate | anchor | agent-batch:core-frameworks-reasoning | 1 | Game-theoretic evaluation for agents |
| 394 | KQML as an Agent Communication Language | Finin et al | 1994 | DOI:10.1145/191246.191322 | candidate | anchor | agent-batch:marl-emergent-classical | 1 | Performatives for inter-agent messages |
| 395 | Intelligent Agents: Theory and Practice | Wooldridge & Jennings | 1995 | KER 10(2) | candidate | anchor | manual-gap | 1 | classical MAS foundation |
| 396 | The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver | Smith | 1980 | DOI:10.1109/TC.1980.1675516 | candidate | anchor | agent-batch:marl-emergent-classical | 0 | Task allocation protocol |
| 397 | Teamwork | Cohen & Levesque | 1991 | Nous 25(4) | candidate | anchor | manual-gap | 0 | joint intention foundation |
| 398 | Market-Oriented Programming: Some Early Lessons | Wellman | 1993 | Market-based Control | candidate | anchor | manual-gap | 0 | market-based coordination |
| 399 | SharedPlans: A Model of Collaborative Plans and Intentions | Grosz & Kraus | 1996 | AIJ 86(2) | candidate | anchor | manual-gap | 0 | collaborative planning foundation |
| 400 | FIPA ACL Message Structure Specification | FIPA | 2002 | FIPA SC00061 | candidate | anchor | manual-gap | 0 | agent communication standard |

## Next Expansion Rounds

- [x] Trial seed expansion: promote a trend-biased 100-paper seed set in `docs/seeds.md`.
- [x] Agent batch expansion across core frameworks/reasoning, benchmarks/software/web, and science/safety/surveys.
- [x] Local BibTeX snowball merge over checked-in paper sources.
- [ ] Fill remaining missing identifiers and venue metadata for watchlist entries.
- [ ] Score candidates with the 0-100 rubric before promoting entries to `docs/top100.md`.
