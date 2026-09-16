# Round 1 Structure Improvement Plan

## Goal

Improve the manuscript architecture of `manuscript/multi-agent-review-draft/index.qmd` so the review reads like a field-shaping synthesis rather than a sequence of short topic essays.

The current thesis is strong: modern LLM-driven multi-agent systems are best understood as structured test-time computation over separately stateful attempts, durable artifacts, and verification. The structural task is to make every major section serve that thesis more cleanly.

## Diagnosis

The manuscript currently has the right material but too many peer-level sections. Several sections are narrative beats that should either be merged or made subordinate to a larger argument.

Main problems:

- `Introduction` and `Scope and Terms` are both opening contract material and should be combined.
- `The 2023 Bet: Simulated Organizations` and `From Prompts to Runtimes` describe one historical transition and need a clearer boundary or a merge.
- `The Evaluation Turn` and `The Coordination Reality Check` are both central, but their distinction should be sharpened: evaluation made failures measurable; the reality check explains what those measurements overturned.
- `Search Plus Verification` and `From Conversation to Artifacts` overlap; artifacts are the operational form of search plus verification.
- `Memory, Shared State, and Degradation` and `Safety Is a Coordination Problem` are under-integrated; both should be organized around one claim: shared state is where reliability and safety failures propagate.
- The manuscript lacks an explicit mechanism taxonomy that lets readers classify new work by how multi-agent value is supposed to arise.
- The manuscript mentions learned or searched orchestration only in future directions, but this is now a major structural turn: after naive role prompting proved unreliable, the field began optimizing and training coordination itself. The review should distinguish system-level optimization from agent-level collaboration training.

## Target Structure

Use this as the preferred 11-section architecture, plus a short conclusion.

1. **Introduction and Scope**
   - Merge the existing introduction and scope contract.
   - Define the reviewed object operationally: separately stateful LLM-backed, tool-backed, or human-backed attempts whose outputs must be routed, checked, selected, or merged.
   - State the review's central claim early: agent count is not the unit of progress; verified progress per cost, risk, and review bandwidth is.

2. **Coordination Was Hard Before LLMs**
   - Preserve the conceptual bridge to MAS and MARL.
   - Emphasize partial observability, credit assignment, communication bandwidth, non-stationarity, and decentralized execution.
   - End with an explicit mapping to LLM systems: context partitioning, lossy summaries, shared memory, merge policy, and verification.

3. **The 2023 Organization Bet**
   - Cover CAMEL, Generative Agents, ChatDev, MetaGPT, debate, AutoGen, AgentVerse, and AutoAgents as the moment when role decomposition became vivid.
   - Keep the section fair: the organization metaphor was productive because it exposed roles, topology, memory, tools, and turn-taking.
   - Make the limitation precise: many gains confounded collaboration with extra inference, role prompts, selection, judging, or sampling.

4. **From Prompts to Runtimes**
   - Keep only if it becomes a real systems section, not a short framework catalogue.
   - Focus on runtime substrate: tools, sandboxes, event streams, ledgers, file systems, memory stores, validators, permission boundaries, and benchmark harnesses.
   - Explain why this transition makes orchestration an engineering object.

5. **The Evaluation Turn**
   - Organize by what became measurable: browser state, GUI state, code patches, API state, workplace workflows, repeated trials, and partial progress.
   - Use historical benchmark numbers as turning-point evidence, not as current capability claims.
   - End by explaining why multi-agent claims now need stronger controls.

6. **The Coordination Reality Check**
   - Make this the skeptical evidence section.
   - Cover cost controls, equal-budget single-agent baselines, failure taxonomies, communication overhead, cooperative coding failures, and degradation studies.
   - Distill the lesson: coordination has a cost and only pays off when decomposition, diversity, and verification create value greater than that cost.

7. **Mechanisms of Multi-Agent Value**
   - Add this as a new central synthesis section.
   - Classify mechanisms:
     - independent sampling and voting;
     - heterogeneous model or prompt diversity;
     - debate and critique;
     - tool or domain specialization;
     - branch-and-merge artifact work;
     - shared memory and stateful delegation;
     - human-governed portfolios of attempts;
     - optimized or trained coordination.
   - For each mechanism, state the necessary task condition, the expected benefit, and the dominant failure mode.

8. **From Designed Teams to Optimized Coordination**
   - Add this as the answer to the missing "how do agents get better at coordination?" question.
   - Explain the historical transition: hand-written roles -> programmable workflows -> measured mechanisms -> optimized or trained coordination.
   - Separate four lanes:
     - topology and communication optimization around mostly fixed models;
     - architecture/workflow search and controller policies;
     - query-conditioned MAS generation;
     - agent-level collaboration training and post-training.
   - Use GPTSwarm, DyLAN, MaAS, OMAC, AgentNet, MAS-GPT, ACC-Collab, MAPoRL, and evolving orchestration as the core evidence already available in the local corpus.
   - Keep the evidentiary caveat visible: most collaboration-training evidence is narrower than the artifact/verification evidence and still needs transfer, cost, reward-hacking, and long-horizon tool-use tests.

9. **Verification and Artifacts**
   - Merge most of `Search Plus Verification` and `From Conversation to Artifacts`.
   - Make artifacts the causal hinge: they make partial work inspectable, replayable, comparable, mergeable, and rejectable.
   - Include a verifier hierarchy from weak conversational consensus to tests, execution, provenance, replication, and human expert review.

10. **Governing Shared State**
   - Merge memory, degradation, and safety under one organizing claim: multi-agent systems become risky when messages, memories, artifacts, and tool outputs are treated as trusted shared state without provenance or validation.
   - Frame shared state as both capability and contamination surface.
   - Cover memory provenance, deletion and repair, long-horizon degradation, tool permissions, safety topology, logs, and escalation.
   - Mention human review here only as a governance mechanism for uncertain, irreversible, high-impact, or safety-sensitive state changes; put review-allocation strategy in the orchestration section.

