# Presentation review

Reviewed September 16, 2026. Deliverable: [standalone HTML deck](index.html), 18 slides (15 main + 3 appendices). Editable input: [content.json](content.json); generator: [build.py](build.py). The presentation implements the existing thesis and claims C001–C012; no new empirical conclusion was introduced.

## Original build: visual and interaction checks

- Opened the final HTML directly with `file://` in local Chromium, without a server or network dependencies.
- Rendered and visually inspected all 18 slides individually at presentation size (1440 × 900 browser viewport; scaled 1280 × 720 slide canvas). Checked typography, tables, chart labels, margins, citations, qualifications, and title wrapping. Changed slides were inspected again.
- Fixed a CSS class collision that initially exposed an inactive slide. Verified exactly one visible slide for each of the 18 navigation states. Automated checks found no horizontal content overflow or content overlapping the qualification/footer region; no page JavaScript errors occurred.
- Verified arrow/Home navigation, slide selection, deep linking to slide 10, notes open/close, notes present for all 18 slides, overview selection, continuous reading view, and fullscreen enter/exit. Print-mode setup removes overview/reading styles and restores them afterward.
- Verified the print CSS exposes all 18 slides. A scratch PDF contained exactly 18 pages, with a rendered empirical page visually checked against the browser. A stray final blank page was fixed by hiding the screen-reader status node in print. No PDF is part of the delivered materials.
- Source anchors use the canonical primary URLs in content.json; checked 48 rendered citation/reference anchors and all reference keys. Remote availability was not rechecked in this presentation-only pass; retain the source register’s access records.
- A mobile-sized viewport was exercised, but the fixed-ratio deck is intended for presentation-size screens. Full accessibility with assistive technology and cross-browser Safari/Firefox behavior were not independently tested.

The in-app browser runtime could not initialize (`Cannot redefine property: process`) on two attempts, including a fresh session. Review used a local headless Chromium fallback. Browser tooling and screenshots remain outside the repository under the system temporary directory in `codex-presentations/self-evolving-agents/html-qa/`.

## Evidence checks

- Read the session thesis, ledger, workflow, and relevant primary-source notes. Reopened retained original PDF text for WikiSkill 29.9/47.4, SEAL 39.7/47.0, the harness critique 67.4/72.3 and 68.3, R-Zero 49.12/46.52, and Hyperagents 0.640/0.610. Other findings retain their documented source-review depth.
- Preserved units and populations: FinEvo rubric points are not accuracy; SEAL questions share passages; WikiSkill averages benchmarks equally; AgentStream cells share tasks; R-Zero checkpoints are not independent runs. No CIs were invented. Hyperagents’ nonsignificant endpoint and Dream-RSI’s incomplete cost accounting stay visible or in notes.
- The fixed-skill gap (89.47 − 86.67 = 2.80), WikiSkill gain (47.4 − 29.9 = 17.5 pp), and SEAL gain (47.0 − 39.7 = 7.3 pp) match the ledger. Charts have zero baselines and 0–100 axes.
- Shopify is explicitly company-reported architecture. The four-arm comparison and evaluation criteria are visibly proposals. R-Zero’s disputed main-table aggregates and GEPA’s disputed average are not charted.
- Claim IDs and reference keys resolve. Figure provenance identifies adaptations, source versions, and permission limits. No inaccessible social content or illustrative demo numbers are used as results.

## Scope and completion

The skill now defaults to HTML, with Office output requiring an explicit request. The installed skill is a symlink to the edited repository copy. Skill validation and `git diff --check` passed. The README records navigation and the standard-library-only rebuild command.

No fresh discovery, training, benchmark reproduction, external publication, or sending was performed. The talk uses the September 16 analysis handoff; concurrent research-worker additions were not silently incorporated. Any subsequent thesis or ledger changes should be propagated before the session. Existing evidence limitations remain in force.


## Styling revision — September 16, 2026

Applied the revised presentation skill to the existing 18-slide deck. Replaced the
white/blue treatment with ivory evidence pages, forest-green opening/discussion/
closing pages, Georgia headlines, sage/teal charts, clearer result emphasis, and
small topic/section labels. Added an original, explicitly conceptual learning-loop
motif. Confirmed presenter credit **Robert Yang · Fundamental Research Labs** appears
on slides 1 and 15, driven by editable metadata. `theme.css` is editable source;
the build embeds it into the offline HTML.

Rendered and visually inspected all 18 slides at 1440 × 900. Re-rendered after
adding the confirmed attribution and inspected opening and closing credits.
The final automated layout check found no main-body content crossing into the
caveat/footer region and no JavaScript errors. Verified one active slide, all
speaker notes, keyboard navigation, deep links, overview selection, continuous
reading view, fullscreen, and print mode restoration. Scratch print output has
18 pages; no PDF is delivered. Browser runtime initialization again failed with
`Cannot redefine property: process`; local headless Chromium was used.

Compared the content against the pre-revision staged version: all slide content,
chart values, citations, and notes are unchanged; only presenter metadata was
added. Remote source availability was not rechecked. Skill validation passed with
`uv run --with pyyaml python .../skill-creator/scripts/quick_validate.py`, and
`git diff --check` passed. No runtime dependency was added to the deck.

This completes the styling/attribution revision. The existing content reconciliation
with expanded claims C013–C019 remains outstanding; this revision does not claim
to incorporate the expanded thesis. Cross-browser and assistive-technology testing
remain outside the verified scope.
