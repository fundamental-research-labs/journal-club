# Sample 50 Paper Review Audit

Date: 2026-05-04

This audit samples 50 local paper folders from `papers/` and reviews them with the criteria in `docs/review-rubric.md`. The goal is collection quality control: estimate whether the maintained local corpus contains too many weak papers before the final top-100 selection.

## Sampling Protocol

- Sampling frame: 98 local folders under `papers/`.
- Sampling method: deterministic stratified sample by seed role, using seed `2026-05-04-local-papers-quality-audit-v1`.
- Role targets: 17 core, 9 trend, 16 bridge, 7 anchor, 1 survey.
- Review evidence: local `metadata.yaml`, `summary.md`, `claims.md`, `notes.md`, existing full reviews where present, and targeted source/PDF-derived notes already stored in the paper folders.
- Important scoring note: bridge papers can be strong agent papers but still receive an overall cap around 6 when the multi-agent-specific rubric gives them low multi-agent specificity.

Criterion abbreviations:

- `N`: Novelty
- `S`: Significance
- `R`: Technical correctness and rigor
- `B`: Empirical breadth and generality
- `M`: Multi-agent specificity
- `Rep`: Reproducibility and transparency
- `C`: Clarity and positioning
- `U`: Practical usefulness

## Aggregate Finding

The sample does not show a serious bad-paper problem in the local corpus.

| Band | Overall score | Count | Share | Interpretation |
|---|---:|---:|---:|---|
| Strong keep | 8 | 9 | 18% | Clear top-corpus candidates or anchors |
| Keep | 7 | 13 | 26% | Useful and mostly convincing |
| Useful but limited | 6 | 24 | 48% | Worth keeping as bridge, history, or bounded evidence |
| Watchlist / borderline | 5 | 4 | 8% | Useful idea but weak evidence, narrow setup, or overclaiming |
| Cut-grade | 1-4 | 0 | 0% | No sampled paper was clearly bad enough to cut outright |

Mean overall score: 6.54.

By role:

| Role | Count | Mean overall | Read |
|---|---:|---:|---|
| Anchor | 7 | 7.71 | Strong historical foundations |
| Survey | 1 | 7.00 | Useful organizing reference |
| Core | 17 | 6.76 | Generally solid, with a few early/weak-evidence frameworks |
| Bridge | 16 | 6.06 | Strong agent benchmarks/infrastructure, capped by low MAS specificity |
| Trend | 9 | 6.00 | Highest uncertainty; several recent papers need follow-up before top-100 promotion |

Main quality-control conclusion: the corpus is not overloaded with bad papers, but the top-100 process should be careful with recent trend papers and early framework papers that have weak budget controls, synthetic evaluations, or loose claims about collaboration.

## Score Table

