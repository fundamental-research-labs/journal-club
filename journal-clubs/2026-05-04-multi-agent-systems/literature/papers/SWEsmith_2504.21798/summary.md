# SWE-smith: Scaling Data for Software Engineering Agents

**Authors:** John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang
**arXiv:** 2504.21798
**Venue:** Preprint
**Date:** May 2025

## Problem
Open-source software engineering agents are bottlenecked by training data. Pull-request crawls lack reliable execution-based validation, while SWE-bench-style datasets provide testable tasks but are hard to scale because each task often requires costly environment work and storage.

## Method
SWE-smith inverts the SWE-bench collection order: first construct a reusable execution environment for a Python repository, then synthesize many task instances inside that environment. It uses SWE-agent-assisted setup, manual verification of install/test instructions, and four bug-generation families: LM generation (modify and rewrite), procedural AST edits, bug-patch combination, and PR mirroring. Candidate patches are kept only if they break existing passing tests, and issue descriptions are generated from the bug patch, failing test, and execution output.

## Key Findings
- SWE-smith creates 50,137 validated task instances from 128 real-world Python repositories, with shared repository environments rather than one Docker image per task.
- The dataset is substantially larger than earlier execution-backed SWE training sets while using 295 GB of environments; the paper estimates a SWE-bench-style approach at similar scale would require 50-150 TB.
- Fine-tuning Qwen 2.5 Coder Instruct 32B on 5,016 successful SWE-smith trajectories yields SWE-agent-LM-32B, which reaches 40.2% Pass@1 on SWE-bench Verified in the authors' single-attempt SWE-agent setup.
- Ablations find PR Mirror trajectories strongest, while LM Rewrite and Procedural Modification remain competitive; LM-generated issue text performs comparably to original PR issue text in the tested setup.
- More repository diversity improves general performance, and SymPy-specialized training improves target-repository performance with only small generalization loss in the paper's experiments.
- Failure analysis shows SWE-agent-LM-32B is efficient on solved tasks but often fails through localization stalls, repeated actions, or runtime/cost limits.

## Tags
`software-engineering-agents`, `synthetic-data`, `SWE-bench`, `SWE-agent`, `execution-validation`, `fine-tuning`, `open-weight-models`, `Python-repositories`

## Connections
- Extends the SWE-bench/SWE-agent line by focusing on scalable training data rather than only evaluation.
- Complements **SWEagent** and **OpenHands** by providing data and trajectories that can train agent backbones for existing SWE scaffolds.
- Related to **SWERL**, **R2E-Gym**, and **SWE-gym** as an open-weight SWE-agent training approach, but SWE-smith emphasizes synthetic, test-validated task generation across many repositories.
- Useful alongside **MultiSWEbench** and **SWEbenchGoesLive** for discussions of how SWE benchmarks scale across repositories, languages, and time.
- Relevant to **CAID** and **CooperBench** as background data infrastructure for stronger coding agents, though SWE-smith itself studies single-agent fine-tuning rather than multi-agent coordination.
