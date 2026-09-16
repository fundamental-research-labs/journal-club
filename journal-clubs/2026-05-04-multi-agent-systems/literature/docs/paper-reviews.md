# Multi-Agent Paper Reviews

These reviews apply `docs/review-rubric.md` to ten papers in `papers/`. Reviews were produced by parallel agents from each paper's local `metadata.yaml`, `summary.md`, `claims.md`, `notes.md`, and targeted source/PDF inspection where needed.

`AI_Scientists_Dont_Reason_2604.18805` was excluded to keep the set to 10 papers and because it is less centrally about multi-agent coordination than the selected papers.

## Score Summary

| Paper | Overall | Confidence | Repo Role |
|---|---:|---:|---|
| CooperBench | 8 | 4 | Core negative result for cooperative coding agents |
| Single-Agent Outperforms | 8 | 4 | Core budget-matched skepticism paper |
| Science of Scaling | 8 | 4 | Central when-to-use-MAS empirical map |
| Why Multi-Agent Fail | 8 | 4 | Main diagnostic taxonomy for MAS failures |
| MaAS | 8 | 4 | Adaptive architecture search reference |
| Agent Scaling Diversity | 7 | 4 | Diversity/effective-channel scaling reference |
| CAID | 7 | 4 | Positive structured SWE delegation reference |
| DELEGATE-52 | 7 | 4 | Long-horizon artifact corruption benchmark |
| MemMA | 7 | 3 | Memory-cycle multi-agent architecture |
| SlopCodeBench | 6 | 4 | Coding trajectory quality benchmark |

## Cross-Paper Takeaways

- Strong multi-agent papers increasingly need budget-matched single-agent, sampling, and workflow baselines.
- Agent count alone is a weak design variable; diversity, topology, task decomposability, and verification matter more.
- The most convincing multi-agent value appears when coordination is externalized into structure: worktrees, explicit contracts, dependency graphs, memory lifecycle roles, or architecture search.
- Free-form collaboration remains fragile, especially under partial observability, artifact handoffs, and long horizons.
- Long-horizon evaluation should measure artifact preservation, maintainability, cost, latency, and failure trajectories, not only final success.

## Review: CooperBench: Why Coding Agents Cannot be Your Teammates Yet

## Verdict

A strong benchmark paper showing that current coding agents often lose capability when forced to cooperate, with convincing evidence that coordination under partial observability is a real bottleneck.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | New benchmark and sharp coordination-gap framing for coding agents. |
| Significance | 5 | Directly changes how multi-agent coding systems should be evaluated. |
| Technical correctness and rigor | 4 | Strong Solo vs Coop baseline, tests, CIs, communication ablations; some qualitative/LLM-judge caveats. |
| Empirical breadth and generality | 4 | 652 tasks, 12 repos, 4 languages, 5 models; scaling-to-4-agents experiment is smaller. |
| Multi-agent specificity | 5 | Isolates communication, commitment, expectation, merge, and coordination failures. |
| Reproducibility and transparency | 4 | Open benchmark/framework claimed, prompts and containers described; full artifact completeness not verified. |
| Clarity and positioning | 4 | Clear framing and taxonomy, with minor overreach beyond coding. |
| Practical usefulness | 5 | Highly actionable for agent teams: solo baselines, verifiable commitments, merge-aware protocols. |

**Overall score:** 8
**Confidence:** 4

## Strengths

- Cleanly separates solo capability from cooperative capability.
- Verifiable coding tasks with expert tests and realistic conflicting-but-compatible feature pairs.
- Strong evidence that communication reduces merge conflicts but not end-to-end correctness.
- Useful failure taxonomy around communication, commitment, and expectation.
- Practical prescriptions around verifiable shared state and insertion-point contracts.

## Weaknesses

- The more-agents result is based on a relatively small 46-task scaling subset.
- Communication channel is text-only; richer shared-state mechanisms may change results.
- Some failure analysis relies on manual interpretation and LLM-as-judge labeling.
- Benchmark focuses on isolated branches and merge integration, not all collaborative SWE.
- Claims about broader social intelligence are plausible but broader than the direct evidence.

## Questions for Authors