| # | Paper | Role | N | S | R | B | M | Rep | C | U | Overall | Conf. |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | ACC-Collab | trend | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 7 | 4 |
| 2 | AgentCoder | core | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 4 |
| 3 | Agent Hospital | trend | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 5 | 3 |
| 4 | Agent Laboratory | trend | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 6 | 4 |
| 5 | AgentRxiv | trend | 3 | 3 | 2 | 2 | 4 | 3 | 4 | 3 | 5 | 3 |
| 6 | AgentsNet | core | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 8 | 4 |
| 7 | AndroidWorld | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 5 | 6 | 4 |
| 8 | AutoAgents | core | 3 | 3 | 2 | 2 | 4 | 3 | 3 | 3 | 5 | 3 |
| 9 | BrowserGym Ecosystem | bridge | 4 | 4 | 4 | 5 | 2 | 5 | 4 | 5 | 6 | 4 |
| 10 | CAMEL | core | 4 | 4 | 2 | 3 | 3 | 4 | 4 | 4 | 6 | 4 |
| 11 | ChatDev | core | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 4 |
| 12 | COMA | anchor | 4 | 4 | 4 | 3 | 5 | 3 | 4 | 4 | 8 | 4 |
| 13 | CooperBench | core | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 8 | 4 |
| 14 | DELEGATE-52 | core | 4 | 5 | 4 | 5 | 2 | 3 | 4 | 5 | 7 | 4 |
| 15 | OpenAI Five / Dota 2 | anchor | 4 | 5 | 4 | 2 | 5 | 2 | 4 | 3 | 7 | 4 |
| 16 | Grounded Compositional Language | anchor | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 4 | 7 | 4 |
| 17 | Emergent Multi-Agent Communication Survey | survey | 3 | 4 | 4 | 5 | 5 | 3 | 5 | 4 | 7 | 4 |
| 18 | Emergent Tool Use | anchor | 5 | 5 | 4 | 3 | 5 | 3 | 4 | 4 | 8 | 4 |
| 19 | GAIA | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 5 | 6 | 4 |
| 20 | GPTSwarm | core | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 7 | 4 |
| 21 | G-Safeguard | core | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 | 7 | 4 |
| 22 | MaAS | core | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 8 | 4 |
| 23 | MADDPG | anchor | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 4 | 8 | 4 |
| 24 | MAPoRL | trend | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 4 | 7 | 4 |
| 25 | MemGPT | bridge | 4 | 5 | 4 | 3 | 1 | 4 | 4 | 5 | 6 | 4 |
| 26 | MemMA | core | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 7 | 3 |
| 27 | MetaGPT | core | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 5 | 7 | 4 |
| 28 | Mind2Web | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 4 | 6 | 4 |
| 29 | MIRROR | trend | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 4 |
| 30 | More Agents Is All You Need | core | 3 | 4 | 3 | 4 | 2 | 3 | 4 | 5 | 6 | 4 |
| 31 | Evolving Orchestration | core | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 | 7 | 4 |
| 32 | Multiagent Debate | core | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 7 | 4 |
| 33 | OMAC | trend | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 3 |
| 34 | OpenHands | bridge | 4 | 4 | 4 | 5 | 2 | 5 | 4 | 5 | 6 | 4 |
| 35 | OSWorld | bridge | 4 | 5 | 4 | 5 | 1 | 4 | 4 | 5 | 6 | 4 |
| 36 | ReAct | bridge | 5 | 5 | 4 | 4 | 1 | 4 | 5 | 5 | 6 | 5 |
| 37 | RIAL/DIAL | anchor | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 4 | 8 | 4 |
| 38 | SafeArena | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 5 | 6 | 4 |
| 39 | SlopCodeBench | bridge | 4 | 4 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 4 |
| 40 | SOTOPIA | bridge | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 7 | 4 |
| 41 | SWE-smith | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 4 | 6 | 4 |
| 42 | tau-bench | bridge | 4 | 4 | 4 | 3 | 1 | 4 | 4 | 5 | 6 | 4 |
| 43 | Teams of LLM Agents Exploit Zero-Days | trend | 4 | 4 | 3 | 2 | 5 | 2 | 4 | 3 | 6 | 3 |
| 44 | TheAgentCompany | bridge | 4 | 4 | 4 | 4 | 2 | 4 | 4 | 5 | 6 | 4 |
| 45 | Two Heads are Better Than One | trend | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 3 |
| 46 | VDN | anchor | 4 | 5 | 4 | 3 | 5 | 3 | 4 | 4 | 8 | 4 |
| 47 | WarAgent | core | 3 | 3 | 2 | 2 | 4 | 3 | 4 | 3 | 5 | 3 |
| 48 | WebArena | bridge | 5 | 5 | 4 | 4 | 1 | 4 | 4 | 5 | 6 | 4 |
| 49 | Why Do Multi-Agent LLM Systems Fail? | core | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 8 | 4 |
| 50 | WorkArena | bridge | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 5 | 6 | 4 |

## Compact Reviews

### 1. ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration

Verdict: A solid trained-collaboration paper that makes two-agent actor-critic deliberation more convincing than prompt-only debate on QA-style tasks, but it remains bounded by small models and answer-verifiable settings.

Strengths: learns collaboration rather than assuming it; uses guided trajectory preference data; compares against several debate/fine-tuning baselines; includes useful actor/critic ablations.

Weaknesses: QA tasks with known answers are much easier to reward than open-ended agent work; gains may partly reflect extra training/search machinery; limited evidence for larger models, tools, or long-horizon workflows.

Question: How does ACC-Collab compare against budget-matched single-agent self-consistency or verifier-guided sampling at equal tokens and training data?

Repo takeaway: Keep as a recent positive result for trained collaboration, but do not treat it as broad evidence that generic multi-agent discussion helps.

### 2. AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation

Verdict: A useful early coding-agent system where programmer/tester/executor role separation is practical, though evidence is mostly function-level Python benchmark performance.

Strengths: clear role decomposition; independent test generation is a real mechanism; executable feedback loop is actionable; ablations support the full loop over partial variants.

Weaknesses: HumanEval/MBPP-style tasks are narrow; baselines and costs are not always fully controlled; generated tests can encode false confidence; repository-level software work is not covered.

Question: Does independent test generation still help on real codebases where tests require fixtures, state, and integration setup?

Repo takeaway: Keep as a precursor to stronger SWE-agent and multi-agent coding work, but rank below repository-level benchmarks and coordination studies.

### 3. Agent Hospital

Verdict: An interesting hospital simulacrum and synthetic-experience paper, but its medical claims rely heavily on generated patients and in-simulation validation.

Strengths: ambitious closed-loop environment; combines patient, nurse, and doctor agents; uses case and experience memories; reports broad department coverage and MedQA comparisons.

Weaknesses: synthetic training and synthetic testing are tightly coupled; clinical validity is not established; multi-agent benefit is not cleanly isolated from RAG and reflection; reproducibility and safety details matter greatly.

Question: How do evolved agents perform on externally sourced, clinician-reviewed patient cases that were not generated by the same simulacrum?

Repo takeaway: Keep as a trend/watchlist paper, not as strong evidence for deployed medical multi-agent systems.

### 4. Agent Laboratory

Verdict: A practical end-to-end research-assistant workflow with useful human evaluation, but the generated papers remain below conference quality and the multi-agent contribution is mostly workflow decomposition.

Strengths: open workflow across literature, experiments, and writing; includes autonomous and co-pilot modes; human reviews expose inflated automated scores; `mle-solver` provides a concrete coding/evaluation loop.

