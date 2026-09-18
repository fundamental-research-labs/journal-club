# Presentation storyboard

Revision: September 18, 2026 — explanation-first revision. **25 main slides + 12 appendices**. Approximately 30–35 minutes plus discussion; live rehearsal pending. Research cutoff remains September 16.

## Argument and visual direction

Start with the agent’s work, then explain what changes, then read the evidence. Preserve the forest-green/ivory palette and original source artwork. FinEvo now takes three slides: an actual report mistake and saved check (8), three alternative ways to prepare the agent (9), and their outcomes/costs (10). The full benchmark overview is supporting material (37). The distinction between an observed saved edit and demonstrated future benefit stays explicit.

The introduction ends with the main question on slide 5. The results ask whether experience adds expertise (6–12), remains relevant and survives later learning (13–19), and improves future adaptation (20–22). The conclusion (23) answers with useful later corrections and their costs. Proposed tests (24) and discussion (25) follow. Plain-language definitions precede technical labels; supporting details remain in notes.

The SEAL sequence explicitly answers the durability section’s second question: after showing that an update learns new facts, test whether those facts survive subsequent updates. Slide 16 keeps the original mechanism figure full-width and defines its symbols; slide 17 explains the no-passage test and comparison; slide 18 walks down one heatmap column. The AgentStream-to-SEAL transition separates relevance of external guidance from retention under weight updates.

## Concept-to-evidence audit

| Example | Concept → result | Inspected source artwork and locators |
| --- | --- | --- |
| WikiSkill | 6 → 7 | v1 Figure 2, §3; Table 1 |
| FinEvo | 8–9 → 10; overview 37 | v1 Appendix C, Tables 25–27 and Figure 10 calculation row; §§3–4, Table 5; original Figure 1 |
| Harness evaluation | 11 → 12 | v2 Figure 2; Tables 1/3 |
| AgentStream | 14 → 15; aggregate 27 | v1 Figure 1(b), §3, §5.4, Tables 5/6 |
| SEAL | 16 → 17–18 | v2 Figure 1/§3, Table 2, Figure 6/§5, Appendix B.6 |
| Sidekick | 19 | First-party process account; company report distinguished from measured causal evidence |
| Hyperagents | 21 → 22; endpoint 26 | v1 Figure 1/§3; Figure 3/§5.2; Figure 4/§5.3 |
| SkillsBench | 31 | Scoped curated/no-skill/one-shot comparison; no iterative-learning claim |

No new experimental claim is introduced. Figure 10’s excerpt is original source artwork, not reconstructed instructions. The whole FinEvo result table remains visible. The 7-point title rounds 7.04; 3.9× rounds 615,600 / 159,200. Counts, statistical scope and resource exclusions remain in notes. Foundational methods are conceptual context, not additional paper reviews.

## Sequence and traceability

## 01 · Self-evolving agents

- Role: INTRODUCTION / introduction
- Purpose: Introduce the topic and practical promise.
- Visual: Large typographic cover; Codex Grid 01.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Work can be valuable twice: the completed task and expertise that helps later work. Ask when that retained expertise is worth obtaining and maintaining. Main talk follows useful skills, selective reuse and retention, then learned adaptation. Recursive acceleration is a further question, not the definition of useful learning. Research cutoff remains September 16; foundation readings and presentation checks are September 18.

## 02 · What should the agent do better next time?

- Role: INTRODUCTION / introduction
- Purpose: What should survive a completed task?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: This is an illustrative cross-paper teaching example, not a reported FinEvo task or measured result. A trace records a run; an agent skill packages reusable instructions, scripts or resources. The example motivates relevance, transfer and maintenance before any numerical evidence. Retention alone is not improvement; self-directedness concerns which update decisions the agent controls.

## 03 · Learning new tasks also raises two different questions

- Role: INTRODUCTION / concepts
- Purpose: Learning over time and learning to adapt are different questions
- Visual: Editable synthesis with source attribution.
- Claims: C020, C021
- Sources: Lifelong Learning: A Case Study — https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1995_1/thrun_sebastian_1995_1.pdf — §§1–2; Gradient Episodic Memory for Continual Learning — https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf — §§1–3: stability–plasticity, forward/backward transfer; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Thrun §§1–2 motivates transfer from earlier tasks; GEM §§1–3 distinguishes forward and backward transfer and stability–plasticity. Here the complete agent can learn through external state even with fixed model weights. MAML is an incidental example of learned initialization, not a new empirical case: it optimizes starting parameters for performance after gradient adaptation. SEAL will provide the developed example of a learned update-data policy. Transfer before adaptation differs from faster adaptation, which needs learning curves. Neither persistence nor editing code proves durable learning.

## 04 · What can experience change?

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

## 06 · WikiSkill keeps lessons from rejected changes

