# Presentation storyboard

Revision: September 18, 2026 — review-driven revision 1. **24 main slides + 11 appendices**; approximately 30–35 minutes plus discussion, pending live rehearsal. Empirical cutoff remains September 16; foundation review and source-visual inspection September 18.

## Argument and visual direction

Keep the forest-green/ivory palette, serif titles, original paper artwork, offline assets, and confirmed presenter attribution. Open with an explicitly illustrative later-task example, then distinguish continual learning from meta-learning and state carriers from learned functions. The main question is answered by the conditional synthesis on slide 22. Each evidence section states the question that motivates it. The closing discussion follows that synthesis; no duplicate closing slide.

Use original tables for evidence, guided crops for dense mechanisms, and a new original retention heatmap. External reading guidance is author commentary and never alters the source pixels. Preserve the whole FinEvo result table, AgentStream method table, and Hyperagents test comparators. Distinguish gain metrics, endpoint metrics and partial token accounting visibly.

## Scope and concept → evidence audit

| Example / role | Concept and evidence slides | Inspected source / visual choice |
| --- | --- | --- |
| WikiSkill / retained knowledge | 6 → 7 | v1 §3/Figure 2 and Table 1; original framework and result excerpt |
| FinEvo / value of persistence and expertise | 8 → 9 | v1 Figure 1, §4.1, Tables 3/5; original landscape crop, visible paired-reset explanation, complete Table 5 |
| Harness critique / extra-attempt alternative | 10 → 11 | v2 Figure 2 and Table 1; original complete diagrams and table; no-test pass@1 visibly defined |
| AgentStream / relevance under task mixing | 13 → 14; aggregate details 26 | v1 Figure 1(b), §5.4, Tables 5/6; original framework and complete method-level Table 5 |
| SEAL / learned adaptation and retention | 15 → 16 → 17 | v2 §3/Figure 1, Table 2, §5/Figure 6 and B.6; original mechanism, all baselines, full retention heatmap |
| Sidekick / practical correction pipeline | 18 | First-party pipeline account; attributed text, reported design separated from our evaluation recommendation |
| Hyperagents / learned proposal behavior | 20 → 21; endpoint 25 | v1 §3/Figure 1, §5.2/Figure 3, §5.3/Figure 4; left/central mechanism crop, preserved test comparators; explicit gain/endpoint distinction |
| SkillsBench / curated baseline qualification | 30 | Existing scoped text explanation of curated/no-skill/one-shot conditions; no numerical result reconstruction |

Thrun, GEM, MAML and predecessor names supply conceptual context rather than new standalone empirical cases. The former compressed R-Zero/Continual Internalization and Dream-RSI slides are omitted to give the selected mechanisms adequate explanation. Their source notes, evidence, caveats and reading-list links remain in the research corpus. SEAL does not imply that every update recipe forgets: bounded positive internalization evidence remains explicitly noted. No claim of exhaustive C001–C021 slide coverage is made.

## Sequence and traceability

## 01 · Self-evolving agents

- Role: INTRODUCTION / introduction
- Purpose: Introduce the topic and practical promise.
- Visual: Large typographic cover; Codex Grid 01.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Work can be valuable twice: the completed task and expertise that helps later work. Ask when that retained expertise is worth obtaining and maintaining. Main talk follows useful skills, selective reuse and retention, then learned adaptation. Recursive acceleration is a further question, not the definition of useful learning. Research cutoff remains September 16; foundation readings and presentation checks are September 18.

## 02 · What should survive a completed task?

- Role: INTRODUCTION / introduction
- Purpose: What should survive a completed task?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: This is an illustrative cross-paper teaching example, not a reported FinEvo task or measured result. A trace records a run; an agent skill packages reusable instructions, scripts or resources. The example motivates relevance, transfer and maintenance before any numerical evidence. Retention alone is not improvement; self-directedness concerns which update decisions the agent controls.

## 03 · Learning over time and learning to adapt are different questions

- Role: INTRODUCTION / concepts
- Purpose: Learning over time and learning to adapt are different questions
- Visual: Editable synthesis with source attribution.
- Claims: C020, C021
- Sources: Lifelong Learning: A Case Study — https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1995_1/thrun_sebastian_1995_1.pdf — §§1–2; Gradient Episodic Memory for Continual Learning — https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf — §§1–3: stability–plasticity, forward/backward transfer; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Thrun §§1–2 motivates transfer from earlier tasks; GEM §§1–3 distinguishes forward and backward transfer and stability–plasticity. Here the complete agent can learn through external state even with fixed model weights. MAML is an incidental example of learned initialization, not a new empirical case: it optimizes starting parameters for performance after gradient adaptation. SEAL will provide the developed example of a learned update-data policy. Transfer before adaptation differs from faster adaptation, which needs learning curves. Neither persistence nor editing code proves durable learning.