Weaknesses: small human-evaluated topic set; fixed workflow limits adaptivity; self-review and report generation can hallucinate; multi-agent roles are not cleanly isolated from tools and scaffolding.

Question: Which agent roles remain useful when a strong single agent gets the same tools, checkpoints, and human review budget?

Repo takeaway: Keep as a research-agent bridge/trend paper, especially for human-in-the-loop evaluation and the self-review gap.

### 5. AgentRxiv

Verdict: A conceptually useful artifact-sharing layer for autonomous research agents, but the empirical evidence is narrow and vulnerable to benchmark-driven discovery artifacts.

Strengths: makes cumulative agent research concrete; uses shared retrieval over generated papers; compares sequential and parallel laboratories; candid about hallucination and reward-hacking risks.

Weaknesses: main result is one MATH-500 prompt-discovery setting; generated-paper quality is not deeply validated; parallel gains are compute-inefficient; novelty of the discovered method is uncertain.

Question: Does AgentRxiv improve discovery on tasks where progress cannot be measured by a simple benchmark score?

Repo takeaway: Keep as a watchlist item for asynchronous agent memory/artifact sharing, but require stronger domains before top-100 promotion.

### 6. AgentsNet

Verdict: A strong benchmark paper that cleanly isolates local communication and global coordination in multi-agent LLM networks.

Strengths: distributed-computing tasks make coordination explicit; local message-passing protocol is well scoped; evaluates topology, size, and model variation; strict network-level scoring exposes brittle coordination.

Weaknesses: stylized graph tasks may not transfer directly to practical agent workflows; homogeneous agents under fixed synchronous rounds are a narrow protocol; strict binary scoring can hide partial progress.

Question: Which structured protocols or verification layers improve AgentsNet without giving agents global state?

Repo takeaway: Promote as a core coordination benchmark because it directly tests whether LLM agents can use a network topology.

### 7. AndroidWorld

Verdict: A strong mobile-agent benchmark and bridge paper, but not a multi-agent paper.

Strengths: executable Android tasks; device-state rewards are much stronger than action imitation; parameterized seeds reveal robustness failures; baseline gap to humans is informative.

Weaknesses: low multi-agent specificity; app suite is bounded to controllable apps; reward logic is hand-authored; absolute results age quickly as mobile agents improve.

Question: Can multi-agent mobile workflows help by separating perception, planning, and verification, or does coordination overhead dominate?

Repo takeaway: Keep as a bridge benchmark for real UI-agent evaluation, not as evidence about multi-agent coordination.

### 8. AutoAgents

Verdict: A useful early dynamic-team-generation framework, but the evidence is too preference-heavy and narrow for strong claims.

Strengths: targets fixed-role limitations directly; observer-mediated drafting/execution is a clear design; dynamic role generation is relevant to later architecture-search work; includes ablations over observers and memory.

Weaknesses: MT-Bench and trivia evaluations do not establish robust task success; GPT-4-based preference comparisons are confounded by verbosity and model strength; role optimality is not tested; software examples are mostly illustrative.

Question: Does automatic role generation beat a small set of hand-designed roles under equal model calls and token budget?

Repo takeaway: Keep as historical context for dynamic agent generation, but treat as borderline until stronger evaluations are available.

### 9. BrowserGym Ecosystem

Verdict: A strong infrastructure paper for reproducible web-agent research, but its contribution is evaluation plumbing rather than multi-agent mechanisms.

Strengths: unifies major web benchmarks; AgentLab adds experiment, relaunch, logging, and trace inspection support; strong reproducibility orientation; useful cross-benchmark results.

Weaknesses: low multi-agent specificity; benchmark heterogeneity remains beneath the API; live/open-web drift remains hard; platform value depends on community adoption.

Question: Can BrowserGym support standardized multi-agent web protocols with shared state, delegation, and conflict logging?

Repo takeaway: Keep as a key bridge artifact for evaluating web agents and future multi-agent browser workflows.

### 10. CAMEL

Verdict: Foundational and practically influential, but weak as current evidence for intrinsic multi-agent advantage.

Strengths: early role-playing framework; reusable prompts, data, and code; clear operational recipe for AI user/assistant task solving; documents concrete communication failures.

Weaknesses: no strong budget-matched single-agent baseline; GPT-4 judging and summarization can bias results; broad "society" claims exceed the evidence; mostly two-agent role-play.

Question: Which CAMEL gains remain after matching tokens, samples, conversation length, and answer verbosity?

Repo takeaway: Keep for historical significance and terminology, but do not over-rank on empirical rigor.

### 11. ChatDev

Verdict: A historically important multi-agent software prototype system with useful workflow ideas, but evaluation quality is weaker than later coding-agent benchmarks.

Strengths: role-specialized software workflow; chat-chain phases are easy to understand; communicative dehallucination is a concrete mechanism; ablations support roles and review/testing phases.

Weaknesses: quality metrics are proxy-heavy; generated projects are prototypes; cost and single-agent baselines are not cleanly matched; results depend on requirements and judge design.

Question: How does ChatDev perform on repository-level tasks with hidden tests and budget-matched solo agents?

Repo takeaway: Keep as early multi-agent SWE history, but rely on CooperBench, CAID, SWE-bench, and OpenHands-style work for stronger evidence.