- Role: RESULTS / USEFUL EXPERTISE / mini-introduction + concept
- Purpose: Develop the latest thesis’s central mechanism example.
- Visual: Original source conceptual figure, extracted without redrawing: Tang et al. · WikiSkill v1 · Figure 2, p. 4 · Complete diagram; caption omitted
- Claims: C003, C013
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; SkillOpt — https://arxiv.org/abs/2605.23904v2 — §§3.5–3.6; rejected edits retained as feedback
- Speaker notes: Plain-language introduction: a trace is a record of what the agent tried. A wiki collects lessons from those records. A skill is a reusable set of instructions. Another agent proposes a new skill and validation tasks test it. Keep the better skill, but retain the accumulated wiki even when that proposal fails. Read the original figure from the task traces at the bottom to the wiki and proposed skills above. WikiSkill §3/Figure 2: a maintenance agent consolidates traces in the wiki; a skill agent uses both the wiki and original traces to propose skills. The task agent receives skills directly, not the wiki. Validation can reject a skill while the accumulated wiki persists. SkillOpt already keeps rejected-edit feedback; separate organized knowledge is the distinction, not first use of failure. Our inference: the validation gate tests a procedure, not the truth of every retained interpretation. A rejected proposal can leave a mistaken lesson as well as a useful one. Proposed wiki test: retain versus remove an entry from a rejected proposal, then compare the quality of subsequent proposals. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes. Part 1 setup: a completed attempt is only a record. The question is whether organizing it yields reusable guidance. The next result compares complete methods; it does not isolate the causal value of keeping the rejected proposal’s wiki entry.

## 07 · WikiSkill’s learned instructions help on unseen tasks

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Establish a positive retained-state result.
- Visual: Original source extraction; Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Interpretation below, separate from source artwork.
- Claims: C003, C013
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B
- Speaker notes: WikiSkill separates traces, accumulated wiki knowledge, and deployed skills. When a candidate skill is rejected, knowledge from the attempt can still persist. Qwen-3.5-9B gains 17.5 percentage points in macro accuracy across five benchmarks with equal benchmark weighting and three evolution runs. Test sizes are 124, 85, 280, 172, and 134. Table 1 gives no numerical confidence intervals. Skills are directly injected, validation sets are small, and OfficeQA has reference-page assistance. Qwen-3.5-4B declines from 30.2 to 28.5 on OfficeQA. The result supports useful benchmark learning, not universal improvement. Transition: compare learning against a strong procedure supplied from the start. Visual: Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 excerpt, including all methods for Qwen-3.5-4B and 9B. Qwen-3.5-9B average rises from 29.9 to 47.4; Qwen-3.5-4B OfficeQA falls from 30.2 to 28.5. Original Table 1 caption: scores average three full evolution runs; all methods start with an empty skill set and evolved skills are directly injected. Bold denotes the best or results not significantly different from it under the authors’ paired bootstrap test (1,000 resamples, p < .05); yellow highlighting is the authors’ own. The strongest competing method for Qwen-3.5-9B is EvoSkill at 42.3: 47.4 − 42.3 = 5.1 pp. Both comparisons are whole-method comparisons and do not isolate the wiki’s causal contribution. SkillOpt already retains failed-edit feedback.

## 08 · Can one mistake teach the agent a reusable check?

- Role: RESULTS / USEFUL EXPERTISE / concept
- Purpose: Use a real source example to explain what learning changes before introducing comparison conditions.
- Visual: Two short narrative panels above an original Figure 10 calculation-check excerpt. This explains the observed update; it is not a new mechanism diagram.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10
- Speaker notes: FinEvo Appendix C follows a financial-statement-analysis report. Gross margin is the share of sales revenue left after subtracting the cost of those sales. The agent reported 40.02%; its revenue 115.05 and cost 67.88 imply (115.05 − 67.88)/115.05 = 41.00% after rounding. Tables 25–26 show the mistake and feedback. Table 27 and Figure 10 show the saved rule: recompute gross margin and verify the summary against detailed calculations. The original Figure 10 calculation-validation row is displayed, with other rows explicitly omitted. This is an actual reported edit, not an invented success story. No experiment isolates how many later errors this one instruction prevented. The paper tests a broader question with many tasks and alternative ways to retain experience, introduced next. Its Figure 1 benchmark overview and task workspace remain in appendix slide 37. Source inspected: v1 Appendix C.1–C.5, PDF pp.18–21; §§3–4.1. The agent learns in external instructions, not weight updates. Same starting model, paired task order and scoring do not imply equal token use.

## 09 · Why learn the check if an expert could supply it?

- Role: RESULTS / USEFUL EXPERTISE / comparison setup
- Purpose: Make the three practical alternatives understandable before the original result table.
- Visual: Three text columns defining the comparison conditions; no recreated empirical chart or replacement mechanism diagram.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10
- Speaker notes: The preceding report example makes a reusable instruction concrete. Now supply the crucial counterfactual: an expert could write a useful procedure beforehand. The next slide compares starting fresh, fixed expertise, and learned procedures. Fixed expert skills are derived from each scene’s reference workflow. The learning example highlighted next is skill-only evolution. FinEvo also tests memory-only and both memory plus skills, retained in the complete table. A skill packages reusable procedural instructions; memory here stores guidance in notes. Model weights remain fixed. The three alternatives are distinct conditions, not successive checkpoints and not learning added on top of expert initialization. The benchmark has 120 tasks (20 scenes × 6 cases) in three globally shuffled, interleaved orders. Source: v1 §§3–4.1, §4.4/Table 5. Equal tasks and model do not imply equal token cost.

