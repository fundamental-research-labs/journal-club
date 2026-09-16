# Claims

## Claim 1: AgentNet replaces centralized orchestration with agent-local routing.

**Evidence:** The system is formalized as a graph of autonomous agents. Each agent has a router and executor; the router independently decides whether to forward, split, or execute the task, while edge weights are updated after task interactions and low-weight edges are pruned.

**Caveats/Scope:** The paper demonstrates the mechanism algorithmically and empirically on benchmark tasks, but does not run adversarial fault-injection or production-scale distributed-system tests.

**Source pointers:** `paper.pdf`, Sections 3.1-3.4; Algorithm 1; Figures 3-4

## Claim 2: Local retrieval memory is intended to support agent specialization without fixed roles.

**Evidence:** Each agent stores local trajectory fragments for its router and executor, retrieves relevant fragments for new tasks, and prunes memories when capacity is reached. The analysis reports increasingly differentiated ability scores and evolved connection strengths after training on BBH.

**Caveats/Scope:** Specialization is shown through the paper's reported ability scores and network visualizations, primarily on BBH; it is not validated across open-ended work, real organizations, or independently audited expertise metrics.

**Source pointers:** `paper.pdf`, Section 3.3; Sections 5.2-5.3; Figures 9-10

## Claim 3: AgentNet is competitive with or better than the listed baselines on the reported benchmarks.

**Evidence:** Table 1 compares AgentNet with Direct, ReAct, Synapse, self-consistency, self-refinement, MorphAgent, MetaGPT, AFLOW, and GPTSwarm on MATH, BBH, and API-Bank using DeepSeek-V3, GPT-4o-mini, and Qwen-turbo. AgentNet is best or tied best in most settings and is particularly strong on BBH and API-Bank.

**Caveats/Scope:** The benchmark splits are constructed by the authors, all multi-agent methods use 3 agents, and the paper does not report statistical significance. On Qwen-turbo MATH, AFLOW is slightly higher than AgentNet.

**Source pointers:** `paper.pdf`, Sections 4.1-4.2; Table 1

## Claim 4: Router policy quality materially affects AgentNet performance.

**Evidence:** The router ablation compares the full AgentNet router with totally random routing, random operation selection, random next-agent selection, and a global-router comparison on BBH. The text reports AgentNet at 82.14% training accuracy and 86.00% test accuracy, above the ablated variants in the figure.

**Caveats/Scope:** The result is reported for BBH with GPT-4o-mini, so it should not be generalized to all tasks, models, or routing-policy designs without further evidence.

**Source pointers:** `paper.pdf`, Section 4.4; Figure 5

## Claim 5: The evolution phase improves over a no-evolution baseline.

**Evidence:** Table 3 reports GPT-4o-mini with 3 agents: AgentNet improves over the no-evolution variant on MATH (85.00 vs. 77.86), API-Bank (32.00 vs. 23.00), and BBH (86.00 vs. 76.00).

**Caveats/Scope:** This ablation is shown for one backbone and one agent count; it measures benchmark accuracy rather than cost, latency, memory quality, or robustness under distribution shift.

**Source pointers:** `paper.pdf`, Section 4.4; Table 3

## Claim 6: Scaling and heterogeneity benefits are conditional rather than monotonic.

**Evidence:** The heterogeneity experiment shows fully homogeneous agents perform best with 3 agents on BBH, while heterogeneous settings improve over the homogeneous setting with 5 agents. The scalability analysis reports only slight gains as the number of agents and executor pool limit increase, with diminishing returns.

**Caveats/Scope:** These analyses are limited to BBH-style tasks and small agent counts, and the paper does not provide a full cost, latency, or privacy leakage analysis.

**Source pointers:** `paper.pdf`, Section 4.3; Section 5.1; Table 2; Figure 8
