# Section Review and Evidence Log

This log records the section-level critique and paper-specific evidence used to revise `index.qmd`. It is intentionally separate from the manuscript so the review trail is visible before prose changes.

## Rubric

Scores use a 1-5 scale: 1 = weak, 3 = adequate but needs work, 5 = strong. Criteria: clarity, importance, relevance to the "History of Modern Multi-Agent" thesis, evidence support, narrative force, and coherence with adjacent sections.

| Section | Clarity | Importance | Thesis relevance | Evidence | Narrative force | Coherence | Main revision need |
|---|---:|---:|---:|---:|---:|---:|---|
| Key Messages | 5 | 5 | 5 | 3 | 4 | 5 | Add sharper evidence hooks and define multi-agent as structured test-time computation over separately stateful attempts. |
| Introduction | 4 | 5 | 5 | 4 | 4 | 4 | Avoid overclaiming that all modern agentic LLM work began with agent societies; distinguish single-agent tool-use lineage from multi-agent branch. |
| Scope and Terms | 4 | 5 | 5 | 3 | 4 | 5 | Define the unit as a separately controlled trajectory whose output must be selected, routed, checked, or merged. |
| Coordination Before LLMs | 4 | 4 | 4 | 4 | 3 | 4 | Make the MARL-to-LLM mapping explicit: context partitioning, lossy summaries, credit assignment, and decentralized execution. |
| The 2023 Bet | 4 | 5 | 5 | 4 | 4 | 4 | Keep the optimism, but ground it in concrete stabilizers and caveats from CAMEL, ChatDev, MetaGPT, AutoGen, and debate. |
| From Prompts to Runtimes | 4 | 4 | 5 | 3 | 3 | 3 | Make runtime primitives concrete: sandboxes, event streams, ledgers, tool APIs, Docker, benchmark harnesses, and logs. |
| Agent Benchmarks Changed the Evidence Standard | 4 | 5 | 4 | 4 | 4 | 4 | Replace benchmark catalogue with typology of executable outcome evaluation. |
| The Coordination Reality Check | 4 | 5 | 5 | 4 | 4 | 5 | Add quantitative evidence for coordination costs and equal-budget controls. |
| Search Plus Verification | 4 | 5 | 5 | 3 | 4 | 4 | Add a verifier hierarchy and positive examples where verification selects useful search. |
| From Conversation to Artifacts | 4 | 5 | 5 | 4 | 4 | 5 | Make artifacts the causal hinge: they make partial work inspectable, replayable, comparable, and mergeable. |
| Memory, Shared State, and Degradation | 4 | 5 | 4 | 4 | 4 | 5 | Frame memory as persistent coordination state, not just context storage. |
| Safety Is a Coordination Problem | 4 | 5 | 5 | 3 | 4 | 4 | Add concrete propagation chain and safety benchmark numbers. |
| Design Principles | 5 | 5 | 5 | 3 | 4 | 5 | Group principles by evidence family instead of leaving a flat list. |
| Future Directions | 4 | 5 | 5 | 4 | 3 | 4 | Replace citation stack with research programs: architecture selection, diversity measurement, artifact-native protocols, safety/state systems, human review allocation. |
| Conclusion | 5 | 5 | 5 | 4 | 5 | 5 | Add historical callback: LLM agents changed the medium, not the underlying coordination problem. |

## Evidence Packets

### Foundations and 2023 Systems

