# Self-evolving agents: topic map and initial evidence

**Update:** Start with the [September 16 research landscape](research/landscape.md) and [detailed source notes](research/sources.md). They add newer sources and deepen the initial readings below, including WikiSkill's splits/statistical procedure, Hyperagents' qualified transfer evidence, and the current MetaRSI version. These initial notes are preserved as context.

Prepared September 16, 2026 for September 18. These notes synthesize selected primary-source sections; the [reading list](reading-list.md) records review depth and versions. Reported results below are authors' results, not independent replications.

## 1. Define the system boundary first

Working definition for discussion: a self-evolving agent uses experience and feedback to make retained changes that affect later behavior. Specify **what changes, when it changes, who proposes the change, and who evaluates it**. Model parameters, memory, tools, and architecture are distinct adaptation targets in the broad [Gao et al. survey](https://arxiv.org/abs/2507.21046).

For this talk, distinguish three questions:

1. Can the system improve an answer during one task?
2. Can it retain an update that helps future tasks?
3. Can it improve the procedure that generates future updates?

This is our explanatory structure, not a universal taxonomy. The September [Duan et al. preprint](https://arxiv.org/html/2609.11873v1) offers a more detailed autonomy framework, spanning execution, strategy, experience acquisition, deployment adaptation, and meta-improvement (Figure 1 and §3). Its title and roadmap should not be interpreted as experimental proof of unrestricted recursive improvement.

## 2. Map the whole topic by what changes

| Update target | Concrete question for the audience | Supporting reading |
| --- | --- | --- |
| Prompts and context | Can failed trajectories become better instructions? | GEPA; AgentStream's context branch |
| Memory | What experience should be stored, retrieved, revised, or forgotten? | SelfMem; AgentStream |
| Skills and tools | Can experience become reusable procedures? | WikiSkill; Voyager as background |
| Agent code and workflows | Can an agent change its control logic and tool interfaces? | Recent harness-evaluation study; DGM/SICA as background |
| Model parameters and training data | When should experience be internalized through training? | MetaRSI; Self-Adapting Language Models as background |
| Learning process and curriculum | Can the system choose better updates, experiments, or future practice? | Hyperagents; MetaRSI; September autonomy survey |
| Collaboration structure | Can the organization of multiple agents adapt? | Broad survey; coding survey's workflow/topology category |

The taxonomy is a synthesis; rows overlap. The [August coding survey](https://arxiv.org/html/2608.03392v1) explicitly separates framework, memory, skills/tools, model, and workflow/topology evolution (§3). “Evolution” also need not imply a biological genetic algorithm.

## 3. Explain the shared loop

Include examples from [practitioner sources](practitioner-sources.md) throughout this discussion. The [autoresearch repository](https://github.com/karpathy/autoresearch) provides an accessible experiment-loop example; [Hermes documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) provides a practical skill-lifecycle example. Distinguish documented behavior from demonstrated gains, and identify the human-maintained parts of each system.

Our schematic: **execute → collect feedback → propose a change → evaluate → retain or reject → try later tasks**. Describe both the editable state and the fixed infrastructure. Ask whether learning happens offline, between tasks, or during deployment, and whether feedback comes from tests, humans, another model, or the environment.

**Recent example—knowledge and skills.** WikiSkill separates execution traces, a persistent wiki, and executable skills. Its method validates proposed skills and rolls back rejected skill edits while retaining the wiki (§§2–3). Across five benchmarks and five models, Table 1 averages three independent evolution runs. For Qwen-3.5-9B, average test performance is 47.4 versus 29.9 without skills: **+17.5 percentage points**, not a 17.5% relative gain. Some settings regress: Qwen-3.5-4B on OfficeQA scores 28.5 versus 30.2 without skills. [WikiSkill, §§3–4, Table 1](https://arxiv.org/html/2608.27454v1).

Our interpretation: separated state and validation make the mechanism inspectable. Aggregate gains do not establish universal benefit. Full skill injection into the inference prompt also leaves practical skill retrieval as a separate question. The paper reports bootstrap testing; confidence intervals and dataset sample sizes should be extracted from the appendices before preparing result slides.

**Recent example—changing the improver.** Hyperagents makes the task agent and meta agent parts of one editable program, including the procedure that generates modifications. Its introduction describes coding, paper review, robotics reward design, and math-solution grading experiments. This broadens the question beyond coding-agent optimization. [Hyperagents, §1](https://arxiv.org/html/2603.19461v1).

Our interpretation: permission to edit the improvement mechanism is an architectural property. Demonstrating sustained acceleration requires additional empirical evidence; detailed results have not yet been audited here.

**September frontier—composing update types.** MetaRSI organizes changes to data, harness, and model state, with scheduling across operators. Its methodology places the sealed evaluator and release rules outside those writable surfaces (§4). [MetaRSI v1, §§4.1–4.4](https://arxiv.org/html/2609.06396v1).

Our interpretation: this is a useful example for asking how a system decides *where* to learn and what remains externally fixed. Treat it as a new proposal whose quantitative evidence still needs close review.

## 4. Make evaluation a central theme

The September [NVIDIA technical writeup](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/) adds a non-paper measurement example; the [practitioner notes](practitioner-sources.md) record its sample sizes and regressions. Apply the same scrutiny to experiments regardless of publication venue.

**Does evolution beat spending the same budget differently?** The July harness-evaluation study compares methods on 89 Terminal-Bench 2.1 tasks, with three models and two independent runs. In its no-unit-test setting, Table 1 reports average pass@1 of **67.4 for harness evolution versus 72.3 for parallel sampling**, a **4.9-point gap**. The setup uses a common initial harness and a five-rollout budget. [Wang et al., §§3–4.2, Table 1](https://arxiv.org/html/2607.12227v1).

Our interpretation: matched baselines and held-out tasks are essential. This study tests a particular implementation and benchmark; it does not establish that all self-evolution fails. Rollout matching also deserves scrutiny against total token, latency, and monetary costs. Two runs provide limited evidence about variability; no confidence interval is supplied here.

**Does retained experience help in a changing task stream?** AgentStream tests five methods, three models, and isolated, sequential, and interleaved scenarios. Its setup samples 50 tasks from each of six benchmarks (300 distinct tasks), with three task-order seeds. It covers context, memory, skills, and an integrated harness. The authors report that no single method dominates across models and scenarios. [AgentStream, §§3–5](https://arxiv.org/html/2608.00155v1).

Our interpretation: this is a better question for deployment than simply comparing one initial score with one final score. Ordering, interference, retention, and cost matter. Three shuffled streams reuse the same task set; they are not 900 independent tasks. Detailed effect sizes and uncertainty remain to be extracted before quoting individual comparisons.

Suggested evaluation questions for every example:

- Are proposal, validation, and final test tasks separated?
- Is the frozen-agent control given comparable tools, feedback, and compute?
- Does an update help on new tasks, models, domains, or later time periods?
- What regresses, and can the system detect and reverse it?
- Is the evaluator independent of the state being modified?
- Does the gain justify the full cost of learning and subsequent execution?

## 5. Use older work to explain the trajectory

DGM illustrates agent-code search with frozen foundation models and an archive of variants. Its original SWE-bench headline concerns a subset, and its outer exploration mechanism remains fixed (§§3–4). SICA illustrates self-editing with performance, time, and cost in the utility. Its Table 1 reports SWE-bench subset scores of 17% initially, a best 53% at iteration 14, and 51% at iteration 15; §4 specifies 50 SWE-bench questions. [DGM v1](https://arxiv.org/html/2505.22954v1), [SICA v1](https://arxiv.org/html/2504.15228v1).

Our interpretation: these are useful historical demonstrations, but they should occupy a small part of the session. The current story includes persistent skills, meta-level changes, and stronger evaluation questions across domains.

## 6. Discussion questions and remaining preparation

1. What is the smallest retained change we would count as learning?
2. When are prompts or skills sufficient, and when are weight updates needed?
3. Which evidence would distinguish reusable improvement from benchmark adaptation?
4. Should failed proposals still update memory? How could incorrect lessons accumulate?
5. If an agent changes its own evaluator, what external measurement remains trustworthy?
6. What experiment would demonstrate improvement of the learning process rather than just improved task scores?

For the presentation, choose examples across mechanisms and pair positive evidence with evaluation critiques. Read the newest source versions, audit the result appendices selected for slides, and refresh September additions. This initial pass has not reproduced experiments or completed full-text review of every reading-list entry.