## 10 · Learning adds 7 points over expert instructions

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Explain the three practical choices before interpreting the five original table rows; distinguish the gain from reset from the gain over expert instructions.
- Visual: Original complete Table 5 on the left, plain-language row definitions below it, and three guided score comparisons on the right.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10
- Speaker notes: Main takeaway: learned procedures score 7.04 points above expert instructions, with about 3.9 times the recorded execution-plus-reflection tokens (615600 / 159200 = 3.8668). The title rounds 7.04 to 7. The values compare separate systems; there is no experiment here adding learning to an expert-initialized agent. Whether the score improvement is worth its cost depends on the workload and value of errors prevented. Read the first, second, and last rows first. Starting fresh scores 71.58. Expert instructions supplied in advance score 86.67. Learning reusable procedures from feedback scores 93.71. Thus learning helps on these recurring tasks, but the relevant advantage over supplied expertise is 7.04 points, not the 22.13-point advantage over reset. These are alternative conditions, not a sequence of training checkpoints: the skill-only condition does not start from the fixed-expert-skill baseline. Explain the remaining rows next: memory-only updates stored notes (90.42); skill-only updates packaged procedures (93.71); full evolution permits both stores (89.47). The names describe allowed persistent representations, not progressively stronger intelligence. Full evolution did not beat either restricted update setting in this comparison; do not infer that combining stores always harms performance. The complete original Table 5 is preserved. Score is task quality /100; Comp. is compliance issues per task, lower is better; Exec. counts task-execution tokens; Reflect. counts post-task feedback processing and persistent-state updates. Costs are in 10^4 tokens per task. Fixed expert skill: 15.92 × 10^4 = 159,200 tokens. Skill-only: (17.53 + 44.03) × 10^4 = 615,600 tokens. Full evolution: (16.31 + 60.19) × 10^4 = 765,000 tokens. Visible totals round to 159k and 616k; these exclude judging and expert authoring. No lifetime cost or break-even estimate follows. One software framework, Claude Code, uses Qwen3.7-Max in this experiment; this is not a Claude-versus-Qwen model comparison. The full benchmark has 120 tasks and three shuffled orders; this table reports averages, not just final-task scores. No across-run intervals are reported. Table 3 separately reports improvements over reset for all four frameworks; its range is 9.33–19.37 points. Our practical interpretation: compare learning to strong initial guidance and include its extra cost. Transition to slide 11: another use for that compute is more attempts at solving the task. Source: FinEvo v1 §4.4/Table 5, PDF p.6; definitions in §4.1. No causal conclusion about individual memories, novel procedure transfer, or general recursive improvement.

## 11 · Could the same effort buy better answers directly?

- Role: RESULTS / USEFUL EXPERTISE / concept
- Purpose: Explain the core idea before its result.
- Visual: Original source conceptual figure, extracted without redrawing: Wang et al. · Harness evaluation v2 · Figure 2, p. 3 · All four panels and legend
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Harness critique v2 §3/Figure 2. Original Figure 2 shows the four mechanisms; guide attention to panels (a) and (c), while preserving the other panels and legend. Figure 1 is a results chart, not a mechanism overview. The displayed result next uses five rollouts without unit-test feedback; the separate train/validation/test experiment asks whether an evolved harness transfers. Equal rollouts do not match all compute costs. The shared harness is optimized across a batch (§3.4), unlike task-specific harness scaling (§3.5). Without tests, the final harness is used; parallel sampling uses model self-selection. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes. Transition from FinEvo: supplying expertise and improving the update recipe are not the only alternatives. Extra attempts can also buy task success.

## 12 · In this test, trying more solutions beats revising the agent

- Role: RESULTS / USEFUL EXPERTISE / result
- Purpose: Test reusable changes against extra inference.
- Visual: Original source extraction; Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; ReasoningBank — https://arxiv.org/abs/2509.25140v2 — §§3–4; retained lessons plus test-time search
- Speaker notes: This is a counterexample from one tested harness-evolution implementation, not a universal negative result. Table 1 compares five rollouts on 89 Terminal-Bench 2.1 tasks, three models, two runs, without test feedback. Retain the printed averages 67.4 and 72.3 despite rounded-cell arithmetic. A separate train/validation/test partition of 45/10/34 yields 68.3 for evolved versus 67.7 for initial harness on the 34 held-out tasks. Do not combine those experimental populations. No numerical CIs in the tables. Equal rollouts are not equal dollars or tokens; a reused harness could repay development cost across future tasks. Transition: follow the system beyond development and watch for damage. Visual: Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 showing per-model results and printed averages for direct sampling, parallel sampling, sequential refinement, harness evolution and harness scaling. Reported averages: parallel sampling 72.3, harness evolution 67.4. Source caption: unit tests unavailable, pass@1; bold is best and underline is second best. The displayed 67.4 is the printed average, without correcting the source’s rounded-cell arithmetic. ReasoningBank combines test-time search and retained lessons: computation and learning can complement each other. Report development cost separately from operating cost at explicit amounts of reuse. Equal attempts alone do not normalize dollars or tokens. Part takeaway: learned procedures can help, but expertise and extra attempts are serious alternatives. Next ask whether a gain survives continued use. Define pass@1 as success of the submitted answer, not the probability that any generated candidate passes. Five rollouts may be used inside a method; no unit tests are supplied for candidate selection here.

