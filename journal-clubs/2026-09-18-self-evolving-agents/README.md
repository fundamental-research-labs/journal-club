# Self-evolving agents

**Session:** Friday, September 18, 2026  
**Research cutoff:** September 16, 2026  
**Presenter:** Robert Yang · Fundamental Research Labs

**Scope:** Topic-wide research for an audience familiar with LLM basics.

Central question: **How can agents turn experience into lasting improvements—and how can we tell whether those improvements generalize?**

## Start here

- **[Open the HTML presentation](slides/index.html)** — 19 talk slides plus 7 appendices, citations, and speaker notes. Opens directly in a browser; no install or network required.

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

The September 18 analysis rewrite organizes the thesis around when experience creates lasting value, with developed comparisons and explicit conditional synthesis. The [architecture review and resolution](analysis/architecture-review.md) records the changes. The current slides still require reconciliation with this revised argument and the scholarly foundations.

## Selected supporting resources

The ranked ten are **WikiSkill; Rethinking the Evaluation of Harness Evolution for Agents; GEPA; SEAL; Hyperagents; AgentStream; R-Zero; HarnessDev; FinEvo-Bench; and Shopify's Sidekick continual-learning account**. They cover retained knowledge, prompt/harness evolution, weight adaptation, self-generated curricula, meta-improvement, longitudinal evaluation, and production practice. Papers are supporting examples for the field's questions, not ten separate talk sections.

Strong alternatives include **Dream-RSI, EvoHarnessBench, Library Drift, NemoClaw, ACE, HGM/DGM, Absolute Zero, Agent-World, and Reef**. September frontier coverage includes ScienceBuddy, MetaRSI, and the Economics of Recursive Self-Improvement, with explicit distinctions between controlled results, provisional claims, and theory. Social/talk leads with unverified provenance or inaccessible content are not used as empirical evidence.

## Repository and review notes

All reading-note filenames use `YYYY-short-title.md` in lowercase kebab-case, with the source publication year as the prefix. For SoL-Pi, `2026` identifies the reviewed repository snapshot year because first publication is unverified. Original-source folders use the same year-prefixed name as their reading notes, and retained filenames use `YYYY-short-title-artifact-version.ext`. Existing source keys are preserved; the source register maps them to the year-prefixed notes and originals. Canonical URLs, notes, and licensed originals are linked through the register. Original PDFs are unmodified; source-specific licenses and hashes are recorded. Temporary downloads, text extraction, and rendered inspection images remain outside this repository.

Research used the journal-club-research skill's discovery → screening → coordinator-verification workflow. Primary methods/results, relevant appendices, first-party repositories, and original practitioner articles were inspected to the depths recorded. Selected tables were visually checked; AgentStream's published aggregates were reconstructed. No training experiments were reproduced. The journal-club-analyze pass is complete: thesis and claim ledger are ready with explicit qualifications. Before the scholarly-foundations revision, the HTML presentation in `slides/` followed the thesis and maps C001–C019 into slides and notes. The September 18 revision develops WikiSkill’s retained-knowledge mechanism, distinguishes both Hyperagents transfer experiments, includes the bounded positive internalization counterexample, and corrects the proposed controls. The presentation now follows introduction → main question → three motivated results parts → conclusion, with 25 main slides and 11 appendices. All 36 slides were visually reviewed; [review scope and limitations](slides/review.md) are recorded. The research cutoff remains September 16, 2026.

[Initial research notes](research-notes.md) remain as historical context; the current shortlist, landscape, and source notes supersede their earlier reading-status and numerical qualifications.

The September 18 concept revision adds method explanations before result tables and conceptual source figures for AgentStream, Hyperagents, and SEAL. **[AgentStream explanation](slides/index.html#slide-13)** now precedes **[its results](slides/index.html#slide-14)**; these replace the former result-only slide 11. The [storyboard](slides/storyboard.md) records the deck-wide concept-to-evidence audit.

## Presentation use and editing

Open [slides/index.html](slides/index.html). Arrow keys or Space navigate; **N** opens notes, **O** opens the overview, and Home/End go to the first/last slide. The slide menu and buttons provide the same controls. URLs such as `index.html#slide-6` open a specific slide. **All slides** provides a continuous reading view; browser printing uses one slide per page. Speaker notes are for on-screen use and are excluded from printing.

The default scope is approximately 30–35 minutes plus discussion for an audience familiar with LLM basics. Edit [content.json](slides/content.json) for presenter/company metadata, copy, source-figure metadata, citations, and speaker notes; edit [theme.css](slides/theme.css) for the visual theme and [build.py](slides/build.py) for markup, base layout, and navigation. The build embeds the theme and original-source PNG excerpts so the delivered HTML remains standalone. Source extraction is optional; its command and PyMuPDF dependency are recorded in [figure provenance](slides/figures/provenance.md). Rebuild from the repository root with Python 3 (standard library only):

```sh
python3 journal-clubs/2026-09-18-self-evolving-agents/slides/build.py
```

[Storyboard and claim mapping](slides/storyboard.md) · [Figure provenance](slides/figures/provenance.md) · [Visual and factual review](slides/review.md).

The presentation skill now defaults to HTML. PowerPoint and PDF are not deliverables for this session.

The source-figure correction replaces homemade conceptual diagrams on slides 6, 8 and 10 with the original WikiSkill Figure 2, FinEvo Figure 1 and harness Figure 2. Source artwork is preserved; explanations accompany it.
