# Self-evolving agents: research landscape

Prepared September 16, 2026. This updates the [initial topic map](../research-notes.md) for the September 18 journal club. Audience and format remain the session's existing assumption: LLM-literate participants, 45 minutes including discussion. Source details and access depths are in the [register](sources.md).

## What counts as evolution?

Use a working operational definition: **experience changes retained state that affects later behavior**. Always name the state, feedback, update rule, acceptance test, and fixed infrastructure. Distinguish improving an output, improving an agent, and improving the process that generates agent changes. These are discussion categories, not an agreed universal hierarchy.

| Editable state | What it buys | Main tradeoff / evaluation question | Examples |
| --- | --- | --- | --- |
| Prompt or contextual procedure | Cheap, inspectable behavioral changes | Extra context, brittle instructions; does it transfer? | AgentStream, GEPA background |
| Memory or skills | Reuse lessons across tasks | Retrieval, stale guidance, conflicts, retirement | WikiSkill, Library Drift, Hermes |
| Harness code and tools | Change execution, recovery, and control flow | Noisy program search, overfitting, model dependence | HarnessDev, harness-evaluation study |
| Data and model parameters | Internalize learning beyond injected text | Training cost, contamination, forgetting | MetaRSI, ScienceBuddy; SEAL background |
| Improvement procedure | Change how future modifications are generated | Hard to distinguish better search from more search | Hyperagents |
| Serving and release infrastructure | Connect real experience to accepted updates | Delayed feedback, version attribution, rollback | Reef |

The table is our synthesis of the linked sources. These mechanisms overlap; “self-evolving” does not necessarily imply a genetic algorithm or model-weight updates.

## Does accumulated experience become useful knowledge?

WikiSkill provides a useful positive example because the knowledge representation, skill edits, validation gate, and test splits are inspectable. Its design also leaves a practical gap: full skill injection excludes retrieval failures. Library Drift studies routing and lifecycle management, including harm from overly aggressive retirement. These studies address different bottlenecks and use different models, tasks, and budgets; their scores should not share a leaderboard. See [WikiSkill methods and appendix notes](notes/wikiskill.md) and [Library Drift protocol and ablations](notes/library-drift.md).

Pair these experiments with the [Hermes and LangChain implementation descriptions](../practitioner-sources.md). Documentation establishes how a system stores or updates procedures; a controlled comparison is still needed to determine whether those changes help. The NVIDIA memory example in that register adds a concrete instance of aggregate gains coexisting with a smaller-category regression.

**Question to resolve:** Is the bottleneck extracting a good lesson, deciding when it applies, or retiring it when circumstances change? A useful experiment varies these independently and measures future-task accuracy, regressions, retrieval cost, and storage growth.

## Does evolution beat another use of the same budget?

The harness-evaluation study supplies direct competing uses of additional rollouts and a separate held-out test. HarnessDev independently examines feedback-based selection and subsequent generalization across runtime models. Together they motivate stronger controls, but neither proves that harness evolution is generally ineffective. Their evidence concerns particular tasks, implementations, budgets, and selection procedures. See [budget and transfer comparison](notes/harness-evolution-evaluation.md) and [HarnessDev](notes/harnessdev.md).

The important denominator is future useful work. Offline optimization may be worthwhile when its cost is amortized across many later tasks, even if it loses on a single five-attempt comparison. Conversely, a better final score may be unattractive if it incurs much more search or inference cost. Record proposal, validation, unsuccessful experiments, deployment, and rollback costs separately.

**Question to resolve:** What is the cost per additional correctly completed future task, and how long does the gain persist?

## What happens when deployment changes?

AgentStream varies task order and domain mixing. EvoHarnessBench varies the externally supplied tools, skills, and specialist agents. These are complementary sources of change, and neither should be collapsed into a single “continual learning” score. Gains differ by model and environment; some configurations regress. Read [AgentStream](notes/agentstream.md) beside [EvoHarnessBench](notes/evoharnessbench.md).

Measure old-task retention, new-task acquisition, task-order sensitivity, version compatibility, and forward transfer. Use the same tasks and resource accounting for meaningful comparisons, while ensuring that final tests do not feed adaptation. Repeated measurements on one stream do not become independent trials merely because there are many steps.

