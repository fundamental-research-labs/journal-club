# Presentation storyboard

Revision: September 18, 2026 — explain ideas before interpreting results. Existing quantitative claims, source versions, and September 16 research cutoff preserved.

## Narrative and visual direction

25 main slides + 11 appendices; approximately 30–35 minutes plus discussion. Introduction (1–4), useful procedures (5–11), durability (12–16), improving the improver (17–21), conclusion/discussion (22–25). Keep the forest-green/ivory palette, editable sources, offline images, and presenter attribution. Concept slides get their own space; original result artwork and caveats remain intact.

## Core idea → evidence audit

| Substantive example | Visible explanation | Evidence | Conceptual source reviewed / choice |
| --- | --- | --- | --- |
| WikiSkill | 6: traces → persistent wiki → candidate skill; rollback does not erase wiki | 7 | §3/Figure 2; original Figure 2, complete framework |
| FinEvo | 8: related cases, post-task feedback, retained procedure, paired reset | 9 | Figure 1/§§3–4.1; original Figure 1 shows coverage and a sample task; subtitle explains the persistence control |
| Harness critique | 10: batch traces → meta-agent edits shared harness → reuse; fixed-harness sampling control | 11 | Figure 2/§§3.2–3.4; original Figure 2 retains all four panels and legend; subtitle guides attention to (a) and (c) |
| AgentStream | 13: original Figure 1(b), explicitly identified as an evaluation framework | 14, with state definitions | Figures 1–2/§3; original panel (b); homemade ordering diagram removed; panel (a) omitted explicitly |
| R-Zero / Continual Internalization | 15: Challenger/Solver curriculum vs lessons → step guidance → successful-trajectory training | 15 | §2 and §§3–5, respectively; visible text explains the update recipes without conflating their results |
| Shopify Sidekick | 16: harness, repair, training, compression and dependencies | 16: company architecture, no isolated efficacy claim | Existing first-party process explanation retained |
| Hyperagents | 18: original Figure 1; task and meta code in one editable program | 19–20 | §3/Figure 1; predecessor table moved to 32, preserving detail |
| Dream-RSI | 21: replay histories → select controller edit → online search | 21 | Existing §3-based explanation and replay limitation retained |
| SEAL | 28: original Figure 1; self-edits supply training data/update instructions, downstream tests reward them | 29 | §3/Figure 1, inner weight updates vs outer policy learning explained in notes |
| SkillsBench | 31: curated vs absent vs one-shot self-authored skills | 31 | Existing scoped comparison made explicit in visible subtitle |

Incidental names on the opening map and citation-only supporting references are not separate paper reviews. No extra numerical claims introduced. The prior scholarly-foundations/expanded-thesis reconciliation remains a separate pending task.

Paper-specific conceptual diagrams use source artwork wherever it exists. Slides 6, 8 and 10 now use the original WikiSkill Figure 2, FinEvo Figure 1 and harness Figure 2. No homemade replacement is justified by simpler styling or a different explanatory emphasis.

## Sequence and claim traceability

## 01 · Self-evolving agents
- Section / role: INTRODUCTION / introduction
- Purpose: Introduce the topic and practical promise.
- Visual: Large typographic cover; Codex Grid 01.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Open with the possibility that work is valuable twice: the completed task and a procedure that helps later. The revised thesis separates useful procedures, transferable improvement behavior, and sustained compounding. The first has bounded positive evidence; the second has promising finite evidence; the third remains unestablished. This is a presentation revision of the latest local thesis, retaining its September 16 research cutoff.

## 02 · Why should the next task be easier?
- Section / role: INTRODUCTION / introduction
- Purpose: Why should the next task be easier?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Motivate the topic before stating findings. A completed task may also teach a reusable procedure, but an explanation of one success or failure may not apply again. Here self-evolution means experience changes retained state that affects later behavior; retaining more history alone does not establish improvement. Next: locate the components that can change.

## 03 · A lesson can change context, software, or weights
- Section / role: INTRODUCTION / concepts
- Purpose: Give a map of update mechanisms.
- Visual: Editable four-row comparison table, Codex Grid 14.
- Claims: C001, C002, C004, C013, C014
- Sources: Voyager: https://arxiv.org/abs/2305.16291v2 — §§2–3; WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; GEPA: https://arxiv.org/abs/2507.19457v2 — Algorithm 1; §4; Self-Adapting Language Models (SEAL): https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; STOP: https://arxiv.org/abs/2310.02304v3 — Algorithm 1; §3; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: These are editable components, not levels on a universal capability ladder. A harness is the instructions and software that organize model calls and tool use. Weight updates change numerical model parameters. Improver code chooses how candidate changes are generated or searched. STOP already edited improver code in 2023, so avoid presenting meta-improvement as a new 2026 invention. Ask which decisions remain outside the loop. GEPA uses traces to propose prompts and keeps complementary candidates; it is an example of harness/prompt search, not a numerical comparison here. Automated design can produce a reusable fixed program without improving the designer. SEAL makes generated update data the object of learning: Table 2 is in the appendix. None of these state carriers guarantees useful transfer. Transition: these mechanisms define what can change. The central question is whether the changes create a lasting advantage worth learning.