## 04 · What is retained—and what does it help the system do?

- Role: INTRODUCTION / concepts
- Purpose: What is retained—and what does it help the system do?
- Visual: Editable four-row comparison table, Codex Grid 14.
- Claims: C001, C004, C014, C020, C021
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; GEPA — https://arxiv.org/abs/2507.19457v2 — Algorithm 1; §4; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1
- Speaker notes: This replaces the old four-category map. Rows describe state carriers; task execution versus improving adaptation is a separate axis. Harness means the prompts/software organizing model calls and tools. SEAL learns update-data generation in weights; Hyperagents makes improvement code editable. Both still have externally specified evaluation and selection. More editable components are not a capability ladder. Offline harness search, deployment learning, and task-local retries must be distinguished by the actual protocol.

## 05 · When does experience create a lasting advantage worth the cost?

- Role: INTRODUCTION / main-question
- Purpose: When does experience create a lasting advantage worth the cost?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: The central question is lasting advantage worth its cost. First ask whether experience adds expertise beyond strong initial guidance and extra attempts. Then ask when retained knowledge is relevant and whether later learning preserves earlier abilities. Finally consider learned adaptation. The conclusion will return to these conditions, with economic value an unresolved empirical test rather than a claimed break-even result.

## 06 · Can a rejected skill still teach the next proposer?

- Role: RESULTS / USEFUL EXPERTISE / mini-introduction + concept
- Purpose: Develop the latest thesis’s central mechanism example.
- Visual: Original source conceptual figure, extracted without redrawing: Tang et al. · WikiSkill v1 · Figure 2, p. 4 · Complete diagram; caption omitted
- Claims: C003, C013
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; SkillOpt — https://arxiv.org/abs/2605.23904v2 — §§3.5–3.6; rejected edits retained as feedback
- Speaker notes: WikiSkill §3/Figure 2: a maintenance agent consolidates traces in the wiki; a skill agent uses both the wiki and original traces to propose skills. The task agent receives skills directly, not the wiki. Validation can reject a skill while the accumulated wiki persists. SkillOpt already keeps rejected-edit feedback; separate organized knowledge is the distinction, not first use of failure. Our inference: the validation gate tests a procedure, not the truth of every retained interpretation. A rejected proposal can leave a mistaken lesson as well as a useful one. Proposed wiki test: retain versus remove an entry from a rejected proposal, then compare the quality of subsequent proposals. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes. Part 1 setup: a completed attempt is only a record. The question is whether organizing it yields reusable guidance. The next result compares complete methods; it does not isolate the causal value of keeping the rejected proposal’s wiki entry.

## 07 · Learned skills beat both no skills and a strong rival

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Establish a positive retained-state result.
- Visual: Original source extraction; Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Interpretation below, separate from source artwork.
- Claims: C003, C013
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B
- Speaker notes: WikiSkill separates traces, accumulated wiki knowledge, and deployed skills. When a candidate skill is rejected, knowledge from the attempt can still persist. Qwen-3.5-9B gains 17.5 percentage points in macro accuracy across five benchmarks with equal benchmark weighting and three evolution runs. Test sizes are 124, 85, 280, 172, and 134. Table 1 gives no numerical confidence intervals. Skills are directly injected, validation sets are small, and OfficeQA has reference-page assistance. Qwen-3.5-4B declines from 30.2 to 28.5 on OfficeQA. The result supports useful benchmark learning, not universal improvement. Transition: compare learning against a strong procedure supplied from the start. Visual: Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 excerpt, including all methods for Qwen-3.5-4B and 9B. Qwen-3.5-9B average rises from 29.9 to 47.4; Qwen-3.5-4B OfficeQA falls from 30.2 to 28.5. Original Table 1 caption: scores average three full evolution runs; all methods start with an empty skill set and evolved skills are directly injected. Bold denotes the best or results not significantly different from it under the authors’ paired bootstrap test (1,000 resamples, p < .05); yellow highlighting is the authors’ own. The strongest competing method for Qwen-3.5-9B is EvoSkill at 42.3: 47.4 − 42.3 = 5.1 pp. Both comparisons are whole-method comparisons and do not isolate the wiki’s causal contribution. SkillOpt already retains failed-edit feedback.

## 08 · FinEvo tests whether a procedure survives a new case

