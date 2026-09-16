# Field Map 50-Paper Subagent Review Audit

Date: 2026-05-04

This audit samples 50 entries from the auto-expanded part of `docs/field-map-1000.md` and reviews them with `docs/review-rubric.md`.

Unlike `docs/sample-50-review-audit.md`, this audit was reviewed by subagents. Five independent reviewer agents each handled a disjoint batch of 10 papers, inspected the field-map row plus available primary sources such as arXiv pages, DOI pages, publisher records, PDFs, project pages, and code links, then returned rubric scores and a keep/watch/cut recommendation.

## Sampling Protocol

- Sampling frame: rows 401-1000 from `docs/field-map-1000.json`.
- Rationale: these are the auto-expanded field-map entries, not the curated first 400.
- Sampling method: deterministic stratified sample, 5 papers from each of the 10 sub-areas.
- Random seed: `2026-05-04-field-map-rank401-1000-50-review-v1`.
- Local overlap: none of the sampled papers had a matching folder in `papers/`.
- Review design: one independent subagent review per sampled paper. This is a source-backed triage pass, not a multi-reviewer stability check per paper.

Criterion abbreviations: `N` novelty, `S` significance, `R` rigor, `B` breadth, `M` multi-agent specificity, `Rep` reproducibility, `C` clarity, `U` usefulness.

## Aggregate Finding

The auto-expanded field map is much noisier than the maintained local `papers/` corpus. It contains many useful candidates, but also several sub-area mismatches, non-MAS bridge papers, thin demos, weak surveys, and classical-MAS false positives.

| Band | Overall score | Count | Share | Interpretation |
|---|---:|---:|---:|---|
| Strong keep | 8 | 4 | 8% | High-priority follow-up candidates |
| Keep | 7 | 16 | 32% | Useful and mostly convincing |
| Useful but limited | 6 | 12 | 24% | Keep or watch depending on role fit |
| Borderline | 5 | 10 | 20% | Needs cleanup, corrected role, or stronger evidence |
| Weak / cut-grade | 1-4 | 8 | 16% | Likely remove from quality-focused candidate set |

Mean overall score: 5.86.

Reviewer recommendations:

| Recommendation | Count | Share |
|---|---:|---:|
| Keep | 26 | 52% |
| Watch | 16 | 32% |
| Cut | 8 | 16% |

By sub-area:

| Sub-area | Avg. overall | Keep | Watch | Cut | Read |
|---|---:|---:|---:|---:|---|
| Benchmarks and Evaluation | 7.0 | 4 | 1 | 0 | Strongest slice; several real MAS evaluation papers |
| Safety, Security, and Reliability | 6.4 | 3 | 2 | 0 | Timely but preprint-heavy |
| MARL, Emergent Communication, and Social Behavior | 6.4 | 4 | 1 | 0 | Mostly legitimate anchors/trend papers |
| Debate, Reasoning, and Aggregation | 6.2 | 2 | 2 | 1 | Some strong debate/safety papers, some misfiled |
| Scientific and Domain Agents | 6.0 | 4 | 0 | 1 | Useful domain systems; reproducibility uneven |
| Agent Foundations and Infrastructure | 5.8 | 2 | 2 | 1 | Good routing/allocation papers plus weak memory/HCI fits |
| Software, Web, and Computer-Use Agents | 5.8 | 3 | 1 | 1 | Mix of strong domain benchmarks and thin code-agent proposals |
| Surveys and Taxonomies | 5.4 | 1 | 3 | 1 | Several role/sub-area errors |
| LLM Multi-Agent Frameworks and Coordination | 5.0 | 2 | 2 | 1 | Many application demos, few rigorous core MAS papers |
| Classical MAS and Game-Theoretic Foundations | 4.6 | 1 | 2 | 2 | Noisy tail; several weak historical false positives |

## Score Table

