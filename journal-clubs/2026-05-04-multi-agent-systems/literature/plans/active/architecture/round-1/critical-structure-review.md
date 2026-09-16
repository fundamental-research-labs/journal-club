# Critical Structure Review

Date: 2026-05-07

Target: `manuscript/multi-agent-review-draft/index.qmd`

Context read:

- `overview/multi-agent-field-narrative.md`
- `docs/best-review-article-qualities.md`
- `plans/active/architecture/round-1/structure-improvement-plan.md`
- `manuscript/multi-agent-review-draft/index.qmd`
- `manuscript/multi-agent-review-draft/section-review-evidence.md`
- local paper summaries and claims for MAPoRL, ACC-Collab, MAS-GPT, OMAC, GPTSwarm, MaAS, AgentNet, DyLAN, and evolving orchestration

## Executive Diagnosis

The manuscript has the right thesis and many of the right papers, but the structure is still too close to a sequence of topical essays. The central argument is strong:

> Multi-agent LLM systems matter when they convert extra test-time computation into verified, inspectable progress over artifacts.

The current section order supports that argument, but not yet with enough architectural force. It alternates among chronology, evaluation standards, mechanisms, artifacts, memory, safety, principles, and future directions at the same heading level. That gives the review breadth, but weakens the reader's ability to classify new work by mechanism and evidence quality.

The most important missing structural component is an explicit treatment of **coordination optimization and coordination training**. The draft mentions adaptive orchestration in `Future Directions`, but it does not yet separate:

1. optimizing the **system architecture** around mostly fixed models;
2. training a **policy or controller** that routes, selects, or stops agents;
3. training the **agents themselves** to collaborate better;
4. constructing **post-training data** from multi-agent interaction.

That gap matters because it is the natural answer to the skeptical middle of the review. If the field learned that prompting roles does not reliably create coordination, the next historical move is not just "use artifacts." It is also "make coordination itself an optimization target."

## Highest-Priority Structural Changes

### 1. Add A Central Section On Mechanisms Before Artifacts

The existing `Search Plus Verification` section contains a mechanism paragraph and a help/hurt table, but this material is too important to be embedded inside a broader conceptual section.

Add a major section after `The Coordination Reality Check`:

```text
## Mechanisms of Multi-Agent Value
```

This should be the review's classification engine. It should let readers place new papers quickly.

Suggested table:

| Mechanism | What is being multiplied or separated? | When it helps | Evidence to demand | Main failure mode |
|---|---|---|---|---|
| Sampling and voting | attempts | compact answers with cheap verification | budget-matched best-of-N and voting controls | correlated wrong answers |
| Heterogeneous aggregation | models, prompts, data priors | complementary errors or styles | model/prompt diversity ablations | diversity without correct-path evidence |
| Debate and critique | claims and counterclaims | errors are exposable by critique | extra-token and single-agent critique controls | persuasive wrong consensus |
| Tool/domain specialization | tools, evidence, action spaces | task naturally partitions by capability | tool ablations and routing traces | orchestrator loses global state |
| Branch-and-merge | artifact branches | outputs can be isolated and tested | diff/test/provenance/merge evidence | integration bottleneck |
| Shared memory/delegation | persistent state | long-horizon context matters | memory provenance, repair, deletion, degradation metrics | stale or poisoned state |
| Human-governed portfolios | judgment and accountability | human taste/review is scarce but decisive | review-time and integration metrics | human bottleneck |
| Coordination optimization/training | topology, routing, prompts, policies, or agent weights | fixed prompting under-coordinates | held-out tasks, cost controls, transfer tests, agent-behavior diagnostics | overfitting, reward hacking, brittle controllers |

The last row is currently the most underdeveloped in the manuscript.

### 2. Promote Coordination Optimization/Training From Future Direction To Historical Turn

The draft's current future section lists GPTSwarm, DyLAN, MaAS, OMAC, AgentNet, MAS-GPT, ACC-Collab, MAPoRL, and evolving orchestration together. That is too compressed. These papers represent a major structural transition:

```text
roles are hand-written -> workflows are programmable -> mechanisms are measured -> coordination is optimized or trained
```

Recommended section title:

```text
## From Designed Teams to Optimized Coordination
```

This can either be a standalone section after `Mechanisms of Multi-Agent Value` or the first half of a later `Orchestration as a Control Problem` section. I prefer standalone, because it directly answers the missing "how do agents get better at coordination?" question.

Organize it into four lanes:

