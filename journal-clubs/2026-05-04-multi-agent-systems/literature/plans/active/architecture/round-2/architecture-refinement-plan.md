# Round 2 Architecture Refinement Plan

Date: 2026-05-07

Target: `manuscript/multi-agent-review-draft/index.qmd`

## Goal

Move the manuscript from a strong section-level synthesis to a more deliberate review architecture. Round 1 gave the draft the right core sections: history, evaluation, skeptical controls, mechanisms, optimized coordination, artifacts, shared state, and orchestration. Round 2 should make the structure feel inevitable to a reader.

The target reader should understand the review as one causal argument:

```text
coordination was already hard -> LLMs made role-organizations easy to build
-> runtimes made them programmable -> evaluations exposed brittleness
-> skeptical controls forced mechanism-level claims -> mechanisms need
verification and artifacts -> shared state creates reliability and safety risks
-> mature systems optimize orchestration and human review.
```

## Current Diagnosis

The current manuscript has the right thesis and mostly the right topics. The remaining architecture issues are higher-level:

- The manuscript is still visually flat: nearly every major idea is a peer-level `##` section.
- `From Designed Teams to Optimized Coordination` appears before `Verification and Artifacts`, which weakens the causal logic. The stronger order is to explain what mechanisms survive, then why verification/artifacts/state are necessary, then why orchestration must be optimized.
- `Governing Shared State` currently carries memory, degradation, and safety. The shared-state framing is good, but safety risks becoming too buried for a field-shaping review.
- Human-in-the-loop multi-agent scaling is present, but not structurally visible enough given its importance as the most plausible near-term deployment pattern.
- The manuscript lacks a short methods/scope note explaining how the core corpus, extra corpus, surveys, and evidence hierarchy were used.
- The conclusion is good, but the final third should more explicitly answer: what should readers do differently when designing or evaluating a new multi-agent system?

## Round 2 Target Architecture

Use part-level headings or unnumbered divider sections to make the causal flow explicit. Quarto can keep them as ordinary `##` sections if needed, but the manuscript should visibly group the argument into four parts.

Preferred table of contents:

```text
Key Messages

Part I. Scope and Historical Setup
1. Introduction and Scope
2. Coordination Was Hard Before LLMs
3. The 2023 Organization Bet
4. From Prompts to Runtimes

Part II. What Evaluation Changed
5. The Evaluation Turn
6. The Coordination Reality Check
7. Mechanisms of Multi-Agent Value

Part III. The Durable Substrate
8. Verification and Artifacts
9. Governing Shared State
10. Safety and Security as Coordination Problems

Part IV. Allocation and Control
11. From Designed Teams to Optimized Coordination
12. Orchestration as a Control Problem
13. Conclusion
```

If length pressure is severe, keep safety inside `Governing Shared State`, but add clear subsections and a stronger section title:

```text
## Governing Shared State, Memory, and Safety
```

Do not collapse `Mechanisms of Multi-Agent Value`; it is the manuscript's main reusable classification framework.

## Structural Changes

### 1. Add A Short Review Scope And Evidence Note

Add a compact paragraph or boxed note near the end of `Introduction and Scope`.

It should state:

- the review prioritizes primary papers over surveys for evidentiary claims;
- `papers/` is the deeply reviewed core corpus;
- `papers_extra/` and the field map are used for coverage checks and gap discovery, not as equal-weight reviewed evidence;
- claims are weighted by evidence type: controlled results, realistic benchmarks, failure analyses, released artifacts, demos, surveys, and forecasts.

This should not become a full systematic-review methods section. The goal is trust and scope discipline.

### 2. Add Part-Level Signposts

Add short transition paragraphs at the start of each part.

Each signpost should tell the reader what changed:

- Part I: multi-agent LLM systems inherit old coordination problems, even though the medium changed.
- Part II: realistic evaluation and budget controls changed what counts as evidence.
- Part III: durable artifacts and governed state are the substrate that lets multi-agent search become inspectable.
- Part IV: the mature design problem is allocation: when to use serial reasoning, sampling, delegation, verification, training, humans, and stopping.

### 3. Move Optimized Coordination Later

Move `From Designed Teams to Optimized Coordination` after `Verification and Artifacts`, `Governing Shared State`, and the safety treatment.

Rationale:

- Mechanisms explain how multi-agent value can arise.
- Verification and artifacts explain how useful search is selected.
- Shared state and safety explain what must be governed.
- Optimized coordination then becomes the control layer that allocates these mechanisms under cost and risk.

