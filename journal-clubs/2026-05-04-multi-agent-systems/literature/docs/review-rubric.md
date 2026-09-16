# Multi-Agent Paper Review Rubric

Use this rubric to review LLM-based multi-agent papers in an ICLR-style format. The goal is not just to assign a score, but to decide whether the paper changes what we should believe about multi-agent systems.

## Review Output

Each review should include:

1. **One-sentence verdict**: the paper's main contribution and whether it is convincing.
2. **Scores**: rate each criterion below from 1-5.
3. **Overall score**: ICLR-style score from 1-10.
4. **Confidence**: reviewer confidence from 1-5.
5. **Strengths**: 3-5 concrete points.
6. **Weaknesses**: 3-5 concrete points.
7. **Questions for authors**: the highest-value clarifications or missing experiments.
8. **Takeaway for this repo**: how the paper changes our map of multi-agent research.

## Criterion Scores

Use 1-5 for each criterion:

| Score | Meaning |
|---|---|
| 5 | Excellent: unusually strong for a top ML conference |
| 4 | Good: solid and above the acceptance bar |
| 3 | Adequate: useful but has important limitations |
| 2 | Weak: substantial flaws or unclear contribution |
| 1 | Poor: not convincing or not meaningfully evaluated |

### 1. Novelty

Does the paper introduce a genuinely new idea, benchmark, phenomenon, theoretical framing, or empirical result?

- **5**: Opens a new direction or reframes an important question; not just a recombination of known agent patterns.
- **4**: Clear new contribution relative to existing multi-agent, agent, or LLM evaluation work.
- **3**: Incremental but useful extension, synthesis, or benchmark.
- **2**: Mostly repackages known ideas with limited differentiation.
- **1**: No clear novelty.

Check specifically:

- Is the novelty in the agent architecture, the task setting, the evaluation method, the analysis, or the finding?
- Would the contribution still matter if the same experiments were run with a single-agent baseline?
- Does the paper distinguish itself from frameworks such as AutoGen, CAMEL, MetaGPT, ChatDev, debate, self-consistency, and agentic workflow papers?

### 2. Significance

Would the result matter if true?

- **5**: Changes how researchers or builders should design, evaluate, or reason about multi-agent systems.
- **4**: Important for a clear sub-area such as coding agents, debate, memory, coordination, benchmarks, or agent scaling.
- **3**: Useful but narrow.
- **2**: Mostly engineering detail or limited-scope result.
- **1**: Low consequence even if correct.

Check specifically:

- Does it address a central bottleneck: coordination, communication, specialization, scaling, memory, delegation, reliability, cost, or evaluation?
- Does it identify when multiple agents are better, worse, or simply more expensive than alternatives?
- Does it produce reusable artifacts: benchmark, dataset, code, taxonomy, protocol, or analysis framework?

### 3. Technical Correctness and Rigor

Are the claims supported by sound methods?

- **5**: Strong experimental design, careful controls, valid statistics, and claims that match the evidence.
- **4**: Mostly rigorous with minor gaps.
- **3**: Plausible but missing some controls, ablations, or uncertainty analysis.
- **2**: Major confounds or overclaiming.
- **1**: Evidence does not support the claims.

Check specifically:

- Are baselines fair, current, and budget-matched?
- Are single-agent, multi-agent, and more-sampling baselines separated cleanly?
- Are token budget, wall-clock time, number of model calls, tool access, context length, and model version controlled?
- Are metrics valid for the claimed capability, or merely convenient proxies?
- Are statistical tests, confidence intervals, or repeated runs provided where stochasticity matters?
- Are failure cases analyzed rather than averaged away?

### 4. Empirical Breadth and Generality

Does the evidence generalize beyond a narrow demo?

- **5**: Evaluates across diverse tasks, models, seeds, and settings with consistent analysis.
- **4**: Covers enough variation to support the main claims.
- **3**: Reasonable but limited coverage.
- **2**: Too narrow to support broad conclusions.
- **1**: Demo-level evidence only.

Check specifically:

- Are results shown across multiple LLM families or only one provider/model?
- Are tasks diverse enough for the claimed scope?
- Are agent counts, roles, communication protocols, and orchestration choices varied?
- Does the paper test robustness to prompt changes, model upgrades, tool availability, and context pressure?
- Are long-horizon effects measured when the paper claims to study agentic workflows?

### 5. Multi-Agent Specificity

Is the multi-agent framing necessary and well justified?

- **5**: Clearly isolates mechanisms that only arise, or matter distinctly, in multi-agent systems.
- **4**: Strong evidence that agent interaction, specialization, diversity, or coordination drives the result.
- **3**: Multi-agent framing is plausible but not fully isolated.
- **2**: Could mostly be a single-agent, ensemble, or workflow paper.
- **1**: "Multi-agent" is branding rather than substance.

Check specifically:

- What is the mechanism: debate, decomposition, specialization, redundancy, diversity, critique, tool partitioning, social simulation, or memory sharing?
- Is improvement due to multiple agents, or just more tokens, more samples, more context, or more tool calls?
- Are communication and coordination costs measured?
- Does the system show emergent benefits or emergent failure modes?
- Are interactions between agents inspected, not just final task scores?

### 6. Reproducibility and Transparency

Could another researcher verify or build on the work?