11. **Orchestration as a Control Problem**
    - Combine practical principles and future directions around one claim: the mature field should decide when to reason serially, sample, delegate, specialize, verify, merge, escalate, or stop.
    - Start with a decision framework: when to use one strong agent, best-of-N, a fixed workflow, specialist agents, branch-and-merge, optimized/trained coordination, or human escalation.
    - End with open research programs that follow from the control framing: task decomposability prediction, online diversity measurement, coordination optimization/training, artifact-native trace formats, state governance, safety controls, and human review allocation.

12. **Conclusion**
    - Keep short.
    - Restate the historical arc and the final conceptual unit: verified progress, not number of agents.

## Rewrite Steps

### Step 1: Restructure Headings

- Merge `Introduction` and `Scope and Terms` into `Introduction and Scope`.
- Decide whether `From Prompts to Runtimes` has enough systems substance to remain separate.
- Add `Mechanisms of Multi-Agent Value` after `The Coordination Reality Check`.
- Add `From Designed Teams to Optimized Coordination` after the mechanism section.
- Merge `Search Plus Verification` and `From Conversation to Artifacts` into `Verification and Artifacts`.
- Merge `Memory, Shared State, and Degradation` and `Safety Is a Coordination Problem` into `Governing Shared State`.
- Merge `Design Principles` and `Future Directions` into `Orchestration as a Control Problem`.

### Step 2: Move Existing Material

- Move the definition of multi-agent LLM systems into the first section.
- Move the help/hurt table from `Search Plus Verification` into the new mechanism or verification section.
- Move CAID, Agentless, software artifacts, scientific artifacts, and PaperBench discussion into `Verification and Artifacts`.
- Move MemGPT, A-Mem, MemMA, DELEGATE-52, SlopCodeBench, SafeArena, OpenAgentSafety, and G-Safeguard into `Governing Shared State`.
- Move human review allocation into `Orchestration as a Control Problem`, while keeping human escalation as a governance mechanism in `Governing Shared State`.
- Move GPTSwarm, DyLAN, MaAS, OMAC, AgentNet, MAS-GPT, ACC-Collab, MAPoRL, and evolving-orchestration work into `From Designed Teams to Optimized Coordination`.
- Move diversity-scaling work into `Mechanisms of Multi-Agent Value` or `Orchestration as a Control Problem`, depending on whether the paragraph is classifying diversity as a mechanism or using it as a design variable.

### Step 3: Add the Mechanism Taxonomy

Create a compact table with columns like:

| Mechanism | When it helps | Evidence to demand | Failure mode |
|---|---|---|---|
| Sampling/voting | Cheap independent attempts with compact verifier | Budget-matched best-of-N controls | Correlated wrong answers |
| Debate/critique | Errors can be exposed by adversarial review | Single-agent critique and extra-token controls | Persuasive wrong consensus |
| Tool specialization | Evidence or actions are naturally partitioned | Tool-ablation and routing evidence | Orchestrator loses state |
| Branch-and-merge | Artifacts can be isolated and tested | Diff/test/provenance evidence | Merge quality bottleneck |
| Shared memory | Long-horizon context must persist | Provenance, repair, deletion, degradation metrics | Stale or poisoned state |
| Human-governed portfolios | Human judgment is scarce but decisive | Review-time and integration metrics | Human bandwidth bottleneck |
| Optimized/trained coordination | Fixed prompting under-coordinates | Held-out tasks, cost controls, transfer tests, behavior diagnostics | Overfitting, reward hacking, brittle routing |

### Step 4: Tighten Section Endings

Each major section should end with the concept the reader should carry forward.

Examples:

- Pre-LLM section: coordination is a design achievement, not a byproduct of multiplicity.
- 2023 section: role decomposition made orchestration visible but did not prove collaboration.
- Evaluation section: executable environments changed the standard of evidence.
- Reality-check section: more agents help only when added search survives cost, aggregation, and verification.
- Mechanism section: multi-agent value must be attributed to a specific mechanism, not to agent count.
- Optimized-coordination section: if coordination does not emerge reliably from role prompts, it must be optimized externally or trained into the interacting agents.
- Verification/artifacts section: durable artifacts are the medium through which search becomes inspectable progress.
- Governance section: shared state is both memory and attack surface.

## Acceptance Criteria

The revised manuscript should satisfy these checks:

- The table of contents has about 11 major sections, not 14 short peer sections.
- Every section title states an argument or turning point, not merely a topic.
- The manuscript contains one explicit mechanism taxonomy.
- Coordination optimization/training is treated as a first-class historical turn, not only as a future direction.
- The distinction among evaluation, skepticism, mechanisms, and design principles is clear.
- Artifact-centered verification is presented as the synthesis, not as a side theme.
- Safety and memory are integrated into the core coordination story.
- The conclusion introduces no new evidence.
- A technically literate reader can summarize the review in one sentence: multi-agent LLM systems are useful when they turn extra test-time computation into verified, inspectable progress over artifacts.

## Files To Edit

- `manuscript/multi-agent-review-draft/index.qmd`
- `manuscript/multi-agent-review-draft/section-review-evidence.md`, only if the evidence log should track the restructuring rationale
- `manuscript/multi-agent-review-draft/references.bib`, only if new citations are added during restructuring

## Non-Goals

- Do not expand the review into a catalogue of all 700 extra papers.
- Do not add new primary-paper claims unless they strengthen a structural transition.
- Do not let future directions become a citation stack.
- Do not preserve current headings just because the material already exists.