- Role: RESULTS / USEFUL EXPERTISE / concept
- Purpose: Explain the core idea before its result.
- Visual: Original cropped source artwork on the left; large reading guidance on the right.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5
- Speaker notes: FinEvo v1 Figure 1 and §§3–4.1. Figure 1 depicts task coverage and a stock-analysis example; the visible subtitle explains the persistence control used in the evaluation. 20 scenes × 6 cases = 120 tasks. Streams interleave scenes. Agents receive post-task problem/reason summaries, not the hidden rubric. The next slide adds fixed expert skills as a strong alternative to learning. Original artwork retained. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes. New crop retains Figure 1(a); the workspace panel is omitted explicitly. Guidance outside the source artwork explains §4.1. The original figure is a task map, not a diagram of the reset control. Same model does not mean equal total tokens: evolving agents also reflect. FinEvo also interleaves scenes: do not contrast its positive results with AgentStream as if mixing were unique to AgentStream. Their tasks, feedback and metrics differ.

## 09 · Expertise and update design both change the payoff

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Expertise and update design both change the payoff
- Visual: Original source extraction; Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5
- Speaker notes: FinEvo tests recurring professional procedures with 120 financial tasks in 20 scenes and three shuffled task orders. Four scaffolds use the same Qwen3.7-Max backbone. Paired gains over reset range from 9.33 to 19.37 rubric points. The displayed Table 5 ablation is only the Claude Code scaffold: these labels are software frameworks, not vendor model identities. Reset is 71.58, fixed expert skill 86.67, unrestricted evolution 89.47. The 2.80-point difference is descriptive, not a tested causal advantage at matched cost. No across-run intervals are reported. Scoring and feedback share rubric design. Strong recurring-procedure evidence; novel procedures and full cost remain unresolved. Visual: Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original FinEvo Table 5, all five conditions, score, compliance, execution and reflection costs. Reset 71.58, fixed expert skill 86.67, full evolution 89.47, memory only 90.42, skill only 93.71. Source table definitions: Score is the rubric score; Comp. is compliance issues per task; costs are 10^4 tokens per task. Table 5 is on PDF page 6 in the retrieved v1; earlier reading notes said page 7. The four-scaffold paired-reset experiment uses 120 tasks and three orders, with 9.33–19.37 rubric-point gains. This Table 5 comparison is one scaffold only. SkillsBench adds a curated-skill counterfactual, but its one-shot self-authoring diagnostic does not test iterative learning; see appendix. New arithmetic from the displayed table: skill-only 17.53 + 44.03 = 61.56; full evolution 16.31 + 60.19 = 76.50, in units of 10^4 tokens/task. Fixed expert skill has execution 15.92 and no reflection. Full evolution exceeds fixed skill by 2.80 rubric points; skill-only exceeds it by 7.04. The result argues for comparing concrete update designs and strong initial expertise; it is not a universal argument against learning. Human authoring and judging costs are not in these totals.

## 10 · Spend the next attempt on a solution—or the harness?

- Role: RESULTS / USEFUL EXPERTISE / concept
- Purpose: Explain the core idea before its result.
- Visual: Original source conceptual figure, extracted without redrawing: Wang et al. · Harness evaluation v2 · Figure 2, p. 3 · All four panels and legend
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Harness critique v2 §3/Figure 2. Original Figure 2 shows the four mechanisms; guide attention to panels (a) and (c), while preserving the other panels and legend. Figure 1 is a results chart, not a mechanism overview. The displayed result next uses five rollouts without unit-test feedback; the separate train/validation/test experiment asks whether an evolved harness transfers. Equal rollouts do not match all compute costs. The shared harness is optimized across a batch (§3.4), unlike task-specific harness scaling (§3.5). Without tests, the final harness is used; parallel sampling uses model self-selection. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes. Transition from FinEvo: supplying expertise and improving the update recipe are not the only alternatives. Extra attempts can also buy task success.

## 11 · More attempts are a serious competing baseline

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Test reusable changes against extra inference.
- Visual: Original source extraction; Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; ReasoningBank — https://arxiv.org/abs/2509.25140v2 — §§3–4; retained lessons plus test-time search
- Speaker notes: This is a counterexample from one tested harness-evolution implementation, not a universal negative result. Table 1 compares five rollouts on 89 Terminal-Bench 2.1 tasks, three models, two runs, without test feedback. Retain the printed averages 67.4 and 72.3 despite rounded-cell arithmetic. A separate train/validation/test partition of 45/10/34 yields 68.3 for evolved versus 67.7 for initial harness on the 34 held-out tasks. Do not combine those experimental populations. No numerical CIs in the tables. Equal rollouts are not equal dollars or tokens; a reused harness could repay development cost across future tasks. Transition: follow the system beyond development and watch for damage. Visual: Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 showing per-model results and printed averages for direct sampling, parallel sampling, sequential refinement, harness evolution and harness scaling. Reported averages: parallel sampling 72.3, harness evolution 67.4. Source caption: unit tests unavailable, pass@1; bold is best and underline is second best. The displayed 67.4 is the printed average, without correcting the source’s rounded-cell arithmetic. ReasoningBank combines test-time search and retained lessons: computation and learning can complement each other. Report development cost separately from operating cost at explicit amounts of reuse. Equal attempts alone do not normalize dollars or tokens. Part takeaway: learned procedures can help, but expertise and extra attempts are serious alternatives. Next ask whether a gain survives continued use. Define pass@1 as success of the submitted answer, not the probability that any generated candidate passes. Five rollouts may be used inside a method; no unit tests are supplied for candidate selection here.