### 12. COMA

Verdict: A strong anchor paper for cooperative MARL credit assignment through centralized critics and counterfactual baselines.

Strengths: clean multi-agent credit-assignment mechanism; centralized training/decentralized execution is well motivated; StarCraft micromanagement evidence is meaningful; became a durable baseline family.

Weaknesses: empirical breadth is modest by current standards; critic quality is a dependency; theory has errata and should be cited carefully; not LLM-agent-specific.

Question: Which lessons from counterfactual credit assignment can transfer to LLM-agent team training or attribution?

Repo takeaway: Keep as a high-quality anchor for credit assignment and CTDE.

### 13. CooperBench

Verdict: A strong negative result showing that coding agents often lose capability when forced to cooperate under partial observability.

Strengths: clean Solo vs Coop comparison; realistic repository tasks and expert tests; communication ablation separates merge conflicts from semantic success; failure taxonomy is actionable.

Weaknesses: setup emphasizes isolated branches and text chat; more-agent results use a smaller subset; richer shared-state mechanisms may change results; some qualitative labels depend on interpretation.

Question: Can structured shared state, typed contracts, or diff visibility close the semantic coordination gap?

Repo takeaway: Promote as a core skepticism paper for multi-agent coding systems.

### 14. DELEGATE-52

Verdict: A strong delegated-editing reliability benchmark with broad practical value, though it is only indirectly multi-agent.

Strengths: broad 52-domain evaluation; long-horizon artifact preservation focus; strong warning about sparse severe corruption; practical for document and code handoff workflows.

Weaknesses: not actually an agent-agent coordination paper; round-trip edit structure may not capture all real workflows; full reproducibility depends on task/evaluator release; tool-use harness may be basic.

Question: Do verifier/editor multi-agent workflows reduce corruption, or do they add new preservation failures?

Repo takeaway: Keep as a reliability bridge for any MAS that passes artifacts between agents.

### 15. OpenAI Five / Dota 2

Verdict: A landmark scaled self-play result for team-based MARL, with enormous significance but limited reproducibility and breadth.

Strengths: world-champion-level team-game performance; documents scaling, rollout freshness, reward horizons, and training surgery; strong evidence for self-play coordination at scale; clear caveats about restrictions.

Weaknesses: one heavily engineered game domain; restricted Dota setting; huge compute makes reproduction unrealistic; not a compact algorithmic contribution.

Question: Which parts of the coordination result require homogeneous shared policy, self-play scale, or Dota-specific reward shaping?

Repo takeaway: Keep as an anchor for large-scale self-play and team coordination, with explicit reproducibility caveats.

### 16. Emergence of Grounded Compositional Language

Verdict: A useful early emergent-communication paper showing grounded symbolic protocols can arise under cooperative pressure, though the environment is synthetic.

Strengths: language emerges from task reward rather than text data; communication improves cooperative reward; analyses compositionality and context sensitivity; includes non-verbal alternatives.

Weaknesses: particle-world setup is small and abstract; human-interpretable meanings are post-hoc; limited external validity; reproducibility depends on training details and random seeds.

Question: Do similar pressures produce robust protocols in higher-dimensional environments with heterogeneous agents?

Repo takeaway: Keep as an anchor for grounded emergent language and communication-as-coordination.

### 17. Emergent Multi-Agent Communication in the Deep Learning Era

Verdict: A strong survey that remains useful because it warns against equating task success with meaningful communication.

Strengths: broad coverage of deep emergent communication; clear discrete/continuous channel distinction; strong cautions about degenerate codes and co-adaptation; useful diagnostic vocabulary.

Weaknesses: survey rather than new evidence; literature cutoff is 2020; does not cover LLM-native natural-language agent systems; reproducibility is not directly applicable.

Question: Which survey warnings best predict failure modes in current LLM-agent communication?

Repo takeaway: Keep as the main conceptual bridge from emergent communication to modern MAS reliability concerns.

### 18. Emergent Tool Use from Multi-Agent Autocurricula

Verdict: A landmark MARL self-play paper showing emergent tool use and counter-strategy cycles under competitive pressure.

Strengths: striking autocurriculum; coordination and tool use arise without explicit tool rewards; strong qualitative and quantitative analyses; scale/environment ablations are informative.

Weaknesses: one engineered MuJoCo world; extremely sample-hungry; some behaviors exploit simulator affordances; transfer evidence is mixed.

Question: Which autocurriculum ingredients are necessary for open-ended progress rather than a bounded strategy sequence?

Repo takeaway: Keep as a top anchor for self-play, emergent behavior, and environment-induced capability growth.

### 19. GAIA

Verdict: A strong general-assistant benchmark and bridge paper, but not multi-agent-specific.

Strengths: short-answer grading avoids excessive judge dependence; tasks require real tool use and browsing; human/model gap is clear; difficulty levels and held-out split are useful.

Weaknesses: low MAS specificity; GPT-4 plus plugins baseline was not reproducible; final-answer grading misses trajectory quality; benchmark may age with web drift and contamination.

Question: Can multi-agent systems improve GAIA under equal dollar and latency budgets, or do they mostly spend more calls?

Repo takeaway: Keep as a bridge benchmark for tool-heavy assistant evaluation.

