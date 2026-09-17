# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

## Source and access

Key: `2026-skillsbench`. Xiangyi Li et al. [Primary v4](https://arxiv.org/html/2602.12670v4); [register](../sources.md#2026-skillsbench). First submitted February 13, 2026; v4 June 14; companion release 1.1 June 16. Preprint record; venue not independently checked. Read September 16: full v4 PDF screening, methods/results and relevant appendices; coordinator reopened current HTML Table 2, §5.1 and Appendix D.6. [Retained CC BY 4.0 original](../originals/2026-skillsbench/2026-skillsbench-paper-v4.pdf). [Version and evidence audit](../workers/thesis-additions-screening.md).

## Question and methods

Does an agent benefit from curated procedure, and can it author an effective substitute? V4 uses 87 containerized tasks in eight domains, 18 model–harness configurations and three trials per condition/task. The matched main frame has 9,396 selected public result files (18×87×2×3), not independent tasks. The self-generated diagnostic covers only three dedicated harness configurations. Deterministic verifiers, task-level pairing and released traces are strengths.

## Results and evidence

Table 2: configuration-macro mean pass rate rises from 33.9% to 50.5% with curated skills (+16.6 percentage points). Thirteen of 87 tasks have negative deltas. Table 6/Appendix D.6: self-generated skills fall below no-skills by 8.1, 11.3 and 11.5 points in the three configurations; curated skills add 18.2–24.8 points there. Three trials per cell do not establish independent authoring-run uncertainty or long-term learning.

## Appraisal and limitations

The authors' results support a curated-skill counterfactual, not a universal effect of instructions. Skill packs contain scripts/assets as well as prose; there is no length-matched irrelevant-context or retrieval-only control. Task construction filters out low-signal submissions without measurable separation, potentially enriching skill-sensitive tasks. Human curation effort is not matched to automated authoring. The Claude self-generation arm changes effort and shares creator/solver sandbox state; Codex/Gemini reuse one authored pack across trials. One-shot generation lacks iterative feedback. This comparison therefore cannot establish that continual skill learning fails. No experiment reproduced.

## Discussion and follow-up

Compare a continual learner with curated skills at matched lifetime cost, including authoring and selection. Check both weak procedures that can be improved and strong procedures that learning might damage. Earlier worker statistics from an obsolete 84-task snapshot are superseded; do not mix those numbers with v4.
