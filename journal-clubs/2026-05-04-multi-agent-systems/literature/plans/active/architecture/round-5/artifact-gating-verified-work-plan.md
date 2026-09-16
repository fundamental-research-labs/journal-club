# Round 5 Artifact Gating Plan

Date: 2026-05-08

Target: `manuscript/multi-agent-review-draft/sections/verified-work.qmd`

Primary focus: current section `Only Verified Work Becomes Progress`

## Goal

Sharpen the section so it explains why artifact gating is important for agents
in general, but becomes a first-order coordination problem in multi-agent
systems.

The current section correctly argues that unverified outputs do not become
reliable progress. The weakness is that this argument also applies to a strong
single-agent loop. Round 5 should make the multi-agent-specific claim explicit:

```text
Verification matters for any agentic system because agents can build on their
own untrusted outputs. It matters especially for multi-agent systems because
parallel workers can produce more artifacts than any single manager, agent, or
human can deeply integrate, and because ungated artifacts can contaminate other
agents' state. The multi-agent problem is not just verification; it is deciding
which artifacts may cross from private attempt to shared progress.
```

## Diagnosis

The current section has strong evidence and examples:

- verifier hierarchy from conversational consensus to executable validators;
- Agentless as evidence that artifact-centered validation can strengthen even
  non-agentic or single-agent baselines;
- CAID as a positive branch-and-merge software example;
- scientific-agent workflows as artifact chains requiring replication,
  provenance, and expert review;
- human-governed portfolios as a near-term scaling pattern.

Main problems:

- The opening frames verified accumulation as if it were uniquely
  multi-agent, but single-agent systems also need gated plans, patches,
  memories, claims, and tool results.
- The section does not yet name the multi-agent-specific scaling problem:
  artifact volume can grow with agent count, branch count, tool calls, memory
  updates, review comments, and candidate outputs.
- The section underplays integration bandwidth. A multi-agent system can
  generate more candidate artifacts than one coordinator, model context, or
  human reviewer can inspect.
- The section treats verification and artifacts as the main concepts, but the
  sharper concept is artifact gating: what is allowed to enter shared state,
  what remains isolated, what is pruned, what is ranked, and what is merged.
- The handoff boundary should be more central. In multi-agent systems, every
  message, patch, memory entry, plan, or experiment report can become another
  worker's starting point.

## New Section Thesis

Replace the implicit thesis:

```text
Multi-agent systems need verified artifacts so divided labor can accumulate.
```

with:

```text
All agents need artifact gates, but multi-agent systems need them more because
they multiply both artifact production and artifact propagation. A single agent
can be limited by one serial context-integration path. A multi-agent system can
produce candidate patches, tests, plans, memories, logs, hypotheses, and
reviews across many branches at once. Without gates, this parallelism overwhelms
integration bandwidth and spreads unverified state. The gate is the boundary
between private attempt and shared progress.
```

## Proposed Section Arc

### 1. Start With The General Agent Principle

Open by acknowledging that gating is not unique to multi-agent systems.

Core claim:

```text
Any agentic system needs gates because agents create intermediate artifacts
that can later be mistaken for facts: plans, summaries, tests, patches,
memories, retrieved evidence, and tool outputs. A single agent can build on its
own unverified work, so validators, tests, retrieval checks, and human review
matter even before multiple agents enter the picture.
```

This prevents overclaiming and makes the review sound more rigorous.

### 2. Then State The Multi-Agent Amplification

Move immediately to what changes when there are multiple separately stateful
workers.

Core claim:

```text
Multi-agent systems amplify the gating problem in two ways. First, artifact
volume can grow with the number of agents, branches, tool calls, memory
updates, and candidate outputs. Second, artifacts propagate: one worker's
summary, patch, memory entry, or experiment report can become another worker's
starting state. The risk is therefore not only wrong local work, but wrong work
entering shared state and shaping many later decisions.
```

This should be the section's distinctive contribution.