## 04 · When does experience create a lasting advantage worth the cost?
- Section / role: INTRODUCTION / main-question
- Purpose: When does experience create a lasting advantage worth the cost?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: This is the main question. We will ask first whether experience yields a useful procedure, then whether the gain survives changing tasks, and finally whether experience can improve how the agent learns. Keep usefulness, transfer, and efficiency separate.

## 05 · Can experience become a useful procedure?
- Section / role: RESULTS / USEFUL PROCEDURES / mini-introduction
- Purpose: Can experience become a useful procedure?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: The first requirement is turning one attempt into guidance that helps later. WikiSkill supplies a concrete mechanism and positive result. FinEvo and the harness critique test competing explanations: supplied expertise and extra attempts. None of these comparisons alone isolates every causal component.

## 06 · A rejected skill can leave a useful lesson
- Section / role: RESULTS / USEFUL PROCEDURES / concept
- Purpose: Develop the latest thesis’s central mechanism example.
- Visual: Original source conceptual figure, extracted without redrawing: Tang et al. · WikiSkill v1 · Figure 2, p. 4 · Complete diagram; caption omitted
- Claims: C003, C013
- Sources: WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; SkillOpt: https://arxiv.org/abs/2605.23904v2 — §§3.5–3.6; rejected edits retained as feedback
- Speaker notes: WikiSkill §3/Figure 2: a maintenance agent consolidates traces in the wiki; a skill agent uses both the wiki and original traces to propose skills. The task agent receives skills directly, not the wiki. Validation can reject a skill while the accumulated wiki persists. SkillOpt already keeps rejected-edit feedback; separate organized knowledge is the distinction, not first use of failure. Our inference: the validation gate tests a procedure, not the truth of every retained interpretation. A rejected proposal can leave a mistaken lesson as well as a useful one. Proposed wiki test: retain versus remove an entry from a rejected proposal, then compare the quality of subsequent proposals. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes.

## 07 · Learned skills beat both no skills and a strong rival
- Section / role: RESULTS / USEFUL PROCEDURES / result
- Purpose: Establish a positive retained-state result.
- Visual: Original source extraction; Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Interpretation below, separate from source artwork.
- Claims: C003, C013
- Sources: WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B
- Speaker notes: WikiSkill separates traces, accumulated wiki knowledge, and deployed skills. When a candidate skill is rejected, knowledge from the attempt can still persist. Qwen-3.5-9B gains 17.5 percentage points in macro accuracy across five benchmarks with equal benchmark weighting and three evolution runs. Test sizes are 124, 85, 280, 172, and 134. Table 1 gives no numerical confidence intervals. Skills are directly injected, validation sets are small, and OfficeQA has reference-page assistance. Qwen-3.5-4B declines from 30.2 to 28.5 on OfficeQA. The result supports useful benchmark learning, not universal improvement. Transition: compare learning against a strong procedure supplied from the start. Visual: Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 excerpt, including all methods for Qwen-3.5-4B and 9B. Qwen-3.5-9B average rises from 29.9 to 47.4; Qwen-3.5-4B OfficeQA falls from 30.2 to 28.5. Original Table 1 caption: scores average three full evolution runs; all methods start with an empty skill set and evolved skills are directly injected. Bold denotes the best or results not significantly different from it under the authors’ paired bootstrap test (1,000 resamples, p < .05); yellow highlighting is the authors’ own. The strongest competing method for Qwen-3.5-9B is EvoSkill at 42.3: 47.4 − 42.3 = 5.1 pp. Both comparisons are whole-method comparisons and do not isolate the wiki’s causal contribution. SkillOpt already retains failed-edit feedback.

## 08 · FinEvo tests whether a procedure survives a new case
- Section / role: RESULTS / USEFUL PROCEDURES / concept
- Purpose: Explain the core idea before its result.
- Visual: Original source conceptual figure, extracted without redrawing: Deng et al. · FinEvo-Bench v1 · Figure 1, p. 3 · Both panels; caption omitted
- Claims: C005
- Sources: FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5
- Speaker notes: FinEvo v1 Figure 1 and §§3–4.1. Figure 1 depicts task coverage and a stock-analysis example; the visible subtitle explains the persistence control used in the evaluation. 20 scenes × 6 cases = 120 tasks. Streams interleave scenes. Agents receive post-task problem/reason summaries, not the hidden rubric. The next slide adds fixed expert skills as a strong alternative to learning. Original artwork retained. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes.