- How do results change with shared read-only visibility into partner diffs?
- Can structured protocols, branch summaries, or typed interface contracts close the semantic coordination gap?
- Are results robust to agent frameworks beyond OpenHands?
- How much Coop failure is due to hidden partner state versus weak task decomposition?
- Would budget-matched multi-sample solo baselines outperform Coop?

## Takeaway for Multi-Agent Literature

CooperBench is a core negative result for multi-agent coding: multiple agents need explicit shared-state and commitment mechanisms, not just chat.

## Review: Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

## Verdict

A strong, compute-controlled critique of multi-agent reasoning claims; convincing for text-only multi-hop QA, less decisive for tool-heavy or long-horizon agent settings.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Clear reframing around equal thinking-token budgets plus DPI/context degradation argument. |
| Significance | 5 | Directly changes how MAS results should be interpreted. |
| Technical correctness and rigor | 4 | Good controls, multiple architectures/models/datasets, CIs; Gemini token accounting remains approximate. |
| Empirical breadth and generality | 4 | FRAMES and MuSiQue, Qwen/DeepSeek/Gemini, several MAS variants; still text QA. |
| Multi-agent specificity | 5 | Isolates coordination/message bottlenecks, aggregation failures, debate/roles/ensemble variants. |
| Reproducibility and transparency | 4 | Source and detailed appendices appear available; API hidden reasoning limits exact replication. |
| Clarity and positioning | 4 | Clear thesis and calibrated limitations. |
| Practical usefulness | 5 | Highly actionable: normalize compute and prefer single-agent unless task structure justifies MAS. |

**Overall score:** 8
**Confidence:** 4

## Strengths

- Strong budget-matched comparison against multiple MAS designs.
- Separates architectural benefit from extra test-time compute.
- Useful theory-to-experiment link via information loss and context degradation.
- Identifies when MAS may help: degraded context, decomposition, or hybrid regimes.
- Includes diagnostic analysis of benchmark and API accounting artifacts.

## Weaknesses

- Scope is mostly multi-hop QA, not tools, software engineering, vision, safety, or long-horizon workflows.
- Thinking-token control is imperfect for opaque API models.
- DPI argument is suggestive but idealized.
- LLM-judge accuracy metric may miss nuanced answer quality and failure modes.

## Questions for Authors

- How do results change under equal dollar cost, latency, and total prompt plus completion tokens?
- Do MAS advantages reappear on tool-use tasks where agents hold different state or permissions?
- Can aggregation failures be reduced with stronger verifier/finalizer designs?
- Are results stable under human evaluation rather than LLM-as-judge answer matching?

## Takeaway for Multi-Agent Literature

Treat this as a core skepticism paper: MAS papers should be penalized unless they beat budget-matched single-agent, sampling, and workflow baselines or identify a regime where coordination genuinely helps.

## Review: Towards a Science of Scaling Agent Systems

## Verdict

A strong empirical paper that meaningfully advances when-to-use-MAS reasoning, showing that architecture-task alignment and coordination overhead dominate naive agent scaling.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Quantitative architecture-selection framing is substantial. |
| Significance | 5 | Directly changes how builders should choose single-agent vs MAS architectures. |
| Technical correctness and rigor | 4 | Strong controls, cross-validation, CIs/statistics, and explicit caveats. |
| Empirical breadth and generality | 4 | Six agentic benchmarks, five architectures, three model families; expensive subsets are smaller. |
| Multi-agent specificity | 5 | Directly isolates coordination topology, overhead, verification, redundancy, and error amplification. |
| Reproducibility and transparency | 3 | Setup is well described, but full code/prompts/config availability was not clear. |
| Clarity and positioning | 4 | Clear definitions and honest limitations. |
| Practical usefulness | 5 | Very actionable decision rules for decomposable vs sequential/tool-heavy tasks. |

**Overall score:** 8
**Confidence:** 4

## Strengths

- Strong controlled comparison across single-agent and four MAS topologies.
- Directly addresses practical decision-making rather than aggregate MAS gains.
- Useful failure boundaries around single-agent saturation, tool coordination, and error amplification.
- Evaluates real agentic benchmarks including SWE-bench Verified and Terminal-Bench.
- Strong caveats around small clusters, benchmark limits, and economic viability.

## Weaknesses

