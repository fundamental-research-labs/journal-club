# Claims

## Claim 1
**Claim:** Base-model capability is the main driver of scientific-agent performance, while scaffold choice has only a small effect.

**Evidence:** The paper evaluates three models with ReAct and structured tool-calling across eight domains and reports that reasoning ability and environment/scope dominate explained variance, with scaffold and tool-description verbosity contributing minimally.

**Caveats/Scope:** The comparison is limited to the studied models, scaffolds, tool interfaces, and Corral environments.

**Source pointers:** `summary.md`; `source/main.tex`; `source/sections/results.tex`; `source/sections/methods.tex`

## Claim 2
**Claim:** Outcome success can hide poor epistemic process in scientific agents.

**Evidence:** The authors separately analyze task performance and reasoning traces, finding frequent evidence non-uptake, untested claims, missing belief updates, and rare convergent multi-test evidence even when agents produce usable results.

**Caveats/Scope:** Trace analysis uses annotated ReAct traces and a specific taxonomy of epistemic operations and motifs.

**Source pointers:** `summary.md`; `source/sections/results.tex`; `source/tables/reasoning_breakdowns.tex`; `source/tables/productive_motifs.tex`

## Claim 3
**Claim:** Agents do not substantially adapt their reasoning topology to different scientific epistemic demands.

**Evidence:** The paper groups tasks from workflow execution to hypothesis-driven inquiry and reports similar reasoning patterns across domains and scopes, despite different scientific demands.

**Caveats/Scope:** This is a behavioral pattern over the benchmark's selected domains, not a proof about all scientific tasks.

**Source pointers:** `source/sections/results.tex`; `source/tables/domain_summary_table.tex`; `summary.md`

## Claim 4
**Claim:** Providing partial successful trajectories helps workflow tasks earlier than hypothesis-driven tasks.

**Evidence:** Trace intervention experiments inject prior successful or failed trajectories; workflow-construction environments improve with early successful steps, while spectra, wet-lab, and retrosynthesis need near-complete successful traces for gains.

**Caveats/Scope:** Interventions replay prior traces from the study setup and do not cover every possible scaffold or memory method.

**Source pointers:** `source/sections/results.tex`; `source/sections/methods.tex`; `summary.md`

## Claim 5
**Claim:** Reliability decays quickly when repeated success is required in epistemically demanding domains.

**Evidence:** The paper analyzes pass-hat, requiring all repeated trials to succeed, and reports sharp decay in hypothesis-driven domains even under early success-trace interventions.

**Caveats/Scope:** Reliability is measured under the paper's task definitions, trial settings, and intervention protocol.

**Source pointers:** `source/sections/results.tex`; `source/main.tex`; `summary.md`
