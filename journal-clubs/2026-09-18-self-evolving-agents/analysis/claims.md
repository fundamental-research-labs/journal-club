# Claim ledger

September 16, 2026. Confidence is an analytic judgment about the scoped claim, not a statistical probability. “Reported” does not mean reproduced. Source keys resolve in the [register](../research/sources.md); methods, denominators, and review depths remain in its linked notes. Presentation mapping belongs in the storyboard when slides are developed.

## C001

- **Claim / type:** Self-evolution here means experience changes retained state that affects subsequent behavior; “self” identifies which update decisions the agent controls. Operational definition / analyst synthesis.
- **Support:** `2023-reflexion`, [Algorithm 1](https://arxiv.org/abs/2303.11366v4); `2023-voyager`, [§2](https://arxiv.org/abs/2305.16291); `2025-self-adapting-language-models`, [§3](https://arxiv.org/abs/2506.10943v2).
- **Challenge / comparability:** Authors use different boundaries, including within-task retries. Persistent state alone does not demonstrate improvement; these distinct systems are examples, not replications.
- **Confidence / status:** High for usefulness as an explicit convention; usable with that label.
- **Change criterion:** Revise if the session includes systems without retained changes; distinguish their task-local search.

## C002

- **Claim / type:** The reviewed 2023–2026 literature broadens the editable components and increasingly tests reuse through stream, reset, and held-out controls. Dated synthesis, not a publication-count or adoption estimate.
- **Support:** `2023-stop`, [October 3, 2023, Algorithm 1](https://arxiv.org/abs/2310.02304v3); `2025-gepa`, [July 25, 2025, Algorithm 1](https://arxiv.org/abs/2507.19457v2); `2025-r-zero`, [August 7, 2025, §2](https://arxiv.org/abs/2508.05004v4); `hyperagents`, [March 19, 2026, §3](https://arxiv.org/abs/2603.19461v1); `agentstream`, [July 31, 2026, setup](https://arxiv.org/html/2608.00155v1); `harnessdev`, [September 1, 2026, §4.3](https://arxiv.org/abs/2609.01437v1). Dates from the register; revisions differ.
- **Challenge / comparability:** STOP already changes improver code in 2023. Selection of recent papers can create a false historical progression; these studies do not share a capability scale. Related DGM/Hyperagents methods are not independent confirmations.
- **Confidence / status:** Moderate; usable as a trend in this corpus. **Change criterion:** Broader dated coverage could weaken the claimed shift in emphasis.

## C003

- **Claim / type:** WikiSkill reports useful held-out skill gains under its benchmark protocol, with exceptions. Reported finding.
- **Support:** `wikiskill`, [v1 Table 1, Appendix B Table 6, Appendix C](https://arxiv.org/abs/2608.27454v1): Qwen-3.5-9B macro accuracy 29.9→47.4; strongest competing method for this model is EvoSkill at 42.3. Thus +17.5 pp versus no skills and +5.1 pp versus EvoSkill; three evolution runs. Test sizes across five benchmarks: 124/85/280/172/134. Qwen-3.5-4B OfficeQA declines 30.2→28.5.
- **Challenge / comparability:** Five benchmarks are equally weighted; small validation sets, injected skills, and OfficeQA reference-page assistance limit deployment extrapolation. No numerical CI in Table 1. Comparisons and ablations belong to one evidence family; extra computation is not fully normalized. Whole-method comparisons do not isolate the wiki. SkillOpt already retains rejected-edit feedback (§§3.5–3.6); WikiSkill’s separate evolving knowledge representation is the relevant architectural distinction (§1/§4.1).
- **Confidence / status:** Moderate; usable within protocol. **Change criterion:** Matched-cost replication with realistic retrieval or new domains could narrow the gain.

## C004

- **Claim / type:** A learned policy for generating weight-update data improves SEAL's single-passage adaptation, but continued editing still forgets. Reported finding.
- **Support:** `2025-self-adapting-language-models`, [v2 Table 2, §5/Figure 6, Appendix B](https://arxiv.org/abs/2506.10943v2): Qwen2.5-7B 47.0% with SEAL versus 39.7% with untrained synthetic data; 974 questions from 200 held-out passages. Later updates degrade prior knowledge.
- **Challenge / comparability:** Stronger-model synthetic data scores 46.3% here and exceeds SEAL in the larger incorporation conditions. Questions share passages; final-score repeated-run uncertainty is absent. This is one study, separate from skill benchmarks.
- **Confidence / status:** Moderate; usable. **Change criterion:** Independent repeated runs and retention-aware evaluation could change the advantage.

## C005

- **Claim / type:** Retained experience helps recurring FinEvo procedures relative to paired resets; a strong static skill explains much of one scaffold's improvement. Reported finding.
- **Support:** `2026-finevo-bench`, [v1 §§4.1–4.3, Tables 3/5](https://arxiv.org/html/2608.06144v1): 120 tasks, 20 scenes, three order permutations; common Qwen3.7-Max backbone. Four scaffold gains: 9.33–19.37 rubric points. Claude Code carrier comparison: reset 71.58, static expert skill 86.67, full evolution 89.47.
- **Challenge / comparability:** Main effects lack across-run intervals. Repeated tasks/orders are not 360 independent task types. Scoring and feedback share rubrics; one expert calibrates 120 outputs. Skill ablation is one scaffold, and updating adds computation. Rubric points are not accuracy percentage points.
- **Confidence / status:** Moderate; usable for recurring procedures, not open-world transfer. **Change criterion:** Novel procedures, independent judging, or cost-matched static controls could reduce the advantage.

## C006

- **Claim / type:** The tested harness evolution does not beat parallel sampling at equal rollout count; its separate held-out gain is small. Reported finding.
- **Support:** `harness-evolution-evaluation`, [v2 §§4.1–4.4, Tables 1–3](https://arxiv.org/abs/2607.12227v2): 89 Terminal-Bench 2.1 tasks, five rollouts, two runs; reported no-test averages 67.4 evolution versus 72.3 sampling. Separate 45/10/34 split: 68.3 evolved versus 67.7 initial.
- **Challenge / comparability:** Rollouts do not match tokens, dollars, or future amortization. Small held-out set; no table CIs. One implementation cannot establish that all harness evolution fails. Retain the printed average despite rounded-cell arithmetic differences.
- **Confidence / status:** Moderate; usable. **Change criterion:** A stronger evolved harness with repeated, independent transfer and lifetime-cost superiority would narrow the critique.

## C007

- **Claim / type:** AgentStream's tested retained-state methods have modest aggregate gains and substantial configuration-dependent regressions. Reported finding plus documented arithmetic reconstruction.
- **Support:** `agentstream`, [v1 Tables 2 and 11–13](https://arxiv.org/html/2608.00155v1), [existing audit](../research/check-agentstream-aggregates.py): six benchmarks × 50 tasks, three models, five methods, three order seeds. Isolated/sequential/interleaved mean gains: +1.37/+0.75/+0.90 pp. Interleaved has 28 positive and 17 negative cells. Table 5 reports ACE +2.28 pp isolated versus −1.26 interleaved; ReasoningBank and A-Mem peak on the interleaved condition. The essay uses the directional pattern, not a pooled comparison with another benchmark.
- **Challenge / comparability:** The 45 cells share tasks; they are not independent datasets. The reported ± reproduces sample SD of three seed-level means, not a CI. Native benchmark metrics differ. FinEvo's larger gains use different tasks and rubric feedback, so they are not a direct contradiction or ranking. The context-integrated versus retrieval-based comparison changes several method components; interference is the authors’ interpretation, not a retrieval-only causal ablation.
- **Confidence / status:** Moderate for generality; usable descriptive finding. **Change criterion:** Diverse independent streams and controlled retrieval/feedback ablations could revise the pattern.

## C008

- **Claim / type:** Additional self-generated training can reverse an earlier gain; label degradation alone is not an established causal explanation. Reported finding / causal limitation.
- **Support:** `2025-r-zero`, [v4 Appendix D Table 6, Appendix E](https://arxiv.org/abs/2508.05004v4): two-model math score 49.12 at step 45 falls to 46.52 at step 60; model-size-specific collapse occurs at different pseudo-label accuracies.
- **Challenge / comparability:** Missing training-run intervals and full compute ledger; judge-based label audits; curriculum difficulty and synthetic-data diversity also change. This is a bounded counterexample to monotonicity, not the typical collapse rate. Disputed main-table/prose aggregates are excluded.
- **Confidence / status:** Moderate; usable for the observed decline, causal mechanism unresolved. **Change criterion:** Replicated fixed-label-quality and fixed-difficulty interventions could identify causes or show instability was run-specific.

## C009

- **Claim / type:** Learned improvement behavior transfers in a bounded Hyperagents experiment; a separate continued-evolution experiment leaves the added transfer benefit uncertain. These studies do not demonstrate sustained domain-general acceleration. Evidence synthesis.
- **Support:** `hyperagents`, [v1 §§3/5.2–5.3, Figures 3–4](https://arxiv.org/abs/2603.19461v1): §5.2 holds the meta agent fixed for 50 iterations: transferred median improvement@50 0.630 (95% run-bootstrap CI 0.540–0.630), initial median 0.0 (CI 0.0–0.130); authors report p<0.05 over five runs. §5.3 permits continued meta-level changes for 200 iterations: transferred/fresh math scores 0.640/0.610, p>0.05 over five runs. `2026-dream-rsi`, [v1 §§3–4, Figure 3](https://arxiv.org/html/2609.14858v1): same-model Lasso discovery 550→317 calls, downstream mean runtime 3,587.1→2,931.0 ms across six held-out datasets.
- **Challenge / comparability:** These positive mechanisms challenge blanket skepticism. However, Hyperagents transfers the whole implementation, not only improvement code; the initial task agent has formatting failures. The §5.2 comparison does not isolate pure meta-code transfer. Run-level bootstrap intervals omit task-sampling uncertainty; the audited tests are one-sided with pairing/multiplicity limitations. Hyperagents also retains outer controls; Dream-RSI omits complete meta-optimization costs/repeat uncertainty and replay covers recorded branches. Its six datasets evaluate discovered solvers, not six independent controller-training runs. Distinct systems, not replications.
- **Confidence / status:** Moderate; usable with finite scope. **Change criterion:** Repeated cross-domain transfer of the improver at fixed lifetime cost, with increasing improvement efficiency across cycles, would strengthen the acceleration case.

## C010

- **Claim / type:** Shopify describes an integrated production learning pipeline; its article does not isolate the causal benefit of continual learning. First-party reported architecture / evidence limitation.
- **Support:** `2026-shopify-sidekick`, [August 5 article, trajectory repair, training, and GraphQL sections](https://shopify.engineering/sidekicks-continual-learning-loop): harness search, repaired data, SFT/GRPO, daily weight updates, serving compression.
- **Challenge / comparability:** No public ablation, longitudinal quality table, identified frontier baseline, or full cost ledger. One company account is an existence signal, not industry adoption evidence. Shared judge use across stages permits correlated blind spots; it does not prove gaming.
- **Confidence / status:** Moderate for the described design; usable with company attribution. Efficacy superiority remains provisional. **Change criterion:** Released longitudinal evaluations and independent judging could strengthen efficacy claims.

## C011

- **Claim / type:** Self-evolving agents can turn experience into reusable improvements; their scope and value depend on selection, retention, reuse, and full cost. Specialization can be useful learning. Bounded transfer of improvement behavior has positive evidence; sustained economical compounding remains unestablished. Central analyst inference.
- **Support:** C003–C010, with primary links and locators above. Positive matched controls and negative stress tests jointly explain the preferred thesis. The thesis-driven coverage pass adds C013–C019 and the original 56 source families, now supplemented by four bounded mechanism/foundation reviews; these are not independent replications. ReasoningBank and bounded internalization gains qualify a simple learning-versus-compute dichotomy.
- **Challenge / comparability:** Extra computation and supplied static expertise may account for gains attributed to updating; specialization narrows transfer rather than disproving learning. Computation and retained experience can also complement each other. No pooled effect or estimate of which bottleneck dominates is defensible. Study families and shared benchmarks prevent treating every paper as independent confirmation.
- **Confidence / status:** Moderate; usable as interpretation. **Change criterion:** Broad, replicated, economical improver transfer would strengthen the recursive view; disappearance of gains under strong controls would weaken the added-value case for updating.

## C012

- **Claim / type:** Compare evolution against static expertise, reset state plus extra inference, and a fixed improver under a complete lifetime budget. Match starting state/code for fixed-versus-editable improvers; separately test frozen reuse, resumed adaptation, and fixed learned-versus-original improvers on identical task agents. Analyst recommendation.
- **Support:** C004–C010; especially FinEvo Table 5, harness critique Tables 1–3, and R-Zero Appendix D.
- **Challenge / comparability:** The four practical alternatives alone do not isolate four causal contributions; a paired reset control is needed for retained experience. Independent evaluators also have errors; controls are expensive, and highly personalized tasks may resist fixed splits. State carriers have different costs and capabilities. This recommendation is not an experimentally proven universal optimum.
- **Confidence / status:** Moderate; usable as a proposed decision protocol. **Change criterion:** Application-specific constraints can change the control or held-out unit; report what causal distinction is then lost.

## C013

- **Claim / type:** Persistent learning includes choosing memory content, selecting experience, editing reusable skills, and evolving the operations that write memory. Mechanism synthesis.
- **Support:** `2023-expel`, [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144v3); `2025-reasoningbank`, [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2); `2025-agentic-context-engineering`, [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618); `2026-memrl`, [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192); `2026-selfmem`, [SelfMem: Self-Optimizing Memory for AI Agents](https://arxiv.org/abs/2607.03726); `2026-memskill`, [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474); `2026-evoskill`, [EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.02766v1); `2026-trace2skill`, [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](https://arxiv.org/abs/2603.25158v5); `2026-skillopt`, [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904v2).
- **Additional primary mechanism support:** `2025-dynamic-cheatsheet`, [v1 §§2.1–2.2](https://arxiv.org/abs/2504.07952v1), separates generation/curation and retrieval/synthesis; ACE §3/Figure 4 explicitly credits this architecture. `2025-a-mem`, [v11 §§3.1–3.4](https://arxiv.org/abs/2502.12110v11), constructs and updates linked notes. Selected-method reviews; no new numerical efficacy claims.
- **Locators / evidence:** ExpeL §4; ReasoningBank §3; ACE §3; MemRL §4; SelfMem §§3/5; MemSkill §3 and Table 2; EvoSkill/Trace2Skill §2; SkillOpt §3. Each source implements a different choice of persistent state or update operation.
- **Challenge / comparability:** MemSkill cross-model and conversational-dataset transfer does not establish conversational-to-embodied transfer. Trace2Skill has negative cells, EvoSkill single-run transfer, and SkillOpt lacks independent-run intervals. Memory QA is not equivalent to task-performing agent improvement.
- **Confidence / status:** High for mechanism distinctions; moderate for generality; usable.
- **Change criterion:** Factorial, repeated tests could change the usefulness attributed to a particular update operation.

## C014

- **Claim / type:** Automated design can produce reusable fixed workflows; agent code evolution and evolution of the designer remain distinct. Synthesis / scope boundary.
- **Support:** `2024-automated-design-agentic-systems`, [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435v2); `2024-aflow`, [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762v4); `2025-darwin-godel-machine`, [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954); `2025-huxley-godel-machine`, [Huxley-G\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://arxiv.org/abs/2510.21614); `2026-agentic-harness-engineering`, [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850); `2026-evo-harness`, [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071); `2026-shaper`, [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350v2).
- **Additional primary mechanism/theory support:** `2025-self-improving-coding-agent`, [SICA v2 §3/Algorithm 1](https://arxiv.org/abs/2504.15228v2), retains an archive but expands the best-scoring agent. `2003-goedel-machines`, [v5 §§2.2/3.2/4.1](https://arxiv.org/abs/cs/0309048v5), requires a proof of greater expected utility than continuing proof search under encoded assumptions; empirical DGM does not inherit this guarantee.
- **Locators / evidence:** ADAS §§3–4; AFlow §§4–5; DGM §§3–6 and Hyperagents §1/Appendix B distinguish the editable coding agent from DGM’s fixed improvement-instruction generator; archive stepping stones remain in Hyperagents. Shared lineage, not independent confirmation. HGM §§3–4; AHE v4 Tables 2–3; Evo-Harness §4.5/Table 4; SHAPER §§3–4. AHE held-out success gain is 0.4 pp; token means exclude timeouts.
- **Challenge / comparability:** Fixed search algorithms, selection data, different budgets and sparse repeats constrain transfer claims. HGM scheduling and selection both change. SHAPER is one artifact-search run with category regressions.
- **Confidence / status:** Moderate; usable within reported protocols.
- **Change criterion:** Repeated future-task transfer at matched lifetime budget could strengthen the case beyond reusable artifact search.

## C015

- **Claim / type:** Executable rewards, consensus pseudo-labels, generated environments, and combined harness/weight schedules provide different kinds of learning signal. Mechanism and evidence-boundary synthesis.
- **Support:** `2025-absolute-zero`, [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335); `2025-test-time-reinforcement-learning`, [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084); `2026-agent-world`, [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292); `2026-spontaneous-world-knowledge`, [Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration](https://arxiv.org/abs/2604.18131); `2026-sia`, [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276); `metarsi`, [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396v2); `sciencebuddy`, [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523v1).
- **Locators / evidence:** AZR §3; TTRL §§2–3; Agent-World §§3–4; World Knowledge Exploration §§3–4; SIA §§5–6; MetaRSI §§3–5/Appendix F; ScienceBuddy §§4/7.
- **Challenge / comparability:** TTRL adapts to scored test inputs without labels; World Knowledge deployment creates context rather than updating weights. Agent-World private inputs and inconsistent evolution table, SIA selection on test evaluator, MetaRSI missing realized-cost ledgers and ScienceBuddy differing released recipe all constrain stronger efficacy claims.
- **Confidence / status:** High for inspected update boundaries; moderate/low for broad efficacy; usable with source-specific qualifications.
- **Change criterion:** Independent releases with untouched tests and cost-matched operator controls could change attribution.

## C016

- **Claim / type:** Durability and integrity require separate tests of task shift, interface shift, memory lifecycle and evaluation access; rising development scores alone do not establish lasting value. Synthesis.
- **Support:** `harnessdev`, [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](https://arxiv.org/abs/2609.01437v1); `2026-sea-eval`, [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988v3); `evoharnessbench`, [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280v2); `library-drift`, [Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576v3); `2026-self-evolution-backfires`, [When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents](https://arxiv.org/abs/2608.05810); `2026-reflection-in-the-dark`, [Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization](https://arxiv.org/abs/2603.18388); `2026-ground-truth-first`, [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962); `2026-reward-hacking-agents`, [RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents](https://arxiv.org/abs/2603.11337v1); `2026-reward-hacking-benchmark`, [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964v1).
- **Locators / evidence:** HarnessDev version-switch analysis (34/64 direction agreements); SEA-Eval §§4–5; EvoHarnessBench §§3–4; Library Drift §§5–7; Backfires Tables 1–4; VISTA Tables 1–3; GTF §§5–7; RHA §§III–VI; RHB §§4–6.
- **Challenge / comparability:** These are different stress tests, not estimates of a common failure rate. Backfires collapse uses development tasks; GTF tenure uses six synthetic users; constructed attack regimes and prompt defects cannot establish population incidence.
- **Confidence / status:** Moderate; usable as a requirement for evidence, not a universal claim of failure.
- **Change criterion:** Independent streams, users, attack detection and cost-aware retention experiments could change the practical importance of each limitation.

## C017

- **Claim / type:** Improved artifacts, improved search within a fixed problem, transferable improvers and economy-wide acceleration require distinct evidence. Synthesis and theory interpretation.
- **Support:** `2025-alphaevolve`, [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131); `autoresearch`, [autoresearch](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117); `sol-pi`, [SoL-Pi](https://github.com/NVIDIA/SoL-Pi); `2026-evox`, [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413v2); `2026-escher-loop`, [Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization](https://arxiv.org/abs/2604.23472); `2026-mlevolve`, [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473v1); `2026-economics-rsi`, [The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802); `reef`, [Reef: inference-time learning infrastructure](https://github.com/Human-Agent-Society/reef/tree/401db3670d34b1b5a77989234272e0bee4b90ce8); `2026-nemoclaw-memory`, [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/).
- **Locators / evidence:** AlphaEvolve §§2–3; pinned autoresearch/SoL-Pi READMEs; EvoX §§3–6; Escher-Loop §§2–3/Table 1; MLEvolve §§3–4/Table 3; Economics §§2–4; Reef/NemoClaw primary artifact audits in notes.
- **Challenge / comparability:** Escher-Loop static pool ties AUC and slightly exceeds mean best on Circle Packing. MLEvolve memory ablation is a smaller subset with no ablation interval. Theory calibration is conditional and practitioner releases do not establish independent efficacy. Runtime cost, calls, iterations and equivalent tokens are not interchangeable.
- **Confidence / status:** Moderate; usable as taxonomy/interpretation; economic trajectory not predicted.
- **Change criterion:** Matched-cost transfer of improvement policies and measured R&D-productivity effects could strengthen a recursive acceleration claim.

## C018

- **Claim / type:** SkillsBench v4 provides a useful curated-skill counterfactual and a bounded failure of one-shot self-authoring; it does not test continual skill learning. Reported finding / scope qualification.
- **Support:** `2026-skillsbench`, [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670v4).
- **Locators / evidence:** v4 Tables 2/6, §5.1, Appendix D.6: 87 tasks, 18 configurations, three trials; 33.9→50.5 configuration-macro pass rate. Self-generation diagnostic in three configurations: −8.1/−11.3/−11.5 pp versus no skills; 13 tasks have negative curated-skill deltas.
- **Challenge / comparability:** Low-signal task filtering can inflate average lift; curation includes unmatched human labor/scripts/assets. No length-matched irrelevant-context control. Claude self-generation effort/sandbox differs; Codex/Gemini reuse one pack. Three trials do not measure authoring-run uncertainty.
- **Confidence / status:** Moderate; usable within v4 protocol.
- **Change criterion:** Feedback-based iterative authoring with matched resources and an unfiltered task population could reverse the self-authoring comparison.

## C019

- **Claim / type:** A fixed, carefully designed experience-internalization recipe can sustain bounded multi-cycle weight gains even when other variants deteriorate. Reported finding / synthesis.
- **Support:** `2026-rethink-continual-internalization`, [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1).
- **Locators / evidence:** v1 §§3–5, Figures 1/6, Tables 1–4: two Qwen sizes; 15K web-reasoning corpus; three internalized-update cycles. Final Qwen3-4B/DeepSeek-experience Table 4 WebWalkerQA 30.6→30.7→33.1 and GAIA 29.8→30.1→33.3; BrowseComp-ZH 5.2→4.4→5.9.
- **Challenge / comparability:** WebWalkerQA in-domain; same evaluation suites reused, no training-seed uncertainty or total teacher/training cost parity. In-context results tabulated only through cycle 2. The teacher can be the student conditioned on experience; stronger-model extraction is not the same as a different teacher backbone. Fixed researcher-designed update recipe does not demonstrate autonomous improver redesign.
- **Confidence / status:** Moderate; usable for bounded multi-cycle behavior.
- **Change criterion:** Longer independent task streams, retention checks, repeated training and equal lifetime budgets could change durability/generalization conclusions.

## Thesis section mapping

The [coverage audit](../research/thesis-coverage.md) preserves all 60 reviewed evidence families and identifies the 36 cited in the current essay. C001–C019 remain stable, including supporting claims no longer illustrated individually in prose. Citation selection does not change a claim's status or turn related sources into independent confirmations.

| Thesis section | Supporting claims |
| --- | --- |
| Why should the next task be easier? | C001, C003, C011 |
| How an experience becomes a working procedure | C001, C003–C004, C013–C014 |
| What does learning add to a good starting agent? | C005–C006, C011–C013, C018 |
| The next task can change the verdict | C004, C007–C008, C010, C013, C015–C016, C019 |
| Can the agent learn a better way to learn? | C009, C011, C013–C014, C017 |
| What would distinguish the achievements? | C011–C012 |

The WikiSkill mechanism explanation is grounded in v1 §3 and Figure 2: immutable traces, a persistent wiki, proposed skills, and validation/rollback. The conclusion that retained interpretations need scrutiny is analyst inference, not a measured contamination result. The proposed final experiment remains a recommendation under C012. The citation-coverage revision restores predecessor/comparator explanations, adds the existing WikiSkill Table 1 competitor comparison and AgentStream Table 5 method contrast, and preserves the recorded empirical uncertainty. No new experiment was performed.

## Sentence-specificity revision — September 18, 2026

The [editorial audit](sentence-audit.md) and revised thesis preserve C001–C019 and the section mapping above. The wiki discussion now proposes comparing retained versus removed entries from rejected proposals, making the existing analyst inference testable without asserting a new finding. The final experiment retains independent evaluation, matched starting state, retention tests, and total resource accounting. Source URLs and numerical results are preserved; no claim status changed.
