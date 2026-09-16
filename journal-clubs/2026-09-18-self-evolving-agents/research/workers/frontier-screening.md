# Frontier screening: 2026 weight, harness, and RSI candidates

**Screening date and cutoff:** September 16, 2026. **Scope:** every candidate in `weights-2026-update.md` and `survey-map-audit.md`, plus *The Economics of Recursive Self-Improvement* (arXiv:2609.15802). Dream-RSI is screened here but not reread deeply because another lane owns its full-text review. Ratings are **H/M/L/U** for high, medium, low, or unknown. Evidence ratings reflect the material actually inspected, not venue or author claims. PDFs for SIA v2, Escher-Loop v2, and Economics of RSI v1 were read locally from temporary downloads; no experiment was reproduced.

## Decision summary

1. **Escher-Loop — reserve / strongest new empirical meta-improvement candidate.** It evolves executable task programs and optimizer prompts, matches methods at 10M output-equivalent tokens per task, and reports three-run mechanism ablations. Its scope remains three fixed geometry instances; the paper explicitly leaves cross-domain transfer to future work. It changes prompts/programs, not model weights.
2. **SIA — reserve / clearest combined weight+harness mechanism, evidence caution.** It couples scaffold search with LoRA updates on gpt-oss-120b, but all three results reuse the optimized evaluator as the reported endpoint. The most serious case is LawBench: generated scripts are explicitly executed against the 913-example test split during improvement. No fresh post-selection test, repeated-run uncertainty, realized cost ledger, or capability-regression evaluation is reported.
3. **Economics of RSI — shortlist as theory/interpretation only.** It supplies the best bridge from local benchmark gains to a macro claim: feedback-loop gain depends on products of elasticities, and narrow verifiable-task acceleration need not imply broad capability or economic acceleration. Its 0.15 threshold is a back-of-the-envelope calibration with an essentially unmeasured key elasticity, not an empirical agent result.
4. **Dream-RSI, Agent-World, spontaneous world-knowledge evolution — reserves pending their assigned/full reviews.** Their abstracts indicate consequential exploration, environment-curriculum, and trained adaptation mechanisms, but abstract-only screening cannot establish split integrity, matched resources, uncertainty, or persistence.
5. **GAI and the three surveys/roadmaps — framing reserves.** They help define editable state, external anchoring, and levels of autonomy; they do not provide independent effect estimates.

## Per-candidate screens

### 2026-sia — SIA: Self Improving AI with Harness & Weight Updates

- **Access:** primary PDF v2, relevant methods/results/limitations read; arXiv metadata and license checked. [Full note](../notes/2026-sia.md).
- **Editable state:** generated scaffold (prompt, tools, parser, retry/search logic) plus rank-32 LoRA weights on gpt-oss-120b. Claude Sonnet 4.6 remains the frozen Meta-Agent and Feedback-Agent.
- **Rubric:** **Relevance H** — the only candidate directly combining harness and weight actions in one loop. **Evidence L** — three task endpoints and a harness-only ablation, but evaluator/test reuse, no independent repetitions or intervals, no fresh post-selection split, incomplete compute/training detail, and no regression or retention tests. **Novelty H** — direct joint control of two update surfaces. **Teaching H** — an unusually clear example of why an editable-state diagram and split audit matter. **Coverage H** — fills the actual weight+harness gap.
- **Disposition:** **reserve with strong qualification**. Use the mechanism diagram; do not present the reported gains as clean generalization evidence or recursive improvement.

### 2026-dream-rsi — Dream-RSI: Recursive Self-Improvement through Evolving Worlds

- **Access:** primary arXiv abstract/metadata v1 and project-level description in the discovery record; deep review assigned elsewhere.
- **Rubric:** **Relevance H** — directly improves exploration policy through replay simulators while leaving the coding model fixed. **Evidence U** — abstract reports quality/cost results, but protocols, denominators, uncertainty, and held-out controls were not read in this lane. **Novelty H** — turns accumulated discovery trees into an off-policy simulator that is expanded by redeployment. **Teaching H** — separates policy/harness recursion from weight learning. **Coverage H** — represents cost-aware recursive exploration.
- **Disposition:** **reserve pending full review**; classify as recursive exploration-policy improvement, not foundation-model weight self-training.

### 2026-escher-loop — Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization

- **Access:** primary PDF v2, full methods/results and Appendix A inspected; code repository linked but not audited. [Full note](../notes/2026-escher-loop.md).
- **Editable state:** executable task programs plus optimizer prompts/programs; Gemini 3 Flash weights stay fixed.
- **Rubric:** **Relevance H** — directly changes the improvement procedure itself. **Evidence M** — matched 10M-equivalent-token budgets, OpenEvolve baseline, and three-run ablations on two tasks; limited by only three fixed problem instances, best-so-far selection, no uncertainty for main endpoints, and no held-out cross-task transfer. **Novelty H** — optimizer populations recursively rewrite optimizer agents and receive relative Elo feedback from shared task contexts. **Teaching H** — concrete meta-improvement with inspectable controls and equally concrete limits. **Coverage H** — strongest new meta-improvement evidence in this batch.
- **Disposition:** **reserve / high-priority candidate**. Suitable for a qualified empirical example, not evidence of general or weight-level RSI.

