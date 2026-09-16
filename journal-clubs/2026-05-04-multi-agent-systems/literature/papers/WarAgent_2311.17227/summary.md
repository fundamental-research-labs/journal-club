# War and Peace (WarAgent): LLM-based Multi-Agent Simulation of World Wars

**Authors:** Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, Yongfeng Zhang
**arXiv:** 2311.17227
**Venue:** Preprint
**Date:** January 2024

## Problem
Can LLM-based multi-agent systems simulate historically plausible international conflict dynamics rather than simply replaying memorized facts? The paper focuses on whether country-agent interactions can reproduce strategic planning and escalation in World War I, World War II, and the Warring States Period, and whether counterfactual changes to triggers or country conditions reveal when war becomes more or less likely.

## Method
WarAgent represents each country as an LLM agent with a structured profile covering leadership, military capability, resources, historical background, key policy, and public morale. Agents choose from a diplomatic and military action space: wait, mobilize, declare war, request or publish alliances, request or publish non-intervention treaties, propose peace agreements, and send messages. A secretary agent checks each country's proposed actions for action validity, formatting, and basic logical consistency. A per-agent Board tracks external relations such as wars, alliances, non-intervention treaties, and peace agreements; a Stick tracks domestic state, especially mobilization. To reduce direct historical recall, the authors anonymize country names, locations, and events. Experiments use GPT-4-1106-preview, GPT-3.5-turbo-1106, and Claude-2, with evaluation via human judgment, Board-based accuracy against historical alliance/war/mobilization states, and counterfactual analysis.

## Key Findings
- GPT-4 gives the strongest default simulations. In Table 2, the WWI setting reaches 77.78 alliance accuracy, 54.60 war-declaration accuracy, and 92.09 mobilization accuracy; war declarations are consistently the weakest evaluated dimension.
- Human analysis of GPT-4 WWI runs finds recurring plausible alliance patterns, including Britain-France, German Empire-Austria-Hungary, and Serbia-Russia, plus U.S. and Ottoman non-intervention behavior.
- Anonymization changes behavior: de-anonymized prompts converge quickly and consistently toward known historical narratives, while anonymized simulations produce more varied and sometimes non-historical relations.
- Counterfactual trigger experiments suggest escalation depends on trigger intensity but is not mechanically determined: a null trigger produced a cold-war-like mobilized standoff, an Anglo-German naval incident produced war in one of three runs, and an Austria-Russia Dardanelles conflict produced global war in two of three runs.
- War inevitability experiments identify prompt-level aggressiveness, historical background, key policy, and public morale as important levers; changing raw military capacity or resources alone showed no obvious change in the focused France-German Empire tests.
- The authors frame WarAgent as a suggestive social-simulation tool, not a predictive model: major limitations include synchronous rounds, simplified communication publicity, missing espionage, and simplified mobilization timing.

## Tags
`multi-agent`, `llm-agents`, `social-simulation`, `historical-simulation`, `international-relations`, `counterfactual-analysis`, `war-and-peace`, `agent-communication`

## Connections
- Related to **AgentVerse** and **CAMEL** as role-playing multi-agent systems, but WarAgent applies role-play to geopolitical history rather than task completion.
- Complements **Generative Agents**-style social simulation by adding explicit country profiles, diplomatic actions, and state trackers for international relations.
- Relevant to multi-agent coordination work such as **CooperBench** and **CAID** because it exposes how communication, partial observability, and state tracking shape collective agent behavior, though in a social-science simulation rather than coding.
- Useful for discussions of LLM memory leakage in simulations: the anonymization and de-anonymization experiments directly test whether agents are reasoning from profiles or recalling historical narratives.