### 20. GPTSwarm

Verdict: A solid graph-optimization paper that makes agent structure explicit and learnable, though the empirical story is still benchmark-specific.

Strengths: unifies prompts, tools, and agents as graphs; optimizes edges and node prompts; adversarial-agent experiments show topology value; spans reasoning, code, puzzles, and GAIA.

Weaknesses: search spaces and utility signals encode much of the benefit; budget matching is imperfect; generalization across tasks is not guaranteed; reproducibility hinges on prompts/configs.

Question: Do learned graph structures transfer, or must each benchmark/task family be optimized from scratch?

Repo takeaway: Keep as a core architecture-search/optimization reference.

### 21. G-Safeguard

Verdict: A valuable topology-aware security paper for LLM-MAS, with convincing motivation and useful experiments but mixed robustness across attack types.

Strengths: treats communication topology as a security surface; GNN detector and edge pruning are concrete; evaluates multiple topologies and attacks; high multi-agent specificity.

Weaknesses: reacts after communication data exists; tool-attack results can be mixed; detector labels and transfer claims need more stress testing; reproducing attack setups may be hard.

Question: Can a topology-aware guard prevent initial infection rather than only pruning after risky communication is observed?

Repo takeaway: Keep as a core MAS safety/security paper.

### 22. MaAS

Verdict: A strong cost-aware architecture-search paper arguing that agentic structure should be query-adaptive rather than fixed.

Strengths: clear agentic-supernet framing; evaluates reasoning, coding, and tool use; reports cost/accuracy tradeoffs; ablations identify textual gradients and efficiency controls.

Weaknesses: search-space design may drive gains; equal-budget single-agent and sampling baselines need sharper separation; long-horizon messy tasks are not deeply covered; reproducibility depends on optimization details.

Question: Can MaAS choose architectures online for real multi-step environments with persistent state and failure recovery?

Repo takeaway: Promote as a core reference for adaptive MAS design and cost-aware orchestration.

### 23. MADDPG

Verdict: A foundational deep MARL paper that made centralized critics for mixed cooperative-competitive settings practical.

Strengths: strong novelty for its era; handles mixed rewards and decentralized actors; includes opponent-policy and ensemble ideas; broad particle-world tasks show real coordination effects.

Weaknesses: small simulated domains by current standards; critic input scales with agent count; reproducibility relies on environment/prompt details; not LLM-agent-specific.

Question: Which MADDPG ideas map to learned critics or verifiers for language-agent teams?

Repo takeaway: Keep as a high-priority MARL anchor for CTDE and mixed-motive coordination.

### 24. MAPoRL

Verdict: A promising trained-collaboration paper for LLM debate, with high multi-agent specificity but still limited to small models and a narrow set of tasks.

Strengths: frames collaboration as multi-agent RL; rewards influence on self and other agents; includes no-collaboration controls; shows transfer between GSM8K and ANLI in the tested setting.

Weaknesses: mostly small instruction models; verifier quality and reward hacking are concerns; debate setting is narrower than general MAS; compute and budget controls remain incomplete.

Question: Does MAPoRL scale to frontier models, tool tasks, or open-ended collaboration without verifier leakage?

Repo takeaway: Keep as a trend paper showing collaboration can be trained, with follow-up needed before top-tier ranking.

### 25. MemGPT

Verdict: A highly useful agent-memory paper, but it is a bridge foundation rather than a multi-agent contribution.

Strengths: clear virtual-context architecture; strong memory retrieval gains; function-calling memory loop is practical; durable influence on agent memory designs.

Weaknesses: low MAS specificity; performance depends on reliable tool/function calls; document QA remains retriever-limited; memory benchmarks do not test inter-agent coordination.

Question: How should MemGPT-style memory be shared, partitioned, or audited across multiple agents?

Repo takeaway: Keep as a bridge foundation for persistent memory in MAS.

### 26. MemMA

Verdict: A useful multi-agent memory-cycle architecture with promising evidence, but evaluation is narrower than the concept.

Strengths: decomposes memory into planning, retrieval, diagnosis, and repair roles; backend-agnostic framing; addresses delayed supervision; practical probe-and-repair loop.

Weaknesses: main evidence is concentrated on conversational memory; gains may partly reflect extra inference budget; synthetic probe quality matters; long-term repair drift is unclear.

Question: Does MemMA outperform an equally budgeted single memory-manager agent with the same tools and stopping rules?

Repo takeaway: Keep as a core memory-coordination paper, but mark confidence lower until broader tasks are tested.

### 27. MetaGPT

Verdict: A strong early structured-workflow paper for multi-agent software engineering, with more convincing design than evaluation.

Strengths: SOP/document handoffs are a real coordination mechanism; role ablations are informative; executable feedback improves code generation; high practical influence.

Weaknesses: SoftwareDev evaluation is small and partly self-authored; costs and role count are not fully controlled; function-level coding benchmarks are not full SWE; production claims should be avoided.

Question: Which SOP artifacts actually drive gains when compared to a solo agent using the same documents and execution feedback?

Repo takeaway: Keep as an influential core framework, but place later evidence-heavy coding papers above it.

### 28. Mind2Web

Verdict: A strong web-agent dataset and grounding benchmark, but not a multi-agent paper.