| Lane | Representative evidence | What it optimizes |
|---|---|---|
| Topology and communication optimization | GPTSwarm, DyLAN, G-Designer, AgentDropout/pruning work if used | communication edges, team size, agent selection |
| Architecture/workflow search | MaAS, OMAC, evolving orchestration, ADAS/AFlow if included as adjacent workflow-search context | operators, depth, routing, early exit, cost-performance |
| MAS generation | MAS-GPT, Multi-Agent Design | query-conditioned system construction |
| Agent collaboration training | ACC-Collab, MAPoRL, MALT if added, post-training-data simulation | critic behavior, revision, influence, collaborative policy |

The key claim should be cautious:

> Current evidence suggests that coordination can be optimized, but the evidence is still narrower than the artifacts/verification story: many results are on QA, math, coding-function, or synthetic collaboration settings, with limited proof of transfer to long-horizon tool use, scientific work, or cooperative software engineering.

This section should not become a citation stack. Its job is to define the research program and its evidentiary standard.

### 3. Merge `Search Plus Verification` And `From Conversation to Artifacts`

The current draft says "artifacts are not a separate theme" at the end of `Search Plus Verification`, then immediately makes artifacts a separate peer-level section. That is structurally inconsistent.

Use one major section:

```text
## Verification and Artifacts
```

Suggested internal flow:

1. State the loop: search -> artifact -> verification -> prune/merge/refine.
2. Present verifier hierarchy from weak to strong.
3. Explain why artifacts are the medium that lets verification operate across agents.
4. Give software and science examples.
5. End with the durable claim: artifacts turn extra inference into inspectable progress.

Move the current help/hurt setting table either into `Mechanisms of Multi-Agent Value` or keep it here after converting it from "setting" to "artifact/verifier pair."

### 4. Merge Memory, Degradation, And Safety Into Shared-State Governance

The current `Memory, Shared State, and Degradation` and `Safety Is a Coordination Problem` sections are both strong, but they belong under a shared structural argument:

```text
## Governing Shared State
```

Memory, documents, code, tool outputs, messages, and safety-relevant logs are all state surfaces. They can help because they preserve work. They can hurt because they preserve contamination.

Suggested subsections:

- persistent memory as coordination state;
- degradation across handoffs;
- communication and artifact contamination;
- permissions, provenance, reversibility, and escalation.

This keeps safety in the main argument rather than making it look like a late applied topic.

### 5. Rebuild The Ending Around Orchestration Decisions

`Design Principles` and `Future Directions` overlap. Both say the mature field needs to decide when to use one agent, sampling, specialists, verification, human review, and stopping.

Merge them into:

```text
## Orchestration as a Control Problem
```

Start with a decision framework instead of a flat principle list:

| If the task looks like... | Prefer... | Demand evidence that... |
|---|---|---|
| compact, context-fit, weakly decomposable | one strong agent or best-of-N | multi-agent overhead beats equal-budget alternatives |
| many independent attempts with cheap checking | sampling/voting | errors are not highly correlated |
| evidence/tool partitioned | specialists plus routing | routing preserves global state |
| artifact can be isolated and tested | branch-and-merge | integration quality is measured |
| uncertain or high-impact | human-governed portfolio | human review bandwidth is allocated well |
| repeated workflow family | optimized/trained coordination | learned policy generalizes beyond training tasks |

Then turn the open questions into programs:

- task decomposability prediction;
- online diversity measurement;
- coordination optimization/training;
- artifact-native traces;
- shared-state governance;
- human review allocation;
- topology-scaled safety.

## Proposed Table Of Contents

This is my preferred architecture after reading the current draft and the round-1 plan:

```text
Key Messages
1. Introduction and Scope
2. Coordination Was Hard Before LLMs
3. The 2023 Organization Bet
4. From Prompts to Runtimes
5. The Evaluation Turn
6. The Coordination Reality Check
7. Mechanisms of Multi-Agent Value
8. From Designed Teams to Optimized Coordination
9. Verification and Artifacts
10. Governing Shared State
11. Orchestration as a Control Problem
12. Conclusion
```

This is one section longer than the round-1 plan, but it fixes the training/optimization gap without burying the issue. If length becomes a problem, combine sections 7 and 8 under:

```text
## Mechanisms and Optimization of Multi-Agent Value
```

I do not recommend burying coordination training only under future directions.

## Section-Level Critique

### Introduction and Scope

The introduction has a strong thesis, but `Introduction` and `Scope and Terms` should be merged. The reader should not have to wait until section 2 for the operational definition.

