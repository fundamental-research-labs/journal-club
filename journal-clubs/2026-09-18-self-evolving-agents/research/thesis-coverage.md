# Thesis-driven coverage audit

**Prepared September 16, 2026; cutoff unchanged.** The question is whether experience produces reusable future-task value beyond strong static procedures and additional inference, and whether the update procedure itself becomes better. The thesis is a hypothesis to challenge; the search also used independent field vocabulary and earlier method lineages.

## Counts and what they mean

| Measure | Before | After |
| --- | ---: | ---: |
| Canonical candidate/resource records | 151 | 153 |
| Shortlist + reviewed-reserve families | 49 | 56 |
| Substantive standalone reading notes | 48 | 55 |
| Distinct reviewed references actually cited in thesis prose | 13 | 56 |
| Reading priorities | 10 | 10 |

Counts deduplicate arXiv versions/HTML/PDF by paper identifier and companion project/blog/code artifacts by underlying family. The 56 thesis references represent 56 registered evidence families, **not 56 independent confirmations**: they share datasets, models, authors and method lineages. Two distinct integrity studies share one note, hence 55 notes. Reviews include relevant primary sections, method/result readings and first-party repository documents, not necessarily every page. No metadata-only lead counts as empirical thesis support. A theory paper and practitioner architecture records count for their explanatory role, not as capability experiments.

Two works were missing from the register: ExpeL (2023) and Rethinking Continual Experience Internalization (June 2026). Five retained candidates were promoted into the reviewed thesis set: ADAS, AFlow, ReasoningBank, MemSkill and SkillsBench. The other expansion restores relevant reviewed reserves to the argument. Thus most of the deficiency was selection/integration, with two substantive discovery omissions. About 50 is a useful breadth diagnostic; reaching 56 does not establish exhaustive recall.

## Questions, competing evidence and disposition

| Thesis question / claims | Existing anchor | Strongest challenge or omitted approach | Search / resolution |
| --- | --- | --- | --- |
| What persists? C001–C003, C013 | Reflexion, Voyager, WikiSkill | Cross-task experience predates newer skill libraries; memory operations themselves can evolve | ExpeL and ReasoningBank lineage; MemSkill methods/citations. Added mechanism comparisons and seven new notes across audit. |
| Does learning beat static expertise? C005, C018 | FinEvo static-skill control | Curated versus self-authored skills; task construction may favor skills | SkillsBench v4 read. Preserve 87-task/18-config frame, one-shot limitation, curation costs and selection bias. |
| Does it beat more search? C006, C014 | Harness critique | ADAS/AFlow design search yields useful frozen artifacts; ReasoningBank explicitly couples learning and extra compute | Reopened primary workflow/memory methods. Revised false dichotomy: learning and computation can complement one another. |
| Can weight gains persist? C004, C008, C015, C019 | SEAL, R-Zero | Successful multi-cycle internalization recipe as well as collapse | New June paper read and screened; three-cycle bounded results, non-monotonic BrowseComp and fixed recipe retained. |
| Does reuse survive task/interface change? C007, C016 | AgentStream | HarnessDev, SEA-Eval, EvoHarnessBench, SHAPER and lifecycle regressions | Reused prior primary-reading notes; explicit task/order/interface distinction and narrow transfer claims. |
| Does the improver improve? C009, C017 | STOP, Hyperagents, Dream-RSI | EvoX, Escher-Loop, MLEvolve; artifact versus policy transfer | Seed citation/keyword pass; static-pool tie and mixed Dream-RSI mathematics corrected. No general acceleration claim. |
| Is the measurement trustworthy and economically useful? C010–C012, C016–C017 | Shopify, fixed-budget critique | Integrity benchmarks; first-party logs; theory of R&D bottlenecks | Practitioner/counterevidence lane; Reef/NemoClaw/SoL-Pi/AlphaEvolve architecture and limits integrated. Optional new vendor leads remain outside core evidence. |

## Reference roles in the thesis

Every entry below is used in the essay itself. Citation labels retain result/section locators. Notes contain source-specific populations, comparators, uncertainty and limitations. Grouping follows the argument, not a recommended reading order.

### Learning that lasts