## 12 · Will retained expertise fit the next task—and survive later learning?

- Role: RESULTS / DURABILITY / mini-introduction
- Purpose: Do the gains survive the next tasks?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Part 1 established useful local learning under demanding alternatives, without a full economic verdict. Part 2 distinguishes relevance failure from forgetting. Relevance means selecting experience that belongs in the current task. Forgetting means an update reduces performance on previously learned work under otherwise fixed conditions. Changed tools are a third failure mode, not automatically forgetting.

## 13 · AgentStream tests learning across different task sequences

- Role: RESULTS / DURABILITY / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Yan et al. · AgentStream v1 · Figure 1(b); independent-evaluation panel (a) omitted
- Claims: C007
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: AgentStream v1 §3.1/Figure 1. This is an evaluation framework, not a new learning algorithm. Read left to right along the tasks; then follow the feedback down into retained state and forward to the next task. State starts empty. Ground-truth labels are unavailable to the updating agent; it uses execution outcomes and self-reflection. The no-evolution comparison keeps state empty on every task. Three models and five methods are crossed with three stream arrangements. Figure 1(a), omitted here, shows the independent empty-state baseline. Next slide defines the three arrangements and preserves the original calculated results. Before the table: isolated means separate state per benchmark; sequential means shared state carried across benchmark blocks; interleaved means shared state across mixed tasks. Unlike FinEvo, no rubric-derived corrective summaries are supplied. Methods differ in more than retrieval.

## 14 · Mixed tasks change which memory methods help

- Role: RESULTS / DURABILITY / result
- Purpose: Mixed tasks change which memory methods help
- Visual: Original Table 5, complete; external interpretation of contrasting method responses.
- Claims: C007, C013, C016
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: Inspected AgentStream v1 PDF p.11, complete Table 5, caption, §5.4 and Table 6. Table 5 averages over three models and three order seeds, nine shared-task configurations per method. Positive/negative figures are percentage-point gains over the same model’s no-evolution baseline; the source labels them gain (%). Last columns count which scenario wins in nine configurations; a tie explains totals below nine. ACE keeps a playbook integrated into context. A-Mem and ReasoningBank retrieve entries from external stores. Each method differs in multiple components, so this is not a retrieval-only ablation. Sequential carries state across domain blocks; interleaved shuffles tasks across domains; isolated has separate state for each benchmark. No confidence interval is in this table. The full aggregate-count calculation is retained in the appendix. Contrast with FinEvo is not causal: tasks, metrics, feedback, models and protocols differ. Takeaway: storing experience is insufficient; its relevance to the next task matters.

## 15 · SEAL learns which training data make an update useful

- Role: RESULTS / DURABILITY / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Zweiger et al. · SEAL v2 · Figure 1, p. 2; caption omitted
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: SEAL v2 §3/Figure 1. Ctx is the supplied context; SE is a generated self-edit, specifying training content and optionally optimization directives. Inner loop: gradient updates adapt weights using that edit. Outer loop: downstream success rewards the policy that produced it. In the knowledge-incorporation example, a passage becomes synthetic training material; the result tests whether learning to generate that material helps question answering after adaptation. This differs from simply storing a passage in context. Figure 1 is the method overview; Table 2 follows. The learned update policy does not guarantee retention through later edits. Link back to meta-learning: a learned update-data policy is a way to learn to adapt without editing the update algorithm’s source code. Ctx is supplied context, SE is self-edit, theta denotes weights, and the check/cross marks downstream evaluation. In the example, external context is a passage and the output is training data. This leads to two tests: new passage answers, then earlier passage retention.

## 16 · Learning to write update data improves adaptation

