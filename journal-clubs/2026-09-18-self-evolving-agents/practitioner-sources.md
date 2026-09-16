# Practitioner research, blogs, and social posts

Searched September 16, 2026. These sources contribute to the main topic alongside papers. Publication format does not determine evidence quality: examine the method, artifacts, comparison, and reproducibility. No software was installed or experiments reproduced for this pass.

## Sources to weave into the talk

### Autonomous experiments: Andrej Karpathy's autoresearch

- **Source/date:** [Official repository and README](https://github.com/karpathy/autoresearch), March 2026 project; live documentation inspected September 16.
- **What it adds:** A compact, inspectable experiment loop. The agent edits `train.py`, runs five-minute training experiments, and retains or discards changes using validation bits per byte. The README assigns `program.md` to human editing and leaves preparation/evaluation utilities fixed.
- **Evidence/status:** README read; executable project available, not reproduced here. An implementation example rather than a controlled estimate of general self-improvement.
- **Discussion:** Which system is improving—the trained model, the experiment procedure, or the coding agent? Our interpretation: the default editing boundary demonstrates automated research without establishing that the agent autonomously improves every part of its own learning process.
- **Social context:** The repository links the author's [announcement](https://x.com/karpathy/status/2030371219518931079) and [follow-up](https://x.com/karpathy/status/2031135152349524125). Direct X retrieval failed. Preserve these original links; do not quote inaccessible posts or import numerical claims from reposts. Exact post dates remain unverified here.

### Persistent procedural learning: Hermes Agent

- **Source/date:** Nous Research's [Skills System documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills), live documentation accessed September 16, 2026; publication date not shown.
- **What it adds:** The agent can create, update, and delete skills using `skill_manage`. Documentation describes recording reusable procedures after difficult workflows, errors, or user corrections, and loading skills when relevant.
- **Evidence/status:** Relevant documentation sections read. This establishes documented functionality, not the size of a performance gain or its reliability over months.
- **Discussion:** Compare creation, selection, retrieval, and retirement of a skill. A saved procedure only helps if it is correct, applicable, and loaded at the right time. Pair this implementation view with WikiSkill's experimental evidence.

### Trace-to-memory engineering: LangChain

- **Source/date:** Jake Broekhuizen, [How To Give Your Agent Memory](https://www.langchain.com/blog/how-to-give-your-agent-memory), June 24, 2026.
- **What it adds:** A concrete capture-traces → analyze-traces → update-memory workflow, using observability, background analysis, and versioned context. The post distinguishes stored history from lessons that change later behavior.
- **Evidence/status:** Article read. Engineering guidance and a vendor implementation description; no controlled benchmark gain is established by the sections reviewed.
- **Discussion:** What should become durable context, an evaluation example, a tool fix, or a code change? The article also highlights stale runtime context: storing an update is insufficient if subsequent runs never load it.

### September example with measurements: NVIDIA NemoClaw

- **Source/date:** Xuan Wu et al., [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/), September 4, 2026; [linked recipe](https://github.com/NVIDIA/nemoclaw-community/tree/main/examples/recipes/nvidia/memory-driven-chief-of-staff).
- **What it adds:** Structured Markdown knowledge, a separate judgment ledger, and user corrections that update a readable preference policy.
- **Reported evidence:** Table 1 compares the self model with agentic RAG using the same NVIDIA Nemotron 3 Ultra model: 90.9% versus 82.8% overall accuracy on **186 questions**, **+8.1 percentage points**. Changed-fact tracking is 100% versus 60%, but involves only **five questions**. Faithfulness declines from 100% to 92.3% on **13 questions**.
- **Evidence/status:** Article body and table read; recipe landing page inspected. Repetitions and confidence intervals were not established in this pass. The article explicitly describes invented sample entities and recorded decisions in its offline walkthrough; distinguish that walkthrough from benchmark measurements.
- **Discussion:** Our interpretation: aggregate memory gains can coexist with regressions. This is evidence about the evaluated memory configuration, not proof of indefinitely compounding improvement.

### Practitioner proposal: improving coding skills through experiments

- **Source/date:** Kirill Krainov, [Karpathy's Autoresearch: Improving Agentic Coding Skills](https://zerocopy.blog/2026/03/25/karpathys-autoresearch-improving-agentic-coding-skills/), March 25, 2026.
- **What it adds:** A proposed loop that edits a skill, repeats test cases, evaluates correctness/time/cost, and retains or reverts the change.
- **Evidence/status:** Article read. Its conclusion says initial results and a working version are future work; classify it as a design proposal, not an empirical success report.
- **Discussion:** Its additive scoring scheme invites a useful critique: can efficiency points compensate for correctness failures? Our interpretation: objective design deserves the same scrutiny as the agent's update mechanism.

## Additional social lead

[Karpathy post associated with LLM knowledge bases](https://x.com/karpathy/status/2039805659525644595): discovered through search, but direct access failed. Keep as a discovery lead, not verified evidence or a quotation. Its relevance is the transition from accumulated traces to maintained knowledge; inspect the original before using it in a slide.

## How this changes the presentation

Use autoresearch when defining the improvement boundary; use Hermes and LangChain when explaining retained procedural knowledge; use NVIDIA alongside academic evaluations when discussing measurements and regressions. Let papers, code, and practitioner experience answer the same topic questions rather than presenting a separate “social media” appendix.

For the final refresh, search X/Twitter and author/project blogs alongside paper indexes. Follow original posts to code, experiment logs, negative results, and technical explanations. Record post time, edits, release/commit identifiers where available, and what was actually inspected. Avoid counting an announcement, its blog, and its paper as three independent pieces of evidence. Direct X coverage in this pass was limited by retrieval failures; this is not a comprehensive review of recent threads.