**Question to resolve:** Can a system distinguish obsolete memory from a newly confusing tool interface?

## Can the agent improve its own learning process?

Hyperagents makes meta-agent code editable and tests transferred improvement strategies. Its cross-run evidence is more qualified than an “unbounded improvement” interpretation: the notes identify a nonsignificant endpoint comparison, limited iterations, and fixed outer infrastructure. This remains informative evidence about a narrower question. See [Hyperagents](notes/hyperagents.md), especially Figures 3–4.

MetaRSI and ScienceBuddy explore complementary update surfaces. MetaRSI compares scheduled composition with individual operators and fixed composition under stated budget controls. ScienceBuddy alternates harness learning and model learning; its auxiliary reflector remains fixed, and its controlled experimental feedback should be distinguished from researcher interaction examples. See [MetaRSI](notes/metarsi.md) and [ScienceBuddy](notes/sciencebuddy.md).

**Question to resolve:** What would distinguish an improved modification policy from warm-starting with a stronger task agent? Freeze the task initialization, expose candidate improvers to unseen domains, equalize total budgets, and measure the quality and cost of descendants over repeated runs.

## What is new as of this preparation date?

| Candidate trend | Observations across time | Alternative explanation / confidence limit |
| --- | --- | --- |
| Evaluation expands beyond initial-versus-final scores | July harness-budget critique; July AgentStream; September HarnessDev and EvoHarnessBench | More benchmarks need not mean more independent replication; task and model changes prevent a simple progress curve |
| Persistent state needs management, not just accumulation | May Library Drift; June memory engineering guidance; August WikiSkill; September Reef | Different artifacts solve different problems; not evidence that one memory design universally wins |
| Harness and weight updates are increasingly combined | September MetaRSI and September 15 ScienceBuddy | New designs and limited experiments, not established long-term compounding; stronger helpers and added compute can explain gains |
| Research loops produce reusable infrastructure | March autoresearch; September Reef and SoL-Pi | Code releases show implementation activity, not controlled population-level performance improvements |

These are candidate interpretations supported by distinct project families in the [source register](sources.md), not a settled thesis or a claim of exhaustive historical coverage. The newest verified primary additions are ScienceBuddy and Reef on September 15; the ScienceBuddy lab announcement is September 16. SoL-Pi's inspected commit is September 15, but its original release date is unverified.

## Suggested discussion and evidence choices

Retain the topic-wide format. Use WikiSkill to explain retained knowledge; pair it with Library Drift and practitioner skill systems. Use the harness-budget critique and HarnessDev for evaluation, AgentStream for changing task distributions, and Hyperagents for the stronger meta-improvement question. Give the September composition work a brief, explicitly provisional frontier segment.

Useful figures to inspect for a later presentation: WikiSkill Figure 2 and Table 6; HarnessDev Figure 8 and Table 6; Hyperagents Figures 3–4; ScienceBuddy Figures 8–10. Redraw mechanisms with attribution; do not compare unlike score scales or treat pass@4 as single-attempt accuracy.

Discussion prompts:

1. Which retained changes deserve to be called learning?
2. When should the system modify memory, code, or weights?
3. Should failed edits still leave durable knowledge?
4. Who evaluates the evaluator, and which parts must stay fixed for a credible experiment?
5. Would a more expensive agent with fewer regressions be preferable to a cheaper one with higher average accuracy?
6. What finite experiment would change your belief about recursive improvement?

## Coverage and handoff

Ready for analysis: mechanism map, twelve detailed source notes, positive and negative findings, current practitioner releases, dates, and explicit qualifications. No single thesis has been forced. No slides or experiments were produced.

Remaining limits: selected-section rather than exhaustive paper review; incomplete financial/embodied-domain coverage; scarce independent replication; failed direct X access; no talk/video viewing; unreviewed recipe-level logs. Some uncertainty definitions and evaluation denominators remain unresolved and are marked in the notes. The [work queue](../workflow.md) identifies follow-ups needed only if those quantitative claims are selected for presentation.