- Role: RESULTS / DURABILITY / result
- Purpose: Learning to write update data improves adaptation
- Visual: Original source extraction; Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Interpretation below, separate from source artwork.
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: SEAL has an outer loop that rewards self-generated edits when an inner weight update helps downstream performance. This example is single-passage SQuAD incorporation with Qwen2.5-7B, not the curated ARC experiment. The tested learned policy reaches 47.0 versus 39.7 for base-model synthetic data, a 7.3 percentage-point difference. A stronger external generator, GPT-4.1, reaches 46.3; SEAL does not generally dominate it and loses to it in the larger incorporation conditions. There are 974 questions clustered within 200 held-out passages. Final-score repeated-run uncertainty is not supplied. Figure 6 shows forgetting across sequential edits. Transition: an improvement still needs strong controls. Visual: Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original SEAL Table 2, all five methods and three passage settings. Single-passage SEAL scores 47.0 versus 39.7 for untrained synthetic data and 46.3 for GPT-4.1 data. GPT-4.1 wins in both continued-pretraining settings. This is useful learned adaptation, not evidence of durable accumulation. The next slide shows the paper’s distinct sequential-edit test.

## 17 · A useful update can still damage earlier knowledge

- Role: RESULTS / DURABILITY / result
- Purpose: Distinguish adaptation quality from continual retention using one developed method.
- Visual: Original cropped source artwork on the left; large reading guidance on the right.
- Claims: C004, C020
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Gradient Episodic Memory for Continual Learning — https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf — §§1–3: stability–plasticity, forward/backward transfer
- Speaker notes: Re-read SEAL v2 §5 pp.8–9 and Appendix B.6. The paper sequentially updates on new passages and revisits prior tasks. Read downward after a passage is first incorporated; many earlier-passage scores decline, but not every adjacent cell declines and no universal collapse is claimed. The original colormap, cell values and axes remain unchanged. §5 states retention is not explicitly optimized. Table in B.6 gives entrywise SEM, but the nearby text does not make the repeat denominator clear. This is a distinct evaluation from Table 2, not the same task average tracked across time. Other recipes can sustain bounded gains: C019 and the Continual Internalization reading note remain in supporting research. Removing its rushed slide does not imply all weight learning fails.

## 18 · Production learning needs a source of reliable corrections

- Role: RESULTS / DURABILITY / result
- Purpose: Production learning needs a source of reliable corrections
- Visual: Flat sequence of changing components opposite the fixed external support.
- Claims: C010, C016
- Sources: Sidekick’s continual learning loop — https://shopify.engineering/sidekicks-continual-learning-loop — Harness optimization; trajectory repair; training; GraphQL sections; Reward Hacking Benchmark — https://arxiv.org/abs/2605.02964v1 — §§4–6; evaluation integrity separate from task correctness
- Speaker notes: Shopify describes a production pipeline rather than releasing a controlled longitudinal evaluation. Product criteria become rubric judges. Harness search modifies prompts, tool descriptions and orchestration. Frontier models repair low-scoring trajectories; unresolved cases go to human annotators. Repaired trajectories feed SFT and GRPO; old and new trajectories are reused in daily full-parameter training. Serving compression learns gist tokens. Treat all as company-described architecture. The article supplies no component ablations or cycle-by-cycle held-out quality. A shared judge can propagate a blind spot across stages, but that possibility is not proof of reward hacking. We deliberately omit the estimated 96% cost saving because it does not measure the total causal value of continual learning. Shared judges may carry correlated blind spots across selection and assessment; this does not establish observed gaming at Shopify. Reward Hacking Benchmark distinguishes evaluator integrity from task correctness. An evaluator outside edit permissions is our design recommendation, not a sufficient guarantee. Part takeaway: retention and continued gains depend on the setting; production combines several loops without isolating their benefits. Can the method that produces changes itself improve? Keep report and recommendation distinct: the separate-evaluation sentence is our implication, not a claim that Shopify has released an independent longitudinal evaluation. Reliable correction is the common requirement across generated lessons and training data.

## 19 · Can experience improve the adaptation process?

- Role: RESULTS / IMPROVING THE IMPROVER / mini-introduction
- Purpose: Can experience improve the adaptation process?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C009, C021
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1
- Speaker notes: Meta-learning is the broader question. SEAL supplied a learned update-data example; MAML is a learned-initialization example. This section develops editable improvement code as a further route, not a definition or prerequisite. Hyperagents offers bounded transfer evidence. The main claim remains future-task value; acceleration would require several cycles of better gains per resource.

## 20 · Hyperagents makes the proposal method editable

