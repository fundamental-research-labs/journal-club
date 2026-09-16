# Multi-Agent LLM Systems: Coordination, Scaling, and the Limits of More

**Executive Summary for Journal Club — May 2026**

---

The past eighteen months have seen an explosion of work on multi-agent LLM systems, driven by the intuition that complex tasks benefit from division of labor. This collection of eleven papers, spanning benchmarks, scaling laws, failure taxonomies, and architectural search, tells a surprisingly coherent story — one that is more cautionary than triumphant. The central narrative is this: multi-agent coordination can work, but it works far less often than we assume, for reasons that are becoming increasingly well-characterized.

## Theme 1: The Scaling Mirage — When More Agents Help and When They Don't

The most persistent tension across these papers is whether multi-agent systems actually outperform single agents given equivalent resources. Tran & Kiela (Paper 10) make the sharpest version of this argument, using information-theoretic analysis to show that single agents are more information-efficient under fixed token budgets, and that many multi-agent gains dissolve once compute is properly equalized. Kim et al. (Paper 7), in the most comprehensive scaling study to date, find that coordination yields diminishing returns once single-agent baselines exceed a performance threshold — a finding with uncomfortable implications for the field's trajectory.

And yet the picture is not uniformly bleak. Geng & Neubig's CAID framework (Paper 2) demonstrates genuine multi-agent gains of 26.7% on PaperBench through branch-and-merge coordination with git worktree isolation, showing that architectural tasks with natural decomposition boundaries do benefit from parallelism. Critically, they show that simply doubling single-agent iterations does not match these gains — the coordination structure itself matters. Yang et al. (Paper 11) reconcile these conflicting results elegantly: performance is bounded not by agent count but by effective information channels, and two diverse agents can match sixteen homogeneous ones. The implication is that most multi-agent evaluations have been measuring the wrong thing. Raw scaling is a mirage; what matters is whether the coordination topology matches the task's information structure, a point Kim et al. independently confirm.

## Theme 2: Degradation Is the Default — Quality Erodes With Horizon and Interaction

A second theme, less discussed but equally important, is that LLM-based systems degrade reliably over extended interactions, regardless of architecture. SlopCodeBench (Paper 5) quantifies this precisely: code quality erodes in 80% of trajectories, verbosity grows in nearly 90%, and no agent among eleven models solves any of their twenty iterative problems end-to-end. Most disturbingly, prompt interventions shift the intercept but not the slope — degradation is structural, not incidental. DELEGATE-52 (Paper 3) extends this finding beyond code to document editing across 52 professional domains, showing that even frontier models degrade documents by 25% on average, with degradation compounding over document size and interaction length. Their finding that agentic tool use does not help is particularly deflating for the multi-agent paradigm.

MemMA (Paper 4) represents the most promising counter-strategy: by separating strategic reasoning from execution and introducing in-situ self-evolving memory construction with synthetic probe QA, it detects and repairs memory failures before they propagate. This "immune system" approach to degradation — building monitoring and repair into the architecture rather than hoping prompts will prevent drift — may be the most important design pattern to emerge from this literature.

## Theme 3: Agents Execute but Do Not Reason — The Epistemic Gap

Ríos-García et al. (Paper 1) deliver perhaps the most fundamental challenge to the entire enterprise. Across 25,000+ runs of scientific agents in eight domains, they find that the base model explains 41.4% of variance while the scaffold contributes only 1.5%. Agents ignore evidence in 68% of traces, and genuine belief revision occurs in only 26%. These are systems that execute workflows competently but do not exhibit the epistemic reasoning patterns that would make them reliable autonomous actors. CooperBench (Paper 8) reveals a parallel deficit in the social domain: when two agents must collaborate on coding tasks that can conflict, success drops to roughly half of single-agent baselines, bottlenecked not by coding ability but by social intelligence — jammed communication, commitment deviation, and incorrect mutual expectations.

Cemri et al.'s MAST taxonomy (Paper 6) provides the organizational framework these failure modes have been lacking, identifying 14 failure categories across system design, inter-agent misalignment, and task verification. Together with MaAS (Paper 9), which shows that the right multi-agent architecture varies per-query and that query-dependent topology selection can cut inference costs by 55–94% while improving accuracy, these papers suggest that the field needs to move from static multi-agent designs toward adaptive systems that select coordination strategies based on task characteristics — and that know when not to coordinate at all.

## Discussion Questions

- If scaffold design explains only 1.5% of variance in agent performance (Paper 1), what is the actual value proposition of multi-agent frameworks? Are we building elaborate scaffolding around a capability that must come from pretraining?

- Papers 5 and 3 show that degradation is structural and resists prompt-level interventions. MemMA (Paper 4) proposes architectural self-repair. Is "monitor and repair" the only viable strategy, or can we envision training objectives that produce models resistant to horizon-dependent quality erosion?

- Yang et al. (Paper 11) argue that diversity, not agent count, drives multi-agent gains, while Tran & Kiela (Paper 10) argue single agents are more information-efficient. Under what precise conditions does the diversity benefit of multiple agents overcome the information loss of inter-agent communication?

- CooperBench (Paper 8) shows agents fail at collaboration due to social intelligence deficits. Is social intelligence a capability that scales with model size, or does it require fundamentally different training signals — and what does this imply for the ceiling of autonomous multi-agent systems?

- MaAS (Paper 9) shows that optimal topology is query-dependent. If we take this seriously, should the field abandon fixed multi-agent architectures entirely in favor of learned meta-controllers, and how do we prevent the meta-controller itself from becoming the new bottleneck?

---

## Paper Index

| # | Paper | Authors | ID | Venue |
|---|-------|---------|-----|-------|
| 1 | AI Scientists Produce Results Without Reasoning Scientifically | Ríos-García et al. | 2604.18805 | Preprint |
| 2 | CAID: Effective Strategies for Asynchronous SWE Agents | Geng & Neubig | 2603.21489 | Preprint |
| 3 | DELEGATE-52: LLMs Corrupt Your Documents When You Delegate | Laban et al. | 2604.15597 | Preprint |
| 4 | MemMA: Coordinating the Memory Cycle | Lin et al. | 2603.18718 | Preprint |
| 5 | SlopCodeBench: Benchmarking Coding Agent Degradation | Orlanski et al. | 2603.24755 | Preprint |
| 6 | Why Do Multi-Agent LLM Systems Fail? | Cemri et al. | 2503.13657 | NeurIPS 2025 Spotlight |
| 7 | Towards a Science of Scaling Agent Systems | Kim et al. | 2512.08296 | Preprint |
| 8 | CooperBench: Why Coding Agents Cannot Be Your Teammates Yet | Khatua et al. | 2601.13295 | Preprint |
| 9 | MaAS: Multi-agent Architecture Search via Agentic Supernet | Zhang et al. | 2502.04180 | ICML 2025 Oral |
| 10 | Single-Agent LLMs Outperform Multi-Agent Under Equal Token Budgets | Tran & Kiela | 2604.02460 | Preprint |
| 11 | Agent Scaling in LLM-Based MAS via Diversity | Yang et al. | 2602.03794 | Preprint |
