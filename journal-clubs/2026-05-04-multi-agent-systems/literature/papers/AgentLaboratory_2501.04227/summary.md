# Agent Laboratory: Using LLM Agents as Research Assistants

**Authors:** Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum
**arXiv:** 2501.04227
**Venue:** Preprint
**Date:** June 2025

## Problem
Machine-learning research is slow and labor intensive, and many promising ideas are never explored because researchers must spend substantial time on literature search, implementation, experiment execution, and writeup. The paper asks whether LLM agents can act as research assistants for human-provided ideas rather than trying to replace human ideation entirely.

## Method
Agent Laboratory is an open-source LLM-agent workflow with three phases: literature review, experimentation, and report writing. A PhD agent uses arXiv search and paper-reading actions to curate background work; PhD and Postdoc agents formulate a plan; ML/SW Engineer agents prepare data and run experiments through `mle-solver`, which iteratively edits, executes, scores, and reflects on ML code; and PhD/Professor agents use `paper-solver` to scaffold, edit, compile, review, and refine a LaTeX-style research report. The system can run autonomously after the initial idea or in co-pilot mode, where a human reviews outputs at subtask checkpoints and can request retries with guidance.

## Key Findings
- In autonomous evaluation across five ML topics and three backends, human reviewers rated o1-preview as most useful and best overall by NeurIPS-style scores, while o1-mini achieved the highest experimental-quality rating.
- Human reviewers gave generated autonomous papers much lower NeurIPS-style overall scores than automated reviewers, suggesting automated self-review overestimates paper quality.
- Co-pilot mode improved external NeurIPS-style overall scores over autonomous mode, but generated papers still remained below the average score reported for accepted NeurIPS 2024 papers.
- Runtime/cost measurements show a speed-cost-quality tradeoff: gpt-4o was fastest and cheapest, while o1-preview had the highest subtask success rate but much higher cost.
- On a 10-task low-complexity text/tabular subset of MLE-Bench, `mle-solver` submitted valid solutions for all tasks and earned more medals than the compared MLAB, OpenHands, and AIDE baselines in the paper's setup.
- Limitations include fixed workflow structure, dependence on LLM-based self-evaluation, occasional hallucinated experimental details, literature-review failures, token-limit issues, and safety concerns around generated code and research misuse.

## Tags
`LLM-agents`, `autonomous-research`, `research-assistant`, `human-AI-collaboration`, `automated-machine-learning`, `paper-generation`, `MLE-Bench`

## Connections
- Closely related to **AIScientist_2408.06292**: both automate parts of scientific discovery, but Agent Laboratory emphasizes human-provided ideas and a co-pilot mode rather than fully autonomous ideation.
- Relevant to multi-agent workflow papers because it decomposes research into specialized roles and tool-mediated phases rather than free-form agent discussion.
- Connects to automated ML-agent benchmarks such as MLE-Bench, MLAgentBench/MLAB, OpenHands, and AIDE through the isolated `mle-solver` comparison.
- Useful context for claims about automated reviewers: the paper finds a substantial gap between automated NeurIPS-style scores and human reviewer judgments.