- Role: RESULTS / IMPROVING THE IMPROVER / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Original cropped source artwork on the left; large reading guidance on the right.
- Claims: C009, C014, C017
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §3/Figure 1. Start with the bottom archive: select a parent, invoke its meta agent to propose an edited child, evaluate the child task agent, add it to the archive. A child may change task code, meta code, or both. The outer archive/selection/evaluation remains specified externally. Top: DGM retains handcrafted improvement-instruction generation. Small right-hand traces illustrate the same contrast; the large central loop carries the explanation. Editability is a mechanism, not evidence that learning accelerates. Next: freeze the resulting improver and see whether its improvement behavior transfers. SICA/DGM boundary details remain in the appendix. Crop retains original left/central panels for both systems; the small right-hand implementation traces are omitted and labeled. The comparison is not an assertion that DGM lacks an archive or that Hyperagents has no external controls.

## 21 · A developed implementation can help learning in a new domain

- Role: RESULTS / IMPROVING THE IMPROVER / result
- Purpose: A developed implementation can help learning in a new domain
- Visual: Original Figure 3 middle/right held-out panels, with all their comparators and uncertainty; training panel omitted.
- Claims: C009
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §§5.1–5.2: select transferred implementations from paper review and robotics reward design, then hold their meta agents fixed for 50 candidate-generation iterations on math grading. Improvement@50 is the held-out score gain of the best validation-selected task agent over its starting agent. Five runs: median 0.630, 95% bootstrap interval 0.540–0.630; initial implementation 0.000 (0.000–0.130). Authors report p<.05; repository audit identifies one-sided tests and run-array bootstrap, not task-population uncertainty. The entire task/meta implementation transfers and initial task behavior has formatting failures. This supports useful transferable improvement behavior without isolating meta code from the rest of the implementation. Figure caption uses stronger language about generality; our title narrows it to the tested domain. Next ask whether that starting advantage remains under continued meta evolution. The on-slide definition separates a gain metric from an endpoint score. Separate continued-evolution experiment is now in the appendix: 0.640 vs 0.610 at 200 iterations, p>.05; it does not contradict the fixed-method result. It leaves added long-run advantage uncertain. No isolated portable improver or repeated efficiency gain is claimed.

## 22 · Experience can pay when useful expertise is reused

- Role: CONCLUSION / synthesis
- Purpose: Experience can pay when useful expertise is reused
- Visual: Three equal cards, without arrows or an implied progression.
- Claims: C004, C005, C007, C011, C020
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Answer the opening question: experience is a promising investment when it supplies expertise absent at the start and future work reuses it, provided relevant state is selected, reliable feedback corrects it, earlier abilities survive, and total costs are justified. This is our conditional synthesis, not a causal cross-benchmark finding. FinEvo’s token accounting and the harness comparison are partial evidence, not a full lifetime economic test. Reuse volume, task recurrence, starting expertise and feedback quality are variables to test. Hyperagents adds bounded transfer evidence without moving sustained compounding into the established column.

## 23 · Test reuse, retention, and cost on the same task stream

- Role: CONCLUSION / implications
- Purpose: Test reuse, retention, and cost on the same task stream
- Visual: Four-row decision table, Codex Grid 14.
- Claims: C011, C012, C020
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Hold out new task families and a later time period before optimizing the system. Revisit earlier tasks to measure retention, failures and regressions, not only the best checkpoint. Count search, weight updates, execution and evaluation: cheap deployment can hide expensive optimization. Use independent repeated runs and a separately designed evaluator. An evaluator can still be wrong; report calibration and the unit of uncertainty. To claim acceleration rather than improvement, repeated cycles would need increasingly efficient gains, not just a higher score. These are recommendations grounded in the observed limitations, not empirical guarantees. Report development cost and operating cost separately at stated reuse volumes. Sustained compounding needs several cycles of improved learning efficiency, adjusted for task difficulty and resources; a D-versus-C endpoint win alone is insufficient. Detailed control arms and frozen-versus-adaptive test lanes are in the appendix. These proposed tests operationalize the conditional conclusion rather than claiming every paper must satisfy every test. Hold model, feedback and budget fixed when varying recurrence/mixing. The earlier row called “does it repeat?” conflated replication with repeated learning-efficiency gains; replication is now in the caveat, and compounding is treated separately.

## 24 · When would you choose to keep learning?

- Role: CONCLUSION / DISCUSSION / discussion
- Purpose: When would you choose to keep learning?
- Visual: Three spacious numbered prompts with a concrete evidence anchor.
- Claims: C004, C005, C007, C011, C012
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Close on decisions rather than repeat the synthesis. Question 1: compare all displayed FinEvo alternatives, including missing authoring/judging costs and uncertainty; do not treat score differences as money. Question 2: distinguish irrelevance, outdated dependencies, and forgetting. Question 3: make a prediction under a particular reuse volume and task distribution, then identify a result that would falsify it. Optional improver-transfer discussion and the separate Hyperagents endpoint experiment are in the appendix.