Keep the sentence-level distinction between single-agent tool-use lineage and the multi-agent branch. That is a strength.

Add one sentence that previews the mechanism taxonomy:

> The review therefore asks which mechanism is being claimed: sampling, diversity, critique, specialization, shared state, artifact branching, human governance, or optimized coordination.

### Coordination Before LLMs

This is structurally sound. Its main job is not to survey MARL, but to inoculate the reader against naive multi-agent optimism. It should end exactly where the current draft ends: coordination is a design achievement.

One sharpening: the section should explicitly distinguish **training-time coordination** in MARL from **test-time coordination** in LLM agents. That contrast sets up why coordination training reappears later.

### The 2023 Organization Bet

This section works. It is fair to the early systems without swallowing their causal story.

Potential issue: AutoGen is currently split between this section and `From Prompts to Runtimes`. That is acceptable only if the first mention treats it as historically part of the 2023 wave and the second treats it as runtime substrate. Make that boundary explicit.

### From Prompts to Runtimes

Keep this section, but do not let it become a framework catalogue. Its best current paragraph is the runtime-substrate paragraph: tools, sandboxes, event streams, file systems, queues, state stores, validators, ledgers, retry logic, permissions, and benchmark harnesses.

This section should end by saying:

> Once agents became runtime components, the field could optimize the program around the model, not only the prompt inside the model.

That sentence sets up coordination optimization.

### The Evaluation Turn

This section is necessary and mostly well-shaped. Its distinction from the reality-check section should be:

- `Evaluation Turn`: what became measurable.
- `Coordination Reality Check`: what those measurements revealed about multi-agent claims.

Avoid adding more benchmark names here. The current benchmark list is already near the limit.

### The Coordination Reality Check

This is one of the strongest sections. It gives the negative evidence needed for the review's credibility.

But it currently carries some material that belongs later:

- DELEGATE-52 and SlopCodeBench can be previewed here, but the deeper discussion belongs in `Governing Shared State`.
- Evidence standards can stay here as Box 1 because this is where the reader learns how to be skeptical.

The section should end with the precise problem that the next sections solve:

> The field therefore needs to identify the mechanism by which extra agents create value, and the verification process that prevents that extra computation from becoming overhead or contamination.

### Mechanisms of Multi-Agent Value

This should be added. Without it, the manuscript gives readers principles but not a reusable classification system.

The mechanism taxonomy is the difference between a good narrative review and a field-shaping review. It should be compact, table-first, and repeatedly referenced later.

### From Designed Teams to Optimized Coordination

This should be added or promoted out of `Future Directions`.

The missing "training agents for multi-agent coordination" issue belongs here. It should be framed as a response to the 2023 failure mode:

> If role prompts do not reliably create specialization, the field can either engineer coordination externally through artifacts and runtimes, or train/optimize the coordination policy itself.

Use MAPoRL and ACC-Collab as the cleanest "train the agents to collaborate" examples. Use GPTSwarm, MaAS, OMAC, MAS-GPT, AgentNet, DyLAN, and evolving orchestration as "optimize the system that coordinates them" examples.

Keep the caveat prominent: most coordination-training evidence is not yet as mature as the benchmark/failure/artifact evidence.

### Verification and Artifacts

This should absorb `Search Plus Verification` and `From Conversation to Artifacts`.

The section should not merely say "artifacts are better than chat." The stronger claim is:

> Artifacts are the selection surface for multi-agent search.

That makes the section central rather than applied.

### Governing Shared State

This should absorb memory, degradation, and safety.

The structural claim:

> Shared state is where coordination becomes durable and where errors become transmissible.

This gives a natural home to MemGPT, A-Mem, MemMA, DELEGATE-52, SlopCodeBench, SafeArena, OpenAgentSafety, G-Safeguard, and zero-day-agent evidence.

### Orchestration as a Control Problem

This section should replace `Design Principles` plus most of `Future Directions`.

The existing decision question is excellent. Make the whole section serve that question.

Avoid ending with too many disconnected questions. Group them by control variable:

- task fit;
- search allocation;
- diversity;
- verification;
- shared state;
- human review;
- safety;
- training and optimization.

### Conclusion

The current conclusion is strong and should stay short. It should not introduce optimized coordination if that topic is not already treated earlier.

## What Is Logically Missing

### Missing 1: Coordination Training And Post-Training

The manuscript should explicitly ask:

> Can agents be trained to coordinate, rather than only prompted or orchestrated to coordinate?