## 09 · A strong fixed skill captures much of the gain
- Section / role: RESULTS / USEFUL PROCEDURES / result
- Purpose: Present the strongest specialization alternative.
- Visual: Original source extraction; Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C005
- Sources: FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5
- Speaker notes: FinEvo tests recurring professional procedures with 120 financial tasks in 20 scenes and three shuffled task orders. Four scaffolds use the same Qwen3.7-Max backbone. Paired gains over reset range from 9.33 to 19.37 rubric points. The displayed Table 5 ablation is only the Claude Code scaffold: these labels are software frameworks, not vendor model identities. Reset is 71.58, fixed expert skill 86.67, unrestricted evolution 89.47. The 2.80-point difference is descriptive, not a tested causal advantage at matched cost. No across-run intervals are reported. Scoring and feedback share rubric design. Strong recurring-procedure evidence; novel procedures and full cost remain unresolved. Visual: Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original FinEvo Table 5, all five conditions, score, compliance, execution and reflection costs. Reset 71.58, fixed expert skill 86.67, full evolution 89.47, memory only 90.42, skill only 93.71. Source table definitions: Score is the rubric score; Comp. is compliance issues per task; costs are 10^4 tokens per task. Table 5 is on PDF page 6 in the retrieved v1; earlier reading notes said page 7. The four-scaffold paired-reset experiment uses 120 tasks and three orders, with 9.33–19.37 rubric-point gains. This Table 5 comparison is one scaffold only. SkillsBench adds a curated-skill counterfactual, but its one-shot self-authoring diagnostic does not test iterative learning; see appendix.

## 10 · Spend the next attempt on a solution—or the harness?
- Section / role: RESULTS / USEFUL PROCEDURES / concept
- Purpose: Explain the core idea before its result.
- Visual: Original source conceptual figure, extracted without redrawing: Wang et al. · Harness evaluation v2 · Figure 2, p. 3 · All four panels and legend
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Harness critique v2 §3/Figure 2. Original Figure 2 shows the four mechanisms; guide attention to panels (a) and (c), while preserving the other panels and legend. Figure 1 is a results chart, not a mechanism overview. The displayed result next uses five rollouts without unit-test feedback; the separate train/validation/test experiment asks whether an evolved harness transfers. Equal rollouts do not match all compute costs. The shared harness is optimized across a batch (§3.4), unlike task-specific harness scaling (§3.5). Without tests, the final harness is used; parallel sampling uses model self-selection. The source conceptual figure replaces the previous homemade diagram at the user’s request. No simplification of the artwork; explanation belongs in the subtitle and notes.

## 11 · More attempts are a serious competing baseline
- Section / role: RESULTS / USEFUL PROCEDURES / result
- Purpose: Test reusable changes against extra inference.
- Visual: Original source extraction; Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C006
- Sources: Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; ReasoningBank: https://arxiv.org/abs/2509.25140v2 — §§3–4; retained lessons plus test-time search
- Speaker notes: This is a counterexample from one tested harness-evolution implementation, not a universal negative result. Table 1 compares five rollouts on 89 Terminal-Bench 2.1 tasks, three models, two runs, without test feedback. Retain the printed averages 67.4 and 72.3 despite rounded-cell arithmetic. A separate train/validation/test partition of 45/10/34 yields 68.3 for evolved versus 67.7 for initial harness on the 34 held-out tasks. Do not combine those experimental populations. No numerical CIs in the tables. Equal rollouts are not equal dollars or tokens; a reused harness could repay development cost across future tasks. Transition: follow the system beyond development and watch for damage. Visual: Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 showing per-model results and printed averages for direct sampling, parallel sampling, sequential refinement, harness evolution and harness scaling. Reported averages: parallel sampling 72.3, harness evolution 67.4. Source caption: unit tests unavailable, pass@1; bold is best and underline is second best. The displayed 67.4 is the printed average, without correcting the source’s rounded-cell arithmetic. ReasoningBank combines test-time search and retained lessons: computation and learning can complement each other. Report development cost separately from operating cost at explicit amounts of reuse. Equal attempts alone do not normalize dollars or tokens. Part takeaway: learned procedures can help, but expertise and extra attempts are serious alternatives. Next ask whether a gain survives continued use.

## 12 · Do the gains survive the next tasks?
- Section / role: RESULTS / DURABILITY / mini-introduction
- Purpose: Do the gains survive the next tasks?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Part 1 found useful local gains with demanding baselines. A system deployed repeatedly must also cope with changing tasks and preserve earlier abilities. We now examine mixed streams, repeated learning, and a production architecture. The production account describes a pipeline; it is not a controlled efficacy result.

