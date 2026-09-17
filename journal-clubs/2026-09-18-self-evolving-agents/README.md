# Self-evolving agents

**Session:** Friday, September 18, 2026  
**Research cutoff:** September 16, 2026  
**Presenter:** Robert Yang · Fundamental Research Labs

**Scope:** Topic-wide research for an audience familiar with LLM basics.

Central question: **How can agents turn experience into lasting improvements—and how can we tell whether those improvements generalize?**

## Start here

- **[Open the HTML presentation](slides/index.html)** — 15 talk slides plus 3 appendices, citations, and speaker notes. Opens directly in a browser; no install or network required.

- **[Central argument: what experience makes possible](analysis/thesis.md)** — a connected essay built around developed examples, drawing on 56 reviewed evidence families and citing 22 directly; the coverage audit preserves the broader evidence and counterarguments.
- **[Thesis coverage audit](research/thesis-coverage.md)** — before/after counts, claims, omissions, source roles, and search limits.
- [Claim ledger](analysis/claims.md) — evidence, confidence, and limits.
- **[Ranked shortlist: ten priority resources](research/shortlist.md)** — why each belongs, what to read, key results, limitations, and strong alternatives.
- **[Research landscape](research/landscape.md)** — mechanisms, competing evidence, and discussion questions organized around the topic.
- **[Source register](research/sources.md)** — 153 candidate/resource records with selection decisions, exact review depths, versions, and acquisition status; 55 substantive reading-note files.
- [Reading routes](reading-list.md) and [practitioner resources](practitioner-sources.md) — ways to navigate the corpus by interest.
- [Search and audit log](research/search-log.md), [originals guide](research/originals/README.md), and [research handoff](workflow.md) — provenance, checks, and remaining limits.

- **[Recent-paper citation audit](research/citation-mining.md)** — seven seeds, parallel low-cost discovery, five newly read comparators, and retained top-ten decision.

## Selected supporting resources

The ranked ten are **WikiSkill; Rethinking the Evaluation of Harness Evolution for Agents; GEPA; SEAL; Hyperagents; AgentStream; R-Zero; HarnessDev; FinEvo-Bench; and Shopify's Sidekick continual-learning account**. They cover retained knowledge, prompt/harness evolution, weight adaptation, self-generated curricula, meta-improvement, longitudinal evaluation, and production practice. Papers are supporting examples for the field's questions, not ten separate talk sections.

Strong alternatives include **Dream-RSI, EvoHarnessBench, Library Drift, NemoClaw, ACE, HGM/DGM, Absolute Zero, Agent-World, and Reef**. September frontier coverage includes ScienceBuddy, MetaRSI, and the Economics of Recursive Self-Improvement, with explicit distinctions between controlled results, provisional claims, and theory. Social/talk leads with unverified provenance or inaccessible content are not used as empirical evidence.

## Repository and review notes

All reading-note filenames use `YYYY-short-title.md` in lowercase kebab-case, with the source publication year as the prefix. For SoL-Pi, `2026` identifies the reviewed repository snapshot year because first publication is unverified. Original-source folders use the same year-prefixed name as their reading notes, and retained filenames use `YYYY-short-title-artifact-version.ext`. Existing source keys are preserved; the source register maps them to the year-prefixed notes and originals. Canonical URLs, notes, and licensed originals are linked through the register. Original PDFs are unmodified; source-specific licenses and hashes are recorded. Temporary downloads, text extraction, and rendered inspection images remain outside this repository.

Research used the journal-club-research skill's discovery → screening → coordinator-verification workflow. Primary methods/results, relevant appendices, first-party repositories, and original practitioner articles were inspected to the depths recorded. Selected tables were visually checked; AgentStream's published aggregates were reconstructed. No training experiments were reproduced. The journal-club-analyze pass is complete: thesis and claim ledger are ready with explicit qualifications. An HTML presentation is now available in `slides/`; it uses the earlier September 16 thesis and C001–C012 claim ledger, with its review scope recorded in `slides/review.md`. **Presentation coverage needs reconciliation with the revised argument, research expansion, and C013–C019**; see the workflow queue.

[Initial research notes](research-notes.md) remain as historical context; the current shortlist, landscape, and source notes supersede their earlier reading-status and numerical qualifications.

## Presentation use and editing

Open [slides/index.html](slides/index.html). Arrow keys or Space navigate; **N** opens notes, **O** opens the overview, and Home/End go to the first/last slide. The slide menu and buttons provide the same controls. URLs such as `index.html#slide-6` open a specific slide. **All slides** provides a continuous reading view; browser printing uses one slide per page. Speaker notes are for on-screen use and are excluded from printing.

The default scope is approximately 25–30 minutes plus discussion for an audience familiar with LLM basics. Edit [content.json](slides/content.json) for presenter/company metadata, copy, source-figure metadata, citations, and speaker notes; edit [theme.css](slides/theme.css) for the visual theme and [build.py](slides/build.py) for markup, base layout, and navigation. The build embeds the theme and original-source PNG excerpts so the delivered HTML remains standalone. Source extraction is optional; its command and PyMuPDF dependency are recorded in [figure provenance](slides/figures/provenance.md). Rebuild from the repository root with Python 3 (standard library only):

```sh
python3 journal-clubs/2026-09-18-self-evolving-agents/slides/build.py
```

[Storyboard and claim mapping](slides/storyboard.md) · [Figure provenance](slides/figures/provenance.md) · [Visual and factual review](slides/review.md).

The presentation skill now defaults to HTML. PowerPoint and PDF are not deliverables for this session.
