<!-- Visual revision: September 16, 2026 -->

## Visual direction: editorial research seminar

Warm ivory pages, dark forest opening and synthesis, deep teal evidence accents,
and muted sage baselines. Georgia headlines pair with system sans-serif body text;
all typography works offline. A small running topic/section line provides orientation.
The opening pairs an oversized title with an explicitly conceptual orbit motif;
the evidence pages give original source figures and tables a large white area,
with separate interpretation and result callouts. Discussion uses a dark page and numbered prompts; appendices use
compact ruled rows. Presenter and company credits come from `content.json` metadata
and appear on the opening and closing. Source citations remain in a separate footer.

This revision changes visual treatment only; the existing C001–C012 evidence scope
and the outstanding C013–C019 reconciliation remain as documented.

# Presentation storyboard

September 16, 2026. HTML presentation; 15 talk slides and 3 appendices. Audience familiar with LLM basics; working assumption: 25–30 minutes plus discussion.

By the end, participants should distinguish retained experience, extra computation, and improvement of the learning process, because bounded gains depend on transfer, retention, and full cost.

Arc: question → mechanisms → evidence → competing explanations → regressions → meta-improvement and practice → proposed experiment → discussion and synthesis.

Design: ivory canvas, forest/teal emphasis, serif headlines and sans-serif body text; original source excerpts, semantic synthesis tables, and one illustrative mechanism. Keyboard navigation, direct links, notes, overview, and print CSS are included. Initial composition references were Codex Grid 01, 05, 14, and 22; the deliverable is HTML and has no Office dependency.

## 01. Self-evolving agents

- Purpose: Open the central question.
- Visual: Large typographic cover; Codex Grid 01.
- Claims: C001, C011


Speaker notes: For an audience familiar with LLM basics. Working assumption: 25–30 minutes of presentation with room for discussion. This is a topic-wide argument using the September 16 corpus. The question is whether solving one task improves future work. Preview the conclusion: useful bounded learning is supported; durable general improvement and its economics need stronger tests.

## 02. Learning has to survive the next task

- Purpose: Define retained change before introducing methods.
- Visual: One simple HTML diagram: experience → proposed change → selection → retained state; later-task test below.
- Claims: C001