- RIAL/DIAL, CommNet, and TarMAC show that learned communication required specific mechanisms before LLMs: differentiable messages, parameter sharing, continuous message passing, and targeted attention. Local notes report CommNet traffic failure at 1.6% vs 9.4% for independent LSTM, and TarMAC hard traffic success at 97.1% with two communication rounds vs 78.9% for CommNet.
- MADDPG, COMA, VDN, QMIX, MAPPO, and SMAC support the claim that credit assignment, centralized training/decentralized execution, value factorization, and benchmark protocol were already core design concerns.
- Sequential social dilemmas and large-scale self-play broaden the older history beyond communication: sequential cooperation is policy-level, OpenAI Five beat OG 2-0 and won 99.4% of 7,257 public Arena games under a restricted Dota setting, and hide-and-seek autocurricula produced emergent tool use with large-scale training and environment caveats.
- CAMEL is a useful anchor for the early "agent society" wave: 25,000 AI Society conversations across 50 assistant roles, 50 user roles, and 10 tasks; reported wins around 73-76% in Table 1, with caveats around GPT-4 summaries, role flipping, loops, false information, and safety.
- Generative Agents supports memory/planning/reflection for social simulation: 25 Smallville agents showed routines, information diffusion, relationships, and party coordination; this is believability evidence, not task-completion reliability.
- ChatDev and MetaGPT should be treated as benchmark-dependent early software-agent evidence: ChatDev reports executability 0.8800 vs GPT-Engineer 0.3583 and MetaGPT 0.4145 on its dataset; MetaGPT reports 85.9% HumanEval, 87.7% MBPP, and executable-feedback gains.
- Debate papers support "structured extra inference plus critique," not proof that conversation itself creates intelligence. Du et al. report improvements on arithmetic, GSM8K, biographies, and MMLU, but with extra compute, selected subsets, and wrong-consensus risks.
- AutoGen, AgentScope, Magentic-One, OpenHands, and AutoAgent support the runtime turn. AutoGen reports MATH 69.48% vs vanilla GPT-4 55.18% and ALFWorld 69% with a grounding agent vs 54%; Magentic-One reports GAIA 38.0% with ledger/worker ablation drops; OpenHands contributes event streams, Docker sandboxing, browser/shell/IPython actions, benchmark harnesses, and delegation primitives.

### Evaluation, Coordination Costs, and Verification

- WebArena and VisualWebArena anchor the agent-benchmark evidence shift: WebArena reports 14.41% best GPT-4 baseline vs 78.24% human on 812 tasks; VisualWebArena reports 16.37% GPT-4V+SoM vs 88.70% human on 910 visually grounded tasks.
- OSWorld, AndroidWorld, WorkArena, GAIA, tau-bench, and TheAgentCompany broaden the point beyond websites: OSWorld 12.24% best model vs 72.36% human; AndroidWorld GPT-4 Turbo M3A 30.6% vs 80.0% human; GAIA GPT-4+plugins around 15% vs around 92% human; tau-bench pass^k shows reliability decay; TheAgentCompany best baseline completes 30.3% full tasks and 39.3% partial.
- SWE-bench and Agentless establish patch/test evaluation as a stronger artifact standard: original SWE-bench baselines resolve under 4% in BM25 settings; Agentless resolves 96/300 SWE-bench Lite tasks at about $0.70 average cost using localization, sampled patches, generated reproduction tests, regression tests, and voting.
- AgentBench, AgentBoard, BrowserGym, MASLab, and AI Agents That Matter support stronger reporting standards: AgentBoard's progress metric correlates above 0.95 with human progress judgments; MASLab shows evaluator choice can move AgentVerse from 79.0 to 25.6; AI Agents That Matter finds 7/17 surveyed benchmarks lacked holdouts.
- Why Do Multi-Agent LLM Systems Fail? gives concrete failure taxonomy evidence: 14 modes across system design, inter-agent misalignment, and task verification; 1,642 annotated traces; human kappa 0.88 and LLM-judge kappa 0.77; high-level verification improved ChatDev by 15.6% but did not solve correctness.
- Science of Scaling and Single-Agent Outperforms are the strongest controls against generic "more agents" claims: MAS effects range from +80.8% to -70.0%; communication overhead scales super-linearly with exponent 1.724; under equal thinking-token budgets, single agents match or beat MAS on FRAMES/MuSiQue except under degraded context.
- CooperBench makes coordination failure concrete: leading two-agent coding setups are roughly 50% below solo; communication reduces merge conflicts but not success; 2/3/4 agents drop 68.6%/46.5%/30.0% in a scaling subset.
- DELEGATE-52 and SlopCodeBench justify long-horizon artifact degradation as a core theme: DELEGATE-52 reports frontier models corrupt roughly 25% of content after 20 interactions and agentic tools add about 6% degradation; SlopCodeBench reports no agent solves any full problem end-to-end, structural erosion rises in 80% of trajectories, and verbosity in 89.8%.
- More Agents, Mixture-of-Agents, AgentScalingDiversity, and Two Heads support search/diversity claims with caveats: homogeneous scaling plateaus around N=4; two diverse agents can match or exceed sixteen homogeneous agents; diversity among wrong paths is not useful.
- CAID and MIRROR are positive verifier-centered examples: CAID improves PaperBench MiniMax from 10.4% to 36.7% and Claude from 57.2% to 63.3% using isolated worktrees and branch/merge; MIRROR's reflection ablations show pre-execution reflection helps tool-use pass rates, but hard planning tasks remain difficult.