- **5**: Code, data, prompts, model versions, configs, and evaluation scripts are complete.
- **4**: Most artifacts are available; minor missing details.
- **3**: Enough detail to approximate the results.
- **2**: Important implementation or evaluation details are missing.
- **1**: Not reproducible.

Check specifically:

- Are prompts, system messages, agent roles, stopping conditions, and tool specs included?
- Are model versions and decoding settings specified?
- Are benchmark tasks and labels available?
- Is the evaluation automated and auditable?
- Are costs reported in tokens, dollars, wall-clock time, or compute?

### 7. Clarity and Positioning

Is the paper easy to understand and honestly situated?

- **5**: Clear problem framing, clean exposition, strong related work, and calibrated claims.
- **4**: Generally clear with minor ambiguities.
- **3**: Understandable but somewhat hard to follow or under-positioned.
- **2**: Important claims, definitions, or comparisons are unclear.
- **1**: Confusing or misleading.

Check specifically:

- Are "agent", "multi-agent", "collaboration", "coordination", and "reasoning" defined operationally?
- Does the paper distinguish benchmark contribution from model/system contribution?
- Are limitations explicit and specific?
- Are figures and tables interpretable without overreading?
- Does the title/abstract match the actual evidence?

### 8. Practical Usefulness

Does the paper help someone build, evaluate, or reason about real systems?

- **5**: Directly actionable for system design or evaluation.
- **4**: Provides useful guidance with some caveats.
- **3**: Offers partial guidance or a useful warning.
- **2**: Hard to translate into practice.
- **1**: No clear practical implications.

Check specifically:

- Does it tell us when to use multi-agent systems and when not to?
- Does it expose reliability, safety, cost, or maintainability tradeoffs?
- Are constraints realistic for deployed agent systems?
- Are recommendations robust to model progress?

## Overall ICLR-Style Score

Use this 1-10 scale after scoring the criteria:

| Score | Recommendation | Meaning |
|---|---|---|
| 10 | Strong Accept | Landmark paper; exceptional contribution and evidence |
| 9 | Strong Accept | Top-tier paper; very strong and broadly important |
| 8 | Accept | Clear acceptance; strong contribution with manageable issues |
| 7 | Accept | Above the bar; useful and mostly convincing |
| 6 | Weak Accept | Marginally above the bar; worthwhile but limited |
| 5 | Borderline | Interesting but not yet convincing |
| 4 | Weak Reject | Some value, but flaws outweigh contribution |
| 3 | Reject | Serious novelty, rigor, or clarity problems |
| 2 | Strong Reject | Major flaws; limited scientific value |
| 1 | Strong Reject | Not suitable as a research contribution |

Suggested mapping:

- **8-10**: At least two criteria are 5, no core criterion below 4, and the paper changes the field's understanding.
- **6-7**: Solid contribution with some limits; most criteria are 3-4.
- **5**: Worth discussing but has unresolved concerns about novelty, controls, or scope.
- **1-4**: Evidence, novelty, or framing is too weak for acceptance.

Core criteria for this repo are **Novelty**, **Technical Correctness and Rigor**, and **Multi-Agent Specificity**. A paper with weak scores on these should rarely receive an overall score above 6, even if it is well written.

## Confidence Score

| Score | Meaning |
|---|---|
| 5 | Very familiar with the area and checked the key details |
| 4 | Familiar with the area and confident in the assessment |
| 3 | Reasonable confidence, but some related work or technical details may be missing |
| 2 | Limited confidence; review is preliminary |
| 1 | Low confidence; needs expert follow-up |

## Common Red Flags for Multi-Agent Papers

- Claims multi-agent gains without budget-matched single-agent or sampling baselines.
- Compares against weak, outdated, or poorly tuned baselines.
- Treats more LLM calls as evidence of better agent design.
- Omits token cost, latency, or model version details.
- Uses LLM judges without calibration, human agreement, or bias checks.
- Reports only aggregate scores while hiding high-variance failures.
- Uses toy tasks while claiming real-world agent capability.
- Attributes gains to collaboration without analyzing agent interactions.
- Conflates role prompting, ensembling, self-consistency, and multi-agent coordination.
- Makes broad claims from one model family, one benchmark, or one prompt.

## Common Strength Signals

- Clean separation between multi-agent mechanism and extra compute.
- Strong single-agent, ensemble, and workflow baselines.
- Analysis of when multi-agent systems fail, not just when they help.
- Long-horizon evaluation with compounding error analysis.
- Robustness checks across models, task types, and orchestration choices.
- Public tasks, prompts, traces, and evaluation scripts.
- Cost-quality tradeoff curves.
- Clear taxonomy or theory that predicts empirical outcomes.
- Qualitative traces that explain quantitative results.

## Review Template

```markdown
# Review: <Paper Title>

## Verdict
<One sentence on contribution and whether the evidence is convincing.>

## Scores
| Criterion | Score (1-5) | Notes |
|---|---:|---|
| Novelty |  |  |
| Significance |  |  |
| Technical correctness and rigor |  |  |
| Empirical breadth and generality |  |  |
| Multi-agent specificity |  |  |
| Reproducibility and transparency |  |  |
| Clarity and positioning |  |  |
| Practical usefulness |  |  |

**Overall score:** <1-10>
**Confidence:** <1-5>

## Strengths
-
-
-

## Weaknesses
-
-
-

## Questions for Authors
-
-

## Takeaway for Multi-Agent Literature
<How this changes the repo's view of multi-agent systems.>
```
