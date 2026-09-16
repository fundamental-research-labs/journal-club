# GAIA: A Benchmark for General AI Assistants

**Authors:** Gregoire Mialon, Clementine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom
**arXiv:** 2311.12983
**Venue:** Preprint
**Date:** November 2023

## Problem
LLM benchmarks were rapidly saturating, while many existing evaluations either targeted expert exams, closed environments, multiple-choice formats, or open-ended generation that required expensive human/model judging. GAIA asks whether assistants can solve conceptually simple real-world tasks that average humans can verify, but that require robust execution across browsing, reasoning, multimodal inputs, files, code, and other tools.

## Method
GAIA contains 466 human-crafted questions with short, unambiguous answers. Questions are designed around real sources of truth, sometimes include attached files, and are validated by independent annotators to reduce ambiguity. The benchmark uses quasi-exact matching on factoid answers, splits difficulty into three levels based on annotator steps and tools, and releases 166 annotated developer questions while withholding answers for 300 leaderboard questions.

## Key Findings
- Human annotators score about 92% overall, while GPT-4 with manually selected plugins is reported around 15% overall and reaches 0% on Level 3.
- Table 4 shows a large gap at every level: humans score 93.9%, 91.8%, and 87.3% on Levels 1-3, while GPT-4 with plugins scores 30.3%, 9.7%, and 0%.
- Web browsing is the dominant annotated capability, but the benchmark also includes coding, multimodality, and diverse filetype reading.
- Tool augmentation helps GPT-4 relative to non-tool baselines, but the paper treats GPT-4 plus plugins as an oracle-like and not exactly reproducible setup because plugins were manually selected and unstable.
- The authors argue that GAIA is intentionally different from harder-for-humans benchmarks: solving it requires human-like robustness on simple but open-world tasks, not specialized expert knowledge.

## Tags
`agent-benchmark`, `general-ai-assistants`, `tool-use`, `web-browsing`, `multimodal-reasoning`, `file-reading`, `exact-match-evaluation`, `leaderboard`

## Connections
- Related to tool-use and agent benchmarks such as AgentBench, ToolQA, APIBench, API-Bank, OpenAGI, and Gorilla, but GAIA emphasizes open-world tasks rather than fixed APIs or closed environments.
- Useful baseline context for later web-agent, computer-use, and general-assistant evaluations that separate easy-to-verify final answers from hard-to-execute task trajectories.
- Complements benchmark-contamination discussions because its questions are designed so answers are not plainly available in pretraining text, though the authors still expect maintenance over time.
