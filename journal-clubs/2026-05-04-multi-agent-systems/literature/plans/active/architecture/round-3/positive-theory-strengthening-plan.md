# Round 3 Positive Theory Strengthening Plan

Date: 2026-05-07

Target: `manuscript/multi-agent-review-draft/index.qmd`

## Goal

Strengthen the manuscript's positive theory of when LLM-driven multi-agent
systems help. Rounds 1 and 2 gave the review a strong architecture and a
credible skeptical center. Round 3 should make the constructive thesis equally
memorable:

```text
Multi-agent systems help when they convert extra test-time computation into
verified, inspectable progress through non-redundant search, durable artifacts,
governed state, and adaptive orchestration.
```

The current draft already says this. The task is to make the positive case more
visible, more evidence-backed, and easier for readers to reuse.

## Diagnosis

The manuscript is strongest when it explains why naive multi-agent claims fail:
coordination costs, equal-budget controls, weak verification, lossy messages,
shared-state contamination, and long-horizon degradation. That skeptical case is
necessary and persuasive.

The positive theory is present but less developed. CAID, MemMA, AgentRxiv,
AI co-scientist, Magentic-One, optimized orchestration work, and human-governed
portfolios appear as examples, but they do not yet form an equally strong
constructive arc.

Main problems:

- The review has a clear negative standard, but the positive theory is spread
  across `Mechanisms of Multi-Agent Value`, `Verification and Artifacts`,
  `Governing Shared State`, and `Orchestration as a Control Problem`.
- Strong positive examples are too brief. They support the thesis, but they do
  not yet function as canonical case studies.
- The manuscript lacks a compact claim/evidence ledger that separates robust
  positive claims from promising but unsettled claims.
- The artifact-centered theory is strong, but the reader could use a sharper
  model of the full positive loop: spawn, isolate, diversify, verify, merge,
  remember, escalate, and stop.
- The conclusion emphasizes verified progress, but it should more directly tell
  readers what a mature multi-agent system should look like.

## Round 3 Target Contribution

After Round 3, the review should answer three constructive questions as clearly
as it answers the skeptical ones:

1. **What is the durable positive theory?**
   Multi-agent systems are useful when separately stateful attempts create
   non-redundant evidence or artifact branches that can be verified and merged.

2. **What are the strongest current positive patterns?**
   Branch-and-merge software work, governed memory cycles, artifact-centered
   scientific workflows, human-governed portfolios, and optimized coordination.

3. **What evidence would make a positive claim convincing?**
   Budget-matched baselines, diversity or routing ablations, artifact-level
   verification, provenance, repeated-run reliability, cost and latency, and
   long-horizon degradation checks.

## Proposed Additions

### 1. Add A Claim/Evidence Ledger

Add a compact table near the end of `Introduction and Scope`, or immediately
after `Mechanisms of Multi-Agent Value`.

Preferred location: after the mechanism taxonomy, because the reader has then
seen the classification system.

Suggested table:

| Positive claim | Strongest evidence | Evidence type | Caveat |
|---|---|---|---|
| Multi-agent value comes from non-redundant search, not raw agent count | AgentScalingDiversity, More Agents, Mixture-of-Agents, Science of Scaling | scaling analyses and ablations | diversity must create correct-path evidence, not just varied wrong answers |
| Branch-and-merge can improve software-agent work | CAID, SWE-bench/Agentless context, CooperBench as negative control | artifact and benchmark evidence | merge quality and task modularity remain bottlenecks |
| Shared memory helps only when governed | MemMA, A-Mem, MemGPT | memory benchmark evidence | memory can preserve stale or poisoned state |
| Scientific-agent workflows need artifact chains | PaperBench, Curie, Agent Laboratory, AI co-scientist, AgentRxiv | benchmark and system evidence | expert review, replication, and statistical validity remain weak points |
| Human-governed portfolios are a plausible near-term scaling pattern | AI co-scientist, Agent Laboratory, CAID-style delegation, co-pilot practice | system and workflow evidence | human review bandwidth becomes the limiting resource |
| Coordination can be optimized or trained | GPTSwarm, DyLAN, MaAS, OMAC, AgentNet, MAS-GPT, ACC-Collab, MAPoRL | architecture search and training evidence | transfer, reward hacking, cost, and long-horizon tool use remain under-tested |

Keep this table short. It should expose evidence quality, not become another
paper catalogue.

### 2. Build Three Positive Case Studies

Convert the strongest positive examples into short, named case studies. Each
case study should follow the same pattern:

```text
problem -> multi-agent mechanism -> verifier/artifact -> result -> caveat
```

Recommended case studies:

#### Case Study A: Branch-And-Merge Software Work

Core evidence:

- CAID as the positive example.
- Agentless and SWE-bench as artifact-verification context.
- CooperBench as the warning that communication alone does not solve joint
  coding.
- SlopCodeBench as the long-horizon quality constraint.

Core claim:

> Software-agent teams work best when agents do not merely chat. They isolate
> attempts, produce diffs and tests, and merge only through evidence.

Manuscript location:

- `Verification and Artifacts`.

#### Case Study B: Governed Memory And Shared State

Core evidence:

- MemMA as the strongest multi-agent memory-cycle example.
- A-Mem and MemGPT as adjacent memory-management lineage.
- DELEGATE-52 and safety work as contamination/degradation warnings.

Core claim:

> Shared memory is valuable when it is constructed, retrieved, diagnosed,
> repaired, scoped, and deleted under explicit rules.

Manuscript location:

- `Governing Shared State`.

#### Case Study C: Human-Governed Research Portfolios

Core evidence:

- AI co-scientist, Agent Laboratory, Curie, PaperBench, AgentRxiv.
- Optional contrast with AI Scientist and AI Scientists Produce Results
  Without Reasoning Scientifically.

Core claim:

> Near-term scientific multi-agent systems are most credible as human-governed
> portfolios of hypotheses, experiments, code, reviews, and replication traces,
> not as fully autonomous scientist societies.

Manuscript location:

- Split between `Verification and Artifacts` and `Orchestration as a Control
  Problem`.

### 3. Add A Positive Loop Figure Or Box

If the existing `test-time-computation-loop.svg` is sufficient, add a short box
that names the loop's positive design stages. If a new figure is needed, create
only after the prose stabilizes.

Suggested box:

```text
Box | The positive multi-agent loop

1. Estimate task fit and decomposability.
2. Spawn separately stateful attempts only where non-redundant search is likely.
3. Isolate work in branches, memories, logs, or typed state.
4. Force agents to produce verifiable artifacts.
5. Apply local validators before errors propagate.
6. Select, merge, or reject through evidence, not conversational confidence.
7. Update shared state with provenance and repair rules.
8. Escalate uncertainty, irreversible actions, and high-impact decisions.
9. Stop when marginal verified progress no longer justifies cost and risk.
```

This should appear in `Orchestration as a Control Problem`, near the decision
table. It gives practitioners a constructive alternative to "use more agents."

### 4. Strengthen Section Endings Around Positive Concepts

Revise section endings so each constructive section hands the reader a reusable
concept:

- `Mechanisms of Multi-Agent Value`: extra agents help only through an
  identifiable mechanism under task conditions that make the mechanism useful.
- `Verification and Artifacts`: artifacts are the selection surface that turns
  search into inspectable progress.
- `Governing Shared State`: state is useful only when provenance, scope,
  validation, repair, and deletion are first-class.
- `From Designed Teams to Optimized Coordination`: coordination is becoming an
  object of search and training, but the evidence standard must include
  transfer, cost, and long-horizon artifacts.
- `Orchestration as a Control Problem`: the mature system allocates reasoning,
  sampling, delegation, verification, memory, human review, and stopping under
  cost and risk.

### 5. Make The Conclusion More Constructive

Keep the current conclusion's skeptical balance, but add one concrete paragraph
answering:

> What should a mature multi-agent system look like?

Suggested content:

```text
A mature system will look less like a room of chatbots and more like an
allocation engine for cognitive work: it predicts decomposability, spawns
isolated attempts, routes tools and evidence, verifies local artifacts, records
provenance, governs shared memory, asks humans at high-value decision points,
and stops when additional coordination no longer buys verified progress.
```

Do not add new citations in the conclusion.

## Rewrite Steps

### Step 1: Mark Positive Claims

In `index.qmd`, identify every paragraph that makes a constructive claim about
when multi-agent systems help. Tag mentally by mechanism:

- diversity/search;
- critique/debate;
- tool specialization;
- branch-and-merge;
- memory/shared state;
- human-governed portfolios;
- optimized coordination.

Remove or rewrite any positive claim that cannot name its mechanism and
evidence type.

### Step 2: Insert The Claim/Evidence Ledger

Add the positive-claim ledger after `Mechanisms of Multi-Agent Value`, unless it
interrupts flow. If it does, add it as a boxed note in `Orchestration as a
Control Problem`.

The ledger should be selective: 6-8 rows maximum.

### Step 3: Expand The Three Case Studies

Add 1-2 focused paragraphs each for:

- branch-and-merge software work;
- governed memory/shared state;
- human-governed scientific/research portfolios.

Each paragraph should include mechanism, artifact/verifier, result, and caveat.

### Step 4: Add The Positive Loop Box

Place the loop in `Orchestration as a Control Problem`, after the decision
question and before the practical principles or decision table.

Keep the box design-oriented, not aspirational.

### Step 5: Tighten Negative-to-Positive Transitions

Add explicit bridges:

- after `The Coordination Reality Check`: skepticism creates the need for a
  mechanism-level positive theory;
- after `Mechanisms of Multi-Agent Value`: mechanisms need artifacts and
  verifiers;
- after `Governing Shared State`: state governance is what lets useful work
  persist without making errors persistent too;
- before `Orchestration as a Control Problem`: the final design problem is
  allocation.

### Step 6: Rebalance The Ending

Revise the conclusion so it does not only say "verified progress matters." It
should also summarize the positive architecture:

```text
non-redundant search -> verifiable artifacts -> governed state -> adaptive
allocation -> human escalation where needed
```

## Acceptance Criteria

- The manuscript contains a visible positive claim/evidence ledger.
- At least three positive examples function as case studies rather than brief
  mentions.
- The positive loop is explicit and reusable.
- Every positive claim names a mechanism, a verifier or artifact, and a caveat.
- The skeptical evidence remains intact and is not softened.
- The final third tells readers what to build or demand in new systems.
- The conclusion describes a mature multi-agent architecture, not only a
  critique of immature ones.
- No new paper is added unless it strengthens a positive mechanism or case
  study.

## Files To Edit

- `manuscript/multi-agent-review-draft/index.qmd`
- `manuscript/multi-agent-review-draft/section-review-evidence.md`, if the
  evidence log should track the new positive-theory changes
- `manuscript/multi-agent-review-draft/references.bib`, only if new citations
  are introduced

## Non-Goals

- Do not weaken the skeptical sections to make the positive story feel cleaner.
- Do not add a broad "applications" section.
- Do not turn scientific agents, coding agents, or memory agents into domain
  surveys. Use them only as evidence for mechanisms.
- Do not add new figures until the prose-level positive theory is stable.
- Do not let the positive loop become generic product advice; keep it tied to
  the manuscript's evidence standard.