This creates a stronger final act than placing optimized coordination immediately after mechanisms.

### 4. Make Safety Structurally Visible

Preferred change: split the safety paragraphs out of `Governing Shared State` into:

```text
## Safety and Security as Coordination Problems
```

The section should not become a generic AI safety survey. It should focus on topology-specific risks:

- tool authority;
- message contamination;
- memory poisoning;
- artifact contamination;
- unsafe specialist capability gains;
- over-trust among agents;
- weak escalation and permission boundaries.

The core claim:

> Multi-agent safety is a property of communication graphs, memory graphs, tool graphs, and artifact pipelines, not only individual model responses.

### 5. Promote Human-Governed Portfolios

Human-in-the-loop scaling should appear in two places:

- In `Mechanisms of Multi-Agent Value`, keep `Human-governed portfolios` as a mechanism row.
- In `Orchestration as a Control Problem`, add a short subsection or paragraph on review-bandwidth allocation.

Do not make a separate human-in-the-loop section unless the manuscript becomes longer. It is better as a recurring design variable than as a detached topic.

### 6. Strengthen The Transition From Mechanisms To Artifacts

End `Mechanisms of Multi-Agent Value` with a stronger bridge:

```text
The mechanism taxonomy identifies where extra computation might help. It does
not by itself explain how the system knows which partial work to keep. That
selection pressure comes from verification, and verification needs artifacts.
```

This makes `Verification and Artifacts` feel necessary rather than adjacent.

### 7. Make The Final Third More Decision-Oriented

`Orchestration as a Control Problem` should be the practical payoff of the review.

Start it with a decision table:

| Task condition | Likely architecture | Evidence to demand |
|---|---|---|
| Compact, context-fit, weakly decomposable | One strong agent or best-of-N | Multi-agent overhead beats equal-budget alternatives |
| Many independent attempts with cheap checking | Sampling, voting, or mixture aggregation | Errors are not strongly correlated |
| Evidence or tools partition naturally | Specialist agents plus routing | Routing preserves global state |
| Work can be isolated and tested | Branch-and-merge artifact workflow | Integration quality is measured |
| State is long-lived or safety-sensitive | Governed memory, permissions, provenance, human escalation | Contamination and irreversible actions are controlled |
| Repeated task family with stable feedback | Optimized topology, controller, or trained collaboration | Learned policy transfers beyond training tasks |
| High-impact, uncertain, or taste-sensitive | Human-governed portfolio | Review bandwidth goes to the right decisions |

The section should then turn future directions into research programs, not a citation stack.

## Proposed Rewrite Order

1. Add part-level signposts and decide whether part headings should be rendered as visible headings or unnumbered dividers.
2. Add the review scope/evidence note in `Introduction and Scope`.
3. Strengthen the final paragraph of `Mechanisms of Multi-Agent Value` so it points directly to artifacts.
4. Move `From Designed Teams to Optimized Coordination` into the final part, after shared-state/safety material.
5. Split safety into its own section, or retitle and subsection `Governing Shared State` if length pressure wins.
6. Add review-bandwidth allocation to `Orchestration as a Control Problem`.
7. Recheck section endings so each one hands the reader a concept, not just a summary.
8. Render the manuscript and inspect the table of contents for visual flatness.

## Acceptance Criteria

- The table of contents exposes a clear four-part arc.
- The review scope/evidence contract is visible in the opening.
- `Mechanisms of Multi-Agent Value` remains the central classification engine.
- `Verification and Artifacts` follows naturally from mechanisms.
- Safety is visibly part of the main argument, not an afterthought.
- Human-in-the-loop scaling appears as a mechanism and as an orchestration constraint.
- Optimized coordination appears as part of allocation/control, not as a detached trend section.
- The final third gives readers a decision framework for when to use multi-agent systems.
- The manuscript still avoids becoming a catalogue of domains or papers.

## Files To Edit

- `manuscript/multi-agent-review-draft/index.qmd`
- `manuscript/multi-agent-review-draft/section-review-evidence.md`, if the restructuring rationale should be logged

Only edit `references.bib` if the rewrite adds new citations. Round 2 should mostly reorganize and sharpen existing evidence.

## Non-Goals

- Do not expand the review into a systematic survey of all `papers_extra/` entries.
- Do not add a domain-by-domain catalogue section.
- Do not add robotics, medicine, legal, or social-simulation material unless it illustrates a mechanism, verifier, safety risk, or human-review constraint.
- Do not let the methods note dominate the introduction.
- Do not weaken the skeptical evidence to make the story smoother.