## 13 · AgentStream carries experience into the next task
- Section / role: RESULTS / DURABILITY / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Yan et al. · AgentStream v1 · Figure 1(b); independent-evaluation panel (a) omitted
- Claims: C007
- Sources: AgentStream: https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13
- Speaker notes: AgentStream v1 §3.1/Figure 1. This is an evaluation framework, not a new learning algorithm. Read left to right along the tasks; then follow the feedback down into retained state and forward to the next task. State starts empty. Ground-truth labels are unavailable to the updating agent; it uses execution outcomes and self-reflection. The no-evolution comparison keeps state empty on every task. Three models and five methods are crossed with three stream arrangements. Figure 1(a), omitted here, shows the independent empty-state baseline. Next slide defines the three arrangements and preserves the original calculated results.

## 14 · Mixed task streams expose uneven gains
- Section / role: RESULTS / DURABILITY / result
- Purpose: Show why aggregate improvement can hide regressions.
- Visual: Prominent mean and flat three-row table, adapted Codex Grid 14.
- Claims: C007, C013, C016
- Sources: AgentStream: https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; Library Drift: https://arxiv.org/abs/2605.19576v3 — §§5–7; retrieval, storage, retirement; EvoHarnessBench: https://arxiv.org/abs/2609.04280v2 — §§3–4; evolving tools, skills and specialist agents
- Speaker notes: AgentStream evaluates six benchmarks with 50 tasks each: 300 distinct tasks, reused across three order seeds. The three models and five methods make 45 model–method–seed cells per stream condition. For interleaving, 28 cells are positive and 17 negative. The local audit reproduces the means and the printed variability as sample SD of three seed means, not a confidence interval or SD over 45 independent datasets. Methods share tasks; benchmark metrics differ. FinEvo and AgentStream use different tasks and feedback, so their effect sizes are not a head-to-head ranking. The uncertainty about causes remains: retrieval, interference, and feedback quality require controlled ablations. The thesis also notes AgentStream Tables 5–6: ACE shifts from positive average gain in isolated streams to negative in interleaved streams, whereas ReasoningBank and A-Mem have their largest mean gains in interleaved streams. This is consistent with relevance selection mattering, but the methods differ in more than retrieval. Library Drift and EvoHarnessBench motivate testing skill retirement and changed interfaces; they do not estimate the same failure rate. The row labels define the streams from §3.2; the earlier homemade domain-order strings have been removed. Isolated still learns within each domain. Methods differ in more than retrieval. Numeric cells remain the documented calculation.

## 15 · Repeated learning can deteriorate—or improve
- Section / role: RESULTS / DURABILITY / result
- Purpose: Balance the failure example with the thesis’s positive counterexample.
- Visual: Two columns distinguish separate studies without comparing effect sizes.
- Claims: C008, C015, C019
- Sources: R-Zero: https://arxiv.org/abs/2508.05004v4 — §2; Appendix D, Table 6; Appendix E; Rethinking Continual Experience Internalization: https://arxiv.org/abs/2606.04703v1 — §§3–5; Figure 1; Table 4
- Speaker notes: Core ideas: R-Zero §2 alternates Challenger and Solver training with difficulty filtering and majority-vote pseudo-labels. Continual Internalization §§3–5 uses principle-level experience, step-wise guidance and successful teacher trajectories to update weights. R-Zero Appendix D Table 6: the two-model math score falls from 49.12 at step 45 to 46.52 at step 60. Label quality, difficulty and training distribution change together; the cause is unresolved and there are no training-run intervals. Continual Internalization §§3–5/Table 4: a revised researcher-designed recipe uses general lessons, step-wise relevant guidance and successful experience-guided trajectories. Two models, three cycles; WebWalkerQA and GAIA improve over those cycles, while BrowseComp-ZH is uneven (5.2→4.4→5.9 in the reported Qwen3-4B/DeepSeek-experience setting). This positive counterexample does not establish indefinite durability or autonomous improver redesign.

## 16 · Production learning combines several loops
- Section / role: RESULTS / DURABILITY / result
- Purpose: Integrate first-party practice into the core argument.
- Visual: Flat sequence of changing components opposite the fixed external support.
- Claims: C010, C016
- Sources: Sidekick’s continual learning loop: https://shopify.engineering/sidekicks-continual-learning-loop — Harness optimization; trajectory repair; training; GraphQL sections; Reward Hacking Benchmark: https://arxiv.org/abs/2605.02964v1 — §§4–6; evaluation integrity separate from task correctness
- Speaker notes: Shopify describes a production pipeline rather than releasing a controlled longitudinal evaluation. Product criteria become rubric judges. Harness search modifies prompts, tool descriptions and orchestration. Frontier models repair low-scoring trajectories; unresolved cases go to human annotators. Repaired trajectories feed SFT and GRPO; old and new trajectories are reused in daily full-parameter training. Serving compression learns gist tokens. Treat all as company-described architecture. The article supplies no component ablations or cycle-by-cycle held-out quality. A shared judge can propagate a blind spot across stages, but that possibility is not proof of reward hacking. We deliberately omit the estimated 96% cost saving because it does not measure the total causal value of continual learning. Shared judges may carry correlated blind spots across selection and assessment; this does not establish observed gaming at Shopify. Reward Hacking Benchmark distinguishes evaluator integrity from task correctness. An evaluator outside edit permissions is our design recommendation, not a sufficient guarantee. Part takeaway: retention and continued gains depend on the setting; production combines several loops without isolating their benefits. Can the method that produces changes itself improve?

