# Claims

## Claim 1: AgentsNet turns distributed computing problems into multi-agent LLM coordination tasks.
**Claim:** The benchmark evaluates coordination through graph coloring, minimal vertex cover, maximal matching, leader election, and consensus.

**Evidence:** Section 3.1 defines each task and Table 1 ties the tasks to distributed-computing problems and round-complexity lower bounds.

**Caveats/Scope:** These are stylized graph tasks, not direct simulations of messy real-world agent work.

**Source pointers:** `paper.pdf`, Sec. 3.1, Fig. 3, Table 1

## Claim 2: The benchmark enforces decentralized local communication.
**Claim:** Agents can communicate only with immediate graph neighbors through fixed-round synchronous message passing before giving a final answer.

**Evidence:** Section 4 describes a LOCAL-model-inspired protocol: each agent receives a task prompt, neighbor list, and message-passing rules, sends JSON messages to neighbors, and later produces a structured final response.

**Caveats/Scope:** The protocol is synchronous and fixed-round; the authors note that other message-passing protocols or structured-output mechanisms may be more effective.

**Source pointers:** `paper.pdf`, Sec. 4, Appendix A, Sec. 6, Appendix G

## Claim 3: The main evaluation spans multiple graph families, sizes, and model families.
**Claim:** AgentsNet evaluates models on small-world, scale-free, and Delaunay graphs with 4, 8, and 16 agents, plus a larger scaling probe.

**Evidence:** Section 5.1 reports 27 network topologies from three graph distributions and three graph sizes, with frontier, reasoning, and open-source models evaluated using strict network-level success.

**Caveats/Scope:** The initial suite uses homogeneous agents and models available at the time of the paper; strict binary scoring can hide partial progress.

**Source pointers:** `paper.pdf`, Sec. 5.1, Table 2, Table 3, Appendix C

## Claim 4: Frontier models do well on some tasks but do not saturate AgentsNet.
**Claim:** The best aggregate model in the reported results is Gemini 2.5 Pro at 0.80, and no model is consistently strong across every task and graph size.

**Evidence:** Table 2 reports aggregate scores of 0.80 for Gemini 2.5 Pro, 0.70 for Claude 3.7 Sonnet, and 0.69 for Gemini 2.5 Flash. Section 5.2 states that even 4-node graphs are not solved consistently across all tasks and that vertex cover is difficult for most models.

**Caveats/Scope:** These numbers are tied to the paper's model versions, prompts, graph samples, and strict scoring metric.

**Source pointers:** `paper.pdf`, Sec. 5.2, Table 2, Fig. 4, Appendix H

## Claim 5: Increasing graph size makes the benchmark substantially harder.
**Claim:** AgentsNet can increase difficulty by scaling the number of agents, and current model performance degrades on larger networks.

**Evidence:** The scaling experiment with Gemini 2.0 Flash evaluates networks from 20 to 100 agents and reports that performance smoothly decreases; at 100 agents, performance is near zero across tasks.

**Caveats/Scope:** The 20- to 100-agent scaling result is shown for Gemini 2.0 Flash rather than all evaluated models.

**Source pointers:** `paper.pdf`, Sec. 5.3, Fig. 5, Sec. 7

## Claim 6: Qualitative failures often come from strategy and information-management issues.
**Claim:** Agents fail when they coordinate strategies too late or not at all, over-accept erroneous or stale neighbor information, or do not synchronize candidate solutions.

**Evidence:** Section 5.4 summarizes three qualitative findings, and Appendix E gives transcript examples for mistaken graph beliefs, outdated matching commitments, conflict resolution in coloring, and synchronization difficulties.

**Caveats/Scope:** The transcript analysis is selective and qualitative; it should be treated as diagnosis rather than a complete taxonomy.

**Source pointers:** `paper.pdf`, Sec. 5.4, Appendix E
