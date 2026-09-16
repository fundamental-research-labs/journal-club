# Agentic Context Engineering (ACE)

## Source and access

**Source key:** `2025-agentic-context-engineering`.

**Originals and source links:** [register](../sources.md#2025-agentic-context-engineering); [canonical source](https://arxiv.org/abs/2510.04618). Retained unmodified: [2025-agentic-context-engineering-paper-v3.pdf](../originals/2025-agentic-context-engineering/2025-agentic-context-engineering-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

. [arXiv v3](https://arxiv.org/abs/2510.04618v3); [PDF](https://arxiv.org/pdf/2510.04618v3). Qizheng Zhang et al. First posted October 6, 2025; v3 March 29, 2026; published at ICLR 2026. Read September 16, 2026: full paper with §§3–5, Tables 1–4 and 12–13 inspected.

## Question and methods

### Question and method

Can evolving a structured playbook avoid the brevity bias and context collapse of monolithic prompt rewriting? ACE separates generation, reflection, and curation, then applies incremental delta updates. It supports offline prompt optimization and online memory updates (§3).

### Evaluation

AppWorld uses official train/test-normal/test-challenge partitions; finance tasks use original train/validation/test splits. Offline methods optimize on training and report pass@1 on test. Online methods process one fixed shuffled test order and update context after each sample (§4.1). The main backbone is DeepSeek-V3.1-671B; appendices add GPT-OSS-120B, GPT-5.1, and Llama-3.3-70B-Instruct. Table 1 reports AppWorld test-normal/test-challenge; Table 2 reports FiNER, Formula, and DDXPlus. No repeated-order uncertainty or confidence intervals accompany the main results.

## Results and evidence

Table 1 reports ACE 59.4/36.9 on AppWorld test-normal/challenge versus 55.4/31.2 for GEPA and 48.8/31.5 for the base agent. Table 2 reports average finance gains of 8.6 points over base and 10.9 over the compared methods as characterized in §4.3, with online adaptation sometimes harmed by misleading execution feedback (§4.3). Table 3 ablations show the generator/reflector/curator and incremental updates matter. Table 4 reports 75.1% fewer rollouts and 86.9% lower adaptation latency than GEPA; Appendix Tables 12–13 give 204.1M→39.3M input tokens and 1.87M→0.31M output tokens for the compared adaptation run. These are implementation-specific cost comparisons, not a hardware-normalized general law. During evaluation, ACE reports 91.8% input-token cache reuse (§4.7).

## Appraisal and limitations

### Authors' claim

Structured, additive playbooks preserve useful detail and improve agents and domain reasoning with lower adaptation overhead.

### Interpretation and limitations

ACE is a strong mechanism and efficiency comparison, and AgentStream supplies a valuable external stress test: Claude Opus 4.7 ACE is 67.0 isolated but 61.9 interleaved, so stream composition can reverse the apparent benefit. The online protocol uses the test stream for adaptation, which is appropriate for deployment-like learning but different from a sealed held-out estimate after learning. A single task order and LLM-based reflection leave order sensitivity and evaluator dependence unresolved. The authors also acknowledge reliance on a sufficiently strong reflector (§5). Use ACE alongside AgentStream and VISTA rather than as stand-alone evidence of reliable improvement.

## Discussion and follow-up

### Useful discussion/figure

The 18,282-token-to-122-token collapse example in §2.2 and Tables 1/4 cleanly motivate why update representation and cost accounting matter.
