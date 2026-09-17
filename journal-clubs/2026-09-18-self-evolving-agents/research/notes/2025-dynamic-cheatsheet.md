# Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory

## Source and access

Key: `2025-dynamic-cheatsheet`. Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou. [Primary v1](https://arxiv.org/abs/2504.07952v1), April 10, 2025, preprint. Read September 16, 2026: §§2.1–2.3 methods/baselines, §3 evaluation setup, §§4.5–5 model dependence and limitations, and selected citation contexts. This is a bounded mechanism review, not a new numerical results audit. [Original PDF](../originals/2025-dynamic-cheatsheet/2025-dynamic-cheatsheet-paper-v1.pdf), unmodified, CC BY 4.0 per the canonical record; [manifest](../originals/manifest.json).

## Question and methods

Can a black-box model preserve reusable problem-solving guidance across queries without weight updates? DC-Cu generates an answer using the current cheatsheet, then curates memory using the query and answer. DC-RS retrieves similar previous query/output pairs, synthesizes memory before answering, and uses that guidance for the new query (§§2.1–2.2). The curator does not receive ground-truth labels. The paper separates a no-memory prompting control, full-history appending, and retrieval without curation (§2.3).

## Results and evidence

The evaluation uses reasoning tasks including AIME, Game of 24 and domain question answering (§3). §§4.5–5 report model-dependent benefits and regressions, plus errors caused by poor retrieval and truncated memory rewriting. No headline aggregate or superiority claim is imported into the thesis; the verified contribution here is the generator/curator and retrieval/synthesis mechanism. No experiments reproduced.

## Appraisal and limitations

ACE explicitly identifies Dynamic Cheatsheet as architectural inspiration and an online comparator (ACE v3 §3/Figure 4, §4.2). That is why it belongs in the explanation of ACE. Self-curated guidance can preserve useful strategies or amplify wrong ones; task similarity, order and base-model competence affect utility (§§4.5–5). The paper's finite reasoning streams do not establish long-term task-agent durability or total-cost superiority.

## Discussion and follow-up

Does itemized updating preserve useful knowledge better than regenerating a cheatsheet when the incoming task domain changes? Separate the curation, retrieval and update-representation contributions under matched resources.

[Prominent citations and their roles](../prominent-citations.md#2025-dynamic-cheatsheet)
