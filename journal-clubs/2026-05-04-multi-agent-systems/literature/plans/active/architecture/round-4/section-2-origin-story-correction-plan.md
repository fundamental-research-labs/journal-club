# Round 4 Section 2 Origin Story Correction Plan

Date: 2026-05-08

Target: `manuscript/multi-agent-review-draft/index.qmd`

Primary focus: current section `Coordination Was Hard Before LLMs`

## Goal

Correct the manuscript's origin story for modern LLM-driven multi-agent
systems.

The current draft gives classical MAS/MARL too much genealogical weight. That
framing is academically respectable, but it risks being historically and
technically misleading. Modern LLM multi-agent work is not mainly MARL with
language. Its core object is an agent harness plus test-time orchestration over
tools, context, memory, artifacts, evaluators, and human review.

Round 4 should replace the current section-2 direction with a sharper claim:

```text
Classical MAS and MARL are useful contrast cases, not the main origin story.
Modern LLM multi-agent systems became possible when LLMs were wrapped in
agent harnesses: tool loops, memory, code execution, browsers, files,
retrieval, logs, benchmarks, and human-inspectable artifacts. Once LLM calls
became stateful workers, multi-agent design shifted from training-time policy
coordination to test-time allocation of diverse attempts, tools, contexts,
branches, verifiers, and human attention.
```

## Diagnosis

The current section argues:

- pre-LLM MAS, MARL, and emergent communication had already identified
  coordination problems;
- LLM agents changed the medium from learned vectors and policies to language,
  tools, files, memories, and artifacts;
- old constraints reappeared as context partitioning, lossy summarization,
  artifact attribution, and routing/merge problems.

This is partly true, but the emphasis is wrong.

Main problems:

- It makes MARL look like the conceptual parent of modern LLM multi-agent
  systems.
- It spends too much section-level attention on low-level learned
  coordination: RIAL/DIAL, CommNet, TarMAC, MADDPG, COMA, VDN, QMIX, MAPPO,
  SMAC, OpenAI Five, and hide-and-seek.
- It underplays the actual substrate that made LLM multi-agent systems matter:
  prompts, tool loops, memory, sandboxes, browser/OS/code interfaces,
  retrieval, file systems, logs, permission boundaries, and benchmark harnesses.
- It does not foreground agent diversity, which is central to modern LLM
  multi-agent value: different models, prompts, roles, tools, contexts,
  retrieval sources, memories, branches, temperatures, evaluators, and human
  reviewers.
- It treats games and simulations as a deeper ancestry than they probably are.
  Modern systems are evaluated on real-work or real-work-like artifacts:
  patches, tests, documents, browser tasks, APIs, workplace tasks, experiment
  logs, reports, and long-horizon degradation.
- The section risks weakening the review's central thesis by making the field
  sound like a continuation of MARL, when the stronger claim is that LLMs
  created a new coordination substrate.

## New Section Thesis

Replace the current thesis:

```text
Coordination was hard before LLMs; LLMs changed the medium but not the
coordination problem.
```

with:

```text
MARL showed that multiple agents do not automatically coordinate, but it is
not the main technical ancestor of modern LLM multi-agent systems. The decisive
change was the agent harness: LLMs became stateful, tool-using, artifact-
producing workers that could be orchestrated at test time. This made
multi-agent systems easy to build and inspect, but it also created a new class
of coordination problems around context, diversity, tools, artifacts,
verification, cost, and human review.
```

## Proposed Section Replacement

Rename the section from:

```text
## Coordination Was Hard Before LLMs
```

to one of:

```text
## The Missing Substrate Before LLM Agents
## From Learned Coordination to Agent Harnesses
## What Changed: Agent Harnesses, Not Just More Agents
## Why MARL Is the Wrong Origin Story
```

Preferred title:

```text
## From Learned Coordination to Agent Harnesses
```

This title is less combative than "wrong origin story" while still making the
historical correction.

## New Section Arc

### 1. Start With A Contrast, Not A Lineage

Open by acknowledging MARL/MAS, then immediately demote it from origin story to
contrast class.

Core claim:

```text
Classical MAS and MARL are important background, but they are not the main
technical lineage of modern LLM-agent systems. Their agents were usually
learned policies in controlled environments, often games or simulations,
coordinating through actions, rewards, latent messages, centralized training,
or environment state. Modern LLM agents are prompted, tool-using, stateful
workers operating over human-readable language, external tools, files,
memories, code, browsers, APIs, logs, and artifacts.
```

Use only a few MARL citations here. Do not keep the current catalogue.

Recommended citations:

- RIAL/DIAL or CommNet/TarMAC for learned communication.
- MADDPG/COMA/QMIX or MAPPO/SMAC for training and credit assignment.
- OpenAI Five or hide-and-seek only if needed as examples of scale and
  simulator dependence.

### 2. Explain What MARL Mostly Did Not Address

Make explicit why MARL is insufficient as the origin story.

Modern LLM multi-agent work centers on:

- agent harness design;
- prompt and role design;
- tool APIs and tool permissions;
- code execution and sandboxes;
- browser, OS, mobile, API, and repository interfaces;
- memory and retrieval systems;
- logs, traces, and provenance;
- file and artifact management;
- heterogeneous model/prompt/tool/context diversity;
- sampling, voting, debate, branch-and-merge, and verifier-guided search;
- budget, latency, and human review bandwidth;
- real-work benchmarks and long-horizon artifact quality.

Most MARL work does not make these the unit of analysis.

### 3. Identify The True Immediate Precondition: The Agent Harness

The section should then pivot to the harness.

Core claim:

```text
The immediate precondition for modern multi-agent LLM systems was not a
breakthrough in MARL. It was the transformation of an LLM call into an agentic
worker: a loop that can observe, reason, call tools, write files, retrieve
state, execute code, inspect results, and leave traces.
```

Evidence and examples:

- ReAct as the reasoning-action-observation loop.
- Toolformer or other tool-use lineage if already in the bibliography and
  useful.
- AutoGen/OpenHands/AgentScope/Magentic-One as runtime/harness frameworks.
- WebArena/OSWorld/SWE-bench/GAIA/tau-bench as executable evaluation harnesses.

This section should set up the later `From Prompts to Runtimes` section, not
duplicate it. Keep it conceptual and historical.

### 4. Define The Modern Multi-Agent Shift

Once an LLM call becomes a stateful worker, multiplicity becomes meaningful in
a new way.

Modern multi-agent systems can vary:

- model;
- prompt;
- role;
- tool access;
- memory;
- retrieval source;
- context window;
- artifact branch;
- temperature or sampling path;
- verifier;
- human reviewer;
- orchestration policy.

This is the modern form of "agent diversity." It is not the same as training
multiple agents from scratch in one simulated environment.

Core claim:

```text
In modern LLM systems, multi-agent value usually comes from test-time diversity
and allocation, not from end-to-end learned team policies. The system spends
inference on different attempts, contexts, tools, branches, critiques, or
verifiers, then selects or merges what survives evidence.
```

This prepares the reader for later sections on mechanisms, artifacts,
verification, and orchestration.

### 5. Preserve A Narrow MARL Lesson

Do not erase MARL completely. Keep the useful warning:

```text
The narrow lesson from MARL is negative but important: multiple agents, message
channels, and shared objectives do not by themselves produce useful
coordination. Communication can be degenerate, credit assignment can remain
unsolved, and local success can fail to compose into global success.
```

Then make the distinction:

```text
But the LLM-agent field rediscovered this lesson in a different substrate:
lossy summaries, shared-memory drift, duplicated attempts, weak verifiers,
artifact corruption, and unclear attribution of which worker or edit improved
the result.
```

This keeps the historical depth without overclaiming lineage.

### 6. Bridge Into The 2023 Organization Bet

End the section by explaining why the 2023 organization metaphor became
plausible.

Core transition:

```text
Language made coordination look solved at the interface level. A designer
could now write "manager," "engineer," "critic," or "scientist" into a prompt;
give each worker tools and memory; and watch a transcript that resembled human
collaboration. That interface-level legibility made the 2023 organization bet
natural. It also made the field vulnerable to confusing role description with
reliable coordination.
```

This should lead directly into `The 2023 Organization Bet`.

## Material To Cut Or Demote

Cut or heavily compress:

- detailed walkthrough of RIAL/DIAL, CommNet, referential games, TarMAC;
- detailed walkthrough of MADDPG, COMA, VDN, QMIX, MAPPO, SMAC;
- broad claim that the mapping from MARL constraints to LLM-agent constraints
  is "direct";
