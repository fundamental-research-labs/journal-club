---
name: journal-club-present
description: Create a visually appealing journal club presentation from an evidence-backed thesis, with editable sources, citations, speaker notes, and visual verification. Use to build or revise the deck and feed argument or evidence gaps back into analysis and research.
---

# Journal Club Present

Turn the analysis into a clear visual argument that an audience can understand,
question, and remember. Preserve the thesis's limits while making its implications
concrete.

Read [the shared workflow](../journal-club-research/references/workflow.md), the
session README, thesis, claim ledger, and unresolved qualifications. Check source notes for the
results and graphics you will use. If analysis is missing, develop it within scope
or record the prerequisite; do not silently replace analysis with paper summaries.

## Design the argument

Default to a local HTML presentation with editable HTML/CSS/JavaScript sources.
It should open directly in a browser without a build service or network dependency.
Provide keyboard navigation, readable source links, accessible speaker notes, and
a print layout. Prefer existing session tooling and a small implementation over
adding a presentation framework. Do not create PowerPoint files or launch Office
apps unless the user explicitly requests that format. Export a PDF only when
requested; use the PDF skill to inspect it when available.

Develop the presentation narrative from the thesis and claims in this stage;
no separate analysis storyline is required. Write `slides/storyboard.md` before
generating the deck. For each slide, record its
purpose, takeaway title, visual plan, claim IDs, source locators, and speaker notes.
Plan around the audience's background and the time available, reserving room for
discussion. A useful arc is question → concepts → argument and evidence → strongest
challenge → synthesis → open decisions. Adapt it rather than imposing a fixed
slide count. Introduce technical concepts before relying on them. Develop
evidence-linked discussion questions that invite a decision, prediction, or
disagreement. Omit minute-by-minute breakdowns unless requested.

Use titles that state a supported takeaway. Give each slide one main idea and use
mechanism diagrams, comparisons, timelines, plots, or concrete examples to explain
it. Choose a coherent palette, type hierarchy, spacing, and alignment system. Use
large, legible text, strong contrast, and visual emphasis that guides attention.
Avoid turning source notes into dense bullet slides; put supporting detail in notes
or the appendix. Visual polish should make the reasoning easier to follow.

## Establish a visual direction

When revising a deck, inspect its current renders and any supplied references
before changing the design. Identify the actual weakness—such as repetitive
layouts, weak hierarchy, crowded evidence, or absent attribution—and preserve
the existing argument, citations, and interactions unless content changes are
needed. Record the chosen direction in the storyboard: palette, typography,
spacing, and the visual roles of opening, evidence, synthesis, and appendix slides.

Treat the deck as a designed sequence. Give the opening a distinctive composition;
vary layout and emphasis with the argument rather than repeating a template.
Use restrained accents with consistent meanings, generous whitespace, and a clear
type contrast. A chart's key comparison should be apparent before its caveats are
read. Avoid decoration that implies unmeasured progress, invented data, or causal
relationships. References can inspire visual treatment, not supply unverified data.
Keep fonts and assets available offline; use deliberate fallback fonts.

Store presenter/author and company/affiliation in editable deck metadata. Use
confirmed spelling on the title slide and, when useful, a restrained closing or
running credit. Keep presenter attribution distinct from research citations.
If either identity is missing, ask one concise question while continuing design
work; do not infer an employer from a username, email domain, or cited company.

Render representative slides (opening, densest evidence, and synthesis) early to
test the direction, then apply it consistently. Review the full sequence as well
as individual slides: rhythm, hierarchy, and readability matter beyond the absence
of overflow. Record concrete design changes and observed verification results.

## Build with provenance

Keep editable slide sources, generated deliverables, and relevant figure assets
inside `slides/`; record generation commands and dependencies in the session README.
Include speaker notes with the explanation, caveats, and transitions needed to
present the argument. Put readable citations near empirical claims and fuller
references and result locators in notes or the appendix.

Use original source figures when legible and permitted; otherwise create clearly
labeled adaptations from verified data. Record source URLs, locators, adaptations,
and permission information where known in `slides/figures/provenance.md` when figures
are used. Label illustrative diagrams and synthetic data explicitly. Do not use
invented values, decorative charts, or generated imagery as empirical evidence.
Retain units, relevant uncertainty, baseline definitions, and meaningful axis scales.

## Review and iterate

Open the HTML in a browser and visually inspect every slide, including appendices,
at presentation size. Check keyboard navigation, source links, notes, direct slide
links, and the print layout; inspect exported PDFs as well when delivered.
Check clipping, overlap, font substitution, contrast, citation
legibility, visual hierarchy, figure quality, and export consistency. Fix defects
and re-render changed slides; recheck the entire deck after global layout changes.

Audit factual claims and numbers against the claim ledger and sources. Check links,
notes, attribution, numerical consistency, and whether the narrative fits the
available time. Record outcomes and any unavailable checks in `slides/review.md`;
a successful build alone is not visual verification.

If a compelling title overstates the evidence, narrow it or return to analysis. If
a key comparison lacks compatible data, return to research. Log the affected slide,
claim, question, and acceptance criterion in the shared workflow; update downstream
slides when the answer changes the argument. Do not hide these gaps with design.

Finish with an accessible current deck, editable source, requested exports, and a
session README linking them. Report unresolved limitations and verification status.
Keep materials local unless publishing or sending is explicitly requested.
