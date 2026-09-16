# Self-evolving agents

**Session:** Friday, September 18, 2026  
**Research cutoff:** September 16, 2026  
**Format:** Topic-wide overview and discussion, organized by concepts and evidence.

Central question: **How can agents turn experience into lasting improvements—and how can we tell whether those improvements generalize?**

## Materials

- [Updated research landscape](research/landscape.md): current starting point, with September additions, competing evidence, and discussion questions.
- [Source register and detailed reading notes](research/sources.md): twelve source notes, publication/version dates, experimental details, and access limits.
- [Search log](research/search-log.md) and [research handoff](workflow.md): coverage, verification, and remaining questions.
- [Research notes](research-notes.md): conceptual map, recent evidence, limitations, and discussion questions.
- [Reading list](reading-list.md): recent primary sources, dates, review status, and historical background.
- [Practitioner sources](practitioner-sources.md): original blogs, project documentation, code releases, and X/Twitter leads, with evidence and access notes.

## Proposed topic outline

Working assumption: 45 minutes including discussion; audience familiar with LLM basics.

| Time | Question | Coverage |
| --- | --- | --- |
| 0–5 min | What does self-evolution mean? | Persistent adaptation, feedback, and the distinction between task improvement and improving the improvement process |
| 5–15 min | What can change? | Prompts, memory, skills, tools, agent code, model weights, curricula, and collaboration |
| 15–25 min | How does experience become an update? | Reflection, selection, validation, retention, rollback; recent examples across several mechanisms |
| 25–35 min | What evidence is convincing? | Held-out tasks, matched compute, task streams, transfer, regressions, and verifier quality |
| 35–45 min | What remains open? | Reliability, forgetting, cost, autonomy, and whether recursive improvement compounds |

## Selected supporting literature

Prioritize **WikiSkill** for retained knowledge, **AgentStream** for task streams, **Rethinking the Evaluation of Harness Evolution for Agents** and **HarnessDev** for evaluation, and **Hyperagents** for improving the improvement process. Pair these with **Library Drift** and **EvoHarnessBench** for regressions and changing interfaces. September frontier coverage includes **MetaRSI** and the September 15 **ScienceBuddy** preprint; their stronger claims retain explicit qualifications. The reading list also includes memory, longitudinal evaluation, and broad surveys.

DGM, SICA, and earlier systems provide historical context. The session does not have a single main paper. These are initial research materials; slides have not yet been created.

Weave practitioner examples into the same themes: autoresearch for experiment loops, Hermes and LangChain for procedural learning, and NVIDIA's September memory-agent writeup for measured benefits and regressions. The update adds **Reef** for continual-learning infrastructure and **SoL-Pi** for reusable harness-efficiency mechanisms. Code releases and demos are distinguished from controlled measurements.

Research was updated September 16 using the journal-club-research skill. Primary methods/results sections and selected appendices were reviewed; no experiments were reproduced. See the source notes for review depth and unresolved statistical details.
