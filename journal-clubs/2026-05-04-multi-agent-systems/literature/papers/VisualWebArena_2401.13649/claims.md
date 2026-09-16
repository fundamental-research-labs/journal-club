# Claims

## Claim 1
**Claim:** VisualWebArena provides a realistic, reproducible benchmark for visually grounded web-agent tasks.

**Evidence:** The paper introduces 910 tasks over three self-hosted environments: a new Classifieds site plus Shopping and Reddit sites inherited from WebArena. All tasks require visual understanding, and some also require cross-site behavior or a self-hosted Wikipedia knowledge source.

**Caveats/Scope:** The benchmark is still limited to three website families and authored task templates; self-hosting improves reproducibility but does not capture every property of the live web.

**Source pointers:** Abstract; Sec. 1; Sec. 4.1; Sec. 4.2; Fig. 1; Appendix A

## Claim 2
**Claim:** The benchmark evaluates more than text extraction by checking visual state, image similarity, VQA-style conditions, and final website state.

**Evidence:** Section 3.3 defines text reward functions, visual functions such as `eval_vqa` and `eval_fuzzy_image_match`, and navigation/action evaluators that inspect target page content after an agent acts. Table 2 shows example tasks whose rewards depend on product images, wishlist state, post creation, and price edits.

**Caveats/Scope:** The rewards are binary, and some checks depend on LLM or VLM evaluators, so evaluator quality can influence measured success on open-ended tasks.

**Source pointers:** Sec. 3.3; Table 2

## Claim 3
**Claim:** Text-only web agents perform poorly on visually grounded tasks, while captions and direct multimodality help but do not close the gap.

**Evidence:** In Table 3, GPT-4 text-only reaches 7.25% overall success. Caption augmentation raises GPT-4 to 12.75%, and GPT-4V with screenshots, captions, and the accessibility tree reaches 15.05%. Human performance is 88.70%.

**Caveats/Scope:** The main experiments are prompt-based with three in-context examples and use the specific models available to the authors at the time.

**Source pointers:** Sec. 5; Sec. 6; Table 3; Sec. 4.3

## Claim 4
**Claim:** Set-of-Marks improves GPT-4V navigability on visually dense web pages.

**Evidence:** The SoM agent labels interactable webpage elements with bounding boxes and unique IDs. Table 3 reports GPT-4V improving from 15.05% overall with the accessibility tree to 16.37% with SoM; Classifieds improves from 8.12% to 9.83%, and Reddit improves from 12.38% to 17.14%.

**Caveats/Scope:** The benefit is model-dependent: the paper reports little or no SoM improvement for weaker VLMs such as Gemini-Pro, IDEFICS-80B, and CogVLM in the main results.

**Source pointers:** Sec. 3.1; Sec. 5.3; Sec. 6; Fig. 2; Table 3

## Claim 5
**Claim:** Current multimodal web agents still struggle with OCR, long-horizon execution, and premature termination.

**Evidence:** Table 4 shows GPT-4V + SoM reaching 13.4% success on OCR-required tasks versus 16.9% on non-OCR tasks. Appendix C.4 describes failure modes where agents undo correct work, miss simple visual targets, or give up too early.

**Caveats/Scope:** The task-subset analysis is centered on GPT-4V + SoM, and qualitative failure modes are drawn from observed examples rather than a fully exhaustive taxonomy.

**Source pointers:** Sec. 6.1; Table 4; Appendix C.4; Fig. 10

## Claim 6
**Claim:** Newer frontier VLMs improve VisualWebArena scores but still leave large headroom.

**Evidence:** Appendix B reports GPT-4o with the SoM setup achieving 19.78% overall success, higher than GPT-4V + SoM at 16.37% in the main table but still far below the 88.70% human baseline.

**Caveats/Scope:** These were additional post-submission experiments and should be compared cautiously with the main experimental setup.

**Source pointers:** Appendix B; Table 5; Table 3