- Regression has modest predictive power in absolute terms.
- Some findings are directional under conservative clustered inference.
- Smaller expensive-benchmark subsets reduce confidence in per-cell comparisons.
- Architecture-specific prompt tuning might change outcomes.
- Heterogeneity is less deeply explored than topology and coordination.

## Questions for Authors

- Are code, prompts, traces, and exact configs available for reproducing all configurations?
- How stable is the reported threshold under newer benchmarks, stronger models, and different tools?
- Would adaptive routing/architecture selection outperform fixed canonical topologies?
- How much MAS degradation comes from token fragmentation versus coordination errors?
- Can the framework predict latency- or dollar-normalized architecture choices?

## Takeaway for Multi-Agent Literature

This should be a central reference for anti-more-agents reasoning: use MAS for naturally decomposable, low-baseline, parallel information-gathering tasks; prefer single-agent or tightly centralized systems for sequential, high-baseline, or tool-heavy workflows.

## Review: Why Do Multi-Agent LLM Systems Fail?

## Verdict

A valuable failure-taxonomy and dataset paper that makes MAS breakdowns inspectable and actionable, though its causal claims about fixes are more preliminary than its taxonomy contribution.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | First systematic MAS failure taxonomy/dataset of this kind. |
| Significance | 5 | Gives the field shared language for coordination, verification, and design failures. |
| Technical correctness and rigor | 4 | Grounded theory, expert annotation, kappa validation, LLM-judge calibration; intervention evidence is narrower. |
| Empirical breadth and generality | 5 | 1600+ traces, 7 frameworks, coding/math/general tasks, several model families. |
| Multi-agent specificity | 5 | Directly studies inter-agent misalignment, role failures, verification, repeated steps, and derailment. |
| Reproducibility and transparency | 5 | Public dataset, taxonomy, annotator, traces, and source pointers. |
| Clarity and positioning | 4 | Clear framework and practical examples. |
| Practical usefulness | 5 | Immediately useful for debugging, evaluation, trace annotation, and verifier design. |

**Overall score:** 8
**Confidence:** 4

## Strengths

- Turns vague coordination failures into concrete failure modes.
- Strong annotation methodology with human agreement and LLM-judge validation.
- Broad framework/task/model coverage.
- Public artifacts make it reusable for benchmarks and diagnostics.
- Practical interventions show role specs and high-level verification can improve outcomes.

## Weaknesses

- Taxonomy is descriptive and does not fully explain every causal mechanism.
- LLM-as-judge annotation has imperfect recall/F1 despite good agreement.
- Cross-framework comparisons may be confounded by tasks, prompts, and implementations.
- Proposed fixes improve results but do not establish a general robust-MAS recipe.

## Questions for Authors

- Which failure modes best predict final task failure after controlling for framework and task?
- How stable is MAST under newer reasoning models and tool-heavy agents?
- Can the taxonomy distinguish MAS architecture failures from base-LLM failures?
- What minimal trace format is required for reliable automated failure annotation?

## Takeaway for Multi-Agent Literature

This should be the repo's main diagnostic vocabulary for MAS reliability, especially around system design, inter-agent misalignment, and verification failures.

## Review: Multi-agent Architecture Search via Agentic Supernet

## Verdict

MaAS makes a convincing case that query-adaptive multi-agent workflow search can improve cost-quality tradeoffs, though some gains may depend on search-space design and extra optimization machinery.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Strong framing of multi-agent design as query-conditioned architecture search. |
| Significance | 4 | Addresses coordination, specialization, and cost allocation. |
| Technical correctness and rigor | 4 | Broad baselines, ablations, cost reporting, and transfer tests; still needs sharper budget matching. |
| Empirical breadth and generality | 4 | Covers math, coding, tool use, multiple backbones, and transfer. |
| Multi-agent specificity | 4 | Operator search and adaptive composition are genuinely workflow-specific. |
| Reproducibility and transparency | 3 | Full reproducibility depends on prompts, configs, APIs, and textual-gradient details. |
| Clarity and positioning | 4 | Clear problem and contribution. |
| Practical usefulness | 5 | Very actionable: adapt agent architecture and depth to query difficulty. |

**Overall score:** 8
**Confidence:** 4

## Strengths