## 13 · Will earlier learning still help after more work?

- Role: RESULTS / DURABILITY / mini-introduction
- Purpose: Motivate the move from useful recurring lessons to changing workloads.
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Conceptual framing; no empirical claim.
- Speaker notes: The coding-to-web-research transition is an illustrative motivation, not a measured individual transfer result. Part 1 established useful local learning under demanding alternatives, without a full economic verdict. Part 2 distinguishes relevance failure from forgetting. Relevance means selecting experience that belongs in the current task. Forgetting means an update reduces performance on previously learned work under otherwise fixed conditions. Changed tools are a third failure mode, not automatically forgetting.

## 14 · Does memory still help when the work changes?

- Role: RESULTS / DURABILITY / concept
- Purpose: Define AgentStream as an evaluation, the retained-state loop, the reset baseline, and the three task arrangements before the result.
- Visual: Original Figure 1(b), preserved; plain-language stream definitions beside it and loop/baseline definitions below.
- Claims: C007
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: AgentStream is an evaluation framework, not a new learning algorithm. Six benchmarks contribute 50 tasks each; the same 300 tasks recur under three ordering seeds. Three models and five update methods are tested. A domain here means one benchmark, not an inferred user topic. Read Figure 1(b) left to right: q is the next task; the robot acts; the bottom green row is retained state carried to the next task. What changes is external guidance (context, memories, skills or harness), not model weights. State starts empty. Isolated still learns across tasks within each benchmark; it is not the no-learning control. Sequential carries one history across complete benchmark blocks; interleaved carries it across shuffled domains. Within-domain task order is held fixed for comparison. The baseline keeps evolution state empty on every task. Updates see execution outcomes and self-reflection, without ground-truth labels; unlike FinEvo, no rubric-derived corrections are supplied. Figure 1(a), the baseline panel, is omitted but defined visibly. This sets up the next question: does a method that helps with separate histories also help with shared mixed-domain history? Source: v1 §§3–4, Figures 1–2.

## 15 · The same memory method can help or hurt

- Role: RESULTS / DURABILITY / result
- Purpose: Use ACE’s sign reversal and ReasoningBank’s contrasting response to explain why workload-specific evaluation matters.
- Visual: Original Table 5, complete; external interpretation of contrasting method responses.
- Claims: C007, C013, C016
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: Read the ACE row first: +2.28 isolated, +2.26 sequential, −1.26 interleaved. These are separate experimental conditions, not three successive stages of learning. Negative means worse than the same model with no retained lessons. Then read ReasoningBank: +0.78, +0.46, +1.79. The talk needs this contrast so the audience does not conclude that mixing always hurts. ACE integrates an accumulated playbook into the prompt; ReasoningBank retrieves selected entries from an external store. Other methods and all three conditions remain in the original table. The visible takeaway is workload dependence, not proof that retrieval caused the difference. All methods differ in multiple components. Inspected AgentStream v1 PDF p.11, complete Table 5, caption, §5.4 and Table 6. Table 5 averages over three models and three order seeds, nine shared-task configurations per method. Positive/negative figures are percentage-point gains over the same model’s no-evolution baseline; the source labels them gain (%). Last columns count which scenario wins in nine configurations; a tie explains totals below nine. ACE keeps a playbook integrated into context. A-Mem and ReasoningBank retrieve entries from external stores. Each method differs in multiple components, so this is not a retrieval-only ablation. Sequential carries state across domain blocks; interleaved shuffles tasks across domains; isolated has separate state for each benchmark. No confidence interval is in this table. The full aggregate-count calculation is retained in the appendix. Contrast with FinEvo is not causal: tasks, metrics, feedback, models and protocols differ. Takeaway: storing experience is insufficient; its relevance to the next task matters. Practical implication (our interpretation): evaluate retained experience on the intended task mix; selective reuse is a candidate explanation to test, not an identified cause. AgentStream does not track one particular lesson causing one later error and does not directly establish forgetting. SEAL next tests earlier knowledge after subsequent updates. Transition to SEAL: AgentStream examined whether saved external guidance fits the workload. Now switch to learning through model weights and ask whether learning new information damages earlier knowledge. These are different failure modes, not matched methods in one benchmark.

## 16 · Can SEAL learn new facts without losing old ones?

