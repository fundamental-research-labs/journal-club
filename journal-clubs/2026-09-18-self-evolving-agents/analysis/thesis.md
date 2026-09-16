# Self-evolving agents: what is actually improving?

Prepared September 16, 2026 for September 18. Topic-wide analysis for an audience familiar with LLM basics; 45 minutes including discussion. [Claim ledger](claims.md) · [Presentation storyline](storyline.md) · [Research landscape](../research/landscape.md).

## Central thesis

**Self-evolving agents are becoming systems that turn experience into reusable changes. The convincing progress is in particular learning loops; whether those loops produce durable, economical gains depends on how changes are evaluated, retained, and reused. Sustained, general recursive improvement remains an open question.**

This is an analyst synthesis, with moderate confidence, of the reviewed corpus through September 16—not a claim that every approach works or that general recursive improvement is impossible. The practical consequence is to judge an agent by what its experience improves on later tasks, including regressions and costs. Counting self-edits or showing the best checkpoint is insufficient. [C011](claims.md#c011).

## The trend: more of the learning loop becomes editable

The dated evidence shows a widening design space and stronger evaluation questions. These are overlapping research directions, not a clean succession in which each generation replaces the last. In particular, improving the improver already appeared in STOP in 2023. This chronology establishes changes in published mechanisms; it does not measure industry adoption or a rate of capability growth. [C001–C002](claims.md#c002).

| Observation | What changes | Why it matters |
| --- | --- | --- |
| March–October 2023: Reflexion, Voyager, STOP | Verbal memories, executable skills, and even improver code | Persistent experience and meta-improvement both have early precedents. Repeated-task recovery and transfer are distinct endpoints. |
| June–August 2025: SEAL, GEPA, R-Zero | Weight-update data/instructions, prompts, and generated curricula | Agents increasingly participate in deciding how to learn, alongside deciding what action to take. |
| March–September 2026: Hyperagents and Dream-RSI | Task/meta-agent code and exploration policies | The improvement procedure itself becomes an explicit optimization target. Transfer of that procedure needs its own test. |
| July–September 2026: harness-evaluation critique, AgentStream, FinEvo, HarnessDev | Evaluation now probes alternative uses of compute, task streams, persistence controls, and version selection | “Did the score rise?” becomes “Did retained learning help later tasks, against a credible alternative?” |
| August 5, 2026: Shopify Sidekick account | Harness search, repaired trajectories, weight training, and serving compression in one production pipeline | Practitioner work shows how multiple mechanisms can be integrated, while public causal evidence remains limited. |

Dates are first-publication dates from the [source register](../research/sources.md); reviewed revisions can be later. GEPA and R-Zero are ICLR 2026 papers; SEAL is NeurIPS 2025. Most of the named 2026 empirical frontier sources are preprints. Shopify is a first-party engineering account. [C002](claims.md#c002), [C010](claims.md#c010).

## The argument

**1. Persistent improvement is real in bounded settings.** WikiSkill's Qwen-3.5-9B macro accuracy rises from 29.9 to 47.4 across five benchmarks with held-out splits. SEAL's learned self-edit data produces 47.0% single-passage knowledge-incorporation accuracy, versus 39.7% for untrained self-generated data. These exemplify two different places learning can live: external skills and model weights. Their metrics cannot be pooled. [WikiSkill Table 1](https://arxiv.org/abs/2608.27454v1), [SEAL Table 2](https://arxiv.org/abs/2506.10943v2); [C003–C004](claims.md#c003).

FinEvo supplies a particularly useful persistence control: four scaffolds, all using the same backbone, retain or reset state across paired streams of 120 tasks. Retention raises mean rubric scores by 9.33–19.37 points. This supports learning recurring professional procedures under that feedback regime. It does not establish equivalent gains on unfamiliar workflows. [FinEvo §§4.1–4.3, Table 3](https://arxiv.org/html/2608.06144v1); [C005](claims.md#c005).

**2. A better score does not identify what improved.** The harness critique finds parallel sampling outperforming harness evolution under a five-rollout budget; its separate held-out experiment reports 68.3 versus 67.7 for evolved versus initial harnesses. More attempts, task specialization, and candidate selection are credible explanations for some apparent evolution gains. This is a counterexample to a broad claim, not a verdict against all harness learning. [Tables 1–3](https://arxiv.org/abs/2607.12227v2); [C006](claims.md#c006).

**3. Retention creates a maintenance problem.** AgentStream finds both gains and regressions when tasks are mixed, with an interleaved mean gain of 0.90 percentage points across its tested configurations. R-Zero's Appendix Table 6 shows performance declining after an earlier peak. Useful experience can become irrelevant, interfere with other tasks, or support poor updates. The studies establish failures under their protocols; they do not isolate one universal cause. [AgentStream Table 2](https://arxiv.org/html/2608.00155v1), [R-Zero Appendix D–E](https://arxiv.org/abs/2508.05004v4); [C007–C008](claims.md#c007).

**4. Improving the improver is a meaningful frontier, with a higher burden of proof.** Hyperagents and Dream-RSI explicitly change improvement strategies. That is more direct evidence about meta-improvement than a growing skill library. Yet finite search gains, downstream artifact transfer, and general improvement of the search procedure are different claims. Dream-RSI's replay guarantee applies to recorded history; Hyperagents' cited transferred-versus-fresh math endpoint is nonsignificant. [Hyperagents §5](https://arxiv.org/abs/2603.19461v1), [Dream-RSI §§3–4](https://arxiv.org/html/2609.14858v1); [C009](claims.md#c009).

## What is established, emerging, and interpretive?

- **Established within the reported experiments:** retained state and learned updates can help; some task/model conditions regress; more update rounds need not improve the terminal score. These are reported results, without independent reproduction here. C003–C008.
- **Emerging direction:** richer editable components, integrated production learning pipelines, and evaluations that follow changes over time. Evidence supports the existence of this direction, not its prevalence or eventual success. C002, C009–C010.
- **Our interpretation:** the useful unit of progress is a retained change whose later benefit survives an appropriate control. Evaluation quality, retention, and cost deserve equal attention to proposal generation. The corpus does not establish that evaluation is the single dominant bottleneck. C011–C012.

## Competing theses and the strongest objection

| Candidate thesis | Best supporting evidence | Why adopt or reject it? |
| --- | --- | --- |
| “We have entered sustained recursive acceleration.” | Explicit improver editing and controlled discovery gains | Too strong: finite runs, fixed outer objectives, limited transfer and cost accounting do not establish sustained acceleration. Retain as a hypothesis. C009. |
| “Self-evolution gains are mostly extra compute and task specialization.” | Harness sampling control; small mixed-stream gains; strong fixed expert skill in FinEvo | Serious alternative. It explains part of the evidence, but does not erase matched persistence effects or learned-update comparisons. “Mostly” cannot be estimated from this selected corpus. C004–C007. |
| **“Useful learning loops are emerging; durability and value must be demonstrated.”** | Positive controlled cases coexist with failures and incomplete economics | Preferred: explains both sides without requiring either universal success or universal failure. C011. |

The strongest objection to our preferred view is that “learning-loop engineering” may simply rename established specialization and search. FinEvo's fixed expert skill scores 86.67, close to unrestricted evolution's 89.47, versus 71.58 with reset state. That comparison raises a practical question: how much does autonomous updating add over a good static procedure? [FinEvo Table 5](https://arxiv.org/html/2608.06144v1). Our thesis allows that the best choice may be static. Its distinctive empirical question is whether accumulated experience improves future work enough to justify the updating process. C005, C012.

## Practical position and discriminating experiment

For a system serving recurring work, start by comparing retained learning with both a strong static skill and a reset control. Keep the evaluator outside the editable agent, version accepted changes, and measure earlier-task regressions. These are engineering recommendations, not a universally validated optimal design. External state is easier to inspect and reverse; weight updates may support behavior beyond available context but add training cost and forgetting risk. The evidence does not select one carrier for all tasks. C003–C005, C008, C012.

The decisive next experiment would give four arms the same initial model, task stream, feedback access, and total resource envelope: a strong static procedure; reset state with extra inference; retained state with a fixed improver; and retained state with an evolving improver. Select updates on development data, then freeze and test on new task families, a later time period, and an independently designed evaluator. Report learning curves, terminal quality, old-task retention, failures, and all search/training/inference/judging costs across independent runs.

If retained state fails to beat the first two arms, specialization or extra inference explains the practical gains. If the evolving improver beats the fixed improver across new families at equal lifetime cost, that would strengthen the meta-improvement thesis. Sustained acceleration would additionally require evidence that improvement efficiency keeps increasing over successive cycles. These are proposed tests, not results. C011–C012.

## Discussion decisions

1. **Would you pay for an update loop over a static expert skill?** Use FinEvo Table 5 and the harness sampling control; specify the future workload over which costs must be recovered.
2. **What counts as transfer for your application: a new question, user, repository, task family, or month?** Use the gap between WikiSkill's held-out splits and AgentStream's mixed streams to choose the test unit.
3. **When should learning stop or roll back?** Use R-Zero's peak-to-terminal decline and SEAL's forgetting probe; choose the old-task regression you would tolerate.
4. **What would convince you the improver has improved?** Compare Hyperagents' transfer design with Dream-RSI's replay; require an outcome that extra task-specific search cannot explain.
5. **Which part of the loop should remain externally controlled?** Use Shopify's shared judge across stages; identify an independent signal that would detect a rubric blind spot.

## Scope and remaining uncertainty

This analysis reuses the completed September 16 research pass and source-specific reading depths; it is not a new systematic review. Exact result conditions, uncertainty, independence, and falsification criteria are in the claim ledger. Missing per-variant ledgers keep MetaRSI/ScienceBuddy headline claims outside the central argument. R-Zero's disputed main aggregates and GEPA's aggregate arithmetic are not used as decisive numbers. Production generalization, complete cost accounting, and independent reproductions remain gaps. These limit the thesis but do not prevent presenting the bounded argument.
