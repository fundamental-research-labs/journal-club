# Claims

## Claim 1: Cooperative coding agents can perform worse than a solo agent doing both tasks.

**Evidence:** In the Coop setting, two agents each implement one feature; in Solo, one agent implements both. Across tested models, Coop success is consistently lower than Solo, with large gaps for leading models.

**Caveats/Scope:** The result is for coding tasks in CooperBench's isolated-branch setup and should not be read as a claim about all human-AI or agent-agent workflows.

**Source pointers:** `summary.md`; `source/sections/04-cooperation.tex`; `source/main.tex`

## Claim 2: Communication reduces spatial merge conflicts but does not significantly improve end-to-end success.

**Evidence:** The paper reports that agents use the communication channel heavily and reduce naive merge conflicts, yet with-communication and no-communication task success are not statistically different.

**Caveats/Scope:** Communication helps with "where to edit" more than "what compatible behavior to implement"; better shared-state mechanisms may change this result.

**Source pointers:** `summary.md`; `source/sections/05-communication.tex`

## Claim 3: Coordination failures concentrate around communication, commitment, and expectation gaps.

**Evidence:** The qualitative analysis of failed Coop trajectories identifies failures to exchange useful information, failures to honor commitments, and failures to model partner state or plans.

**Caveats/Scope:** Root causes are manually interpreted from failed traces; symptom labels are scaled with LLM-as-judge annotations.

**Source pointers:** `source/sections/06-coordination.tex`; `source/sections/06-causes_table.tex`; `summary.md`

## Claim 4: Adding more cooperating agents worsens success in the benchmark setting.

**Evidence:** A pilot scaling experiment over 46 tasks reports monotonically lower success as the number of cooperating agents increases from 2 to 4.

**Caveats/Scope:** The multi-agent scaling result is a smaller experiment than the main 2-agent benchmark.

**Source pointers:** `source/sections/04-cooperation.tex`; `summary.md`

## Claim 5: Successful runs show rare but concrete coordination patterns.

**Evidence:** The paper identifies role division, resource division, and negotiation in successful traces, all of which make commitments more specific and verifiable.

**Caveats/Scope:** These behaviors are described as rare, not reliable default behavior.

**Source pointers:** `source/sections/06-coordination.tex`; `summary.md`