- Role: RESULTS / DURABILITY / concept
- Purpose: Set up the retention question and explain how SEAL learns before showing either result.
- Visual: Original Figure 1 kept full-width; plain-language steps and figure key below it.
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Why SEAL is in this section: AgentStream tested the usefulness of saved external guidance; SEAL lets us test whether gains stored in model weights survive later learning. This is a language-model adaptation study used to explain a component of self-evolving agents, not a full autonomous-agent benchmark. SEAL expands to Self-Adapting LLMs. In the knowledge-incorporation setting, a supplied passage becomes generated training text (called a self-edit); gradient-based finetuning on the passage and generated text changes the weights. Questions are answered without the passage in the prompt. Figure 1 shows candidate edits tried on separate model copies, followed by answer evaluation. Inner loop: learn the passage using that text. Outer loop: reward the generation of text that makes the inner learning effective. The model learns how to prepare its training data; the evaluator and update algorithm remain externally specified. The figure is general: self-edits can also include optimization directives in other settings. Ctx means context, LM language model, SE self-edit, theta model weights, and Ans answer. Read the diagram once left to right; do not require the audience to parse the loss expression. Next test one new passage (Table 2); then test earlier passages after successive new updates (Figure 6). These are separate experiments. Source: SEAL v2 §3, Figure 1, §4.2 and Appendix B.

## 17 · SEAL improves answers about a newly learned passage

- Role: RESULTS / DURABILITY / result
- Purpose: Establish that SEAL learns new information successfully before asking whether later learning preserves it.
- Visual: Original source extraction; Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Interpretation below, separate from source artwork.
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Test 1 asks whether learning to generate training text improves new-passage answers. Use the first numeric column, not a comparison across columns. Each held-out passage is learned separately, and the model is tested without the passage in its prompt. The table aggregates 974 questions from 200 held-out SQuAD passages using Qwen2.5-7B. Both 39.7 and 47.0 train on the original passage plus generated text; the distinction is whether the generator was previously trained to produce effective self-edits. Their difference is 7.3 percentage points. Base model 32.7 means no adaptation; passage-only training yields 33.5. GPT-4.1-generated text yields 46.3 here and outperforms SEAL in both multi-passage columns. LoRA is an efficient weight-update method; full-FT means full finetuning. The other columns train on many passages together, not the sequential-retention test. Questions share passages and final-score repeated-run uncertainty is not supplied. All methods use tuned hyperparameters; these scores are not matched lifetime-cost estimates. Preserve the complete Table 2 and all comparators. Transition: now that we know a single update helps, does that gain survive learning other passages? Source: SEAL v2 §4.2, Table 2 p.8, Appendix B.

## 18 · SEAL’s earlier gains shrink as it learns more passages

- Role: RESULTS / DURABILITY / result
- Purpose: Distinguish adaptation quality from continual retention using one developed method.
- Visual: Original cropped source artwork on the left; large reading guidance on the right.
- Claims: C004, C020
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Gradient Episodic Memory for Continual Learning — https://papers.neurips.cc/paper/2017/file/f87522788a2be2d171666752f97ddebb-Paper.pdf — §§1–3: stability–plasticity, forward/backward transfer
- Speaker notes: Re-read SEAL v2 §5 pp.8–9 and Appendix B.6. The paper sequentially updates on new passages and revisits prior tasks. Read downward after a passage is first incorporated; many earlier-passage scores decline, but not every adjacent cell declines and no universal collapse is claimed. The original colormap, cell values and axes remain unchanged. §5 states retention is not explicitly optimized. Table in B.6 gives entrywise SEM, but the nearby text does not make the repeat denominator clear. This is a distinct evaluation from Table 2, not the same task average tracked across time. Other recipes can sustain bounded gains: C019 and the Continual Internalization reading note remain in supporting research. Removing its rushed slide does not imply all weight learning fails. Concrete reading guide: Figure 6 column 0 has 0.33 at row 0, 0.38 at row 1, and 0.19 at row 8. Multiply the displayed fractions by 100 for the visible 33%, 38%, 19%. These are reported aggregate cell accuracies, not an individual question trajectory or a statistical significance claim. The top row precedes all edits; row 1 follows learning passage 0; row 8 follows all eight passage updates. Part synthesis: AgentStream concerns the relevance of external guidance; SEAL concerns retention through weight changes. Neither higher new-task accuracy nor saved state alone establishes lasting improvement. Bridge to Sidekick: training systems need to decide which corrections to learn from and what old experience to revisit.

## 19 · Who tells a learning agent that it made a mistake?

- Role: RESULTS / DURABILITY / result
- Purpose: Production learning needs a source of reliable corrections
- Visual: Flat sequence of changing components opposite the fixed external support.
- Claims: C010, C016
- Sources: Sidekick’s continual learning loop — https://shopify.engineering/sidekicks-continual-learning-loop — Harness optimization; trajectory repair; training; GraphQL sections; Reward Hacking Benchmark — https://arxiv.org/abs/2605.02964v1 — §§4–6; evaluation integrity separate from task correctness
- Speaker notes: Shopify describes a production pipeline rather than releasing a controlled longitudinal evaluation. Product criteria become rubric judges. Harness search modifies prompts, tool descriptions and orchestration. Frontier models repair low-scoring trajectories; unresolved cases go to human annotators. Repaired trajectories feed SFT and GRPO; old and new trajectories are reused in daily full-parameter training. Serving compression learns gist tokens. Treat all as company-described architecture. The article supplies no component ablations or cycle-by-cycle held-out quality. A shared judge can propagate a blind spot across stages, but that possibility is not proof of reward hacking. We deliberately omit the estimated 96% cost saving because it does not measure the total causal value of continual learning. Shared judges may carry correlated blind spots across selection and assessment; this does not establish observed gaming at Shopify. Reward Hacking Benchmark distinguishes evaluator integrity from task correctness. An evaluator outside edit permissions is our design recommendation, not a sufficient guarantee. Part takeaway: retention and continued gains depend on the setting; production combines several loops without isolating their benefits. Can the method that produces changes itself improve? Keep report and recommendation distinct: the separate-evaluation sentence is our implication, not a claim that Shopify has released an independent longitudinal evaluation. Reliable correction is the common requirement across generated lessons and training data.

