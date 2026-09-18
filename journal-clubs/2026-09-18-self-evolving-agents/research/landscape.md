# Research landscape: self-evolving agents

**Cutoff: September 16, 2026.** This topic map supports a 45-minute, technically literate journal club. It organizes evidence and open questions rather than prescribing a final thesis. Start with the [ranked shortlist](shortlist.md); consult [source records](sources.md) and linked notes for exact versions and access depth. This revision supersedes earlier numerical/access qualifications where the new primary-source audit resolves them.

## Current analysis structure — September 18, 2026

The [revised thesis](../analysis/thesis.md) selects developed examples to explain when experience creates future-task value. It separates relevance/retention from feedback quality and treats learned improvement methods as a further achievement. Its conditional explanation—missing starting expertise plus recurring opportunities for relevant reuse—remains analyst synthesis, with competing explanations and discriminating tests in C011/C012. The [coverage audit](thesis-coverage.md) now records 26 directly cited families out of the unchanged 64 reviewed families, including explicit reasons for the sources moved to supporting evidence. The detailed topic map below remains research breadth, not a required essay structure.

## Scholarly foundations — September 18 analysis revision

The [thesis introduction](../analysis/thesis.md#turning-completed-work-into-future-capability) now situates experience-driven agents within continual/lifelong learning and distinguishes meta-learning from improver-code editing. Four [bounded foundation reviews](thesis-coverage.md#scholarly-foundations-revision--september-18-2026) explain learned bias, parameter protection, episodic gradient constraints, transfer metrics and learned initialization. These concepts make the later questions more precise: distinguish failed forward transfer, loss of earlier ability under fixed conditions, and changes to the environment. Existing 2023–2026 empirical evidence and the frontier cutoff are unchanged.

## Thesis-driven coverage revision — September 16

The [coverage audit](thesis-coverage.md) separates 153 discovery records, 56 reviewed families used in the thesis, and ten reading priorities. This pass restores earlier mechanisms and evaluates counterexamples instead of searching only for confirmation of the existing argument.

[ExpeL](notes/2023-expel.md) establishes cross-task insight/retrieval in 2023; [ADAS](notes/2024-automated-design-agentic-systems.md) and [AFlow](notes/2024-aflow.md) establish fixed-meta-agent workflow search. [ReasoningBank](notes/2025-reasoningbank.md) makes memory and extra test-time compute complementary, so they should not always be framed as rival explanations. [MemSkill](notes/2026-memskill.md) adds evolving memory operations, with fixed designer/executor and preparation-cost limits.

[SkillsBench v4](notes/2026-skillsbench.md) strengthens the static-procedure comparison: curated skills help in aggregate, while self-generation underperforms in three configurations. Task filtering, human curation, executable resources and one-shot design limit that inference. [Continual experience internalization](notes/2026-rethink-continual-internalization.md) supplies both deterioration and a successful bounded three-update recipe; the positive result prevents reducing the field to collapse examples.

The central interpretation remains conditional future-task value. It is now grounded in broader positive and negative evidence, with clearer distinctions between artifact search, learning a fixed procedure, changing the update rule and sustained acceleration. The following topic map retains the earlier detailed questions and quantitative audits.

## 1. What persists, and who changes it?

For this session, an operational definition is: **an agent uses experience or feedback to change state that affects subsequent behavior**. This separates a successful task attempt from improvement across attempts or tasks. “Self” is a matter of which decisions the agent controls; it does not imply absence of human-designed objectives, pretrained knowledge, rewards, or infrastructure.

| Persistent object | How an update happens | Representative resources | What is still externally anchored? |
| --- | --- | --- | --- |
| Reflections, facts, episodic memory | Summarize, retrieve, revise, consolidate | [Reflexion](notes/2023-reflexion.md), [MemRL](notes/2026-memrl.md), [SelfMem](notes/2026-selfmem.md), [NemoClaw](notes/2026-nemoclaw-memory.md) | Base weights, retrieval architecture, reward or evaluator, usually memory budgets |
| Reusable skills and procedural knowledge | Compile experience into code/playbooks; accept, reuse, retire | [Voyager](notes/2023-voyager.md), [WikiSkill](notes/2026-wikiskill.md), [ACE](notes/2025-agentic-context-engineering.md), [Library Drift](notes/2026-library-drift.md) | Task/environment, validation criteria, often tool interfaces and model |
| Prompts, workflow, harness code | Reflective proposals, search, tests, selection | [GEPA](notes/2025-gepa.md), [HarnessDev](notes/2026-harnessdev.md), [DGM](notes/2025-darwin-godel-machine.md), [Evo-Harness](notes/2026-evo-harness.md) | Proposal model, compute envelope, evaluator; edit permissions differ |
| Model weights | Generate update data/instructions; apply gradients | [SEAL](notes/2025-self-adapting-language-models.md), [TTRL](notes/2025-test-time-reinforcement-learning.md), [Shopify](notes/2026-shopify-sidekick.md) | Optimizer/training stack, reward, data access, deployment gates |
| Curriculum and task distribution | Generate questions/programs; judge difficulty/correctness; train | [R-Zero](notes/2025-r-zero.md), [Absolute Zero](notes/2025-absolute-zero.md), [Agent-World](notes/2026-agent-world.md) | Pretraining, filtering/rewards, executable environment or pseudo-label rule |
| Improvement strategy itself | Rewrite the improver, co-evolve optimizers, replay search histories | [STOP](notes/2023-stop.md), [Hyperagents](notes/2026-hyperagents.md), [Escher-Loop](notes/2026-escher-loop.md), [Dream-RSI](notes/2026-dream-rsi.md) | Outer selection, feedback/evaluation, resource limits, often frozen foundation model |

Agent-World makes the environment/curriculum branch explicit: it mines executable environments and targets RL data at observed failures. Its external benchmark breadth is valuable, but generated data and compute are not matched across scaling conditions. World Knowledge Exploration trains a policy to create website guidebooks; deployment adaptation is external Markdown, not a weight update. [Agent-World audit](notes/2026-agent-world.md); [world-knowledge audit](notes/2026-spontaneous-world-knowledge.md).

These are overlapping surfaces, not mutually exclusive product categories. SIA, MetaRSI, ScienceBuddy, and Shopify combine surfaces. A model that edits a prompt is doing useful optimization without necessarily improving its underlying weights; a learned update program can change weights without choosing its own evaluator.

The practical loop to inspect is **experience → feedback → proposed update → validation/selection → retained state → later task**. For every arrow, ask which information is visible, who designed the rule, and where costs accrue. The proposed “self-evolution” label alone answers none of those questions.

## 2. Does improvement generalize beyond the selection process?

The most important comparison is often the same agent with one component changed. WikiSkill compares representations with held-out splits; FinEvo pairs persistent and reset state under the same backbone and stream; the harness-evaluation critique asks whether a five-rollout budget is better spent sampling task solutions. These controls answer different causal questions and should not be combined into one leaderboard. [WikiSkill, Table 1/Appendix B](https://arxiv.org/html/2608.27454v1); [FinEvo, §4.1](https://arxiv.org/html/2608.06144v1); [harness critique, main comparisons](https://arxiv.org/html/2607.12227v2).

**Three distinctions prevent common overclaims:**

- A validation improvement is not a held-out gain. HarnessDev's **34/64** measures directional agreement of adjacent feedback and held-out changes; it is not a count of successful generalization events. [Note](notes/2026-harnessdev.md).
- Repeated attempts on the same problems do not create new independent test items. SEAL's ARC result has eight selected test tasks; GEPA and VISTA repeat 30 AIME questions five times. [SEAL](notes/2025-self-adapting-language-models.md), [GEPA](notes/2025-gepa.md), [VISTA](notes/2026-reflection-in-the-dark.md).
- Re-running a chosen candidate on the same task set addresses stochastic selection noise but does not test transfer to new tasks. Reef's **22/60 vs 21/60** fresh comparison is explicitly in this category. [Reef primary results and audit](notes/2026-reef.md).

**Discussion:** What is the appropriate held-out unit—question, user, repository, task family, environment version, or time period? Which of these sources would still count as improving if the benchmark were retired tomorrow?

## 3. Does retained experience remain useful?

A durable store can accumulate useful procedures and harmful assumptions simultaneously. WikiSkill gives a controlled positive example: Qwen-3.5-9B improves **29.9→47.4** in macro accuracy, while a smaller model regresses on OfficeQA. Library Drift shows that retirement policy can reverse gains, but on a selected 40-task MBPP evaluation set with unequal call budgets. These findings motivate lifecycle management; they do not establish one universally optimal memory format. [WikiSkill, Table 1](https://arxiv.org/html/2608.27454v1); [Library Drift audit](notes/2026-library-drift.md).

AgentStream makes task order and mixing explicit. Across three order seeds, three models, and five methods, the audited isolated/sequential/interleaved mean differences from each model’s vanilla macro average are **+1.37/+0.75/+0.90 percentage points**. Interleaved streams have **28 positive and 17 negative** model–method–seed cells. These cells share tasks; percentages are descriptive, not an independent-binomial success probability. The reported variability is reproduced as the sample SD of three seed-level means. [Tables 2 and 11–13; audit](notes/2026-agentstream.md).

External change is a separate problem: EvoHarnessBench expands tool/API catalogs across 17 streams. An agent can retain an accurate old skill yet fail after its interface changes. The benchmark's **802 unique tasks** differ from **1,510 axis-level examples**, and its ± values are population SDs over three runs. [Benchmark note](notes/2026-evoharnessbench.md).

The weight-space counterpart is forgetting. SEAL explicitly evaluates loss of prior knowledge after later updates. R-Zero's autonomous curriculum improves early and deteriorates later; declining pseudo-label accuracy is a candidate explanation, not a causal decomposition. Its appendix also shows different model sizes deteriorating at different noise levels. [SEAL forgetting tests](notes/2025-self-adapting-language-models.md); [R-Zero, Appendix D–E](notes/2025-r-zero.md).

**Discussion:** Should a rejected skill's supporting memory survive? Who decides what to delete? Should evaluation reward peak accuracy, terminal accuracy, area under the learning curve, or recovery after regressions?

## 4. Can feedback be trusted?

“Verifiable” can mean an executable test, a reference answer, a model's majority vote, or a rubric judge. These signals have different failure modes. R-Zero uses majority-generated pseudo-labels; Absolute Zero uses execution-based self-play. FinEvo calibrates its automated rubric scoring against one financial expert on 120 outputs, but the same rubric ecosystem also supplies learning feedback. That provides a useful control without proving robustness to a new evaluator. [R-Zero](notes/2025-r-zero.md), [Absolute Zero](notes/2025-absolute-zero.md), [FinEvo §4.2](notes/2026-finevo-bench.md).

STOP's reward-hacking example exploited an evaluator shape bug, producing an apparent score above 1000%. RewardHackingAgents and RHB focus directly on evaluation integrity; Self-Evolution Backfires separates repeated optimization on a public benchmark from fresh evaluation. These are reasons to isolate evaluators and audit selection, not grounds to assume every reported improvement is gaming. [STOP §6](notes/2023-stop.md), [evaluation-integrity notes](notes/2026-reward-hacking-agents.md), [Backfires](notes/2026-self-evolution-backfires.md).

VISTA is another useful challenge: a defective starting prompt can trap reflective optimization. Its recovery relies heavily on hand-designed failure hypotheses, and experiments use one optimization seed. It demonstrates a failure case and an intervention under those conditions, not the typical failure rate of GEPA. [VISTA Tables 1–3](notes/2026-reflection-in-the-dark.md).

**Discussion:** If the agent can edit its own improvement code, which evaluator, budget, and audit boundaries should remain immutable? What independent signal would convince us an apparent gain is real?

## 5. Is a better agent worth the adaptation cost?

GEPA's rollout efficiency does not establish total compute efficiency. Reflection, validation, data generation, inner training, and future inference must all be counted. AgentStream supplies a concrete warning: its GPT-5.4/A-Mem cost table reports **$0.297→$1.893 per task**, while action counts fall. The cost table and aggregate accuracy table use different aggregation scopes; do not attach their numbers to one synthetic “paired experiment.” [GEPA](notes/2025-gepa.md); [AgentStream Table 7 audit](notes/2026-agentstream.md).

HGM improves resource accounting by matching evaluation counts and reporting allocated CPU-hours, which still differ from dollars or end-to-end energy. Dream-RSI reduces discovery calls in within-model comparisons but omits a complete cost ledger for replay construction and meta-optimization. FinEvo counts agent execution/reflection tokens and excludes its rubric judge. [HGM](notes/2025-huxley-godel-machine.md), [Dream-RSI](notes/2026-dream-rsi.md), [FinEvo](notes/2026-finevo-bench.md).

The practitioner sources add operational constraints. Shopify describes trajectory repair, daily training, serving, and prompt compression; Reef exposes delayed-feedback attribution and versioned candidates; NemoClaw publishes small evaluation artifacts and category-level regressions. Company reports and inspectable code are useful evidence of design choices. Neither serving savings nor a runnable repository alone isolates learning efficacy. [Shopify](notes/2026-shopify-sidekick.md), [Reef](notes/2026-reef.md), [NemoClaw](notes/2026-nemoclaw-memory.md).

**Discussion:** Over how many future tasks must an update amortize? What happens if better performance requires an ever-growing prompt or skill library? Which costs belong in the comparison?

## 6. Is the improvement process improving?

STOP, Hyperagents, Escher-Loop, and Dream-RSI provide concrete ways to modify an improver. They are more informative than treating every prompt update as equivalent recursion. Their anchors remain important: fixed evaluators, fixed base models in several systems, small task sets, and constrained outer loops. Hyperagents reports five-run experiments, but its mathematical transfer endpoint **0.640 vs 0.610 is not significant**. Escher-Loop matches a 10M equivalent-token budget yet reuses three geometry instances. Dream-RSI's replay guarantee is relative to a finite recorded history; unseen search branches are not evaluated by that guarantee. [Linked methods and audits above](#1-what-persists-and-who-changes-it).

September frontier sources expand the design space but do not close the evidence gaps. ScienceBuddy combines harness and weight updates; its maintained 715/90/90 split has explicitly overlapping source-material groups and differs from the paper's schedule. MetaRSI describes accounting conventions, but actual per-variant budget/split ledgers were not located. Their claims remain provisional pending those artifacts. [ScienceBuddy](notes/2026-sciencebuddy.md), [MetaRSI](notes/2026-metarsi.md).

The Economics of Recursive Self-Improvement asks a different, theoretical question: when do interacting feedback elasticities exceed the threshold for sustained acceleration? Its key research-productivity elasticity is poorly measured and its calibration is illustrative. It helps distinguish a finite gain on a verifiable task from economy-wide acceleration; it does not estimate the probability that a particular agent will recursively improve. [Theory note](notes/2026-economics-rsi.md).

**Discussion:** What experiment would distinguish better search over a fixed space from a growing ability to discover new improvement methods? Would the conclusion survive a new domain, fixed lifetime budget, and an independent evaluator?

## Handoff boundaries

The corpus supports a topic-wide session with positive mechanisms, meaningful controls, regressions, practitioner systems, and a clearly labeled September frontier. It does not supply an independent reproduction or establish open-ended, domain-general recursive acceleration. Multi-agent topology search, embodied systems, and long-horizon organizational deployment are covered more lightly than coding, memory, and reasoning. The register preserves those leads for a focused follow-up if the session emphasis changes.

Primary papers and first-party code/results were read to the depth recorded in each note. Several source PDFs were rendered to verify tables. No videos were watched, no training experiments reproduced, and inaccessible social posts were not used as factual evidence. [Workflow and remaining questions](../workflow.md).

## Citation-mining refinement — September 16

The [citation audit](citation-mining.md) fills two comparison gaps. WikiSkill explicitly contrasts its separate knowledge store with EvoSkill’s proposal history, Trace2Skill’s consolidated lessons, and SkillOpt’s rejected-edit/meta guidance (§1 and §6); all three now have primary reading notes. These are competing ways to preserve experience, not evidence that a separate wiki is universally necessary. The [Trace2Skill note](notes/2026-trace2skill.md) includes a negative math-transfer cell; the [EvoSkill note](notes/2026-evoskill.md) preserves its table/prose inconsistency.

For meta-improvement, [EvoX](notes/2026-evox.md) adapts search strategies online, while [MLEvolve](notes/2026-mlevolve.md) combines cross-branch information and retrospective memory. Compare these with Dream-RSI’s replay controller rather than treating all three as the same recursion mechanism. Iteration/runtime budgets still differ from complete cost matching. Newly indexed embodied and harness-development comparators remain limited-depth leads, so the corresponding empirical coverage gaps are narrowed in discovery but not yet resolved by reading.

## Prominent-citation handoff — September 16

The [per-paper citation map](prominent-citations.md) now makes predecessor and baseline coverage inspectable across the reviewed papers. The [revised thesis](../analysis/thesis.md) explains the Reflexion/ExpeL/Voyager distinction, WikiSkill’s actual comparison set, ACE’s relation to stream interference, DGM’s fixed instruction-generation boundary before Hyperagents, and AlphaEvolve/EvoX before Dream-RSI. The [coverage audit](thesis-coverage.md) gives specific reasons for keeping other reviewed works in supporting records. Counts of citing papers are not independent confirmations; inherited lineages and shared evaluation settings remain important.
