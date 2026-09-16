# AutoAgents: A Framework for Automatic Agent Generation

**Authors:** Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang, Jaward Sesay, Borje Karlsson, Jie Fu, Yemin Shi
**arXiv:** 2309.17288
**Venue:** Preprint
**Date:** September 2023; local PDF is arXiv v3 dated April 29, 2024

## Problem
LLM-based multi-agent systems can improve task solving through role specialization and discussion, but many earlier frameworks depend on handcrafted or user-specified agents. That limits adaptation across tasks and makes it costly to decide which experts, tools, and collaboration structure a task needs.

## Method
AutoAgents dynamically synthesizes a task-specific team and execution plan in two stages. In the Drafting Stage, a Planner proposes agents and a plan, while an Agent Observer critiques role coverage and a Plan Observer critiques step quality and role-plan alignment. Generated agents are specified with a prompt, description, toolset, and execution suggestions. In the Execution Stage, an Action Observer coordinates vertical communication, assigns steps to generated agents, tracks progress, and uses short-term, long-term, and dynamic memory. Task execution can involve self-refinement by one agent or collaborative refinement by multiple agents. Experiments use GPT-4-0613 with temperature 0 and an execution environment based on MetaGPT.

## Key Findings
- On MT-Bench open-ended question answering, AutoAgents wins pairwise comparisons against ChatGPT, Vicuna-13B, and GPT-4 under both FairEval and human evaluation in the paper's setup.
- On Trivia Creative Writing, AutoAgents reports higher answer-inclusion scores than Standard prompting, CoT, SPP-Profile, and SPP for both N=5 and N=10 trivia-question settings.
- Ablations on a 20-instance Trivia Creative Writing subset show lower scores when removing observers, self-refinement, collaborative refinement, or dynamic memory.
- The software-development case study shows AutoAgents generating roles such as game design, UI design, programming, and debugging experts for a Tetris task, but this evidence is illustrative rather than a benchmark.
- The authors note limitations: generated roles and plans can still be wrong, role differences mostly come from prompts and tool access, and the framework relies heavily on GPT-4.

## Tags
`multi-agent`, `LLM-agents`, `automatic-agent-generation`, `role-generation`, `planning`, `observer-agents`, `self-refinement`, `collaborative-refinement`, `agent-memory`

## Connections
- Related to **AutoGen** as another multi-agent conversation framework, but AutoAgents emphasizes dynamic generation of the role list and execution plan.
- Related to **MetaGPT** and **ChatDev** for role-based software collaboration; AutoAgents generalizes beyond fixed software-team roles and uses generated expert agents.
- Related to **AgentVerse** and **SPP** as generated-agent frameworks; the paper argues AutoAgents adds observer feedback for role/plan quality and a more general prompt format.
- Useful contrast for **WhyMultiAgentFail**, **CooperBench**, and **CAID**: AutoAgents is an optimistic early architecture for dynamic collaboration, while later work probes coordination failures, isolation, and integration overhead.