## 20 · Can the agent improve how it proposes its next change?

- Role: RESULTS / IMPROVING THE IMPROVER / mini-introduction
- Purpose: Can experience improve the adaptation process?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C009, C021
- Sources: Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Model-Agnostic Meta-Learning — https://proceedings.mlr.press/v70/finn17a/finn17a.pdf — §2; Algorithm 1
- Speaker notes: Meta-learning is the broader question. SEAL supplied a learned update-data example; MAML is a learned-initialization example. This section develops editable improvement code as a further route, not a definition or prerequisite. Hyperagents offers bounded transfer evidence. The main claim remains future-task value; acceleration would require several cycles of better gains per resource.

## 21 · Hyperagents can edit the code that proposes improvements

- Role: RESULTS / IMPROVING THE IMPROVER / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Original cropped source artwork on the left; large reading guidance on the right.
- Claims: C009, C014, C017
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §3/Figure 1. Start with the bottom archive: select a parent, invoke its meta agent to propose an edited child, evaluate the child task agent, add it to the archive. A child may change task code, meta code, or both. The outer archive/selection/evaluation remains specified externally. Top: DGM retains handcrafted improvement-instruction generation. Small right-hand traces illustrate the same contrast; the large central loop carries the explanation. Editability is a mechanism, not evidence that learning accelerates. Next: freeze the resulting improver and see whether its improvement behavior transfers. SICA/DGM boundary details remain in the appendix. Crop retains original left/central panels for both systems; the small right-hand implementation traces are omitted and labeled. The comparison is not an assertion that DGM lacks an archive or that Hyperagents has no external controls.

## 22 · A developed system makes useful progress on a new task

- Role: RESULTS / IMPROVING THE IMPROVER / result
- Purpose: A developed implementation can help learning in a new domain
- Visual: Original Figure 3 middle/right held-out panels, with all their comparators and uncertainty; training panel omitted.
- Claims: C009
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §§5.1–5.2: select transferred implementations from paper review and robotics reward design, then hold their meta agents fixed for 50 candidate-generation iterations on math grading. Improvement@50 is the held-out score gain of the best validation-selected task agent over its starting agent. Five runs: median 0.630, 95% bootstrap interval 0.540–0.630; initial implementation 0.000 (0.000–0.130). Authors report p<.05; repository audit identifies one-sided tests and run-array bootstrap, not task-population uncertainty. The entire task/meta implementation transfers and initial task behavior has formatting failures. This supports useful transferable improvement behavior without isolating meta code from the rest of the implementation. Figure caption uses stronger language about generality; our title narrows it to the tested domain. Next ask whether that starting advantage remains under continued meta evolution. The on-slide definition separates a gain metric from an endpoint score. Separate continued-evolution experiment is now in the appendix: 0.640 vs 0.610 at 200 iterations, p>.05; it does not contradict the fixed-method result. It leaves added long-run advantage uncertain. No isolated portable improver or repeated efficiency gain is claimed.

## 23 · Learning is useful when a correction helps again

- Role: CONCLUSION / synthesis
- Purpose: Experience can pay when useful expertise is reused
- Visual: Three equal cards, without arrows or an implied progression.
- Claims: C004, C005, C007, C011, C020
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Answer the opening question: experience is a promising investment when it supplies expertise absent at the start and future work reuses it, provided relevant state is selected, reliable feedback corrects it, earlier abilities survive, and total costs are justified. This is our conditional synthesis, not a causal cross-benchmark finding. FinEvo’s token accounting and the harness comparison are partial evidence, not a full lifetime economic test. Reuse volume, task recurrence, starting expertise and feedback quality are variables to test. Hyperagents adds bounded transfer evidence without moving sustained compounding into the established column.

## 24 · Test whether the correction changes what happens next time

- Role: CONCLUSION / implications
- Purpose: Test reuse, retention, and cost on the same task stream
- Visual: Four-row decision table, Codex Grid 14.
- Claims: C011, C012, C020
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Hold out new task families and a later time period before optimizing the system. Revisit earlier tasks to measure retention, failures and regressions, not only the best checkpoint. Count search, weight updates, execution and evaluation: cheap deployment can hide expensive optimization. Use independent repeated runs and a separately designed evaluator. An evaluator can still be wrong; report calibration and the unit of uncertainty. To claim acceleration rather than improvement, repeated cycles would need increasingly efficient gains, not just a higher score. These are recommendations grounded in the observed limitations, not empirical guarantees. Report development cost and operating cost separately at stated reuse volumes. Sustained compounding needs several cycles of improved learning efficiency, adjusted for task difficulty and resources; a D-versus-C endpoint win alone is insufficient. Detailed control arms and frozen-versus-adaptive test lanes are in the appendix. These proposed tests operationalize the conditional conclusion rather than claiming every paper must satisfy every test. Hold model, feedback and budget fixed when varying recurrence/mixing. The earlier row called “does it repeat?” conflated replication with repeated learning-efficiency gains; replication is now in the caveat, and compounding is treated separately.

