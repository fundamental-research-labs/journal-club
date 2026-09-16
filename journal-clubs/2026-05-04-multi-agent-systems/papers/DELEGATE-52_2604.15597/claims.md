# Claims

## Claim 1: Long-horizon delegated editing causes substantial document degradation.

**Evidence:** The benchmark chains reversible edit pairs into a 20-interaction relay and reports that all tested models accumulate errors, with frontier models still losing a meaningful share of document content.

**Caveats/Scope:** Scores depend on domain-specific reconstruction metrics and simulated reversible workflows, not arbitrary user editing sessions.

**Source pointers:** `summary.md`; `source/colm2026_conference_submission.tex`; `source/tables/overall_by_round.tex`

## Claim 2: DELEGATE-52 evaluates delegated work without reference annotations by using round-trip relays.

**Evidence:** Each editing task has a forward instruction and inverse instruction; a perfect model should reconstruct the original seed document after the round trip, enabling automatic scoring by similarity to the seed.

**Caveats/Scope:** The approach assumes tasks are genuinely reversible and that models attempt the edit rather than exploiting the round-trip structure.

**Source pointers:** `source/colm2026_conference_submission.tex`; `summary.md`

## Claim 3: Readiness for delegation varies sharply by domain.

**Evidence:** The paper builds 310 work environments across 52 professional domains and reports that Python is an outlier where most models are near lossless, while most domains remain unreliable.

**Caveats/Scope:** Domain readiness uses the paper's RS@20 threshold and selected textual document formats.

**Source pointers:** `source/colm2026_conference_submission.tex`; `source/tables/round10_by_domain.tex`; `summary.md`

## Claim 4: Basic agentic tool use does not fix document corruption.

**Evidence:** In the tested file read/write/code execution harness, models degrade documents more with tools than without tools, despite increased token and tool-use overhead.

**Caveats/Scope:** The harness is described as basic rather than a fully optimized agent system.

**Source pointers:** `source/colm2026_conference_submission.tex`; `source/tables/agentic_scores.tex`; `source/tables/agentic_behavior.tex`

## Claim 5: Short simulations can miss long-horizon failure modes.

**Evidence:** The paper reports that early reconstruction scores after two interactions do not reliably predict scores after 20 interactions, and studies document size and interaction length as compounding factors.

**Caveats/Scope:** The finding is about preservation under repeated editing, not one-shot task success.

**Source pointers:** `source/colm2026_conference_submission.tex`; `source/tables/context_size.tex`; `summary.md`