| Rank | Paper | Sub-area | N | S | R | B | M | Rep | C | U | Overall | Conf. | Rec. |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 412 | MatPilot | LLM frameworks | 3 | 3 | 2 | 2 | 3 | 1 | 3 | 3 | 5 | 3 | Watch |
| 414 | Thematic-LM | LLM frameworks | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | 6 | 4 | Keep |
| 468 | MageSQL demo | LLM frameworks | 2 | 2 | 2 | 1 | 3 | 2 | 3 | 3 | 4 | 3 | Cut |
| 478 | Concrete design MAS | LLM frameworks | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | Watch |
| 479 | AutoPatch | LLM frameworks | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 4 | 6 | 3 | Keep |
| 501 | iMAD | Debate/reasoning | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 8 | 5 | Keep |
| 517 | PRefLexOR | Debate/reasoning | 4 | 3 | 3 | 2 | 1 | 3 | 3 | 3 | 5 | 4 | Cut |
| 520 | Hive | Debate/reasoning | 4 | 4 | 3 | 2 | 4 | 2 | 4 | 4 | 6 | 3 | Watch |
| 521 | Sponge Tool Attack | Debate/reasoning | 4 | 4 | 4 | 5 | 3 | 2 | 4 | 4 | 7 | 4 | Keep |
| 536 | ROSClaw | Debate/reasoning | 3 | 3 | 2 | 2 | 4 | 3 | 3 | 3 | 5 | 3 | Watch |
| 557 | GraphPlanner | Agent foundations | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 8 | 4 | Keep |
| 580 | Associative Memory Fields | Agent foundations | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 3 | 4 | Cut |
| 592 | Strategy Auctions | Agent foundations | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 5 | 8 | 4 | Keep |
| 597 | Diverse Knowledge Sources | Agent foundations | 3 | 3 | 4 | 2 | 1 | 3 | 4 | 3 | 5 | 4 | Watch |
| 602 | AwesomeLit | Agent foundations | 3 | 3 | 3 | 2 | 2 | 2 | 4 | 4 | 5 | 4 | Watch |
| 606 | Learning to Deliberate | Benchmarks/evaluation | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 7 | 4 | Keep |
| 607 | Beyond Arrow | Benchmarks/evaluation | 4 | 4 | 3 | 2 | 5 | 3 | 3 | 3 | 6 | 3 | Watch |
| 623 | MAD Tabular Anomaly | Benchmarks/evaluation | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 7 | 4 | Keep |
| 635 | Small Agents Collaborate | Benchmarks/evaluation | 4 | 4 | 4 | 3 | 5 | 3 | 4 | 5 | 8 | 4 | Keep |
| 665 | Xolver | Benchmarks/evaluation | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 7 | 4 | Keep |
| 672 | Agentic TDD QA for 6G | Software/web/computer-use | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | 5 | 4 | Watch |
| 687 | CODMAS | Software/web/computer-use | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 7 | 4 | Keep |
| 693 | FunReason-MT | Software/web/computer-use | 4 | 4 | 4 | 4 | 2 | 5 | 4 | 4 | 7 | 4 | Keep |
| 700 | TDD Governance | Software/web/computer-use | 2 | 3 | 1 | 1 | 2 | 3 | 3 | 3 | 3 | 4 | Cut |
| 727 | GUI-CEval | Software/web/computer-use | 4 | 4 | 4 | 4 | 2 | 3 | 4 | 5 | 7 | 4 | Keep |
| 756 | ColaCare | Scientific/domain | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 7 | 4 | Keep |
| 783 | HTP Drawing Assessment | Scientific/domain | 2 | 2 | 1 | 2 | 2 | 1 | 3 | 2 | 3 | 3 | Cut |
| 784 | LungNoduleAgent | Scientific/domain | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 7 | 4 | Keep |
| 788 | SciAgents | Scientific/domain | 4 | 5 | 3 | 3 | 4 | 4 | 4 | 4 | 7 | 4 | Keep |
| 813 | Agentic Metamaterial Design | Scientific/domain | 3 | 4 | 3 | 2 | 3 | 3 | 4 | 4 | 6 | 4 | Keep |
| 828 | CAAF / Harness as Asset | Safety/security | 4 | 4 | 3 | 2 | 3 | 4 | 4 | 4 | 6 | 4 | Watch |
| 832 | More at Stake | Safety/security | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 6 | 4 | Keep |
| 856 | Consensus Trap | Safety/security | 4 | 4 | 3 | 4 | 5 | 2 | 4 | 4 | 7 | 4 | Keep |
| 867 | IoT Security Patterns | Safety/security | 3 | 3 | 3 | 3 | 3 | 2 | 4 | 4 | 6 | 3 | Watch |
| 868 | Agent4Decompile | Safety/security | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 5 | 7 | 3 | Keep |
| 891 | CollabUIAgents | MARL/emergent/social | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 7 | 4 | Keep |
| 909 | Networked MARL + Emergent Comm | MARL/emergent/social | 4 | 3 | 3 | 2 | 5 | 2 | 4 | 3 | 6 | 4 | Keep |
| 913 | Evolving Intrinsic Motivations | MARL/emergent/social | 4 | 4 | 4 | 3 | 5 | 2 | 4 | 3 | 7 | 4 | Keep |
| 936 | Suggestion Sharing MARL | MARL/emergent/social | 4 | 4 | 4 | 3 | 5 | 3 | 4 | 4 | 7 | 4 | Keep |
| 941 | Structured State Abstraction | MARL/emergent/social | 3 | 3 | 3 | 2 | 4 | 2 | 3 | 3 | 5 | 4 | Watch |
| 977 | Coding Agents survey | Surveys/taxonomies | 3 | 4 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 3 | Watch |
| 985 | Agentic AI in Remote Sensing | Surveys/taxonomies | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 6 | 4 | Keep |
| 988 | OmniScientist | Surveys/taxonomies | 4 | 4 | 3 | 3 | 4 | 2 | 3 | 4 | 6 | 4 | Watch |
| 990 | Zodiac | Surveys/taxonomies | 3 | 4 | 3 | 2 | 4 | 2 | 3 | 4 | 6 | 4 | Watch |
| 992 | Dec-POMDP information gathering | Classical MAS | 4 | 4 | 4 | 3 | 5 | 3 | 4 | 3 | 7 | 4 | Keep |
| 994 | LLM negotiator agents | Classical MAS | 3 | 3 | 2 | 2 | 4 | 2 | 3 | 3 | 5 | 3 | Watch |
| 995 | JADE large data exchange | Classical MAS | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 4 | 4 | Cut |
| 996 | Timed-Arc Petri-Nets comms | Classical MAS | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 5 | 4 | Watch |
| 998 | Rotating machinery MAS comms | Classical MAS | 2 | 2 | 1 | 1 | 3 | 1 | 2 | 2 | 2 | 4 | Cut |
| 1000 | GenAI software practices | Surveys/taxonomies | 2 | 3 | 2 | 3 | 2 | 1 | 3 | 3 | 4 | 4 | Cut |