## 25 · When would you choose to keep learning?

- Role: CONCLUSION / DISCUSSION / discussion
- Purpose: When would you choose to keep learning?
- Visual: Three spacious numbered prompts with a concrete evidence anchor.
- Claims: C004, C005, C007, C011, C012
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: Close on decisions rather than repeat the synthesis. Question 1: compare all displayed FinEvo alternatives, including missing authoring/judging costs and uncertainty; do not treat score differences as money. Question 2: distinguish irrelevance, outdated dependencies, and forgetting. Question 3: make a prediction under a particular reuse volume and task distribution, then identify a result that would falsify it. Optional improver-transfer discussion and the separate Hyperagents endpoint experiment are in the appendix.

## 26 · Appendix · continued evolution leaves an uncertain advantage

- Role: APPENDIX / appendix
- Purpose: Distinguish the uncertain endpoint advantage from the positive fixed-improver transfer result.
- Visual: Original Figure 4 with both panels and uncertainty; separate from Figure 3.
- Claims: C009
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Keep this separate from Figure 3. Here task and meta code may both continue evolving after transfer. After 200 iterations, transferred agents reach median held-out score 0.640 versus 0.610 from initial implementation, across five runs; run-bootstrap 95% intervals are 0.550–0.720 and 0.510–0.680. Authors explicitly report p>.05. The plot includes a separate ProofAutoGrader transfer condition and representative baseline, preserved as context rather than the chosen comparison. The first experiment supports bounded transfer of improvement behavior; this experiment leaves added long-run advantage uncertain. Lack of significance is not an equivalence test. Neither measures repeated improvement in learning efficiency at matched resources. Main-talk definition: improvement@50 is a gain; this appendix result is endpoint score. All intervals and original comparators remain in the source figure.

## 27 · Appendix · stream averages hide configuration differences

- Role: APPENDIX / appendix
- Purpose: Show why aggregate improvement can hide regressions.
- Visual: Prominent mean and flat three-row table, adapted Codex Grid 14.
- Claims: C007, C013, C016
- Sources: AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Library Drift — https://arxiv.org/abs/2605.19576v3 — §§5–7; retrieval, storage, retirement; EvoHarnessBench — https://arxiv.org/abs/2609.04280v2 — §§3–4; evolving tools, skills and specialist agents
- Speaker notes: AgentStream evaluates six benchmarks with 50 tasks each: 300 distinct tasks, reused across three order seeds. The three models and five methods make 45 model–method–seed cells per stream condition. For interleaving, 28 cells are positive and 17 negative. The local audit reproduces the means and the printed variability as sample SD of three seed means, not a confidence interval or SD over 45 independent datasets. Methods share tasks; benchmark metrics differ. FinEvo and AgentStream use different tasks and feedback, so their effect sizes are not a head-to-head ranking. The uncertainty about causes remains: retrieval, interference, and feedback quality require controlled ablations. The thesis also notes AgentStream Tables 5–6: ACE shifts from positive average gain in isolated streams to negative in interleaved streams, whereas ReasoningBank and A-Mem have their largest mean gains in interleaved streams. This is consistent with relevance selection mattering, but the methods differ in more than retrieval. Library Drift and EvoHarnessBench motivate testing skill retirement and changed interfaces; they do not estimate the same failure rate. The row labels define the streams from §3.2; the earlier homemade domain-order strings have been removed. Isolated still learns within each domain. Methods differ in more than retrieval. Numeric cells remain the documented calculation.

## 28 · Appendix · compare four practical alternatives fairly

- Role: APPENDIX / appendix
- Purpose: Compare practical alternatives while making initial-state matching and the paired reset requirement explicit.
- Visual: Editable four-arm table; clearly labeled proposed experiment.
- Claims: C012
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: This is a proposed protocol, not an established result. Give four practical alternatives the same task stream, feedback access and common total resource ceiling. C and D must begin with identical task code, improvement code and retained state. A strong fixed procedure can have a different starting method; account for authoring cost. A paired reset counterpart to a retained-state arm separately tests experience. The four alternatives alone do not identify four independent causal effects. D beating C is useful within this protocol but does not by itself prove isolated improver transfer or compounding.

## 29 · Appendix · separate what it knows from what it can learn next

