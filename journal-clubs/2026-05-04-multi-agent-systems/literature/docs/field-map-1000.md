# 1000-Paper Multi-Agent Field Map

Snapshot date: 2026-05-04

This is a field map, not a top-1000 ranking. The first 400 rows are the curated candidate universe from `docs/candidates.md`; rows 401-1000 are automatically expanded candidates from arXiv, OpenAlex, and local BibTeX snowballing. Generated rows are intended for mapping and triage before any top-100 promotion.

## Files

- `docs/field-map-1000.csv`: full 1000-row table for spreadsheet analysis.
- `docs/field-map-1000.yaml`: same entries plus generation metadata and stats.
- `scripts/build_field_map_1000.py`: regeneration script.

## Snapshot Stats

- Total entries: 1000
- Curated base entries: 400
- Auto-expanded entries: 600
- Recent entries from 2025-2026: 523

### By Sub-Area

| Sub-area | Count |
|---|---:|
| LLM Multi-Agent Frameworks and Coordination | 160 |
| MARL, Emergent Communication, and Social Behavior | 140 |
| Software, Web, and Computer-Use Agents | 140 |
| Benchmarks and Evaluation | 110 |
| Agent Foundations and Infrastructure | 100 |
| Safety, Security, and Reliability | 100 |
| Scientific and Domain Agents | 100 |
| Debate, Reasoning, and Aggregation | 90 |
| Surveys and Taxonomies | 41 |
| Classical MAS and Game-Theoretic Foundations | 19 |

### By Role

| Role | Count |
|---|---:|
| trend | 421 |
| bridge | 233 |
| core | 169 |
| anchor | 136 |
| survey | 41 |

### By Year Band

| Year band | Count |
|---|---:|
| 2025 | 293 |
| 2026 | 230 |
| 2024 | 206 |
| 2023 | 121 |
| pre-2020 | 88 |
| 2020-2022 | 62 |

### By Source Family

| Source family | Count |
|---|---:|
| curated-400 | 400 |
| arxiv | 304 |
| openalex | 281 |
| arxiv+openalex | 15 |

## Trend Readout

The 1000-paper map makes the current direction of the field easier to inspect:

- Recent growth is concentrated in `LLM Multi-Agent Frameworks and Coordination` and `Software, Web, and Computer-Use Agents` among the 2025-2026 entries.
- Multi-agent work is moving from static role-play/framework papers toward orchestration, topology search, scaling laws, verification, and failure attribution.
- Software, web, GUI, and computer-use agents form a major bridge lane: many papers are not multi-agent papers by title, but they define the environments where multi-agent systems are now being tested.
- Safety and reliability are no longer peripheral: prompt injection, tool misuse, cyber tasks, delegation failures, and benchmark validity now form a distinct research front.
- Scientific and domain-agent papers are expanding quickly, but the map keeps them separate from core MAS papers so application volume does not swamp architecture and evaluation work.
- MARL and emergent-communication anchors remain important as conceptual foundations, but they are capped to avoid lifetime-citation dominance over recent LLM-agent work.

## Regeneration

```bash
python3 scripts/build_field_map_1000.py
```

Use `--offline` only for parser/debug checks from the curated candidate list and local BibTeX references; it is not expected to reach 1000 rows without online sources. The online path uses public APIs and may change as arXiv/OpenAlex metadata updates.

## Provenance Notes

- `curated-400`: manually curated candidate list already in this repo.
- `auto-map:arxiv-query`: arXiv API query expansion.
- `auto-map:openalex-query`: OpenAlex Works API search expansion.
- `local-bib-auto`: paper discovered in checked-in BibTeX references.

## Source APIs

- arXiv API User's Manual: https://info.arxiv.org/help/api/user-manual.html
- OpenAlex API overview: https://developers.openalex.org/api-reference/introduction
- OpenAlex Works API: https://developers.openalex.org/api-reference/works

## Quality Caveats

- Rows 401-1000 are field-map candidates, not reviewed claims of importance.
- Query APIs can return false positives, especially for robotics, wireless, traffic, and generic agent-based modeling papers; relevance/confidence scores are triage aids.
- Citation counts come from OpenAlex when available and are intentionally not used as the sole ranking signal.