## 17 · Can the improvement method itself improve?
- Section / role: RESULTS / IMPROVING THE IMPROVER / mini-introduction
- Purpose: Can the improvement method itself improve?
- Visual: Spacious question-led composition; conceptual framing, not empirical evidence.
- Claims: C001, C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Part 2 shows why accumulating changes is not enough. Define the improver as the procedure that proposes and selects changes. Distinguish editing task behavior from editing that procedure, then test whether learned improvement behavior transfers. Sustained compounding requires repeated efficiency gains beyond a better endpoint.

## 18 · Hyperagents can rewrite the code that improves them
- Section / role: RESULTS / IMPROVING THE IMPROVER / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Zhang et al. · Hyperagents v1 · Figure 1, p. 4; caption omitted
- Claims: C009, C014, C017
- Sources: Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §3/Figure 1. Start with the bottom archive: select a parent, invoke its meta agent to propose an edited child, evaluate the child task agent, add it to the archive. A child may change task code, meta code, or both. The outer archive/selection/evaluation remains specified externally. Top: DGM retains handcrafted improvement-instruction generation. Small right-hand traces illustrate the same contrast; the large central loop carries the explanation. Editability is a mechanism, not evidence that learning accelerates. Next: freeze the resulting improver and see whether its improvement behavior transfers. SICA/DGM boundary details remain in the appendix.

## 19 · Improvement behavior can transfer to a new domain
- Section / role: RESULTS / IMPROVING THE IMPROVER / result
- Purpose: Restore the positive transfer evidence omitted from the earlier deck.
- Visual: Original Figure 3 middle/right held-out panels, with all their comparators and uncertainty; training panel omitted.
- Claims: C009
- Sources: Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Hyperagents v1 §§5.1–5.2: select transferred implementations from paper review and robotics reward design, then hold their meta agents fixed for 50 candidate-generation iterations on math grading. Improvement@50 is the held-out score gain of the best validation-selected task agent over its starting agent. Five runs: median 0.630, 95% bootstrap interval 0.540–0.630; initial implementation 0.000 (0.000–0.130). Authors report p<.05; repository audit identifies one-sided tests and run-array bootstrap, not task-population uncertainty. The entire task/meta implementation transfers and initial task behavior has formatting failures. This supports useful transferable improvement behavior without isolating meta code from the rest of the implementation. Figure caption uses stronger language about generality; our title narrows it to the tested domain. Next ask whether that starting advantage remains under continued meta evolution.

## 20 · The added long-run advantage remains uncertain
- Section / role: RESULTS / IMPROVING THE IMPROVER / result
- Purpose: Distinguish the uncertain endpoint advantage from the positive fixed-improver transfer result.
- Visual: Original Figure 4 with both panels and uncertainty; separate from Figure 3.
- Claims: C009
- Sources: Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Keep this separate from Figure 3. Here task and meta code may both continue evolving after transfer. After 200 iterations, transferred agents reach median held-out score 0.640 versus 0.610 from initial implementation, across five runs; run-bootstrap 95% intervals are 0.550–0.720 and 0.510–0.680. Authors explicitly report p>.05. The plot includes a separate ProofAutoGrader transfer condition and representative baseline, preserved as context rather than the chosen comparison. The first experiment supports bounded transfer of improvement behavior; this experiment leaves added long-run advantage uncertain. Lack of significance is not an equivalence test. Neither measures repeated improvement in learning efficiency at matched resources.

## 21 · Replay can help revise how a system searches
- Section / role: RESULTS / IMPROVING THE IMPROVER / result
- Purpose: Explain the recent search-controller example without claiming sustained compounding.
- Visual: Mechanism on the left; validity boundary and mixed outcomes on the right.
- Claims: C009, C017
- Sources: EvoX: https://arxiv.org/abs/2602.23413v2 — §§3–4/6.4; Dream-RSI: https://arxiv.org/html/2609.14858v1 — §§3–4; Figure 3; Table 1; replay guarantee in §3; The Economics of Recursive Self-Improvement: https://arxiv.org/abs/2609.15802v1 — §§2–4; conditional model, not measured acceleration
- Speaker notes: EvoX makes search strategy editable while retaining foundation models and evaluation. Dream-RSI v1 §3 replays recorded discovery trees to evaluate controller edits without running each candidate online. Replay generates no new outcomes. Keeping the incumbent guarantees no worse score only on fixed recorded histories. Table 1 mathematics includes a gain on Sum–Difference, a regression on autocorrelation and a circle-packing tie. Lasso Figure 3 reports 550→317 discovery-agent calls for the same Pro model; this omits complete meta-optimization cost and repeats, so do not call it lifetime efficiency. The theory of Economics of RSI models research-productivity assumptions and bottlenecks; it is not a measurement of compounding. Part takeaway: there is bounded evidence for transferable improvement behavior, but full costs and sustained compounding remain unresolved. Return to the main question.

