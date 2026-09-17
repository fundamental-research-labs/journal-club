# A Self-Improving Coding Agent (SICA)

## Source and access

Key: `2025-self-improving-coding-agent`. Maxime Robeyns, Martin Szummer, Laurence Aitchison. [Primary v2](https://arxiv.org/abs/2504.15228v2), May 16, 2025; first April 21, 2025. Read September 16, 2026: §3/Algorithm 1, §§5.1–6 and selected citation contexts. This is a mechanism/limitations review; no new numerical performance claim is used. [Retained unmodified PDF](../originals/2025-self-improving-coding-agent/2025-self-improving-coding-agent-paper-v2.pdf), CC BY 4.0 per canonical metadata; [manifest](../originals/manifest.json).

## Question and methods

Can a coding agent edit its own implementation to improve a benchmark utility? SICA retains an archive of agents and scores, selects the best-scoring agent as the next meta-agent and base agent, lets it inspect the archive and propose an edit, then evaluates and archives the child (§3/Algorithm 1). The parent-selection policy follows the current best; retaining an archive is not the same as exploring its lower-scoring lineages.

## Results and evidence

DGM identifies SICA as its close concurrent comparator (§2). The verified comparison here is architectural: best-agent expansion versus DGM's broader archive sampling for stepping stones. SICA's own benchmark performance is not re-estimated or compared numerically across papers. No experiments reproduced.

## Appraisal and limitations

Early ideas can anchor subsequent proposals; static benchmarks may saturate; time/cost caps influence utility (§§5.1–5.2). Scaffold and prompt edits do not modify model weights. This source prevents misattributing all self-editing or archived search to DGM. It does not demonstrate unbounded or cost-normalized acceleration.

## Discussion and follow-up

With identical proposal and evaluation budgets, does expanding lower-scoring archive members produce discoveries that greedy best-parent search misses?

[Prominent citations and their roles](../prominent-citations.md#2025-self-improving-coding-agent)