### 3. Define Artifact Gates

Introduce "artifact gate" as a reusable concept.

Suggested definition:

```text
An artifact gate is any mechanism that controls whether an intermediate work
product may move from a private attempt into shared state, downstream context,
or final output. Gates include tests, validators, parsers, retrieval checks,
static analysis, review rubrics, provenance checks, merge reviews, memory
repair rules, permission checks, and human escalation.
```

The gate should decide:

- what remains isolated;
- what is pruned;
- what is ranked for review;
- what is merged;
- what is written into memory;
- what is shown to other agents;
- what requires human escalation.

### 4. Reframe The Loop Around Gated Transfer

Replace or reinterpret the current generic loop:

```text
generate search -> create artifacts -> verify -> prune or merge -> refine
```

with a multi-agent-specific loop:

```text
spawn isolated attempts -> produce artifacts -> verify locally
-> rank, prune, or merge -> update shared state -> delegate or stop
```

Do not necessarily change the figure immediately. First adjust the prose so the
existing figure is read as a gated-transfer loop rather than a generic
agent-verification loop.

### 5. Make Integration Bandwidth Explicit

Add a paragraph explaining that multi-agent scaling creates an integration
bottleneck.

Core claim:

```text
The limiting resource is often not generation. It is integration: the context,
attention, tests, and human review needed to decide which artifacts deserve to
survive. Multi-agent systems can create more plausible candidate work than any
single manager or human can read. Gating is therefore also a compression and
selection mechanism.
```

This should connect to human-governed portfolios near the end of the section.

### 6. Reuse Existing Evidence With A Sharper Role

Keep most current examples, but assign each a clearer role in the gating
argument:

| Evidence | Role in revised section |
|---|---|
| Agentless | Shows that artifact gates help even without multiple agents; generated tests, regression tests, voting, and patch validation are strong single-agent/non-agentic baselines. |
| CooperBench | Shows that communication alone does not solve integration; agents can reduce merge conflicts without producing correct joint work. |
| CAID | Positive multi-agent example: isolated worktrees and branch-and-merge make artifacts cross boundaries only through commits, tests, and manager integration. |
| DELEGATE-52 | Shows repeated delegated artifact transformation can cause sparse but severe corruption. |
| SlopCodeBench | Shows local behavioral progress can hide long-horizon structural degradation. |
| MemMA | Shows shared memory needs construction, diagnosis, repair, and commit-like rules before memory becomes shared state. |
| AgentRxiv | Shows cumulative research artifacts need archive retrieval plus human/manual verification; parallel labs increase output and compute burden. |
| Scientific-agent systems | Show that hypotheses, code, logs, datasets, and reports require replication, statistical validity, provenance, and expert review. |

## Proposed Paragraph-Level Changes

### Opening Paragraph

Current function:

- says multi-agent systems scale by preserving verified products of labor.

Revision function:

- first acknowledge general agent gating;
- then state the multi-agent amplification.

Candidate direction:

```text
Gating artifacts is necessary for any agentic system. Agents create plans,
summaries, memories, tests, patches, tool results, and claims that can later be
mistaken for reliable state. A single agent can build on its own unverified
outputs; a multi-agent system can multiply the problem by producing many such
artifacts in parallel and passing them across workers. The central
multi-agent question is therefore not only whether an output is correct, but
whether it is allowed to cross from private attempt into shared progress.
```

### Accumulation Paragraph

Current function:

- names the accumulation problem.

Revision function:

- tie accumulation to artifact explosion and integration bandwidth.

Candidate direction:

```text
This is the accumulation problem. A single agent is constrained by one serial
context-integration path. A multi-agent system can create artifacts that scale
with agents, branches, tool calls, memories, and candidate outputs. Without
gates, the system creates more state than one manager, model context, or human
reviewer can integrate. The result is not progress, but review overload,
redundant artifacts, stale assumptions, incompatible branches, and contaminated
shared memory.
```

### Verifier Hierarchy Paragraph