## 25 · Appendix · continued evolution leaves an uncertain advantage

- Role: APPENDIX / appendix
- Purpose: Distinguish the uncertain endpoint advantage from the positive fixed-improver transfer result.
- Visual: Original Figure 4 with both panels and uncertainty; separate from Figure 3.
- Claims: C009
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Keep this separate from Figure 3. Here task and meta code may both continue evolving after transfer. After 200 iterations, transferred agents reach median held-out score 0.640 versus 0.610 from initial implementation, across five runs; run-bootstrap 95% intervals are 0.550–0.720 and 0.510–0.680. Authors explicitly report p>.05. The plot includes a separate ProofAutoGrader transfer condition and representative baseline, preserved as context rather than the chosen comparison. The first experiment supports bounded transfer of improvement behavior; this experiment leaves added long-run advantage uncertain. Lack of significance is not an equivalence test. Neither measures repeated improvement in learning efficiency at matched resources. Main-talk definition: improvement@50 is a gain; this appendix result is endpoint score. All intervals and original comparators remain in the source figure.

## 26 · Appendix · stream averages hide configuration differences

- Role: APPENDIX / appendix
- Purpose: Show why aggregate improvement can hide regressions.
- Visual: Prominent mean and flat three-row table, adapted Codex Grid 14.
- Claims: C007, C013, C016
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Library Drift — https://arxiv.org/abs/2605.19576v3 — §§5–7; retrieval, storage, retirement; EvoHarnessBench — https://arxiv.org/abs/2609.04280v2 — §§3–4; evolving tools, skills and specialist agents
- Speaker notes: AgentStream evaluates six benchmarks with 50 tasks each: 300 distinct tasks, reused across three order seeds. The three models and five methods make 45 model–method–seed cells per stream condition. For interleaving, 28 cells are positive and 17 negative. The local audit reproduces the means and the printed variability as sample SD of three seed means, not a confidence interval or SD over 45 independent datasets. Methods share tasks; benchmark metrics differ. FinEvo and AgentStream use different tasks and feedback, so their effect sizes are not a head-to-head ranking. The uncertainty about causes remains: retrieval, interference, and feedback quality require controlled ablations. The thesis also notes AgentStream Tables 5–6: ACE shifts from positive average gain in isolated streams to negative in interleaved streams, whereas ReasoningBank and A-Mem have their largest mean gains in interleaved streams. This is consistent with relevance selection mattering, but the methods differ in more than retrieval. Library Drift and EvoHarnessBench motivate testing skill retirement and changed interfaces; they do not estimate the same failure rate. The row labels define the streams from §3.2; the earlier homemade domain-order strings have been removed. Isolated still learns within each domain. Methods differ in more than retrieval. Numeric cells remain the documented calculation.

## 27 · Appendix · compare four practical alternatives fairly

- Role: APPENDIX / appendix
- Purpose: Compare practical alternatives while making initial-state matching and the paired reset requirement explicit.
- Visual: Editable four-arm table; clearly labeled proposed experiment.
- Claims: C012
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: This is a proposed protocol, not an established result. Give four practical alternatives the same task stream, feedback access and common total resource ceiling. C and D must begin with identical task code, improvement code and retained state. A strong fixed procedure can have a different starting method; account for authoring cost. A paired reset counterpart to a retained-state arm separately tests experience. The four alternatives alone do not identify four independent causal effects. D beating C is useful within this protocol but does not by itself prove isolated improver transfer or compounding.

## 28 · Appendix · separate what it knows from what it can learn next

- Role: APPENDIX / appendix
- Purpose: Turn the thesis’s corrected experiment into an explicit design.
- Visual: Two test lanes with a shared matched-start control beneath.
- Claims: C009, C012
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: After development, freeze copies to test accumulated capabilities on fresh cases, new task families and earlier tasks. Separately let copies adapt on new streams to measure future learning. To isolate improvement-method transfer, attach learned and original improvement methods to identical task agents with identical retained state. Hold both methods fixed during candidate generation and match feedback/resources. This directly addresses the confounding of whole-implementation transfer in Hyperagents §5.2. Repeat across streams and report independent-run uncertainty. A single favorable transplant is bounded meta-learning, not sustained compounding.

## 29 · Appendix · read each number with its denominator

- Role: APPENDIX / appendix
- Purpose: Keep uncertainty and independence available during discussion.
- Visual: Concise methods table; no pooled effect.
- Claims: C003, C004, C005, C006, C007, C009
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Different metrics, tasks, populations and resource budgets must not be pooled. SEAL Table 2 questions share passages; Figure 6 is a separate sequential-edit test with entrywise SEM and unclear repeat denominator. AgentStream 45 cells share 300 tasks; Table 2 printed variability is sample SD of three seed means. Hyperagents CIs quantify five-run variation, not task-population uncertainty; improvement@50 and final score are distinct. These values are source-reported or documented calculations, not replicated experiments.

