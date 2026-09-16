# EvoHarnessBench

[Paper v2](https://arxiv.org/html/2609.04280v2). Zixuan Ke et al.; September 3, revised September 10, 2026; preprint. Accessed September 16; §§3–4.1 and Table 2 inspected. Family: EvoHarnessBench.

**Question/method.** Does previous competence survive a growing tool, skill, or specialist-agent catalog? Externally supplied harness expansion is distinct from autonomous harness generation. Seventeen streams, 3–6 stages, 802 unique tasks (§3.1); split adaptation from evaluation, retain old tasks while adding capabilities.

**Reported evidence.** Evolving-tools Table 2 covers EOG 454 and ALE 63 tasks. EOG cumulative deployment pass rate is 30.2±0.8 versus MemToolAgent 38.6±1.0; ALE 12.2±0.7 versus 10.1±2.0. The uncertainty convention and repeat count were not audited, so these ± values must not be labeled confidence intervals. Resource columns show materially different token costs.

**Authors' claim.** Harness expansion and adaptation produce environment-dependent benefits and forgetting.

**Interpretation/limits.** Useful complement to AgentStream: change the interface as well as task distribution. Broader tools can help; catalog growth is not uniformly harmful. This partial review supports the design distinction and listed comparison, not all skill/agent-axis findings. No independent replication.

**Inspect/discuss.** Table 2 and forward/backward-transfer plots. Can added capability make an old task harder even with unchanged weights?
