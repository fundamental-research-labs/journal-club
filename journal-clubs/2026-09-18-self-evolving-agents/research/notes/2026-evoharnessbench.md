# EvoHarnessBench

## Source and access

**Source key:** `evoharnessbench`.

**Originals and source links:** [register](../sources.md#evoharnessbench); [canonical source](https://arxiv.org/abs/2609.04280v2). Retained unmodified: [2026-evoharnessbench-paper-v2.pdf](../originals/2026-evoharnessbench/2026-evoharnessbench-paper-v2.pdf). Paper license: http://creativecommons.org/licenses/by-sa/4.0/. [Manifest](../originals/manifest.json).

[Paper v2](https://arxiv.org/html/2609.04280v2). Zixuan Ke et al.; September 3, revised September 10, 2026; preprint. Accessed September 16; §§3–4.1 and Table 2 inspected. Family: EvoHarnessBench.

## Question and methods

Does previous competence survive a growing tool, skill, or specialist-agent catalog? Externally supplied harness expansion is distinct from autonomous harness generation. Seventeen streams, 3–6 stages, 802 unique tasks (§3.1); split adaptation from evaluation, retain old tasks while adding capabilities.

## Results and evidence

### Reported evidence

Evolving-tools Table 2 covers EOG 454 and ALE 63 tasks. EOG cumulative deployment pass rate is 30.2±0.8 versus MemToolAgent 38.6±1.0; ALE 12.2±0.7 versus 10.1±2.0. The official project-page follow-up establishes ± as population SD over three runs; these values are not confidence intervals. Resource columns show materially different token costs.

### Uncertainty and metric clarification — September 16

The coordinator checked the [official project page](https://mas-orchestra.salesforceresearch.ai/evoharness/), Results/record schema: the published rows use **three runs**, ± is **population standard deviation**, Overall pools solved/attempted task counts rather than averaging environment percentages, and hours sum agent durations rather than wall-clock elapsed time. Consequently a three-run SD must not be labeled SE or CI, and the hours cannot be interpreted as deployment latency. Seventeen streams and 802 unique tasks are benchmark inventory; 1,510 axis-specific examples reuse tasks across tool/skill/agent variants. These are different units.

The live task gallery describes a 1,061-example test split and a richer corpus view than the paper’s headline count. Preserve the versioned manuscript as the results reference rather than assuming a live site’s counts identify identical releases. Per-run raw outcomes and a matching corpus manifest remain desirable before replotting.

## Appraisal and limitations

### Authors' claim

Harness expansion and adaptation produce environment-dependent benefits and forgetting.

### Interpretation and limitations

Useful complement to AgentStream: change the interface as well as task distribution. Broader tools can help; catalog growth is not uniformly harmful. This partial review supports the design distinction and listed comparison, not all skill/agent-axis findings. No independent replication.

## Discussion and follow-up

Table 2 and forward/backward-transfer plots. Can added capability make an old task harder even with unchanged weights?

[Prominent citations and their roles](../prominent-citations.md#evoharnessbench)