## 30 · Appendix · one-shot authoring is a different test

- Role: APPENDIX / appendix
- Purpose: Include the expanded thesis’s curated-skill counterfactual without misreading it.
- Visual: Two-column conceptual contrast; no recreated result chart.
- Claims: C018
- Sources: SkillsBench — https://arxiv.org/abs/2602.12670v4 — Tables 2/6; Appendix D.6
- Speaker notes: SkillsBench v4 Tables 2/6 and Appendix D.6: 87 tasks, 18 configurations, three trials in the curated-skills study. Curated configuration-macro pass rate is 33.9→50.5%; 13 tasks have negative deltas. The self-generation diagnostic includes three configurations, each below no-skills (−8.1/−11.3/−11.5 pp). It is one-shot authoring without repeated outcome feedback. Human authoring effort is not matched, skill packs include scripts/assets, low-signal filtering can enrich skill-sensitive tasks, and authoring-run uncertainty is absent. The design is valuable as a strong curated baseline but cannot establish continual learning failure.

## 31 · Appendix · editing an agent and editing its improver differ

- Role: APPENDIX / appendix
- Purpose: Introduce meta-improvement through a precise predecessor comparison.
- Visual: Three-row comparison of editable components and external constraints.
- Claims: C013, C014, C017
- Sources: Self-Improving Coding Agent — https://arxiv.org/abs/2504.15228v2 — §3; Algorithm 1; Darwin Gödel Machine — https://arxiv.org/abs/2505.22954v3 — §§2–4; Hyperagents §1/Appendix B for the boundary; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Gödel Machines — https://arxiv.org/abs/cs/0309048v5 — §§2.2/3.2/4.1
- Speaker notes: SICA §3/Algorithm 1 retains an archive but expands the best-scoring agent. DGM explores alternate lineages, allowing weaker stepping stones, but retains a handcrafted improvement-instruction generator. Hyperagents puts task and improvement code in the same editable implementation while retaining an outer archive/evaluation procedure. These are related systems, not independent confirmations. STOP already edits improvement code; this is not a claim that Hyperagents invented self-modification. Gödel Machines requires a utility-improvement proof under encoded assumptions; empirical DGM does not inherit that guarantee.

## 32 · Appendix · primary sources 1/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: Lifelong Learning: A Case Study — https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1995_1/thrun_sebastian_1995_1.pdf — §§1–2; Gradient Episodic Memory for Continual Learning — https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf — §§1–3: stability–plasticity, forward/backward transfer; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1; Reflexion — https://arxiv.org/abs/2303.11366v4 — Algorithm 1; §§3–4; Voyager — https://arxiv.org/abs/2305.16291v2 — §§2–3; STOP — https://arxiv.org/abs/2310.02304v3 — Algorithm 1; §3
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 33 · Appendix · primary sources 2/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: GEPA — https://arxiv.org/abs/2507.19457v2 — Algorithm 1; §4; WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 34 · Appendix · primary sources 3/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Sidekick’s continual learning loop — https://shopify.engineering/sidekicks-continual-learning-loop — Harness optimization; trajectory repair; training; GraphQL sections; SkillsBench — https://arxiv.org/abs/2602.12670v4 — Tables 2/6; Appendix D.6; Darwin Gödel Machine — https://arxiv.org/abs/2505.22954v3 — §§2–4; Hyperagents §1/Appendix B for the boundary; Self-Improving Coding Agent — https://arxiv.org/abs/2504.15228v2 — §3; Algorithm 1; Gödel Machines — https://arxiv.org/abs/cs/0309048v5 — §§2.2/3.2/4.1
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 35 · Appendix · primary sources 4/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: The Economics of Recursive Self-Improvement — https://arxiv.org/abs/2609.15802v1 — §§2–4; conditional model, not measured acceleration; SkillOpt — https://arxiv.org/abs/2605.23904v2 — §§3.5–3.6; rejected edits retained as feedback; ReasoningBank — https://arxiv.org/abs/2509.25140v2 — §§3–4; retained lessons plus test-time search; Reward Hacking Benchmark — https://arxiv.org/abs/2605.02964v1 — §§4–6; evaluation integrity separate from task correctness; Library Drift — https://arxiv.org/abs/2605.19576v3 — §§5–7; retrieval, storage, retirement; EvoHarnessBench — https://arxiv.org/abs/2609.04280v2 — §§3–4; evolving tools, skills and specialist agents
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.
