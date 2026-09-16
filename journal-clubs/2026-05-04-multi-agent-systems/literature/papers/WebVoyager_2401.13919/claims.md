# Claims

## Claim 1
**Claim:** Live-web multimodal browsing is a more realistic target for web agents than static or simulator-only evaluation.

**Evidence:** The paper builds WebVoyager to operate through Selenium on real websites rather than locally hosted sites or offline snapshots, and motivates this choice with challenges such as pop-ups, changing pages, and the need for real-time web information.

**Caveats/Scope:** The environment excludes login-required or CAPTCHA-protected tasks, disables multi-tab browsing, and supports only a finite action set.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3.1; Section 4.1; Limitations

## Claim 2
**Claim:** WebVoyager's screenshot-plus-element-text observation design improves over a text-only accessibility-tree setup on the paper's live-website benchmark.

**Evidence:** Table 1 reports 59.1% human-labeled task success for WebVoyager versus 40.1% for WebVoyagerText-only, with especially large gains on visually complex sites such as Booking and Google Flights.

**Caveats/Scope:** The gain is not uniform; the text-only setup is competitive or better on some text-heavy sites, and the comparison depends on GPT-4V-era model capabilities and browser settings.

**Source pointers:** `paper.pdf`, Section 3.3; Section 5.2; Table 1; Section 5.3

## Claim 3
**Claim:** Marking interactive elements on screenshots gives the multimodal model a practical action interface for browser control.

**Evidence:** WebVoyager overlays bounding boxes and numeric labels on interactive elements using a rule-based JavaScript tool, then asks the model to select actions by label. The method supports concise click and input actions without requiring an object-detection model.

**Caveats/Scope:** The paper still reports visual grounding errors, including wrong-element selection and confusion between nearby labels or page content.

**Source pointers:** `paper.pdf`, Figure 2; Section 3.3; Section 3.4; Section 5.4

## Claim 4
**Claim:** LMM-based trajectory judging can approximate human evaluation for open-ended web-agent tasks.

**Evidence:** On a 300-task subset, GPT-4V evaluation reaches 85.3% agreement and 0.70 kappa with consolidated human labels when given the full trajectory, and agreement improves as more screenshots are provided.

**Caveats/Scope:** The evaluator is itself a proprietary multimodal model, and later analysis shows evaluator bias and different strictness across GPT-4V, Claude-3-Opus, and GPT-4o.

**Source pointers:** `paper.pdf`, Section 5.1; Section 5.2; Table 2; Table 3; Appendix B

## Claim 5
**Claim:** WebVoyager's remaining failures point to navigation robustness, visual grounding, and prompt adherence as key bottlenecks.

**Evidence:** Manual error analysis over sampled failed tasks attributes 44.4% of failures to navigation stuck, 24.8% to visual grounding issues, 21.8% to hallucination, and 9.0% to prompt misalignment.

**Caveats/Scope:** These ratios come from a sampled error analysis on the authors' benchmark and taxonomy, not from an exhaustive causal intervention study.

**Source pointers:** `paper.pdf`, Section 5.4; Table 4; Appendix F