Evidence already available locally:

- MAPoRL: multi-agent PPO for collaborative debate, including influence-aware rewards and wrong-to-right revision behavior.
- ACC-Collab: actor-critic DPO training for collaborative answer revision and critic feedback.
- MAS-GPT: supervised training to generate executable MAS designs from queries.
- MALT: candidate/local snowball item for multi-agent LLM training, likely worth triage.
- Synthesizing post-training data through multi-agent simulation: candidate item, likely relevant as a data-generation bridge.
- Memory-R1 and SWERL/SWE-Fixer are adjacent examples of agent post-training, useful only if the section broadens beyond multi-agent coordination.

This should be treated as emerging evidence, not a settled solution.

### Missing 2: Distinction Between System Optimization And Model Training

The current draft blends learned/search-based orchestration papers. The review should distinguish:

- prompt/topology optimization around frozen models;
- controller/policy learning;
- data generation for MAS construction;
- fine-tuning agents for collaborative behavior.

This distinction will prevent the review from using "learned orchestration" too vaguely.

### Missing 3: Credit Assignment In LLM-Agent Teams

The pre-LLM section introduces credit assignment, but the modern sections do not fully cash it out.

Questions to cover:

- Which agent, message, retrieval, test, or edit caused improvement?
- How do systems assign reward to intermediate critics, routers, or branch workers?
- How do evaluation traces support attribution?

MAPoRL, ACC-Collab, GPTSwarm, MaAS, OMAC, and AgentNet all touch this indirectly. This is also a good bridge back to MARL.

### Missing 4: Communication Protocol Design

The draft critiques free-form chat and promotes artifacts, but it could more explicitly discuss structured communication:

- typed messages;
- commitments and contracts;
- state transition schemas;
- handoff protocols;
- communication pruning;
- topology-aware filtering.

This can sit inside `From Prompts to Runtimes`, `Mechanisms`, or `Governing Shared State`.

### Missing 5: Negative Transfer And Distribution Shift For Learned Coordination

If the review adds coordination training, it should also demand evidence of transfer. Learned collaboration policies can overfit to benchmark formats, verifiers, role sets, tool pools, or task families.

Evidence standards:

- held-out task families;
- changed agent pool or model backbone;
- cost and latency reporting;
- transfer from QA/math to tool-use or artifact tasks;
- stress tests under weak verifiers;
- analysis of reward hacking and collusive agreement.

### Missing 6: Human Organizations As A Baseline, Not Just A Metaphor

The draft has a good human-in-the-loop thread, but it can be made more structural:

> Human teams plus agents are the near-term strong baseline for multi-agent scaling.

This prevents the review from implicitly comparing autonomous agent teams only against single agents. For many real workflows, the realistic alternative is human-orchestrated portfolios of agent attempts.

## Risks In The Existing Round-1 Plan

The round-1 plan is directionally right. My main disagreement is that it hides optimized/trained coordination inside `Orchestration as a Control Problem`. That makes the missing training question too easy to underwrite.

Specific risks:

- A 10-section target may force too much compression in the part of the field that is most clearly emerging in 2025-2026.
- Merging `Design Principles` and `Future Directions` is right, but only after promoting coordination optimization/training earlier.
- The mechanism taxonomy should include optimized/trained coordination as a first-class mechanism, not only a future direction.
- `Verification and Artifacts` should not have to carry the entire positive theory. The positive theory has two pillars: artifact-centered verification and optimized coordination.

## Recommended Next Rewrite Order

1. Merge `Introduction` and `Scope and Terms`.
2. Add `Mechanisms of Multi-Agent Value` after `The Coordination Reality Check`.
3. Add or promote `From Designed Teams to Optimized Coordination`.
4. Merge `Search Plus Verification` and `From Conversation to Artifacts`.
5. Merge memory, degradation, and safety into `Governing Shared State`.
6. Merge principles and future directions into `Orchestration as a Control Problem`.
7. Recheck that every section ending carries one concept forward.

## Acceptance Criteria For The Next Draft

- The table of contents lets a reader distinguish chronology, mechanisms, verification, governance, and orchestration.
- The review has one reusable mechanism taxonomy.
- Coordination optimization/training is explicit and not buried in future directions.
- Artifact-centered verification remains the main synthesis, but not the only positive response to the skeptical evidence.
- Safety and memory appear as shared-state governance, not side topics.
- Every major section answers: what changed, why it mattered, what evidence supports it, and what concept survives.