## 22 · Useful learning is established; sustained compounding is not
- Section / role: CONCLUSION / synthesis
- Purpose: Answer the main question by separating three levels of evidence.
- Visual: Three equal cards, without arrows or an implied progression.
- Claims: C001, C011, C017
- Sources: WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; The Economics of Recursive Self-Improvement: https://arxiv.org/abs/2609.15802v1 — §§2–4; conditional model, not measured acceleration
- Speaker notes: Return to the main question: experience can create useful advantages in bounded settings; whether the advantage lasts and pays must be tested. These are distinctions in what an experiment establishes, not maturity levels or a claim that systems inevitably advance. A specialized procedure can be useful learning. Generality and economic value are additional tests. The third claim requires repeated improvements in learning efficiency under a consistent accounting of task difficulty and resources; a higher best score is insufficient.

## 23 · Test the next task, the old task, and the bill
- Section / role: CONCLUSION / implications
- Purpose: Specify success criteria instead of leaving evaluation abstract.
- Visual: Four-row decision table, Codex Grid 14.
- Claims: C011, C012
- Sources: AgentStream: https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; R-Zero: https://arxiv.org/abs/2508.05004v4 — §2; Appendix D, Table 6; Appendix E; Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3
- Speaker notes: Hold out new task families and a later time period before optimizing the system. Revisit earlier tasks to measure retention, failures and regressions, not only the best checkpoint. Count search, weight updates, execution and evaluation: cheap deployment can hide expensive optimization. Use independent repeated runs and a separately designed evaluator. An evaluator can still be wrong; report calibration and the unit of uncertainty. To claim acceleration rather than improvement, repeated cycles would need increasingly efficient gains, not just a higher score. These are recommendations grounded in the observed limitations, not empirical guarantees. Report development cost and operating cost separately at stated reuse volumes. Sustained compounding needs several cycles of improved learning efficiency, adjusted for task difficulty and resources; a D-versus-C endpoint win alone is insufficient. Detailed control arms and frozen-versus-adaptive test lanes are in the appendix.

## 24 · Which result would change your mind?
- Section / role: CONCLUSION / DISCUSSION / discussion
- Purpose: Invite decisions tied to the evidence.
- Visual: Three spacious numbered prompts with a concrete evidence anchor.
- Claims: C003, C005, C009, C012
- Sources: FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: Ask for one prediction and a disconfirming measurement. First, how much reuse would justify the remaining 2.80 rubric-point FinEvo gap after development and execution cost? Second, what evidence should revise or retire a wiki lesson when the corresponding skill fails validation? Third, which identical-start task-agent comparison would isolate the learned improver, and what result would falsify the transfer hypothesis? A measured gain is not automatically a causal explanation.

## 25 · Make experience valuable beyond its original task
- Section / role: CONCLUSION / closing
- Purpose: Resolve the opening question without claiming general recursion.
- Visual: Dark synthesis page states the three achievements with their different evidence status.
- Claims: C011
- Sources: Analyst framing; claim ledger.
- Speaker notes: Return to the opening distinction. A procedure should help later work; a learned improvement method should produce better future procedures; compounding should make further learning repeatedly more efficient. Specialization is compatible with useful learning. Recognize the positive finite evidence without turning it into a claim of indefinite acceleration. This is an interpretation of the reviewed corpus with a September 16 research cutoff. The most consequential missing result is a learned improvement method that repeatedly produces larger gains per unit of total resources when attached to otherwise identical agents on new task streams.

## 26 · Appendix · compare four practical alternatives fairly
- Section / role: APPENDIX / appendix
- Purpose: Compare practical alternatives while making initial-state matching and the paired reset requirement explicit.
- Visual: Editable four-arm table; clearly labeled proposed experiment.
- Claims: C012
- Sources: FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: This is a proposed protocol, not an established result. Give four practical alternatives the same task stream, feedback access and common total resource ceiling. C and D must begin with identical task code, improvement code and retained state. A strong fixed procedure can have a different starting method; account for authoring cost. A paired reset counterpart to a retained-state arm separately tests experience. The four alternatives alone do not identify four independent causal effects. D beating C is useful within this protocol but does not by itself prove isolated improver transfer or compounding.