## High-Priority Follow-Up Candidates

These are the strongest sampled candidates for deeper review or promotion consideration:

- `#501` iMAD: selective multi-agent debate with cost, ablations, baselines, prompts, and code.
- `#557` GraphPlanner: graph-memory routing for agentic workflows with broad task/model coverage and cost analysis.
- `#592` Strategy Auctions: explicit small-agent allocation mechanism with strong multi-agent specificity.
- `#635` Can Small Agents Collaborate to Beat a Single Large Language Model?: clean study of orchestration and structured memory against model scale.
- `#687` CODMAS: structured RTL optimization with real domain metrics and ablations.
- `#756` ColaCare: EHR modeling with multi-agent collaboration, ablations, agent-count sensitivity, and cost reporting.
- `#784` LungNoduleAgent: collaborative diagnostic system with public/private datasets, ablations, GraphRAG, and code link.
- `#788` SciAgents: important scientific-discovery MAS with graph reasoning and open code.
- `#856` Consensus Trap: multi-agent failure/malicious-majority mitigation with strong MAS specificity.
- `#891` CollabUIAgents: language multi-agent RL with credit re-assignment, UI-agent evaluation, and code.
- `#936` Suggestion Sharing MARL: strong collective-welfare MARL paper with theory and social-dilemma experiments.
- `#992` Information Gathering in Decentralized POMDPs: legitimate classical MAS anchor.

## Cut / Cleanup Candidates

Reviewer-recommended cuts:

- `#468` MageSQL demo: useful demo, too thin empirically for a core MAS slot.
- `#517` PRefLexOR: good reasoning paper, but not meaningfully multi-agent.
- `#580` Associative Memory Fields: tiny probe set; too weak as a research-quality MAS entry.
- `#700` TDD Governance: mostly architecture/prompt proposal with very thin evidence.
- `#783` HTP Drawing Assessment: clinical/multi-agent claims not supported strongly enough.
- `#995` JADE large data exchange: dated engineering paper, weak as a modern foundation.
- `#998` Rotating machinery MAS comms: weak evidence and poor fit.
- `#1000` GenAI software practices: broad software-practices overview, not a rigorous MAS survey.

Role/sub-area corrections to consider:

- `#517` PRefLexOR: not multi-agent; remove or reclassify outside MAS.
- `#521` Sponge Tool Attack: better under Safety/Security than Debate.
- `#536` ROSClaw: better under robotics/infrastructure than Debate.
- `#597` Diverse Knowledge Sources: single-agent/cognitive-architecture bridge, not MAS.
- `#693` FunReason-MT: tool-use data synthesis/infrastructure, not core MAS.
- `#727` GUI-CEval: benchmark for GUI agents, not a MAS method.
- `#988` OmniScientist: system/framework paper, not a survey.
- `#990` Zodiac: diagnostic framework, not a survey.
- `#1000` Generative AI and Software Development Practices: broad software overview, not a MAS survey.

## Takeaways

- The auto-expanded rows are useful for discovery but should not be treated as candidate-quality by default.
- About half of the sample is worth keeping (`26/50`), but only `20/50` scored 7 or higher.
- The top failure modes are sub-area misclassification, weak multi-agent specificity, demo-level evaluation, and poor reproducibility.
- Recent papers with deterministic validators, cost reporting, code releases, and clean single-agent/multi-agent controls stand out sharply from generic "multi-agent framework" papers.
- The classical and survey tails need cleanup; query expansion is pulling in papers that mention agents or communication but are not strong foundations for LLM-based MAS.