Strengths: real websites and high-level tasks; cross-task/website/domain splits; candidate-ranking setup is practical; exposes DOM grounding as a bottleneck.

Weaknesses: low MAS specificity; offline snapshots miss alternative live paths; candidate generation can bottleneck; benchmark lacks full environment interaction.

Question: Do multi-agent web systems help by separating candidate generation, action selection, and verification?

Repo takeaway: Keep as a bridge benchmark for web grounding and browser-agent foundations.

### 29. MIRROR

Verdict: A useful multi-agent reflection paper for tool learning, but the contribution is incremental and full feasibility remains limited on harder planning tasks.

Strengths: separates intra- and inter-reflection; Planner/Tool/Answer roles are concrete; StableToolBench ablations support pre-handoff reflection; TravelPlanner results show partial constraint gains.

Weaknesses: final planning success remains low; LLM-judge and benchmark-specific metrics matter; extra reflection increases cost; broader tool environments are not tested deeply.

Question: When does pre-execution reflection prevent errors better than a separate verifier or retry loop?

Repo takeaway: Keep as a useful trend paper for reflection gates, not as decisive evidence for broad MAS superiority.

### 30. More Agents Is All You Need

Verdict: A useful baseline paper showing that simple sampling and voting can explain many "multi-agent" gains.

Strengths: systematic ensemble-size study; strong practical warning for MAS evaluations; covers reasoning and code tasks; layers over existing prompting/debate methods.

Weaknesses: weak multi-agent specificity because agents do not really coordinate; cost grows directly with samples; voting rules are task-specific; does not address long-horizon environments.

Question: Which claimed MAS gains survive against Agent Forest at equal tokens and latency?

Repo takeaway: Keep as a baseline/skepticism paper for separating collaboration from more samples.

### 31. Multi-Agent Collaboration via Evolving Orchestration

Verdict: A promising learned-orchestration paper where a centralized policy selects useful agents dynamically, though some results are average-driven and search-space-dependent.

Strengths: high MAS specificity; cost-aware RL controller; token use declines through training; learned topologies become more compact and cyclic; evaluates heterogeneous agent spaces.

Weaknesses: not all benchmark scores improve; rewards are coarse; agent/tool pool is fixed; equal-budget comparisons and reproducibility need scrutiny.

Question: Does the orchestrator generalize to new task distributions without retraining or overfitting benchmark rewards?

Repo takeaway: Keep as a core dynamic-orchestration paper.

### 32. Multiagent Debate

Verdict: An important early prompt-only debate paper with real influence, but its current evidential strength is limited by compute controls and narrow tasks.

Strengths: simple black-box method; improves factuality/reasoning in reported settings; studies agents, rounds, prompts, and mixed models; useful qualitative failures.

Weaknesses: more calls are not cleanly separated from collaboration; main results use older model versions and subsets; model-judged factuality can bias; debate can converge to wrong consensus.

Question: Does debate beat best-of-N or self-consistency under equal total tokens on modern frontier models?

Repo takeaway: Keep as a core historical debate reference, but pair with later budget-matched skepticism.

### 33. OMAC

Verdict: A useful optimization framework for MAS functionality and structure, but evidence is still black-box, supervised, and benchmark-dependent.

Strengths: five-dimension optimization taxonomy; contrastive refinement loop is reusable; optimizes prompts and collaboration structure; reports cost reductions through selection/routing.

Weaknesses: novelty overlaps with ADAS/AFlow/GPTSwarm-style workflow search; training requires repeated full-system evaluations; exhaustive coverage of dimensions is not proven; confidence depends on prompt/controller details.

Question: Which optimization dimension delivers the most robust out-of-domain gain after equal training cost?

Repo takeaway: Keep as a trend paper for MAS optimization, below MaAS until stronger evidence accumulates.

### 34. OpenHands

Verdict: A high-value platform paper for software-using agents, but its multi-agent claims are mostly infrastructure support.

Strengths: integrated sandbox, event stream, tools, UI, and evaluation harness; broad benchmark support; strong open-source artifact; includes delegation primitive.

Weaknesses: low direct MAS specificity; benchmark results are platform demonstrations rather than proof of a new agent mechanism; hand-crafted workflows remain; safety depends on runtime configuration.

Question: When does `AgentDelegateAction` improve results over a single OpenHands agent under equal budget?

Repo takeaway: Keep as essential bridge infrastructure for coding and web-agent experiments.

### 35. OSWorld

Verdict: A strong computer-use benchmark showing current multimodal agents are far below humans on real desktop workflows, but it is not multi-agent-specific.

Strengths: VM-based real computer tasks; execution-based final-state checks; broad applications and workflow categories; clear human/model gap and failure analysis.

Weaknesses: low MAS specificity; primarily Ubuntu benchmark; hand-authored evaluators may miss side effects; model results age quickly.

Question: Can specialized multi-agent division of labor solve OSWorld workflow tasks, or do GUI grounding errors dominate?

Repo takeaway: Keep as a bridge benchmark for long-horizon digital-agent evaluation.

### 36. ReAct

Verdict: A landmark agent-foundation paper for interleaving reasoning and acting, but not a multi-agent paper.