## 27 · Appendix · separate what it knows from what it can learn next
- Section / role: APPENDIX / appendix
- Purpose: Turn the thesis’s corrected experiment into an explicit design.
- Visual: Two test lanes with a shared matched-start control beneath.
- Claims: C009, C012
- Sources: Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: After development, freeze copies to test accumulated capabilities on fresh cases, new task families and earlier tasks. Separately let copies adapt on new streams to measure future learning. To isolate improvement-method transfer, attach learned and original improvement methods to identical task agents with identical retained state. Hold both methods fixed during candidate generation and match feedback/resources. This directly addresses the confounding of whole-implementation transfer in Hyperagents §5.2. Repeat across streams and report independent-run uncertainty. A single favorable transplant is bounded meta-learning, not sustained compounding.

## 28 · Appendix · SEAL learns how to write its own updates
- Section / role: APPENDIX / concept
- Purpose: Explain the core idea using the source conceptual figure.
- Visual: Zweiger et al. · SEAL v2 · Figure 1, p. 2; caption omitted
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL): https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: SEAL v2 §3/Figure 1. Ctx is the supplied context; SE is a generated self-edit, specifying training content and optionally optimization directives. Inner loop: gradient updates adapt weights using that edit. Outer loop: downstream success rewards the policy that produced it. In the knowledge-incorporation example, a passage becomes synthetic training material; the result tests whether learning to generate that material helps question answering after adaptation. This differs from simply storing a passage in context. Figure 1 is the method overview; Table 2 follows. The learned update policy does not guarantee retention through later edits.

## 29 · Appendix · a model can learn to write update data
- Section / role: APPENDIX / appendix
- Purpose: Explain weight adaptation with the strongest scoped comparison.
- Visual: Original source extraction; Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Interpretation below, separate from source artwork.
- Claims: C004
- Sources: Self-Adapting Language Models (SEAL): https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6
- Speaker notes: SEAL has an outer loop that rewards self-generated edits when an inner weight update helps downstream performance. This example is single-passage SQuAD incorporation with Qwen2.5-7B, not the curated ARC experiment. The tested learned policy reaches 47.0 versus 39.7 for base-model synthetic data, a 7.3 percentage-point difference. A stronger external generator, GPT-4.1, reaches 46.3; SEAL does not generally dominate it and loses to it in the larger incorporation conditions. There are 974 questions clustered within 200 held-out passages. Final-score repeated-run uncertainty is not supplied. Figure 6 shows forgetting across sequential edits. Transition: an improvement still needs strong controls. Visual: Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original SEAL Table 2, all five methods and three passage settings. Single-passage SEAL scores 47.0 versus 39.7 for untrained synthetic data and 46.3 for GPT-4.1 data. GPT-4.1 wins in both continued-pretraining settings.

## 30 · Appendix · read each number with its denominator
- Section / role: APPENDIX / appendix
- Purpose: Keep uncertainty and independence available during discussion.
- Visual: Concise methods table; no pooled effect.
- Claims: C003, C004, C005, C006, C007, C008, C009
- Sources: WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Self-Adapting Language Models (SEAL): https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5; Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; AgentStream: https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; R-Zero: https://arxiv.org/abs/2508.05004v4 — §2; Appendix D, Table 6; Appendix E; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4
- Speaker notes: All values are source-reported or the documented AgentStream reconstruction; none were independently reproduced. These rows are different experiments, with different metrics and costs, and must not be pooled. WikiSkill is a five-benchmark equal-weight average. SEAL questions share passages. FinEvo order permutations reuse tasks. Harness tests include distinct main and held-out populations. AgentStream cell counts share tasks. R-Zero checkpoints share a training trajectory. Hyperagents run uncertainty does not represent task-population uncertainty. Full limitations and result locators are in the local claim ledger and source notes. Hyperagents Figure 3 is improvement@50 with a fixed meta agent; Figure 4 is final score with continued meta evolution. These endpoints differ. Continual Internalization has two model sizes, three cycles, reused evaluation suites, and no training-seed intervals.

## 31 · Appendix · one-shot authoring is a different test
- Section / role: APPENDIX / appendix
- Purpose: Include the expanded thesis’s curated-skill counterfactual without misreading it.
- Visual: Two-column conceptual contrast; no recreated result chart.
- Claims: C018
- Sources: SkillsBench: https://arxiv.org/abs/2602.12670v4 — Tables 2/6; Appendix D.6
- Speaker notes: SkillsBench v4 Tables 2/6 and Appendix D.6: 87 tasks, 18 configurations, three trials in the curated-skills study. Curated configuration-macro pass rate is 33.9→50.5%; 13 tasks have negative deltas. The self-generation diagnostic includes three configurations, each below no-skills (−8.1/−11.3/−11.5 pp). It is one-shot authoring without repeated outcome feedback. Human authoring effort is not matched, skill packs include scripts/assets, low-signal filtering can enrich skill-sensitive tasks, and authoring-run uncertainty is absent. The design is valuable as a strong curated baseline but cannot establish continual learning failure.