- any wording implying that LLM multi-agent systems are a direct successor to
  classical MARL.

Possible replacement:

```text
Classical MAS and MARL studied hard coordination problems such as learned
communication, credit assignment, centralized training with decentralized
execution, and cooperative control [@rialdial; @commnet; @tarmac; @maddpg;
@coma; @qmix; @mappo; @smac]. Those problems remain useful warnings, but they
do not define the modern LLM-agent substrate.
```

## Material To Add

Add a compact table:

| Dimension | Classical MAS/MARL | Modern LLM multi-agent systems |
|---|---|---|
| Agent substrate | learned policies | prompted/tool-using workers |
| Communication | learned signals, actions, environment state | language, structured messages, files, logs, artifacts |
| Coordination phase | mostly training-time or fixed policy execution | mostly test-time orchestration |
| Diversity | agents trained in an environment, sometimes homogeneous policies | model, prompt, role, tool, context, memory, branch, verifier, human reviewer |
| Work product | reward, game outcome, task success | patches, tests, documents, reports, browser/API states, experiment logs |
| Evaluation | games, simulations, cooperative control | real-work benchmarks, artifact quality, cost, latency, degradation, human review |
| Main failure surface | non-stationarity, credit assignment, communication protocol failure | context loss, weak verification, duplicated work, artifact corruption, merge failure, unsafe tool/state propagation |

Keep the table short and claim-making. It should not become a survey table.

## Downstream Manuscript Adjustments

Changing section 2 affects adjacent sections.

### Introduction and Scope

Revise any sentence that implies the historical movement begins with inherited
MARL coordination problems.

Potential replacement for the current table row:

```text
Pre-LLM and adjacent foundations | What did earlier coordination and tool-use
work fail to provide? | MARL, emergent communication, ReAct, tool-use agents,
workflow systems, early benchmarks | MARL warned that agents do not coordinate
automatically, but modern LLM multi-agent systems required a new substrate:
agent harnesses, tools, memory, artifacts, and test-time orchestration.
```

### The 2023 Organization Bet

Strengthen the opening so it follows from the harness section:

```text
Once LLM calls could be wrapped as stateful tool-using workers, the next step
was to arrange them as organizations.
```

### From Prompts to Runtimes

Avoid repeating the harness argument. This section should become more about
runtime maturation:

- from ad hoc harnesses to programmable coordination substrate;
- turn-taking and topology;
- event streams, sandboxes, ledgers, files, queues, state stores, validators;
- why durable artifacts start to matter.

### Evaluation Turn

The evaluation turn should explicitly connect to real-work harnesses:

```text
The benchmark wave evaluated not abstract coordination, but harnessed agents
inside environments: browsers, operating systems, repositories, APIs, mobile
devices, and workplace workflows.
```

## Rewrite Steps

1. Rename section 2 to `From Learned Coordination to Agent Harnesses`.
2. Replace the MARL catalogue with a contrast-class paragraph.
3. Add a short paragraph on what MARL did not address: harnesses, diversity,
   artifacts, real-work benchmarks, costs, and human review.
4. Add the agent-harness thesis paragraph.
5. Add the classical-vs-modern comparison table.
6. Add the test-time diversity/allocation paragraph.
7. Preserve one compact MARL warning paragraph.
8. End with a bridge into the 2023 organization bet.
9. Update the introduction history table row and any abstract/key-message lines
   that overstate MARL inheritance.
10. Re-read `The 2023 Organization Bet` and `From Prompts to Runtimes` to remove
    duplication and improve causal flow.
11. Render the manuscript and inspect whether the revised section feels like a
    necessary origin story rather than an obligatory background survey.

## Success Criteria

The revised section should make a reader believe:

- MARL is relevant background but not the main origin story.
- The decisive change was wrapping LLMs in agent harnesses.
- Modern multi-agent value depends on test-time diversity, allocation,
  artifacts, and verification.
- The 2023 organization bet was plausible because language and harnesses made
  coordination easy to specify and inspect.
- The later skeptical evidence matters because role description and visible
  conversation are not the same as reliable coordination.

The section should no longer feel like it is paying dues to MARL. It should
feel like it is correcting the field's origin story.