- Strong problem framing: static workflows are often wasteful or brittle.
- Good empirical range across reasoning, coding, and tool-use benchmarks.
- Cost-quality evidence is unusually relevant for deployment.
- Ablations identify textual gradients and cost constraints as distinct contributors.
- Transfer across LLM backbones and datasets strengthens the core claim.

## Weaknesses

- The architecture search space may encode much of the advantage.
- Needs sharper separation of multi-agent benefit from more calls, routing, sampling, or prompt optimization.
- Benchmarks may not capture messy long-horizon deployed workflows.
- Reproducibility hinges on natural-language optimization details.

## Questions for Authors

- How does MaAS compare against a budget-matched single-agent adaptive sampling/router baseline?
- Which operators are selected for easy vs hard queries, and are patterns stable across models?
- How sensitive is performance to the initial operator library and controller architecture?
- Does MaAS help on long-horizon tasks with persistent state and tool failures?

## Takeaway for Multi-Agent Literature

MaAS argues that the important unit is dynamic allocation of agentic structure, depth, and cost per query, not a binary single-agent vs multi-agent choice.

## Review: Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

## Verdict

A useful and fairly convincing account of why homogeneous agent scaling saturates, with a strong diversity/effective-channel framing but somewhat limited by static benchmarks and idealized theory.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Effective-channel framing and `K*` are real contributions; diversity itself is not new. |
| Significance | 4 | Directly relevant to agent-count scaling and heterogeneous team design. |
| Technical correctness and rigor | 3 | Good controlled diversity comparisons, but limited statistical treatment and idealized assumptions. |
| Empirical breadth and generality | 3 | Seven benchmarks and several models, but mostly small models and non-long-horizon tasks. |
| Multi-agent specificity | 4 | Clearly studies redundancy, heterogeneity, voting/debate, and agent-count scaling. |
| Reproducibility and transparency | 4 | Code/dataset link claimed; model/task/workflow details mostly clear. |
| Clarity and positioning | 4 | Clean framing with explicit limitations. |
| Practical usefulness | 4 | Actionable guidance: avoid homogeneous scaling; use diversity when it creates correct-path diversity. |

**Overall score:** 7
**Confidence:** 4

## Strengths

- Strong central thesis: scaling depends on non-redundant useful evidence, not raw agent count.
- `K*` is a useful label-free proxy for effective channels.
- Matched agent-call comparisons make the diverse-vs-homogeneous result meaningful.
- Separates model diversity, persona diversity, and combined diversity.
- Good connection between empirical saturation and theory.

## Weaknesses

- Main experiments are mostly static QA/reasoning benchmarks.
- Theory depends on strong independence/coverage assumptions.
- `K*` measures semantic diversity, not necessarily task-relevant information.
- Correct/incorrect channel decomposition requires labels.
- Limited evidence on frontier models and complex tool-use settings.

## Questions for Authors

- Does `K*` predict gains in long-horizon tool-use agents with state changes?
- How sensitive are results to prompt choice, decoding temperature, and persona wording?
- Would budget-matched single-agent self-consistency or best-of-N close the gap?
- Can `K*` be used online to stop adding agents or select agents adaptively?
- Which kinds of diversity increase correct-path diversity rather than just error diversity?

## Takeaway for Multi-Agent Literature

Treat diversity as a first-class MAS design variable. The useful abstraction is effective independent reasoning channels, not team size.

## Review: Effective Strategies for Asynchronous Software Engineering Agents

## Verdict

A practically important systems paper showing that branch-and-merge, worktree isolation, and centralized delegation can make multi-agent coding useful, though the evidence is less cleanly compute-controlled than CooperBench.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Git-worktree branch-and-merge is not conceptually new, but systematic agent architecture and ablations are useful. |
| Significance | 4 | Important positive counterpoint for long-horizon SWE agents. |
| Technical correctness and rigor | 3 | Good ablations and t-tests, but multi-agent uses more total iterations/cost. |
| Empirical breadth and generality | 4 | Two benchmarks, three models, isolation/parallelism analyses. |
| Multi-agent specificity | 4 | Gains tied to delegation, isolation, async execution, and merge integration. |
| Reproducibility and transparency | 4 | Uses OpenHands, reports versions/costs/prompts, and links code; runnable completeness not verified. |
| Clarity and positioning | 4 | Clear method and practical analysis. |
| Practical usefulness | 5 | Direct blueprint for building coding-agent teams. |