Strengths: canonical thought-action-observation pattern; strong practical impact on tool agents; improves grounding and interactive tasks; clear and reproducible prompting template.

Weaknesses: MAS specificity is absent; few-shot prompt results are sensitive to exemplars; constrained tool/action spaces; later agents need stronger controls and environments.

Question: In multi-agent settings, should ReAct traces be private to each agent, shared, or summarized through a coordinator?

Repo takeaway: Keep as a bridge foundation that underlies many MAS designs.

### 37. RIAL/DIAL

Verdict: A foundational emergent-communication paper showing how centralized training can make communication differentiable while execution remains decentralized.

Strengths: high novelty and significance; clean RIAL vs DIAL contrast; strong communication-specific mechanism; interpretable learned protocols; important CTDE precedent.

Weaknesses: small cooperative tasks; discrete protocol results do not imply natural language; parameter sharing assumptions may not hold for heterogeneous agents; reproduction requires old task setups.

Question: Can differentiable communication ideas inform training of natural-language communication policies for LLM agents?

Repo takeaway: Keep as a top anchor for emergent communication and learnable communication channels.

### 38. SafeArena

Verdict: A strong safety benchmark for autonomous web agents, but it is primarily a single-agent harmful-use evaluation.

Strengths: paired safe/harmful design; realistic BrowserGym/WebArena-style environments; ARIA risk levels are useful; jailbreak tests expose practical risk.

Weaknesses: low MAS specificity; explicit harmful intents underrepresent ambiguous misuse; automatic evaluators may miss harms; model/scaffold effects are not fully isolated.

Question: Do multi-agent browser systems amplify or reduce harmful-task completion under paired safe/harmful evaluation?

Repo takeaway: Keep as a bridge safety benchmark for agentic web systems.

### 39. SlopCodeBench

Verdict: A useful long-horizon coding benchmark showing pass rates hide accumulating maintainability debt, though it is not multi-agent-specific.

Strengths: carried-workspace trajectory design; quality metrics beyond tests; hidden tests; prompt interventions expose intercept-vs-slope distinction.

Weaknesses: low MAS specificity; Python track is the main evidence; static metrics are proxies for maintainability; human comparison is not task-matched.

Question: Do reviewer/refactorer agents change degradation slopes, or only add more code and cost?

Repo takeaway: Keep as a bridge benchmark for artifact quality in multi-agent coding pipelines.

### 40. SOTOPIA

Verdict: A strong interactive social-intelligence benchmark with genuine multi-agent relevance.

Strengths: goal-driven dyadic interaction; multi-dimensional evaluation beyond task success; human/model comparisons; shows partner quality affects outcomes.

Weaknesses: short fixed-turn episodes; LLM-as-judge limitations; dyadic settings are simpler than group MAS; scenarios are sampled abstractions rather than deployment.

Question: How do multi-agent teams with explicit theory-of-mind or memory mechanisms perform in SOTOPIA-hard?

Repo takeaway: Keep as a bridge/core social-interaction benchmark for agent-agent and human-agent behavior.

### 41. SWE-smith

Verdict: A strong data-infrastructure paper for software agents, but it is not specifically multi-agent.

Strengths: scalable environment-first task generation; execution-backed synthetic bugs; strong open-weight SWE-agent training result; useful ablations on data source and diversity.

Weaknesses: low MAS specificity; Python-centric; synthetic regressions are not the same as real issues; training/evaluation is scaffold-dependent.

Question: Can SWE-smith generate multi-agent collaboration tasks with interacting patches or handoff failures?

Repo takeaway: Keep as a bridge for SWE-agent training data and execution validation.

### 42. tau-bench

Verdict: A compact and practical tool-agent-user benchmark, valuable for reliability but not multi-agent-specific.

Strengths: combines user dialogue, APIs, and policy following; final database-state evaluation is concrete; `pass^k` captures repeated reliability; domains are deployment-relevant.

Weaknesses: low MAS specificity; only two initial domains; simulator and policy design determine difficulty; rule rewards may miss policy violations or bad dialogue.

Question: Can multiple agents improve tau-bench by separating policy checking, tool execution, and user dialogue under equal latency?

Repo takeaway: Keep as a bridge benchmark for interactive tool-use reliability.

### 43. Teams of LLM Agents can Exploit Zero-Day Vulnerabilities

Verdict: A high-signal dual-use trend paper showing structured teams can improve cyber exploitation, but evidence is small and deliberately hard to reproduce.

Strengths: concrete multi-agent hierarchy; recent sandboxed CVE benchmark; specialist roles and documents matter in ablations; direct relevance to agent safety.

Weaknesses: only 14 vulnerabilities; manual success checks; no public code/prompts for dual-use reasons; strongest result depends on GPT-4-0125-preview; breadth beyond web CVEs is unknown.

Question: Which benefits come from hierarchy versus simply giving a single cyber agent the same specialist documents and tools?

Repo takeaway: Keep as a trend/safety signal, with low reproducibility and dual-use caveats.

### 44. TheAgentCompany

Verdict: A strong workplace-agent benchmark that broadens agent evaluation, though multi-agent interaction is mostly through simulated colleagues rather than agent teams.