- Role: APPENDIX / appendix
- Purpose: Turn the thesis’s corrected experiment into an explicit design.
- Visual: Two test lanes with a shared matched-start control beneath.
- Claims: C009, C012
- Sources: Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: After development, freeze copies to test accumulated capabilities on fresh cases, new task families and earlier tasks. Separately let copies adapt on new streams to measure future learning. To isolate improvement-method transfer, attach learned and original improvement methods to identical task agents with identical retained state. Hold both methods fixed during candidate generation and match feedback/resources. This directly addresses the confounding of whole-implementation transfer in Hyperagents §5.2. Repeat across streams and report independent-run uncertainty. A single favorable transplant is bounded meta-learning, not sustained compounding.

## 30 · Appendix · read each number with its denominator

- Role: APPENDIX / appendix
- Purpose: Keep uncertainty and independence available during discussion.
- Visual: Concise methods table; no pooled effect.
- Claims: C003, C004, C005, C006, C007, C009
- Sources: WikiSkill — https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Self-Adapting Language Models (SEAL) — https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10; Rethinking the Evaluation of Harness Evolution for Agents — https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; AgentStream — https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Different metrics, tasks, populations and resource budgets must not be pooled. SEAL Table 2 questions share passages; Figure 6 is a separate sequential-edit test with entrywise SEM and unclear repeat denominator. AgentStream 45 cells share 300 tasks; Table 2 printed variability is sample SD of three seed means. Hyperagents CIs quantify five-run variation, not task-population uncertainty; improvement@50 and final score are distinct. These values are source-reported or documented calculations, not replicated experiments.

## 31 · Appendix · one-shot authoring is a different test

- Role: APPENDIX / appendix
- Purpose: Include the expanded thesis’s curated-skill counterfactual without misreading it.
- Visual: Two-column conceptual contrast; no recreated result chart.
- Claims: C018
- Sources: SkillsBench — https://arxiv.org/abs/2602.12670v4 — Tables 2/6; Appendix D.6
- Speaker notes: SkillsBench v4 Tables 2/6 and Appendix D.6: 87 tasks, 18 configurations, three trials in the curated-skills study. Curated configuration-macro pass rate is 33.9→50.5%; 13 tasks have negative deltas. The self-generation diagnostic includes three configurations, each below no-skills (−8.1/−11.3/−11.5 pp). It is one-shot authoring without repeated outcome feedback. Human authoring effort is not matched, skill packs include scripts/assets, low-signal filtering can enrich skill-sensitive tasks, and authoring-run uncertainty is absent. The design is valuable as a strong curated baseline but cannot establish continual learning failure.

## 32 · Appendix · editing an agent and editing its improver differ

- Role: APPENDIX / appendix
- Purpose: Introduce meta-improvement through a precise predecessor comparison.
- Visual: Three-row comparison of editable components and external constraints.
- Claims: C013, C014, C017
- Sources: Self-Improving Coding Agent — https://arxiv.org/abs/2504.15228v2 — §3; Algorithm 1; Darwin Gödel Machine — https://arxiv.org/abs/2505.22954v3 — §§2–4; Hyperagents §1/Appendix B for the boundary; Hyperagents — https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Gödel Machines — https://arxiv.org/abs/cs/0309048v5 — §§2.2/3.2/4.1
- Speaker notes: SICA §3/Algorithm 1 retains an archive but expands the best-scoring agent. DGM explores alternate lineages, allowing weaker stepping stones, but retains a handcrafted improvement-instruction generator. Hyperagents puts task and improvement code in the same editable implementation while retaining an outer archive/evaluation procedure. These are related systems, not independent confirmations. STOP already edits improvement code; this is not a claim that Hyperagents invented self-modification. Gödel Machines requires a utility-improvement proof under encoded assumptions; empirical DGM does not inherit that guarantee.

## 33 · Appendix · primary sources 1/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference index
- Sources: Analyst framing; claim ledger.
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 34 · Appendix · primary sources 2/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference index
- Sources: Analyst framing; claim ledger.
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 35 · Appendix · primary sources 3/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference index
- Sources: Analyst framing; claim ledger.
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 36 · Appendix · primary sources 4/4

- Role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference index
- Sources: Analyst framing; claim ledger.
- Speaker notes: References supporting the selected talk and appendix. The research register records exact versions and access depth. Recent experimental sources are mostly preprints; SEAL has a NeurIPS conference version. Foundational reviews are scoped to the mechanisms used, not new empirical comparisons. Source findings were not experimentally reproduced.

## 37 · Appendix · what work does FinEvo ask the agent to do?

- Role: APPENDIX / supporting concept
- Purpose: Retain the original benchmark overview and show a concrete task workspace without interrupting the main report-error story.
- Visual: Complete original Figure 1, both panels, inspected against the source PDF page.
- Claims: C005
- Sources: FinEvo-Bench — https://arxiv.org/html/2608.06144v1 — §§3–4; Table 5; Appendix C / Tables 25–27 / Figure 10
- Speaker notes: Figure 1 is a task and workspace overview, not a persistence-protocol diagram. In the right panel, the agent receives a stock-analysis request and six input files and must write a structured report using the supplied information. This is a different example from the financial-statement error developed on slide 8. Financial-statement tasks, claims, and client communication are among the recurring scenes. Within a scene, different cases share procedures but need different calculations and conclusions. Source: FinEvo v1 Figure 1 and §§3–4.1. Original artwork preserved.