### 2026-spontaneous-world-knowledge — Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

- **Access:** primary arXiv abstract/metadata v1 only.
- **Rubric:** **Relevance M** — trained meta-adaptation creates world-knowledge context at inference, but persistence in weights at deployment is not established. **Evidence U** — abstract reports 20% gains and a model comparison without inspected splits, costs, repetitions, or uncertainty. **Novelty M** — interesting separation between reward-trained exploration and reward-free inference. **Teaching M** — useful correction that “reward-free” applies only at inference. **Coverage M** — covers learned adaptation to unseen web environments.
- **Disposition:** **reserve pending full text**; never describe the training process itself as reward-free.

### 2026-agent-world — Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence

- **Access:** primary arXiv abstract/metadata v1 only; arXiv labels it “Working in progress.”
- **Rubric:** **Relevance H** — jointly evolves training tasks/environments and policy through multi-environment RL. **Evidence U** — claims across 23 benchmarks are unaudited; split independence, arena feedback reuse, rounds, compute, and uncertainty remain unknown. **Novelty H** — large-scale real-tool environment synthesis tied to detected capability gaps. **Teaching M** — useful environment-versus-agent co-evolution example, though complex. **Coverage H** — fills curriculum/environment evolution.
- **Disposition:** **reserve pending full text**.

### 2026-in-place-ttt — In-Place Test-Time Training

- **Access:** primary arXiv abstract/metadata v1 only; arXiv reports ICLR 2026 Oral and released code.
- **Rubric:** **Relevance M** — genuine fast-weight adaptation, but not an autonomous agent or self-chosen improvement loop. **Evidence U** — extensive experiments are claimed but protocols and results were not inspected here. **Novelty H** — adapts existing MLP output projections with a next-token objective and chunk-wise updates. **Teaching H** — clean counterexample showing weight change alone is not RSI. **Coverage M** — covers architectural continual/test-time learning.
- **Disposition:** **reserve as adjacent mechanism**, not a core agent benchmark.

### 2026-agentic-rl-systems — Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents

- **Access:** primary arXiv abstract/metadata v2 only.
- **Rubric:** **Relevance H** — directly proposes production infrastructure for deciding between policy-weight and in-context-harness changes. **Evidence L** — position/architecture argument; the abstract’s AReaL2.0 instantiation does not establish a comparative self-evolution effect. **Novelty M** — useful control-plane and governed-data architecture. **Teaching M** — clarifies infrastructure preconditions. **Coverage M** — fills deployment systems and governance.
- **Disposition:** **reserve as architecture/framing**, not measured evidence.

### 2026-continual-deployed-rl — Position: Deployed Reinforcement Learning should be Continual

- **Access:** primary arXiv abstract/metadata v2 only; accepted to the ICML 2026 Position Paper Track.
- **Rubric:** **Relevance M** — explains deployment non-stationarity and continual feedback. **Evidence L** — position paper, with no new effect estimate in the inspected material. **Novelty L** — continual RL is established; the deployment framing is useful. **Teaching M** — motivates drift and never-ending evaluation. **Coverage M** — supports the deployment axis but overlaps existing Library Drift/EvoHarnessBench coverage.
- **Disposition:** **exclude from core shortlist / retain as framing alternative**.

### 2026-generalized-agent-iteration — Generalized Agent Iteration

- **Access:** primary arXiv abstract/metadata v1 only.
- **Rubric:** **Relevance H** — directly distinguishes improvement-mechanism ownership and external versus self-referential evaluation. **Evidence L** — formal/conceptual framework, not an empirical benchmark. **Novelty M** — useful two-axis unification with generalized policy iteration. **Teaching H** — gives precise language for classifying SIA, Dream-RSI, and Escher-Loop. **Coverage H** — fills definitional discipline around RSI.
- **Disposition:** **reserve as taxonomy/theory**.

### 2026-inverter-rsi — Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification

- **Access:** primary arXiv abstract/metadata v1 only; authors explicitly call it a position paper and proof of concept.
- **Rubric:** **Relevance M** — program evolution with test-time learning, but domain-specific and not weight recursion. **Evidence U** — one reported benchmark result (NRMSE 0.470 to 0.0435; 15-module structure) without inspected protocol, repetitions, split, uncertainty, or comparator. **Novelty M** — interpretable typed block-diagram search is distinctive. **Teaching M** — concrete domain example. **Coverage L** — adds little to the central evaluation argument beyond illustrating narrow verifiable search.
- **Disposition:** **exclude from core shortlist / watchlist**.