**Overall score:** 7
**Confidence:** 4

## Strengths

- Concrete recipe: manager, dependency graph, JSON delegation, worktrees, commits, merges, tests.
- Evaluates against OpenHands single-agent baselines across PaperBench and Commit0-Lite.
- Reports cost/runtime, not just accuracy.
- Isolation ablation is especially informative.
- Shows optimal agent count depends on task modularity and manager capacity.

## Weaknesses

- Multi-agent runs are more expensive and use more total iterations than single-agent baselines.
- Manager dependency graph/delegation is mostly prompt-driven and brittle.
- PaperBench uses Code-Dev plus LLM judging rather than full benchmark evaluation.
- Limited comparison to other multi-agent architectures.
- Some statistically significant gains are modest for stronger baselines.

## Questions for Authors

- What happens under equal dollar, token, or wall-clock budgets?
- How sensitive is CAID to manager model quality versus engineer model quality?
- Can learned or static dependency analysis outperform prompt-based decomposition?
- How often do merges fail, and what fraction of failures are delegation versus implementation?
- Does CAID still help on repos with poor tests or weak module boundaries?

## Takeaway for Multi-Agent Literature

CAID is the practical positive complement to CooperBench: multi-agent coding can work when coordination is externalized into software-engineering primitives.

## Review: LLMs Corrupt Your Documents When You Delegate

## Verdict

A strong benchmark paper showing that delegated long-horizon document editing accumulates sparse but severe corruption, though it is more relevant to agentic reliability than specifically multi-agent coordination.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Round-trip relay evaluation across many professional document domains is a clean contribution. |
| Significance | 5 | Directly challenges trust in delegated LLM editing and long-horizon artifact maintenance. |
| Technical correctness and rigor | 4 | Strong controls via reversible edits and domain metrics; construct validity remains the main risk. |
| Empirical breadth and generality | 5 | 52 domains, 310 environments, many frontier models, long-horizon sweeps. |
| Multi-agent specificity | 2 | Mostly single-agent/delegated editing; not multi-agent interaction. |
| Reproducibility and transparency | 3 | Source and tables present; full tasks/prompts/eval scripts determine real reproducibility. |
| Clarity and positioning | 4 | Clear framing and interpretable failure taxonomy. |
| Practical usefulness | 5 | Highly actionable warning for editing agents, workflow design, and evaluation. |

**Overall score:** 7
**Confidence:** 4

## Strengths

- Excellent long-horizon evaluation design.
- Broad domain coverage exposes a jagged capability frontier.
- Shows short-horizon success does not predict long-horizon preservation.
- Useful failure-mode analysis around sparse critical failures.
- Practical comparison of direct editing vs basic tool-using workflows.

## Weaknesses

- Not really a multi-agent paper.
- Round-trip reversibility may not fully capture real delegated editing.
- Agentic tool-use harness seems basic, so tools-hurt claims should not be overgeneralized.
- Domain-specific metrics may encode uneven tolerance for important changes.
- Readiness thresholds may be arbitrary without user/task-level validation.

## Questions for Authors

- How often do models exploit or misunderstand the inverse-edit structure?
- Are corruption scores calibrated against human judgments of document utility?
- Would stronger editing harnesses with diff planning, validation, or tests reduce failures?
- How sensitive are results to distractor length, edit ordering, and document size?
- Can critical failures be predicted before committing edits?

## Takeaway for Multi-Agent Literature

This is a key reliability benchmark for any multi-agent system that passes shared artifacts between agents: long workflows should be evaluated for preservation and compounding corruption, not just final success.

## Review: MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

## Verdict