## 32 · Appendix · editing an agent and editing its improver differ
- Section / role: APPENDIX / appendix
- Purpose: Introduce meta-improvement through a precise predecessor comparison.
- Visual: Three-row comparison of editable components and external constraints.
- Claims: C013, C014, C017
- Sources: Self-Improving Coding Agent: https://arxiv.org/abs/2504.15228v2 — §3; Algorithm 1; Darwin Gödel Machine: https://arxiv.org/abs/2505.22954v3 — §§2–4; Hyperagents §1/Appendix B for the boundary; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Gödel Machines: https://arxiv.org/abs/cs/0309048v5 — §§2.2/3.2/4.1
- Speaker notes: SICA §3/Algorithm 1 retains an archive but expands the best-scoring agent. DGM explores alternate lineages, allowing weaker stepping stones, but retains a handcrafted improvement-instruction generator. Hyperagents puts task and improvement code in the same editable implementation while retaining an outer archive/evaluation procedure. These are related systems, not independent confirmations. STOP already edits improvement code; this is not a claim that Hyperagents invented self-modification. Gödel Machines requires a utility-improvement proof under encoded assumptions; empirical DGM does not inherit that guarantee.

## 33 · Appendix · primary sources 1/4
- Section / role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: Reflexion: https://arxiv.org/abs/2303.11366v4 — Algorithm 1; §§3–4; Voyager: https://arxiv.org/abs/2305.16291v2 — §§2–3; STOP: https://arxiv.org/abs/2310.02304v3 — Algorithm 1; §3; GEPA: https://arxiv.org/abs/2507.19457v2 — Algorithm 1; §4; WikiSkill: https://arxiv.org/abs/2608.27454v1 — §3, Figure 2; Table 1; Appendix B; Self-Adapting Language Models (SEAL): https://arxiv.org/abs/2506.10943v2 — §3/Figure 1; Table 2; Appendix B; §5/Figure 6; FinEvo-Bench: https://arxiv.org/html/2608.06144v1 — §§4.1–4.3; Tables 3 and 5
- Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.

## 34 · Appendix · primary sources 2/4
- Section / role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: Rethinking the Evaluation of Harness Evolution for Agents: https://arxiv.org/abs/2607.12227v2 — §§4.1–4.4; Tables 1–3; AgentStream: https://arxiv.org/html/2608.00155v1 — §§3.1–3.2; Figures 1–2; Tables 2/5/6 and 11–13; R-Zero: https://arxiv.org/abs/2508.05004v4 — §2; Appendix D, Table 6; Appendix E; Hyperagents: https://arxiv.org/abs/2603.19461v1 — §3/Figure 1; §5.2/Figure 3; §5.3/Figure 4; Dream-RSI: https://arxiv.org/html/2609.14858v1 — §§3–4; Figure 3; Table 1; replay guarantee in §3; Sidekick’s continual learning loop: https://shopify.engineering/sidekicks-continual-learning-loop — Harness optimization; trajectory repair; training; GraphQL sections; Rethinking Continual Experience Internalization: https://arxiv.org/abs/2606.04703v1 — §§3–5; Figure 1; Table 4
- Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.

## 35 · Appendix · primary sources 3/4
- Section / role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: SkillsBench: https://arxiv.org/abs/2602.12670v4 — Tables 2/6; Appendix D.6; Darwin Gödel Machine: https://arxiv.org/abs/2505.22954v3 — §§2–4; Hyperagents §1/Appendix B for the boundary; Self-Improving Coding Agent: https://arxiv.org/abs/2504.15228v2 — §3; Algorithm 1; Gödel Machines: https://arxiv.org/abs/cs/0309048v5 — §§2.2/3.2/4.1; EvoX: https://arxiv.org/abs/2602.23413v2 — §§3–4/6.4; The Economics of Recursive Self-Improvement: https://arxiv.org/abs/2609.15802v1 — §§2–4; conditional model, not measured acceleration; SkillOpt: https://arxiv.org/abs/2605.23904v2 — §§3.5–3.6; rejected edits retained as feedback
- Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.

## 36 · Appendix · primary sources 4/4
- Section / role: APPENDIX / appendix
- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Reference list
- Sources: ReasoningBank: https://arxiv.org/abs/2509.25140v2 — §§3–4; retained lessons plus test-time search; Reward Hacking Benchmark: https://arxiv.org/abs/2605.02964v1 — §§4–6; evaluation integrity separate from task correctness; Library Drift: https://arxiv.org/abs/2605.19576v3 — §§5–7; retrieval, storage, retirement; EvoHarnessBench: https://arxiv.org/abs/2609.04280v2 — §§3–4; evolving tools, skills and specialist agents
- Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.