- Source: `2023-reflexion` — [Reflexion](https://arxiv.org/abs/2303.11366v4); Algorithm 1; §§3–4. NeurIPS 2023; v4 reviewed.

- Source: `2023-voyager` — [Voyager](https://arxiv.org/abs/2305.16291); §§2–3. Foundational 2023 work.

- Source: `2025-self-adapting-language-models` — [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943v2); Table 2; Appendix B; §5, Figure 6. NeurIPS 2025; arXiv v2 reviewed.


Speaker notes: Use this as an explicit operational definition, not a consensus boundary. Reflexion keeps written feedback for later attempts; Voyager accumulates executable skills. Retaining something is not evidence that it helps. A retry can improve the current answer without establishing transfer. The outer objective, feedback and acceptance rule may remain human-designed. Transition: what exactly is being retained?

## 03. “Self” depends on what the agent can edit

- Purpose: Give a map of update mechanisms.
- Visual: Editable four-row comparison table, Codex Grid 14.
- Claims: C001, C002

- Source: `2023-voyager` — [Voyager](https://arxiv.org/abs/2305.16291); §§2–3. Foundational 2023 work.

- Source: `wikiskill` — [WikiSkill](https://arxiv.org/abs/2608.27454v1); Table 1; Appendix B, Table 6; Appendix C. Aug 27, 2026 preprint, v1.

- Source: `2025-gepa` — [GEPA](https://arxiv.org/abs/2507.19457v2); Algorithm 1; §4. 2025 origin; v2 reviewed.

- Source: `2025-self-adapting-language-models` — [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943v2); Table 2; Appendix B; §5, Figure 6. NeurIPS 2025; arXiv v2 reviewed.

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.

- Source: `2023-stop` — [STOP](https://arxiv.org/abs/2310.02304v3); Algorithm 1; §3. 2023 origin; v3 reviewed.

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.


Speaker notes: These are editable components, not levels on a universal capability ladder. A harness is the instructions and software that organize model calls and tool use. Weight updates change numerical model parameters. Improver code chooses how candidate changes are generated or searched. STOP already edited improver code in 2023, so avoid presenting meta-improvement as a new 2026 invention. Ask which decisions remain outside the loop. GEPA uses traces to propose prompts and keeps complementary candidates; it is an example of harness/prompt search, not a numerical comparison here.

## 04. Retained knowledge can improve skills

- Purpose: Establish a positive retained-state result.
- Visual: Original source extraction; Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Interpretation below, separate from source artwork.
- Claims: C003

- Source: `wikiskill` — [WikiSkill](https://arxiv.org/abs/2608.27454v1); Table 1; Appendix B, Table 6; Appendix C. Aug 27, 2026 preprint, v1.


Speaker notes: WikiSkill separates traces, accumulated wiki knowledge, and deployed skills. When a candidate skill is rejected, knowledge from the attempt can still persist. Qwen-3.5-9B gains 17.5 percentage points in macro accuracy across five benchmarks with equal benchmark weighting and three evolution runs. Test sizes are 124, 85, 280, 172, and 134. Table 1 gives no numerical confidence intervals. Skills are directly injected, validation sets are small, and OfficeQA has reference-page assistance. Qwen-3.5-4B declines from 30.2 to 28.5 on OfficeQA. The result supports useful benchmark learning, not universal improvement. Transition: experience can also be stored inside weights. Visual: Tang et al. · WikiSkill v1 · Table 1, p. 8 · Qwen 4B / 9B excerpt. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 excerpt, including all methods for Qwen-3.5-4B and 9B. Qwen-3.5-9B average rises from 29.9 to 47.4; Qwen-3.5-4B OfficeQA falls from 30.2 to 28.5. Original Table 1 caption: scores average three full evolution runs; all methods start with an empty skill set and evolved skills are directly injected. Bold denotes the best or results not significantly different from it under the authors’ paired bootstrap test (1,000 resamples, p < .05); yellow highlighting is the authors’ own.

## 05. A model can learn to write better update data

- Purpose: Explain weight adaptation with the strongest scoped comparison.
- Visual: Original source extraction; Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Interpretation below, separate from source artwork.
- Claims: C004

- Source: `2025-self-adapting-language-models` — [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943v2); Table 2; Appendix B; §5, Figure 6. NeurIPS 2025; arXiv v2 reviewed.


Speaker notes: SEAL has an outer loop that rewards self-generated edits when an inner weight update helps downstream performance. This example is single-passage SQuAD incorporation with Qwen2.5-7B, not the curated ARC experiment. The tested learned policy reaches 47.0 versus 39.7 for base-model synthetic data, a 7.3 percentage-point difference. A stronger external generator, GPT-4.1, reaches 46.3; SEAL does not generally dominate it and loses to it in the larger incorporation conditions. There are 974 questions clustered within 200 held-out passages. Final-score repeated-run uncertainty is not supplied. Figure 6 shows forgetting across sequential edits. Transition: an improvement still needs strong controls. Visual: Zweiger et al. · SEAL v2 · Table 2, p. 8 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original SEAL Table 2, all five methods and three passage settings. Single-passage SEAL scores 47.0 versus 39.7 for untrained synthetic data and 46.3 for GPT-4.1 data. GPT-4.1 wins in both continued-pretraining settings.

## 06. A strong fixed skill captures much of the gain

- Purpose: Present the strongest specialization alternative.
- Visual: Original source extraction; Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C005

- Source: `2026-finevo-bench` — [FinEvo-Bench](https://arxiv.org/html/2608.06144v1); §§4.1–4.3; Tables 3 and 5. Aug 6, 2026 preprint, v1.


Speaker notes: FinEvo tests recurring professional procedures with 120 financial tasks in 20 scenes and three shuffled task orders. Four scaffolds use the same Qwen3.7-Max backbone. Paired gains over reset range from 9.33 to 19.37 rubric points. The displayed Table 5 ablation is only the Claude Code scaffold: these labels are software frameworks, not vendor model identities. Reset is 71.58, fixed expert skill 86.67, unrestricted evolution 89.47. The 2.80-point difference is descriptive, not a tested causal advantage at matched cost. No across-run intervals are reported. Scoring and feedback share rubric design. Strong recurring-procedure evidence; novel procedures and full cost remain unresolved. Visual: Deng et al. · FinEvo-Bench v1 · Table 5, PDF p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original FinEvo Table 5, all five conditions, score, compliance, execution and reflection costs. Reset 71.58, fixed expert skill 86.67, full evolution 89.47, memory only 90.42, skill only 93.71. Source table definitions: Score is the rubric score; Comp. is compliance issues per task; costs are 10^4 tokens per task. Table 5 is on PDF page 6 in the retrieved v1; earlier reading notes said page 7.

## 07. More attempts are a serious competing baseline

- Purpose: Test reusable changes against extra inference.
- Visual: Original source extraction; Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Interpretation below, separate from source artwork.
- Claims: C006

- Source: `harness-evolution-evaluation` — [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2); §§4.1–4.4; Tables 1–3. 2026 preprint; Aug 27 revision, v2.


Speaker notes: This is a counterexample from one tested harness-evolution implementation, not a universal negative result. Table 1 compares five rollouts on 89 Terminal-Bench 2.1 tasks, three models, two runs, without test feedback. Retain the printed averages 67.4 and 72.3 despite rounded-cell arithmetic. A separate train/validation/test partition of 45/10/34 yields 68.3 for evolved versus 67.7 for initial harness on the 34 held-out tasks. Do not combine those experimental populations. No numerical CIs in the tables. Equal rollouts are not equal dollars or tokens; a reused harness could repay development cost across future tasks. Transition: follow the system beyond development and watch for damage. Visual: Wang et al. · Harness evaluation v2 · Table 1, p. 6 · Complete table. Extracted without redrawing or recoloring; caption omitted from image. Original Table 1 showing per-model results and printed averages for direct sampling, parallel sampling, sequential refinement, harness evolution and harness scaling. Reported averages: parallel sampling 72.3, harness evolution 67.4. Source caption: unit tests unavailable, pass@1; bold is best and underline is second best. The displayed 67.4 is the printed average, without correcting the source’s rounded-cell arithmetic.

## 08. Mixed task streams expose uneven gains

- Purpose: Show why aggregate improvement can hide regressions.
- Visual: Prominent mean and flat three-row table, adapted Codex Grid 14.
- Claims: C007

- Source: `agentstream` — [AgentStream](https://arxiv.org/html/2608.00155v1); Table 2; per-seed Tables 11–13. Jul 31, 2026 preprint, v1.


Speaker notes: AgentStream evaluates six benchmarks with 50 tasks each: 300 distinct tasks, reused across three order seeds. The three models and five methods make 45 model–method–seed cells per stream condition. For interleaving, 28 cells are positive and 17 negative. The local audit reproduces the means and the printed variability as sample SD of three seed means, not a confidence interval or SD over 45 independent datasets. Methods share tasks; benchmark metrics differ. FinEvo and AgentStream use different tasks and feedback, so their effect sizes are not a head-to-head ranking. The uncertainty about causes remains: retrieval, interference, and feedback quality require controlled ablations.

## 09. Further self-training can reverse a gain

- Purpose: Challenge monotonic improvement using a scoped counterexample.
- Visual: Two checkpoint scores as typography plus explanatory column, Codex Grid 05.
- Claims: C008

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.


Speaker notes: R-Zero alternates a Challenger that invents math problems and a Solver that learns from generated pseudo-labels. Both start pretrained, with fixed rewards, prompts, filters and evaluators. Appendix D Table 6 is the audited result: two-model math average peaks at step 45, then declines at 60. These are checkpoints in a trajectory, not independent runs. Main-table and prose aggregates disagree in v4, so they are not used here. Missing training-run uncertainty prevents claims about typical collapse rates. Label degradation is not an established cause because difficulty and diversity also change. The math average combines benchmark metrics, so call it a reported math score. Ask what signal would trigger rollback before a test score fell.

## 10. A better improver still has to transfer

- Purpose: Explain meta-improvement and present its strongest challenge fairly.
- Visual: Original source extraction; Zhang et al. · Hyperagents v1 · Figure 4, p. 13 · Both panels. Interpretation below, separate from source artwork.
- Claims: C009

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.

- Source: `2026-dream-rsi` — [Dream-RSI](https://arxiv.org/html/2609.14858v1); §§3–4; Figure 3; Equation 1. Sep 14, 2026 preprint, v1.


Speaker notes: Hyperagents shares editable task-agent and meta-agent code, while outer controls such as parent selection remain designed. Its math grading endpoint after 200 iterations is median 0.640 transferred versus 0.610 fresh over five runs, p>0.05 as reported. Bootstrap 95% intervals are 0.550–0.720 and 0.510–0.680; they resample runs, not task populations. Dream-RSI revises an exploration controller using replay of historical search trees. In the same-model Gemini-3.1-Pro Lasso comparison it uses 317 versus 550 discovery-agent calls, with mean solver runtime 2,931.0 versus 3,587.1 ms on six held-out datasets. The datasets test the discovered solver, not six independent controller runs. Replay guarantees only concern recorded paths; full meta-development cost and repeat uncertainty are missing. These positive mechanisms challenge blanket skepticism, without establishing sustained domain-general acceleration. Visual: Zhang et al. · Hyperagents v1 · Figure 4, p. 13 · Both panels. Extracted without redrawing or recoloring; caption omitted from image. Original Hyperagents Figure 4: training trajectories and held-out math-grading scores with uncertainty bars. DGM-H transfer endpoint 0.640 versus fresh 0.610; five runs, p greater than .05. The plot also includes the ProofAutoGrader initialization. Figure 4 caption claims accumulation; the displayed endpoint comparison is nonsignificant, as §5.3 states. Bands and bars retain the source’s 95% run-bootstrap intervals. Dream-RSI remains a cited numerical summary, not a reconstructed plot.

## 11. Production learning combines several loops

- Purpose: Integrate first-party practice into the core argument.
- Visual: Flat sequence of changing components opposite the fixed external support.
- Claims: C010

- Source: `2026-shopify-sidekick` — [Sidekick’s continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop); Harness optimization; trajectory repair; training; GraphQL sections. Shopify Engineering, Aug 5, 2026; company report.


Speaker notes: Shopify describes a production pipeline rather than releasing a controlled longitudinal evaluation. Product criteria become rubric judges. Harness search modifies prompts, tool descriptions and orchestration. Frontier models repair low-scoring trajectories; unresolved cases go to human annotators. Repaired trajectories feed SFT and GRPO; old and new trajectories are reused in daily full-parameter training. Serving compression learns gist tokens. Treat all as company-described architecture. The article supplies no component ablations or cycle-by-cycle held-out quality. A shared judge can propagate a blind spot across stages, but that possibility is not proof of reward hacking. We deliberately omit the estimated 96% cost saving because it does not measure the total causal value of continual learning.

## 12. Four controls would separate the explanations

- Purpose: Propose the discriminating experiment.
- Visual: Editable four-arm table; clearly labeled proposed experiment.
- Claims: C012

- Source: `2026-finevo-bench` — [FinEvo-Bench](https://arxiv.org/html/2608.06144v1); §§4.1–4.3; Tables 3 and 5. Aug 6, 2026 preprint, v1.

- Source: `harness-evolution-evaluation` — [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2); §§4.1–4.4; Tables 1–3. 2026 preprint; Aug 27 revision, v2.

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.


Speaker notes: This is our proposed protocol, not a published result or proven universal optimum. Use the same initial model, task stream, feedback access and lifetime resource budget. A strong fixed skill controls for prior expertise, a reset agent with extra attempts controls for inference compute, fixed-improver retained state tests experience reuse, and revisable-improver state adds meta-improvement. The fourth versus third comparison is particularly important: task performance improving alone does not establish that the improvement algorithm got better. Implementation differences can still confound these comparisons, so predeclare the update interface and allocation rules. Move to the next slide for the external test.

## 13. Test the next task, the old task, and the bill

- Purpose: Specify success criteria instead of leaving evaluation abstract.
- Visual: Four-row decision table, Codex Grid 14.
- Claims: C011, C012

- Source: `agentstream` — [AgentStream](https://arxiv.org/html/2608.00155v1); Table 2; per-seed Tables 11–13. Jul 31, 2026 preprint, v1.

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.

- Source: `harness-evolution-evaluation` — [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2); §§4.1–4.4; Tables 1–3. 2026 preprint; Aug 27 revision, v2.


Speaker notes: Hold out new task families and a later time period before optimizing the system. Revisit earlier tasks to measure retention, failures and regressions, not only the best checkpoint. Count search, weight updates, execution and evaluation: cheap deployment can hide expensive optimization. Use independent repeated runs and a separately designed evaluator. An evaluator can still be wrong; report calibration and the unit of uncertainty. To claim acceleration rather than improvement, repeated cycles would need increasingly efficient gains, not just a higher score. These are recommendations grounded in the observed limitations, not empirical guarantees.

## 14. Which result would change your mind?

- Purpose: Invite decisions tied to the evidence.
- Visual: Three spacious numbered prompts with a concrete evidence anchor.
- Claims: C005, C008, C009, C012

- Source: `2026-finevo-bench` — [FinEvo-Bench](https://arxiv.org/html/2608.06144v1); §§4.1–4.3; Tables 3 and 5. Aug 6, 2026 preprint, v1.

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.


Speaker notes: Invite a prediction before discussing experimental design. First, would the small remaining gap over expert skills matter after lifetime cost, and which held-out procedure would test it? Second, participants should choose an actual stop or rollback signal for a self-generated curriculum and say how they would distinguish label noise from difficulty or diversity. Third, ask what fourth-versus-third-arm result would convince them the improver itself generalizes. There is no supplied correct answer. Use the appendix for denominators and source references.

## 15. The value appears in the work that comes after

- Purpose: Resolve the opening question without claiming general recursion.
- Visual: Large synthesis plus three short evaluation questions, Codex Grid 01.
- Claims: C011


Speaker notes: The synthesis is ours. Positive retained-state and learned-update experiments justify interest in bounded learning loops. Static expertise, extra inference, regressions and finite transfer limit the stronger interpretation. Ask whether an update helps on future work, keeps earlier abilities, and justifies its total cost. Broad repeated economical transfer of the improver would change the conclusion. The reviewed corpus does not establish sustained domain-general acceleration.

## 16. Appendix · read each number with its denominator

- Purpose: Keep uncertainty and independence available during discussion.
- Visual: Concise methods table; no pooled effect.
- Claims: C003, C004, C005, C006, C007, C008, C009

- Source: `wikiskill` — [WikiSkill](https://arxiv.org/abs/2608.27454v1); Table 1; Appendix B, Table 6; Appendix C. Aug 27, 2026 preprint, v1.

- Source: `2025-self-adapting-language-models` — [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943v2); Table 2; Appendix B; §5, Figure 6. NeurIPS 2025; arXiv v2 reviewed.

- Source: `2026-finevo-bench` — [FinEvo-Bench](https://arxiv.org/html/2608.06144v1); §§4.1–4.3; Tables 3 and 5. Aug 6, 2026 preprint, v1.

- Source: `harness-evolution-evaluation` — [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2); §§4.1–4.4; Tables 1–3. 2026 preprint; Aug 27 revision, v2.

- Source: `agentstream` — [AgentStream](https://arxiv.org/html/2608.00155v1); Table 2; per-seed Tables 11–13. Jul 31, 2026 preprint, v1.

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.


Speaker notes: All values are source-reported or the documented AgentStream reconstruction; none were independently reproduced. These rows are different experiments, with different metrics and costs, and must not be pooled. WikiSkill is a five-benchmark equal-weight average. SEAL questions share passages. FinEvo order permutations reuse tasks. Harness tests include distinct main and held-out populations. AgentStream cell counts share tasks. R-Zero checkpoints share a training trajectory. Hyperagents run uncertainty does not represent task-population uncertainty. Full limitations and result locators are in the local claim ledger and source notes.

## 17. Appendix · mechanisms and positive evidence

- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Framing / references

- Source: `2023-reflexion` — [Reflexion](https://arxiv.org/abs/2303.11366v4); Algorithm 1; §§3–4. NeurIPS 2023; v4 reviewed.

- Source: `2023-voyager` — [Voyager](https://arxiv.org/abs/2305.16291); §§2–3. Foundational 2023 work.

- Source: `2023-stop` — [STOP](https://arxiv.org/abs/2310.02304v3); Algorithm 1; §3. 2023 origin; v3 reviewed.

- Source: `2025-gepa` — [GEPA](https://arxiv.org/abs/2507.19457v2); Algorithm 1; §4. 2025 origin; v2 reviewed.

- Source: `wikiskill` — [WikiSkill](https://arxiv.org/abs/2608.27454v1); Table 1; Appendix B, Table 6; Appendix C. Aug 27, 2026 preprint, v1.

- Source: `2025-self-adapting-language-models` — [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943v2); Table 2; Appendix B; §5, Figure 6. NeurIPS 2025; arXiv v2 reviewed.


Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.

## 18. Appendix · controls, persistence, and practice

- Purpose: Provide stable primary links and publication status.
- Visual: Spacious source list with short labels and stable URLs.
- Claims: Framing / references

- Source: `2026-finevo-bench` — [FinEvo-Bench](https://arxiv.org/html/2608.06144v1); §§4.1–4.3; Tables 3 and 5. Aug 6, 2026 preprint, v1.

- Source: `harness-evolution-evaluation` — [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2); §§4.1–4.4; Tables 1–3. 2026 preprint; Aug 27 revision, v2.

- Source: `agentstream` — [AgentStream](https://arxiv.org/html/2608.00155v1); Table 2; per-seed Tables 11–13. Jul 31, 2026 preprint, v1.

- Source: `2025-r-zero` — [R-Zero](https://arxiv.org/abs/2508.05004v4); §2; Appendix D, Table 6; Appendix E. ICLR 2026; Feb 13 revision, v4.

- Source: `hyperagents` — [Hyperagents](https://arxiv.org/abs/2603.19461v1); §§3, 5.2–5.3; Figure 4. Mar 19, 2026 preprint, v1.

- Source: `2026-dream-rsi` — [Dream-RSI](https://arxiv.org/html/2609.14858v1); §§3–4; Figure 3; Equation 1. Sep 14, 2026 preprint, v1.

- Source: `2026-shopify-sidekick` — [Sidekick’s continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop); Harness optimization; trajectory repair; training; GraphQL sections. Shopify Engineering, Aug 5, 2026; company report.


Speaker notes: References supporting the main talk. Source versions and access depth are recorded in research/sources.md. The majority of 2026 experimental sources here are preprints; SEAL and R-Zero have conference versions. Source notes are based on primary methods/results and relevant appendices to their stated depth. No inaccessible social thread or unverified demo is used as evidence.

## Original-source evidence revision — September 16, 2026

Slides 4–7 replace all four reconstructed bar charts with source table excerpts.
Slide 10 adds the original Hyperagents Figure 4. The source's typography, colors,
scales and uncertainty remain intact; explanatory text stays outside the artwork.
WikiSkill shows the first two complete model blocks with headers, rather than
isolating the favorable 9B mean. SEAL, FinEvo and harness evaluation show complete
tables. Source captions are represented in notes; attribution identifies excerpt
scope and exact PDF pages. Other diagrams/tables remain explanatory synthesis or
explicit calculations, as detailed in figure provenance. This is a visual-evidence
revision, not completion of the separate expanded-thesis reconciliation.
