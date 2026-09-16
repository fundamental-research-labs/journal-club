# Round 5 Shared-State Governance Clarification Plan

Date: 2026-05-08

Target:

- `manuscript/multi-agent-review-draft/sections/verified-work.qmd`
- `manuscript/multi-agent-review-draft/sections/shared-state.qmd`

Primary focus: clarify the difference and relationship between `Only Verified
Work Becomes Progress` and `Governing Shared State`.

## Goal

Make the section boundary reader-obvious.

The current draft has the right ingredients, but the conceptual distinction is
too implicit. Both sections discuss artifacts, memory, verification,
degradation, and safety, so readers can reasonably ask why `Governing Shared
State` is not just a continuation of `Only Verified Work Becomes Progress`.

Round 5 should make the distinction explicit:

```text
Verification controls admission.
Shared-state governance controls accumulation.
```

Or, in the codebase analogy:

```text
CI and review decide whether a PR may enter.
Architecture, ownership, refactoring, provenance, and cleanup decide whether
the codebase remains coherent after many accepted PRs.
```

## Diagnosis

`Only Verified Work Becomes Progress` currently argues that multi-agent systems
need gates: candidate outputs should not become progress unless they can be
inspected, tested, compared, merged, repaired, or rejected.

`Governing Shared State` currently argues that shared memory and artifacts can
preserve useful context but also preserve stale assumptions, false summaries,
prompt injections, architectural decay, document corruption, and unsafe
authority chains.

The problem is not that these claims conflict. The problem is that their
relationship is under-explained.

Main sources of confusion:

- Both sections use artifacts as examples.
- Both sections mention validation.
- Both sections discuss degradation.
- `shared-state.qmd` opens with memory, which can sound like another kind of
  candidate artifact rather than the persistent substrate for future work.
- The manuscript does not yet say clearly that a locally accepted unit of work
  can still degrade the global shared environment over time.

## Core Distinction

The revised section boundary should teach a simple two-level model.

### 1. Verification Is A Local Admission Problem

Verification asks whether a unit of work should be allowed to count.

Examples:

- Does this patch pass tests?
- Does this answer satisfy the evaluator?
- Does this memory entry have a source?
- Does this document edit preserve the requested content?
- Does this experiment produce a valid result?

This is the right frame for `Only Verified Work Becomes Progress`.

### 2. Shared-State Governance Is A Global Accumulation Problem

Shared-state governance asks whether the accumulating workspace remains usable,
truthful, safe, coherent, and repairable after many accepted updates.

Examples:

- The codebase passes CI after every PR but becomes duplicated, brittle, and
  architecturally incoherent.
- The memory store contains individually sourced entries but accumulates stale,
  conflicting, or overgeneralized facts.
- A document edit passes local preservation checks but repeated delegated edits
  slowly damage style, structure, or factual consistency.
- A tool log records valid actions but exposes credentials or creates authority
  paths future agents should not inherit.
- A branch merge passes tests but makes future decomposition and review harder.

This is the right frame for `Governing Shared State`.

## New Section Thesis

Revise the governing-state section around this thesis:

```text
Verification gates are necessary but insufficient. They decide which units of
work enter the shared workspace, but they do not by themselves keep that
workspace coherent over time. Multi-agent systems also need state governance:
rules for what is shared, who can mutate it, how provenance is tracked, when
state is repaired or deleted, how parallel work is isolated, and how long-horizon
degradation is detected.
```

This thesis should appear near the beginning of `shared-state.qmd`, ideally as
the first bridge after the heading.

## Proposed Structural Changes

### 1. End `Only Verified Work` With A Handoff To Accumulation

Current ending:

```text
Durable artifacts are therefore the medium through which test-time search
becomes inspectable progress.
```

This is good, but it should hand off to the next problem:

```text
Durable artifacts are therefore the medium through which test-time search
becomes inspectable progress. But admission is not the end of coordination.
Once artifacts, memories, logs, and tool results become shared context, they
shape the next round of work. The next problem is not whether one unit of work
passed a gate, but whether the accumulating shared state remains coherent,
truthful, safe, and repairable.
```

Keep the final wording shorter than this if the prose gets heavy.

### 2. Reopen `Governing Shared State` With The Admission/Accumulation Contrast

Replace or revise the first paragraph so it does not jump directly to memory.

Suggested shape:

```text
Verification controls admission; shared-state governance controls
accumulation. A patch can pass tests and still make a codebase harder to
maintain. A memory entry can be sourced and still become stale, overgeneralized,
or unsafe when later agents retrieve it as context. A document edit can preserve
the requested fact and still erode structure over repeated transformations.
Long-horizon multi-agent systems therefore need more than gates. They need
rules for how shared state is written, scoped, repaired, deleted, and audited.
```

Then continue into the current memory paragraph:

```text
Long-horizon agents need memory, but memory is also a coordination surface...
```

### 3. Reposition MemMA As State Maintenance, Not Just Memory Accuracy

The MemMA paragraph should emphasize active maintenance:

- construction;
- retrieval;
- diagnosis;
- repair;
- provenance;
- confidence;
- deletion or correction.

