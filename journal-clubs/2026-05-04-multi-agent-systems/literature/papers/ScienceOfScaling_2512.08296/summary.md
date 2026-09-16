# Towards a Science of Scaling Agent Systems

**Authors:** Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu
**arXiv:** 2512.08296
**Venue:** Preprint
**Date:** December 2025

## Problem
There is no principled quantitative framework for predicting when adding agents improves performance versus when coordination costs degrade it. Practitioners rely on heuristics because existing multi-agent evaluations conflate architectural effects with implementation choices (different prompts, tools, compute budgets).

## Method
The authors run 260 controlled configurations across 6 agentic benchmarks (BrowseComp-Plus, Finance-Agent, PlanCraft, Workbench, SWE-bench Verified, Terminal-Bench), 5 canonical architectures (Single-Agent, Independent MAS, Centralized MAS, Decentralized MAS, Hybrid MAS), and 3 LLM families (OpenAI, Google, Anthropic) with 9 models spanning Intelligence Index 42-71. They hold prompts, tools, and compute budgets constant across all configurations to isolate architectural effects. They then fit a mixed-effects regression model using empirical coordination metrics (efficiency, error amplification, message density, redundancy) to derive quantitative scaling principles.

## Key Findings
- Multi-agent performance ranges from +80.8% (Finance-Agent, Centralized) to -70.0% (PlanCraft, Independent) relative to single-agent baselines -- architecture-task alignment determines success, not agent count.
- Capability-saturation threshold at ~45% single-agent baseline: beyond this, adding agents yields diminishing or negative returns (most robust finding, survives cluster-robust inference p=0.004 and Holm-Bonferroni correction p=0.018).
- Tool-coordination trade-off: tool-heavy tasks (e.g., 16-tool workflows) suffer disproportionately from multi-agent overhead (interaction coefficient -0.096, p=0.002).
- Independent architectures amplify trace-level errors 17.2x vs 4.4x for Centralized, due to absence of verification bottlenecks.
- Communication overhead grows super-linearly with agent count (power-law exponent 1.724), creating a hard ceiling beyond 3-4 agents under fixed compute.
- Regression model achieves cross-validated R^2=0.373 (R^2=0.413 with task-grounded ACI metric) and correctly predicts the best architecture for 87% of held-out configurations.
- Decomposable tasks (Finance-Agent) benefit from MAS; sequential-dependency tasks (PlanCraft) universally degrade with MAS.
- All MAS architectures slightly degrade on SWE-bench Verified (-2% to -15%), consistent with high single-agent baselines triggering capability saturation.
- Hybrid architecture has the worst efficiency (515% overhead, 13.6 success/1K tokens vs 67.7 for single-agent).

## Tags
`multi-agent`, `scaling-laws`, `coordination`, `architecture-selection`, `benchmark`, `single-vs-multi-agent`, `error-propagation`, `agentic-evaluation`

## Connections
- **SingleAgentOutperforms**: This paper provides the quantitative framework explaining when and why single agents outperform multi-agent systems (the ~45% capability-saturation threshold and sequential-task degradation).
- **WhyMultiAgentFail**: Complements the failure taxonomy; this paper's error amplification analysis (4.4x-17.2x) and MAST-based error categorization directly build on multi-agent failure mode research.
- **AgentScalingDiversity**: Both study scaling in multi-agent systems; this paper focuses on coordination topology while AgentScalingDiversity examines diversity. The super-linear communication overhead finding constrains diversity-based scaling claims.
- **MaAS**: MaAS achieves comparable performance at 6-45% cost via dynamic architecture search; this paper's regression model provides the theoretical grounding for why architecture selection matters (87% accuracy on held-out configs).
- **DELEGATE-52**: Both address architecture selection for agent systems; this paper's quantitative decision boundary (single-agent baseline ~45%) could inform delegation strategies.
- **CooperBench**: Both evaluate multi-agent cooperation; this paper's finding that task decomposability (not team size) drives MAS success is relevant to cooperative benchmark design.
- **SlopCodeBench**: Code quality evaluation relates to the SWE-bench Verified finding that MAS slightly degrades software engineering performance (-2% to -15%).
- **CAID**: Both study coordination in agent systems; this paper's coordination efficiency metrics and error taxonomy provide empirical grounding.
- **AI_Scientists_Dont_Reason**: The capability-saturation finding suggests that reasoning limitations of individual agents are not overcome by multi-agent coordination.
- **MemMA**: Memory architecture is one dimension this paper identifies but does not deeply explore; MemMA's memory-focused approach complements the coordination topology focus here.
