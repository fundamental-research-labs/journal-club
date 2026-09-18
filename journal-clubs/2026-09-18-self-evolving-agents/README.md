# Self-evolving agents

**Session:** Friday, September 18, 2026  
**Research cutoff:** September 16, 2026  
**Presenter:** Robert Yang · Fundamental Research Labs

**Scope:** Topic-wide research for an audience familiar with LLM basics.

Central question: **How can agents turn experience into lasting improvements—and how can we tell whether those improvements generalize?**

## Start here

- **[Open the HTML presentation](slides/index.html)** — 24 talk slides plus 11 appendices, citations, and speaker notes. Opens directly in a browser; no install or network required.

- **[Central argument: what experience makes possible](analysis/thesis.md)** — a connected essay built around developed examples, grounded in continual/lifelong learning and meta-learning, drawing on 64 reviewed evidence families and citing 26 directly; the coverage audit preserves the broader evidence and counterarguments.
- **[Thesis coverage audit](research/thesis-coverage.md)** — before/after counts, claims, omissions, source roles, and search limits.
- [Claim ledger](analysis/claims.md) — evidence, confidence, and limits.
- **[Ranked shortlist: ten priority resources](research/shortlist.md)** — why each belongs, what to read, key results, limitations, and strong alternatives.
- **[Research landscape](research/landscape.md)** — mechanisms, competing evidence, and discussion questions organized around the topic.
- **[Source register](research/sources.md)** — 158 candidate/resource records with selection decisions, exact review depths, versions, and acquisition status; 63 substantive reading-note files.
- [Reading routes](reading-list.md) and [practitioner resources](practitioner-sources.md) — ways to navigate the corpus by interest.
- [Search and audit log](research/search-log.md), [originals guide](research/originals/README.md), and [research handoff](workflow.md) — provenance, checks, and remaining limits.

- **[Per-paper prominent citations](research/prominent-citations.md)** — 55 papers, 207 verified citation contexts, recurring-reference counts, and links from every reviewed paper note.

- **[Earlier recent-paper citation audit](research/citation-mining.md)** — seven seeds, parallel low-cost discovery, five newly read comparators, and retained top-ten decision.

The September 18 analysis rewrite organizes the thesis around when experience creates lasting value, with developed comparisons and explicit conditional synthesis. The [architecture review and resolution](analysis/architecture-review.md) records the changes. The current slides incorporate that conditional argument, the continual-learning/meta-learning foundations, and the first presentation-review revision.

## Selected supporting resources

The ranked ten are **WikiSkill; Rethinking the Evaluation of Harness Evolution for Agents; GEPA; SEAL; Hyperagents; AgentStream; R-Zero; HarnessDev; FinEvo-Bench; and Shopify's Sidekick continual-learning account**. They cover retained knowledge, prompt/harness evolution, weight adaptation, self-generated curricula, meta-improvement, longitudinal evaluation, and production practice. Papers are supporting examples for the field's questions, not ten separate talk sections.

Strong alternatives include **Dream-RSI, EvoHarnessBench, Library Drift, NemoClaw, ACE, HGM/DGM, Absolute Zero, Agent-World, and Reef**. September frontier coverage includes ScienceBuddy, MetaRSI, and the Economics of Recursive Self-Improvement, with explicit distinctions between controlled results, provisional claims, and theory. Social/talk leads with unverified provenance or inaccessible content are not used as empirical evidence.

## Repository and review notes

All reading-note filenames use `YYYY-short-title.md` in lowercase kebab-case, with the source publication year as the prefix. For SoL-Pi, `2026` identifies the reviewed repository snapshot year because first publication is unverified. Original-source folders use the same year-prefixed name as their reading notes, and retained filenames use `YYYY-short-title-artifact-version.ext`. Existing source keys are preserved; the source register maps them to the year-prefixed notes and originals. Canonical URLs, notes, and licensed originals are linked through the register. Original PDFs are unmodified; source-specific licenses and hashes are recorded. Temporary downloads, text extraction, and rendered inspection images remain outside this repository.

Research used the journal-club-research workflow; primary-source review depths and unresolved qualifications remain in the source records. No training experiments were reproduced. The September 18 presentation revision now has **24 main slides and 11 appendices**. It develops useful expertise, relevance and retention, then learned adaptation, and answers the lasting-value/cost question before discussion. The empirical research cutoff remains September 16; foundation review and presentation verification occurred September 18.

[AgentStream's method comparison](slides/index.html#slide-14) now complements its framework. [SEAL's mechanism](slides/index.html#slide-15), [adaptation result](slides/index.html#slide-16), and [retention test](slides/index.html#slide-17) form a developed example in the main talk. FinEvo includes the skill-only alternative and explicitly partial token costs. Hyperagents' separate continued-evolution endpoint and AgentStream's aggregate counts are in the appendix. R-Zero/Continual Internalization and Dream-RSI remain in the supporting research materials rather than compressed standalone slides.

All 35 slides were rendered and visually inspected; [the current review](slides/review.md) records the changes, checks, and remaining limits. The [storyboard](slides/storyboard.md) is the current sequence and concept-to-evidence map. Earlier review/workflow entries are historical and their slide numbers are superseded.

[Initial research notes](research-notes.md) remain as historical context; the current shortlist, landscape, and source notes supersede their earlier reading-status and numerical qualifications.

## Presentation use and editing

Open [slides/index.html](slides/index.html). Arrow keys or Space navigate; **N** opens notes, **O** opens the overview, and Home/End go to the first/last slide. The slide menu and buttons provide the same controls. URLs such as `index.html#slide-6` open a specific slide. **All slides** provides a continuous reading view; browser printing uses one slide per page. Speaker notes are for on-screen use and are excluded from printing.

The default scope is approximately 30–35 minutes plus discussion for an audience familiar with LLM basics. Edit [content.json](slides/content.json) for presenter/company metadata, copy, source-figure metadata, citations, and speaker notes; edit [theme.css](slides/theme.css) for the visual theme and [build.py](slides/build.py) for markup, base layout, and navigation. The build embeds the theme and original-source PNG excerpts so the delivered HTML remains standalone. Source extraction is optional; its command and PyMuPDF dependency are recorded in [figure provenance](slides/figures/provenance.md). Rebuild from the repository root with Python 3 (standard library only):

```sh
python3 journal-clubs/2026-09-18-self-evolving-agents/slides/build.py
```

[Storyboard and claim mapping](slides/storyboard.md) · [Figure provenance](slides/figures/provenance.md) · [Visual and factual review](slides/review.md).

The presentation skill now defaults to HTML. PowerPoint and PDF are not deliverables for this session.

Source artwork is preserved. Guided FinEvo and Hyperagents crops, AgentStream’s original method table, and SEAL’s retention heatmap have exact crop/version records in the current figure provenance.