| Reference / canonical version | Role and locator | Reading note |
| --- | --- | --- |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366v4) · `2023-reflexion` | foundation / definition; Reflexion, §§3–4 | [Review](notes/2023-reflexion.md) |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) · `2023-voyager` | foundation / definition; Voyager, §§2–3 | [Review](notes/2023-voyager.md) |
| [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943v2) · `2025-self-adapting-language-models` | foundation / definition; SEAL, §3 | [Review](notes/2025-self-adapting-language-models.md) |
| [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304v3) · `2023-stop` | foundation / definition; STOP, §3 and Algorithm 1 | [Review](notes/2023-stop.md) |

### What an agent can change

| Reference / canonical version | Role and locator | Reading note |
| --- | --- | --- |
| [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454v1) · `wikiskill` | mechanism / bounded positive evidence; WikiSkill, §§3–4, Table 1 and Appendix B | [Review](notes/2026-wikiskill.md) |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144v3) · `2023-expel` | mechanism / bounded positive evidence; ExpeL, §4 | [Review](notes/2023-expel.md) |
| [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2) · `2025-reasoningbank` | mechanism / bounded positive evidence; ReasoningBank, §§3–4 | [Review](notes/2025-reasoningbank.md) |
| [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618v3) · `2025-agentic-context-engineering` | mechanism / bounded positive evidence; ACE, §3 | [Review](notes/2025-agentic-context-engineering.md) |
| [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192v2) · `2026-memrl` | mechanism / bounded positive evidence; MemRL, §§4–6 | [Review](notes/2026-memrl.md) |
| [SelfMem: Self-Optimizing Memory for AI Agents](https://arxiv.org/abs/2607.03726v1) · `2026-selfmem` | mechanism / bounded positive evidence; SelfMem, §§3–5 | [Review](notes/2026-selfmem.md) |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474v2) · `2026-memskill` | mechanism / bounded positive evidence; MemSkill, §§3–4 | [Review](notes/2026-memskill.md) |
| [EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.02766v1) · `2026-evoskill` | mechanism / bounded positive evidence; EvoSkill, §§2–3 | [Review](notes/2026-evoskill.md) |
| [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](https://arxiv.org/abs/2603.25158v5) · `2026-trace2skill` | mechanism / bounded positive evidence; Trace2Skill, §§2–3 | [Review](notes/2026-trace2skill.md) |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904v2) · `2026-skillopt` | mechanism / bounded positive evidence; SkillOpt, §§3–4 | [Review](notes/2026-skillopt.md) |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457v2) · `2025-gepa` | mechanism / bounded positive evidence; GEPA, Algorithm 1 and §4 | [Review](notes/2025-gepa.md) |
| [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435v2) · `2024-automated-design-agentic-systems` | mechanism / bounded positive evidence; ADAS, §§3–4 | [Review](notes/2024-automated-design-agentic-systems.md) |
| [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762v4) · `2024-aflow` | mechanism / bounded positive evidence; AFlow, §§4–5 | [Review](notes/2024-aflow.md) |
| [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954v3) · `2025-darwin-godel-machine` | mechanism / bounded positive evidence; Darwin Gödel Machine, §§3–6 | [Review](notes/2025-darwin-godel-machine.md) |
| [Huxley-G\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://arxiv.org/abs/2510.21614v3) · `2025-huxley-godel-machine` | mechanism / bounded positive evidence; Huxley–Gödel Machine, §§3–4 | [Review](notes/2025-huxley-godel-machine.md) |
| [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850v4) · `2026-agentic-harness-engineering` | mechanism / bounded positive evidence; Agentic Harness Engineering, Tables 2–3 | [Review](notes/2026-agentic-harness-engineering.md) |
| [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071v2) · `2026-evo-harness` | mechanism / bounded positive evidence; Evo-Harness, §§4.5–4.6 and Table 4 | [Review](notes/2026-evo-harness.md) |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350v2) · `2026-shaper` | mechanism / bounded positive evidence; SHAPER, §§3–4 | [Review](notes/2026-shaper.md) |

### Where the learning signal comes from

| Reference / canonical version | Role and locator | Reading note |
| --- | --- | --- |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335v3) · `2025-absolute-zero` | feedback / update boundary; Absolute Zero, §3 and Appendix D | [Review](notes/2025-absolute-zero.md) |
| [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084v3) · `2025-test-time-reinforcement-learning` | feedback / update boundary; TTRL, §§2–3 | [Review](notes/2025-test-time-reinforcement-learning.md) |
| [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292v1) · `2026-agent-world` | feedback / update boundary; Agent-World, §§3–4 | [Review](notes/2026-agent-world.md) |
| [Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration](https://arxiv.org/abs/2604.18131v1) · `2026-spontaneous-world-knowledge` | feedback / update boundary; World Knowledge Exploration, §§3–4 | [Review](notes/2026-spontaneous-world-knowledge.md) |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004v4) · `2025-r-zero` | feedback / update boundary; R-Zero, §2 | [Review](notes/2025-r-zero.md) |
| [Hyperagents](https://arxiv.org/abs/2603.19461v1) · `hyperagents` | feedback / update boundary; Hyperagents, §3 | [Review](notes/2026-hyperagents.md) |
| [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/html/2609.14858v1) · `2026-dream-rsi` | feedback / update boundary; Dream-RSI, §3 | [Review](notes/2026-dream-rsi.md) |
| [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/html/2606.04703v1) · `2026-rethink-continual-internalization` | feedback / update boundary; Rethinking Continual Experience Internalization, §§3–5, Figures 1 and 6 | [Review](notes/2026-rethink-continual-internalization.md) |
| [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276v2) · `2026-sia` | feedback / update boundary; SIA, §§5–6 | [Review](notes/2026-sia.md) |
| [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396v2) · `metarsi` | feedback / update boundary; MetaRSI, §§3–5 and Appendix F | [Review](notes/2026-metarsi.md) |
| [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523v1) · `sciencebuddy` | feedback / update boundary; ScienceBuddy, §§4 and 7 | [Review](notes/2026-sciencebuddy.md) |
| [Sidekick's continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop) · `2026-shopify-sidekick` | feedback / update boundary; Shopify Engineering, “Sidekick's continual learning loop” | [Review](notes/2026-shopify-sidekick.md) |
| [Reef: inference-time learning infrastructure](https://github.com/Human-Agent-Society/reef/tree/401db3670d34b1b5a77989234272e0bee4b90ce8) · `reef` | feedback / update boundary; Reef, pinned README and Meta-Harness report | [Review](notes/2026-reef.md) |
| [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/) · `2026-nemoclaw-memory` | feedback / update boundary; NVIDIA, memory-driven agent and linked evaluation | [Review](notes/2026-nemoclaw-memory.md) |

### How much of the gain comes from learning?

| Reference / canonical version | Role and locator | Reading note |
| --- | --- | --- |
| [FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows](https://arxiv.org/html/2608.06144v1) · `2026-finevo-bench` | control / challenge / transfer; FinEvo-Bench, §§4.1–4.3 and Table 3 | [Review](notes/2026-finevo-bench.md) |
| [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670v4) · `2026-skillsbench` | control / challenge / transfer; SkillsBench, Tables 2 and 6, Appendix D.6 | [Review](notes/2026-skillsbench.md) |
| [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2) · `harness-evolution-evaluation` | control / challenge / transfer; Rethinking the Evaluation of Harness Evolution for Agents, Tables 1–3 and §4.4 | [Review](notes/2026-harness-evolution-evaluation.md) |
| [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](https://arxiv.org/abs/2609.01437v1) · `harnessdev` | control / challenge / transfer; HarnessDev, evolution and version-switch analysis | [Review](notes/2026-harnessdev.md) |
| [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988v3) · `2026-sea-eval` | control / challenge / transfer; SEA-Eval, §§4–5 | [Review](notes/2026-sea-eval.md) |
| [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280v2) · `evoharnessbench` | control / challenge / transfer; EvoHarnessBench, §§3–4 | [Review](notes/2026-evoharnessbench.md) |
| [AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?](https://arxiv.org/html/2608.00155v1) · `agentstream` | control / challenge / transfer; AgentStream, Tables 2 and 11–13 | [Review](notes/2026-agentstream.md) |
| [Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576v3) · `library-drift` | control / challenge / transfer; Library Drift, §§5–7 | [Review](notes/2026-library-drift.md) |
| [When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents](https://arxiv.org/abs/2608.05810v1) · `2026-self-evolution-backfires` | control / challenge / transfer; When Self-Evolution Backfires, method, Tables 1–4 | [Review](notes/2026-self-evolution-backfires.md) |
| [Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization](https://arxiv.org/abs/2603.18388v2) · `2026-reflection-in-the-dark` | control / challenge / transfer; Reflection in the Dark, Tables 1–3 | [Review](notes/2026-reflection-in-the-dark.md) |
| [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962v1) · `2026-ground-truth-first` | control / challenge / transfer; Ground Truth First, §§5–7 | [Review](notes/2026-ground-truth-first.md) |
| [RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents](https://arxiv.org/abs/2603.11337v1) · `2026-reward-hacking-agents` | control / challenge / transfer; RewardHackingAgents, §§III–VI | [Review](notes/2026-reward-hacking-agents.md) |
| [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964v1) · `2026-reward-hacking-benchmark` | control / challenge / transfer; Reward Hacking Benchmark, §§4–6 | [Review](notes/2026-reward-hacking-agents.md) |

### Improving the search, or improving the ability to search?

| Reference / canonical version | Role and locator | Reading note |
| --- | --- | --- |
| [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131v1) · `2025-alphaevolve` | artifact-versus-improver boundary / counterevidence; AlphaEvolve, §§2–3 | [Review](notes/2025-alphaevolve.md) |
| [autoresearch](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117) · `autoresearch` | artifact-versus-improver boundary / counterevidence; autoresearch, pinned experiment contract | [Review](notes/2026-autoresearch.md) |
| [SoL-Pi](https://github.com/NVlabs/SoL-Pi/tree/2b791687a489a1d24da816cf1634d8ae1d36befd) · `sol-pi` | artifact-versus-improver boundary / counterevidence; SoL-Pi, pinned README | [Review](notes/2026-sol-pi.md) |
| [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413v2) · `2026-evox` | artifact-versus-improver boundary / counterevidence; EvoX, §§3–6 | [Review](notes/2026-evox.md) |
| [Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization](https://arxiv.org/abs/2604.23472v2) · `2026-escher-loop` | artifact-versus-improver boundary / counterevidence; Escher-Loop, §§2–3 and Table 1 | [Review](notes/2026-escher-loop.md) |
| [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473v1) · `2026-mlevolve` | artifact-versus-improver boundary / counterevidence; MLEvolve, §§3–4 and Table 3 | [Review](notes/2026-mlevolve.md) |
| [The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802v1) · `2026-economics-rsi` | artifact-versus-improver boundary / counterevidence; The Economics of Recursive Self-Improvement, §§2–4 | [Review](notes/2026-economics-rsi.md) |

## Search provenance and unresolved scope

Three Luna discovery lanes and two Sol screening/review lanes worked under the research skill, without recursive delegation. Follow-up assignments read four consequential foundations after the initial count passed 50. Coordinator merged records, reopened pivotal new primary material, checked versions, and revised the argument using the analyze skill. [Memory lane](workers/thesis-memory-coverage.md), [meta lane](workers/thesis-meta-coverage.md), [evaluation lane](workers/thesis-evaluation-coverage.md), [primary screening](workers/thesis-additions-screening.md), [draft review](workers/thesis-review.md), and the [search log](search-log.md) preserve access limits and corrections.

The reviewed essay uses the previously verified September 16 frontier (including September 14–15 papers); this was a cross-field omission audit, not a claim to independently refresh every existing record/version. X/talk access remains limited; no new inaccessible post or unwatched talk supplies a thesis finding. Broader multi-agent topology search, non-LLM meta-learning foundations, embodied diversity, and independent long-term production replications remain incompletely covered. The key evidential gaps are complete lifetime cost, untouched future task families, reliable feedback, repeated trajectories and retention. They narrow the thesis rather than support claims that no such result can exist.

Budgeted discovery and consequential-gap resolution, not demonstrated search saturation, stopped this pass. Original worker files are provisional leads; corrections in shared notes/register and the screening memo take precedence. SkillsBench's obsolete snapshot, MemSkill's overstated conversation-to-embodiment transfer, and stale EvoX/MLEvolve duplicate metadata were rejected before merge. Ancillary Anthropic/METR/STATE-Bench and cost/practitioner leads remain in the lane reports for a future focused update; they are not counted in the 56 thesis references.