### Artifacts, Memory, Science, and Safety

- Software-agent evidence supports artifacts as more than outputs: SWE-bench tasks are repository patches checked by tests; SWE-agent improves through an agent-computer interface; Agentless shows a non-agentic pipeline can be competitive when localization, tests, and voting are strong; CAID shows isolated worktrees and merges matter.
- AgentCoder is a useful earlier testing-loop example: a Programmer/Test Designer/Test Executor loop improves function-level code-generation benchmarks, but this is not repository collaboration evidence.
- Scientific-agent systems produce artifact chains but require caution: AI Scientist estimates about $10-15 per generated paper; Agent Laboratory's auto-review scores diverge from human scores; PaperBench best BasicAgent reaches 21.0% vs ML PhD best-of-3 at 41.4% on a subset.
- AI co-scientist supports scientist-in-the-loop claims: it uses generation, reflection, ranking, and evolution agents over 203 goals, but expert evaluation covers only 11 goals and wet-lab results are preliminary.
- Curie, InternAgent, and MLGym are important additions if cited: Curie emphasizes experimental rigor and structured experiment records; InternAgent covers closed-loop hypothesis-to-verification; MLGym evaluates open-ended AI research workflows with heterogeneous artifacts.
- AgentRxiv shows asynchronous research artifacts can help but also need verification: shared archive improves MATH-500 from 70.2% to 78.2%; parallel labs reach 79.8% but use 120 papers vs 40; human verification is needed because of hallucinated results and reward hacking.
- MemGPT, A-Mem, and MemMA support memory as a coordination surface. MemGPT deep-memory retrieval improves GPT-4 from 32.1% to 92.5% in the local notes; MemMA improves LightMem LoCoMo ACC 75.66 to 81.58 and multi-hop questions 65.62 to 78.12; removing iterative retrieval drops ACC 84.87 to 70.39.
- Safety evidence should emphasize propagation rather than vague collusion: SafeArena contains 250 harmful and 250 safe web tasks and reports GPT-4o harmful completion at 22.8%; OpenAgentSafety reports unsafe behavior on vulnerable trajectories from 49.06% to 72.73%; G-Safeguard reduces attack success through topology-aware edge pruning; zero-day-agent work is sandboxed dual-use evidence.

### Principles and Future Directions

- Design principles should be grouped by evidence family: budget and task fit, non-redundant search, adaptive orchestration, artifact-centered verification, and state/safety governance.
- Architecture selection is a major future program: Science of Scaling, MaAS, DyLAN, OMAC, and GPTSwarm all treat topology or orchestration as something to predict, search, or optimize rather than hand-code once.
- Online diversity measurement is a major future program: AgentScalingDiversity's K* frames useful diversity as effective independent channels, not semantic variety or raw agent count.
- Artifact-native collaboration protocols are a major future program: CAID, Curie, Agent Laboratory, MLGym, and MASLab point toward standard traces with prompts, tools, costs, diffs, tests, memory updates, verifier outcomes, and human interventions.
- Multi-agent state and safety systems are a major future program: MemMA and G-Safeguard make memory repair and topology-aware containment concrete.
- Human-review allocation is a major future program: AI co-scientist, Agent Laboratory, Curie, and MLGym all imply that scarce human judgment should be routed to high-impact, uncertain, irreversible, or integration-heavy steps.

## Planned Manuscript Changes

1. Tighten the key thesis and scope around "separately stateful attempts" and "verified progress."
2. Make the pre-LLM section less generic by adding concrete communication, credit-assignment, self-play, and social-dilemma evidence.
3. Add a 2023 section paragraph that distinguishes productive role decomposition from confounded evidence.
4. Make the runtime section about concrete runtime substrate, not just frameworks.
5. Rewrite agent-benchmark coverage around executable outcome evaluation, with benchmark categories and historical numbers.
6. Add quantitative coordination-cost evidence to the reality-check section.
7. Add a verifier hierarchy and evidence-backed help/hurt table to the search-plus-verification section.
8. Strengthen artifacts, memory, and safety with concrete paper results and caveats.
9. Regroup design principles by evidence family.
10. Replace the future-directions citation stack with research programs.
11. Add missing bibliography entries only when new citation keys are used.