MemMA offers a useful multi-agent architecture for long-horizon memory management, with promising evidence that coordinated planning, retrieval diagnosis, and repair improve conversational memory, but the evaluation is narrower and less mature than a top-tier systems paper.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Full memory-cycle framing plus probe-and-repair loop is meaningful. |
| Significance | 4 | Memory construction, retrieval, and repair are central problems for long-running agents. |
| Technical correctness and rigor | 3 | Ablations are helpful, but judge/probe reliability, compute matching, and baselines remain concerns. |
| Empirical breadth and generality | 3 | Several memory backends, mainly LoCoMo-style conversational memory. |
| Multi-agent specificity | 4 | Role specialization maps cleanly to memory-cycle functions. |
| Reproducibility and transparency | 3 | Probe generation, repair criteria, prompts, and evaluation details are critical. |
| Clarity and positioning | 4 | Clear diagnosis of strategic blindness and delayed supervision. |
| Practical usefulness | 4 | Actionable memory design pattern: plan, retrieve, test, repair, commit. |

**Overall score:** 7
**Confidence:** 3

## Strengths

- Strong conceptual framing of memory as a cycle.
- Specialized roles align with concrete memory operations.
- Large gains on multi-hop questions target a real failure mode.
- Backend-agnostic improvements are encouraging.
- Probe-and-repair loop is practically useful for persistent agents.

## Weaknesses

- Evidence is concentrated on one main benchmark family.
- Gains may partly reflect additional inference budget.
- Synthetic probe QA quality and evaluator reliability are potential failure points.
- Fixed role architecture may be less robust than adaptive designs.
- Long-term effects of repeated self-repair are unclear.

## Questions for Authors

- What are the token, latency, and dollar costs relative to backend-only baselines?
- How reliable are synthetic probes, and how often do repairs introduce false memories?
- Does MemMA improve non-conversational memory tasks or tool-using agents with persistent state?
- Can the system detect when iterative retrieval should stop before drift begins?
- How does a strong single-agent memory manager with the same budget compare?

## Takeaway for Multi-Agent Literature

MemMA supports the view that multi-agent value is strongest when roles correspond to separable lifecycle functions, especially diagnosis, retrieval refinement, and repair.

## Review: SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks

## Verdict

A useful and convincing coding-agent benchmark showing that pass rates hide accumulating maintainability debt, though its contribution is single-agent trajectory evaluation rather than multi-agent behavior.

## Scores

| Criterion | Score | Notes |
|---|---:|---|
| Novelty | 4 | Carried-workspace iterative benchmark plus trajectory-level quality metrics is a clear contribution. |
| Significance | 4 | Important for coding agents and long-horizon software maintenance. |
| Technical correctness and rigor | 4 | Good benchmark protocol, hidden tests, cost/time reporting, prompt intervention tests. |
| Empirical breadth and generality | 3 | 20 problems, 93 checkpoints, 11 models; limited to Python and one main run per model. |
| Multi-agent specificity | 2 | Relevant to multi-agent coding pipelines, but no agent-agent interaction is isolated. |
| Reproducibility and transparency | 3 | Protocol and metrics are given; full task/eval artifacts determine reproducibility. |
| Clarity and positioning | 4 | Clear setup, metrics, and contrast with pass-rate benchmarks. |
| Practical usefulness | 5 | Directly useful for designing coding-agent evals and guardrails. |

**Overall score:** 6
**Confidence:** 4

## Strengths

- Separates passing tests now from remaining extensible later.
- Carried workspace captures compounding effects of early architecture choices.
- Quality metrics are explicit and calibrated against maintained human repositories.
- Reports cost/time and shows quality prompts improve intercepts but not degradation slopes.
- Hidden black-box tests reduce overfitting.

## Weaknesses

- Not multi-agent-specific; implications are inferred.
- Python-only experiments limit the language-agnostic claim.
- Static quality metrics are useful proxies but not direct maintenance-cost measurements.
- One main run per model/harness leaves stochasticity partly unresolved.
- Human repo comparison is not matched to human solutions on the same tasks.

## Questions for Authors

- Do human developers solving the same checkpoint tasks show similar or flatter trajectories?
- How robust are erosion/verbosity metrics across languages beyond Python?
- Would refactoring-specific agents or review agents reduce degradation?
- How much failure comes from missing architecture planning versus weak regression repair?
- Are there task features that predict when degradation becomes irreversible?

## Takeaway for Multi-Agent Literature

Use this as evidence that multi-agent coding workflows need trajectory-level artifact quality checks; handoffs between agents may amplify code degradation unless architecture, regression, and refactoring are explicitly evaluated.