### 2025-survey-self-evolving-agents — A Survey of Self-Evolving Agents

- **Access:** primary arXiv metadata/abstract v4 only in the audit; TMLR publication metadata reported on arXiv.
- **Rubric:** **Relevance H** — broad taxonomy of evolving models, memory, tools, and architecture. **Evidence U** — full survey and cited primary results were not checked in this lane; a survey is not independent efficacy evidence. **Novelty M** — useful synthesis rather than a new mechanism. **Teaching H** — strong map and benchmark-reset warning. **Coverage H** — broad coverage check.
- **Disposition:** **reserve as navigation**, never as proof that a mechanism works.

### 2026-self-evolving-coding-agents — Self-Evolving Coding Agents

- **Access:** primary arXiv metadata/abstract v3 only in the audit; companion GitHub collection not audited.
- **Rubric:** **Relevance H** — coding-specific map of framework, memory, tools, model, workflow/topology, and environment changes. **Evidence U** — no primary cited result was verified here. **Novelty H** — software-specific feedback and maintenance axes sharpen the broad taxonomy. **Teaching H** — maps executable feedback, repository state, rollback, and overfitting. **Coverage H** — exposes coding-harness, workflow, and dependency gaps.
- **Disposition:** **reserve as navigation and discovery index**.

### 2026-last-ai-built-by-humans — The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

- **Access:** primary arXiv metadata/abstract v2 only in the audit.
- **Rubric:** **Relevance H** — five-level RSI roadmap reaches recursive meta-improvement. **Evidence L** — abstract mentions preliminary evidence but exposes no reproducible design, sample, comparator, uncertainty, or transfer test. **Novelty M** — useful autonomy ladder and proposed Headroom-Closed Index. **Teaching H** — helps prevent conflating execution autonomy with improvement-strategy autonomy. **Coverage M** — frontier conceptual framing.
- **Disposition:** **reserve as explicitly proposed framing**; no numerical claim until full text is audited.

### 2026-economics-rsi — The Economics of Recursive Self-Improvement

- **Access:** primary PDF v1, models, data section, and calibration read. [Full note](../notes/2026-economics-rsi.md).
- **Rubric:** **Relevance H** — directly asks when AI-assisted AI R&D becomes self-sustaining and distinguishes narrow from broad acceleration. **Evidence M** — mathematically explicit synthesis and transparent data gaps, but the calibration relies on heterogeneous estimates and an essentially unknown research-effort elasticity; no uncertainty distribution or causal agent experiment. **Novelty H** — feedback graphs reduce RSI claims to measurable loop elasticities. **Teaching H** — provides the cleanest interpretation of why benchmark self-improvement may remain narrow or transient. **Coverage H** — adds economic feedback, bottlenecks, and empirical measurement targets absent from agent benchmarks.
- **Disposition:** **shortlist as theoretical interpretation**, never group it with empirical agent benchmark evidence.

## Cross-source conclusions for analysis

- The strongest new empirical candidates edit **different state**: SIA edits scaffold and LoRA weights; Escher-Loop edits task programs and optimizer prompts; Dream-RSI edits an exploration policy around a fixed coding agent. “Recursive” does not make these commensurate.
- SIA's headline comparison is an **optimization-endpoint comparison**, not a held-out generalization estimate. The same verifier drives selection and final reporting. LawBench explicitly uses the nominal test split inside the update loop.
- Escher-Loop supports a narrower statement: on three fixed mathematical optimization instances, evolving an optimizer population can improve best-so-far search under a token-price-normalized budget. It does not establish cross-domain optimizer transfer, weight learning, or compounding returns.
- Economics of RSI supplies the correct interpretive brake: gains on low-cost, verifiable optimization tasks may be a narrow capability loop, may hit component ceilings, and do not imply broad economic acceleration. The paper estimates that self-sustaining acceleration would require the elasticity of effective R&D effort to AI capability to exceed about 0.15 under its chosen calibration, while conceding that this is the least measured term.
- Across the pool, the recurring missing controls are fresh post-selection test sets, true task streams, regression/forgetting checks, matched total resources rather than token proxies alone, repeated runs with intervals, and evidence that the improvement operator transfers to unseen task families.

## Access and retention

SIA v2 is CC BY-SA 4.0; Economics of RSI v1 is CC BY 4.0. Escher-Loop v2 uses arXiv's non-exclusive distribution license, which does not itself establish third-party redistribution permission. Temporary PDFs were used for reading and were not added to the repository. For all abstract-only candidates, `frontier-candidates.json` records that no copy was retained and that exact license terms were not verified unless stated.