Strengths: self-hosted company environment; multi-app tasks with checkpoint scoring; realistic social and UI bottlenecks; useful benchmark for labor-automation claims.

Weaknesses: low-to-moderate MAS specificity; no human baseline in local summary; only two scaffolds tested; curated tasks are not a labor-market sample.

Question: Do agent teams help on tasks requiring colleague communication, or does UI/social ambiguity dominate?

Repo takeaway: Keep as a bridge benchmark for real-world digital work and social-tool workflows.

### 45. Two Heads are Better Than One

Verdict: A promising collaborative-reasoning trend paper, but its gains depend on generated traces, a specific AgentVerse setup, and incomplete controls.

Strengths: trains on ordered multi-agent traces; CEO controller adapts discussion and budget; reports gains across reasoning/coding benchmarks; studies scaling knobs.

Weaknesses: M500 is generated and filtered by strong models; comparison to all single-agent trace corpora is incomplete; CEO gains are modest over the trained base; generalization outside AgentVerse is uncertain.

Question: Would a single-agent model trained on equal-quality reasoning traces plus adaptive self-refinement close the gap?

Repo takeaway: Keep as a trend paper on trained collaborative reasoning, but require replication before top-100 promotion.

### 46. VDN

Verdict: A foundational cooperative MARL paper that introduced a durable value-factorization baseline.

Strengths: simple additive decomposition with decentralized greedy execution; directly addresses shared-reward credit assignment; empirical results beat independent and centralized baselines; clear predecessor to QMIX.

Weaknesses: additive assumption is restrictive; experiments are small two-agent gridworlds; learned decompositions are not unique; not LLM-agent-specific.

Question: What is the LLM-agent analogue of value decomposition for shared task success across specialist agents?

Repo takeaway: Keep as a high-priority anchor for cooperative value factorization.

### 47. WarAgent

Verdict: A creative LLM social-simulation paper, but evidence is too fragile for strong claims about historical or policy reasoning.

Strengths: structured country profiles and bounded action space; Board/Stick state trackers make simulation inspectable; anonymization experiments directly test historical recall; counterfactual trigger studies are interesting.

Weaknesses: historical accuracy metrics are partial; simulations are prompt- and model-sensitive; war-declaration accuracy is weak; social-science claims risk overinterpretation.

Question: Can WarAgent predictions be validated against held-out historical crises or expert-coded counterfactuals rather than familiar world-war narratives?

Repo takeaway: Keep as a borderline social-simulation example, but avoid using it as strong evidence of MAS reasoning.

### 48. WebArena

Verdict: A landmark web-agent benchmark with high practical value, but not a multi-agent paper.

Strengths: self-hosted realistic sites; functional correctness checks; high-level natural-language intents; clear human/model performance gap; widely reused by later systems.

Weaknesses: low MAS specificity; curated websites are still bounded replicas; some fuzzy evaluations rely on LLM judging; early model results are historically dated.

Question: Which WebArena failures are best addressed by multi-agent decomposition versus better single-agent grounding?

Repo takeaway: Keep as an essential bridge benchmark for browser agents.

### 49. Why Do Multi-Agent LLM Systems Fail?

Verdict: A strong failure-taxonomy and dataset paper that gives the field shared diagnostic language for MAS breakdowns.

Strengths: broad trace dataset across frameworks/tasks/models; grounded-theory taxonomy; human agreement and LLM-judge calibration; public artifacts; practical interventions.

Weaknesses: taxonomy is descriptive more than causal; cross-framework comparisons can be confounded; automated labels are imperfect; interventions do not produce a general recipe.

Question: Which failure labels most strongly predict final task failure after controlling for task and framework?

Repo takeaway: Promote as a core MAS reliability and debugging reference.

### 50. WorkArena

Verdict: A strong enterprise web-agent benchmark, but it is bridge infrastructure rather than a multi-agent contribution.

Strengths: realistic ServiceNow workflows; large parameterized task set; BrowserGym integration; exposes enterprise UI complexity and task-type failures; outcome validators are practical.

Weaknesses: low MAS specificity; one enterprise platform; task content is partly generated; model/scaffold results age quickly.

Question: Can specialized agents for UI navigation, policy reading, and verification solve WorkArena tasks more reliably than a single browser agent?

Repo takeaway: Keep as a bridge benchmark for realistic knowledge-work automation.

## Papers To Watch Before Top-100 Promotion

These are not necessarily bad papers, but they should receive extra scrutiny before promotion:

- `AgentHospital_2405.02957`: high-stakes domain, synthetic simulacrum evidence, weak clinical external validity.
- `AgentRxiv_2503.18102`: interesting cumulative-research loop, but narrow MATH-500 prompt-discovery evidence.
- `AutoAgents_2309.17288`: useful early idea, but weak preference-heavy evaluations.
- `WarAgent_2311.17227`: creative simulation, but fragile historical/social-science claims.

Common issues across borderline and score-6 papers:

- Multi-agent gains are not separated from more model calls, samples, or tokens.
- Evaluation relies on synthetic or self-generated tasks.
- LLM judges are used without enough calibration.
- Reproducibility depends on unreleased prompts, traces, API versions, or expensive systems.
- Bridge papers are excellent agent papers but are not directly about multi-agent mechanisms.
