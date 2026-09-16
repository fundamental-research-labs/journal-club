# AgentBench: Evaluating LLMs as Agents

**Authors:** Xiao Liu*, Hao Yu*, Hanchen Zhang*, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
**arXiv:** 2308.03688
**Venue:** ICLR 2024
**Date:** August 2023

## Problem
LLM agents were becoming popular for autonomous goal completion, but evaluation was fragmented across narrow text games, static NLP tasks, or environment-specific simulators. The paper asks how to evaluate text-only LLMs as agents that must reason, choose actions, follow interaction formats, and recover from environment feedback over multiple turns.

## Method
AgentBench defines an interactive LLM-as-agent setting and builds eight environments grouped into code-grounded tasks (Operating System, Database, Knowledge Graph), game-grounded tasks (Digital Card Game, Lateral Thinking Puzzles, House Holding), and web-grounded tasks (Web Shopping, Web Browsing). The benchmark uses task-specific metrics such as success rate, F1, reward, game progress, and step success, then reports a weighted overall score. The authors evaluate 29 API-based and open-source LLMs with simple CoT-style prompting, temperature 0, isolated task workers, Dockerized environments where needed, and a server-client toolkit for model evaluation over HTTP.

## Key Findings
- Top API models substantially outperform the tested OSS models. GPT-4 (0613) has the highest overall AgentBench score, and the paper reports an API-model average far above the OSS average in its evaluated set.
- GPT-4 leads on most environments but is still uneven: it is strong on House Holding and Digital Card Game, while code, web-browsing, and lateral-puzzle tasks remain difficult.
- The best tested OSS model under the paper's scope is CodeLlama-34B-Instruct, but it remains well below GPT-3.5-turbo and GPT-4 on the weighted overall score.
- Failure analysis points to Task Limit Exceeded as a common failure mode, with Invalid Format especially visible in Database and Digital Card Game, and Invalid Action especially visible in House Holding and Web Browsing.
- The training-signal analysis is mixed: code tuning appears useful for procedural tasks such as Web Shopping but can hurt more strategic or situational tasks; comparison with Vicuna-13B suggests high-quality alignment data helps agent behavior.

## Tags
`llm-agents`, `benchmark`, `interactive-evaluation`, `tool-use`, `web-agents`, `code-agents`, `reasoning`, `decision-making`, `agentbench`

## Connections
- Complements static LLM benchmark work such as MMLU and HELM by emphasizing multi-round interaction, environment feedback, and action validity.
- Builds on environment-specific agent benchmarks such as ALFWorld, WebShop, Mind2Web, and text-game evaluations, but combines multiple domains into one agent benchmark.
- Useful context for later corpus papers on agent evaluation and multi-agent coding systems, including CooperBench and CAID, because it establishes the broader single-agent benchmark tradition and common failure categories.
- Related to tool-use and ReAct-style prompting work: AgentBench uses simple CoT/action prompting rather than search, reflection, or multi-trial scaffolding, making the reported numbers a baseline for stronger agent scaffolds.