Keep the hierarchy, but frame it as gates of increasing strength. Make clear
that weak gates may be acceptable for low-risk fuzzy outputs but not for
artifacts that enter shared state or trigger irreversible actions.

### Artifact Examples Paragraph

Keep domain examples, but sort them by the boundary they control:

- code boundary: diffs, tests, failing traces, passing logs, merge records;
- science boundary: experiment plans, run logs, datasets, statistical outputs,
  replication traces;
- memory boundary: source, timestamp, confidence, update rule, deletion rule,
  repair trace;
- safety boundary: permissions, tool-call logs, policy decisions, escalation
  records.

### CAID Paragraph

Make CAID the central positive case study for gated transfer:

```text
CAID is not merely a many-agent coding system. It is a gated artifact-transfer
system. Engineers work in isolated worktrees; local outputs become commits;
commits are merged by a manager; and integration is mediated by tests and git
history. The gain comes from letting parallel work remain private until there
is enough evidence to merge it.
```

### Scientific-Agent Paragraph

Reframe scientific systems around portfolio overload:

```text
Scientific agents make the same gating problem visible at a larger scale:
many hypotheses, code runs, plots, reports, and reviews can be generated
faster than they can be validated. The gate must include replication,
statistical validity, provenance, novelty checks, and expert review.
```

### Closing Paragraph

Replace the current closing line with a stronger multi-agent concept:

```text
Durable artifacts are the medium of multi-agent progress, but gates decide
whether those artifacts become shared state. Without gates, more agents merely
scale the volume and reach of untrusted work. With gates, parallel attempts can
remain isolated until evidence supports pruning, merging, remembering, or
escalating them.
```

## Evidence To Check Before Editing

Before changing manuscript prose, re-check local claims or primary paper text
for the following points:

- CAID: exact PaperBench and Commit0-Lite numbers; isolation ablation; manager
  delegation caveats.
- Agentless: 96/300 SWE-bench Lite result; 40 candidate patches; reproduction
  and regression test filtering caveats.
- CooperBench: communication reduces merge conflicts but does not significantly
  improve task success; two-agent and scaling results.
- DELEGATE-52: 20-interaction degradation and agentic-tool-use caveat.
- SlopCodeBench: no full end-to-end solves; structural erosion and verbosity
  trajectory claims.
- AgentRxiv: sequential and parallel archive results; manual verification and
  hallucinated-result caveats.
- MemMA: memory construction, diagnosis, repair, and ablation claims.

## Acceptance Criteria

After revision, the section should:

1. Clearly say that verification and artifact gating are necessary for agents
   in general.
2. Clearly say why the problem is more severe and more central in
   multi-agent systems.
3. Introduce artifact gates as the boundary between private attempt and shared
   progress.
4. Explain artifact explosion and integration bandwidth as multi-agent scaling
   bottlenecks.
5. Treat verification as one part of gating, alongside isolation, provenance,
   ranking, pruning, merging, memory update rules, and human escalation.
6. Use Agentless as a baseline/control rather than as a multi-agent proof.
7. Use CAID as the main positive example of gated multi-agent artifact transfer.
8. Preserve the section's existing evidence strength while making the thesis
   more distinctively multi-agent.

## Non-Goals

- Do not rewrite adjacent sections unless a transition sentence is necessary.
- Do not add new papers solely to expand coverage.
- Do not turn the section into implementation advice; keep the prose as
  field-level synthesis.
- Do not claim that artifact gating is unique to multi-agent systems.
- Do not imply that verification alone solves mergeability, contamination, or
  review-bandwidth limits.

## Suggested New Section Title

The current title is usable, but a more specific title may help:

```text
Only Gated Artifacts Become Progress
```

Alternative:

```text
Gated Artifacts Are How Distributed Work Accumulates
```

Preferred title:

```text
Only Gated Artifacts Become Progress
```

It preserves the rhythm of the current heading while making the missing concept
explicit.