The key lesson is not only that MemMA improves LoCoMo accuracy. It is that
memory must be treated as mutable shared infrastructure rather than a passive
append-only transcript.

### 4. Reframe DELEGATE-52 And SlopCodeBench As Accumulation Failures

The manuscript should state why these papers belong in shared-state governance:

- DELEGATE-52: repeated locally plausible transformations can corrupt a shared
  document.
- SlopCodeBench: repeated locally acceptable code changes can erode structure
  and maintainability.

These are not merely failures to verify one output. They are failures to govern
the long-horizon substrate.

### 5. Keep Safety As State Propagation

The safety material belongs in this section if it is framed as propagation
through shared state and authority edges:

```text
message -> memory -> tool call -> artifact mutation -> trusted context
```

Avoid making it a generic agent-safety subsection. The section's specific
contribution is that shared state is both memory and attack surface.

## Section-Level Arc After Revision

`Only Verified Work Becomes Progress` should have this arc:

1. Extra agents create candidate work.
2. Candidate work does not count until it is inspectable and checkable.
3. Verification has levels, from weak consensus to executable validators.
4. Artifacts are the selection surface.
5. CAID and scientific-agent workflows show why isolated, evidence-rich
   artifacts matter.
6. Handoff: accepted artifacts become shared context, which creates the
   accumulation problem.

`Governing Shared State` should have this arc:

1. Admission is not enough; accumulation must be governed.
2. Memory is persistent coordination state, not a passive transcript.
3. MemMA illustrates active construction, retrieval, diagnosis, and repair.
4. DELEGATE-52 shows repeated document edits can corrupt shared artifacts.
5. SlopCodeBench shows locally acceptable code changes can erode structure.
6. Safety failures propagate through shared state and authority edges.
7. Prescription: type, scope, provenance, isolation, validation near actions,
   reversibility, repair, deletion, and escalation.

## Boundary Test

Use this test while editing:

```text
If the sentence asks whether a unit of work should be accepted, it belongs in
Verified Work.

If the sentence asks what accepted or exposed information does to the future
workspace, memory, artifact, authority graph, or repair burden, it belongs in
Governing Shared State.
```

Examples:

| Sentence topic | Section |
|---|---|
| Tests decide whether a patch should merge | Verified Work |
| Many test-passing patches can make the codebase incoherent | Governing Shared State |
| A memory entry needs source and timestamp before trust | Verified Work |
| Memory stores need correction, deletion, and conflict handling | Governing Shared State |
| Candidate document edits should be checked before acceptance | Verified Work |
| Repeated delegated edits can degrade the document over time | Governing Shared State |
| A verifier selects among independent solutions | Verified Work |
| A contaminated memory can trigger later unsafe tool calls | Governing Shared State |

## Evidence Use

Use the existing evidence set; this plan does not require new papers.

Primary citations:

- `@memgpt`, `@amem`, `@memma` for memory as actively managed shared state.
- `@delegate52` for document/artifact degradation over repeated transformations.
- `@slopcodebench` for long-horizon code-quality erosion despite local progress.
- `@caid` for isolation, provenance, and branch-and-merge as a bridge from
  verified artifacts to governed shared work.
- `@gsafeguard`, `@safearena`, `@openagentsafety`, `@zerodayagents` for safety
  as propagation through communication, memory, tools, and authority edges.

Optional analogy, if kept concise:

```text
CI is not architecture.
```

This phrase is useful internally, but manuscript prose should probably use the
full idea rather than the slogan.

## Rewrite Steps

1. Add a short handoff sentence or paragraph at the end of
   `verified-work.qmd`.
2. Rewrite the opening of `shared-state.qmd` around the
   admission/accumulation distinction.
3. Adjust the MemMA paragraph so its main lesson is state maintenance, not only
   memory benchmark improvement.
4. Add one explicit sentence before DELEGATE-52 and SlopCodeBench explaining
   that they are accumulation/degradation cases.
5. Tighten the safety paragraph around propagation through shared state and
   authority edges.
6. Preserve the final prescription list, but add repair/deletion/refactoring
   language if it is missing.
7. Re-read both sections using the boundary test above and move any sentence
   that belongs on the other side.

## Success Criteria

After Round 5, a reader should be able to say:

```text
The previous section is about gates: how candidate work becomes progress.
This section is about stewardship: how the accepted and shared workspace stays
coherent, truthful, safe, and repairable over time.
```

The section should also make the codebase analogy intuitive:

```text
Even if every engineer's PR passes CI, the codebase can still become ugly,
duplicated, brittle, and hard to change. Multi-agent systems have the same
problem with memories, documents, tool logs, branches, and shared artifacts.
They need periodic repair and governance, not only admission checks.
```

## Non-Goals

- Do not add a new major section.
- Do not turn `Governing Shared State` into a generic software-engineering
  analogy.
- Do not weaken the verification section; gates remain necessary.
- Do not add new citations unless a factual gap appears during editing.
- Do not make manuscript prose meta-commentary about the author's confusion.
  The final text should teach the distinction directly.
