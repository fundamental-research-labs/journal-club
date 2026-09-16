# Notes

## Why It Matters
MAS-GPT is an early attempt to make the structure of an LLM-based multi-agent system itself a generated artifact. Instead of asking researchers or users to hand-author roles, prompts, and interaction graphs for each task, it trains a model to emit executable agent code from the query. This makes it a useful reference for learned agent orchestration, synthetic MAS data construction, and the tradeoff between one-time training cost and repeated inference-time MAS search.

## When To Cite
Cite this paper when discussing query-adaptive multi-agent LLM systems, training models to generate agent workflows, executable-code representations of MAS, consistency-oriented synthetic data for agent systems, or comparisons between learned MAS generation and iterative per-query optimizers such as DyLAN, GPTSwarm, ADAS, and AFlow.

## Key Terms
MAS-GPT; LLM-based multi-agent system; query-specific MAS; executable MAS; Python `forward` function; agent prompt variables; LLM call functions; inter-consistency-oriented pair selection; intra-consistency-oriented pair refinement; query-MAS pair; Qwen2.5-Coder-32B-Instruct; MAS-driving LLM; AIME-2024; HumanEval; MMLU; GPQA; SciBench.
