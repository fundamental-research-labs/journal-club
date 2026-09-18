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
discussion. Use the narrative rhythm below as the default, adapting it to the
audience and user’s requested format without imposing a fixed slide count.
Introduce technical concepts before relying on them. Develop
evidence-linked discussion questions that invite a decision, prediction, or
disagreement. Omit minute-by-minute breakdowns unless requested.

### Give the presentation a narrative rhythm

Begin with an introduction that establishes the topic, why it matters, and the
concepts needed to follow the evidence. End the introduction with an explicit main
question that the rest of the presentation will answer.

Organize the results into coherent parts around subquestions, rather than a sequence
of paper reviews. Open each part with a mini introduction: explain the unresolved
problem, why it matters now, and what the upcoming evidence will test. This may be
a short slide or a brief setup integrated into the first evidence slide; a section
label alone does not supply motivation. Present results and their limitations, then
connect the part’s finding to the next question.

Close with a conclusion section that answers the main question and summarizes what
the results established, what remains uncertain, and the implications. Discussion
questions can follow that synthesis; they do not replace it. Match the visual rhythm
to these roles, giving introductions and transitions room to breathe between denser
evidence slides. Mark the introduction, main question, results parts, mini intros,
and conclusion in the storyboard so the sequence can be reviewed explicitly.

Use question titles for motivating slides and supported takeaway titles for results.
Give each slide one main idea and use
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

### Use the source's evidence visuals first

For a result from one source, default to its original figure or table, not a new
chart made from a few headline numbers. Inspect the exact source version and
caption before choosing the visual. If the result is in a table, a readable table
excerpt is preferable to inventing a plot. Preserve competing methods, negative
results, and uncertainty needed to interpret the claim.

Try a high-resolution extraction, a labeled panel/row crop, a larger evidence area,
or an extra slide before deciding an original is unreadable. Preserve aspect ratio,
axes, units, legends, row/column headers, and relevant baselines. Do not recolor or
rebuild empirical artwork just to match the deck theme. Keep explanatory callouts
outside the original; identify any overlays as added annotations. Label crops and
omitted panels/rows, and link the complete source. Keep source-caption qualifications
in notes even when the caption itself will not fit.

Redraw when it serves a concrete purpose: cross-source synthesis, a new calculation,
an unavailable/unusable source visual after inspection, or a specific reuse
restriction. Record that reason per visual; aesthetic consistency alone is not a
reason. Label the result “Adapted from…” or “Calculated from…” and retain verified
data and calculations. Keep conceptual diagrams clearly labeled as illustrations.
Never present synthetic or generated imagery as empirical evidence.

Record each evidence visual's source/creator, stable URL, exact version, PDF page
and figure/table/panel, local asset, crop or other transformations, and reuse/license
information where known in `slides/figures/provenance.md`. Unknown permission is
not a claimed license; follow the user's authorized scope and any concrete source
restrictions without inventing a separate approval workflow. Preserve original
assets separately from editable slide annotations; embed assets for offline use.
For revisions, audit existing result visuals and replace unjustified redraws rather
than merely relabeling them. Record intentional exceptions.

## Review and iterate

Open the HTML in a browser and visually inspect every slide, including appendices,
at presentation size. Check keyboard navigation, source links, notes, direct slide
links, and the print layout; inspect exported PDFs as well when delivered.
Check clipping, overlap, font substitution, contrast, citation
legibility, visual hierarchy, figure quality, and export consistency. Compare extracted figures against the
original page and check readability at actual presentation size, including headers,
legends, error bars, and crop boundaries. Fix defects
and re-render changed slides; recheck the entire deck after global layout changes.

Review the narrative separately from layout: does the introduction end with the
main question, does each results part explain why it is needed before showing its
evidence, and does the conclusion answer that question using the findings?

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
