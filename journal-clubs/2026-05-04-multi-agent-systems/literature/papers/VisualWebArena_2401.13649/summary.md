# VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks

**Authors:** Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
**arXiv:** 2401.13649
**Venue:** Preprint
**Date:** June 2024

## Problem
Most web-agent benchmarks emphasize text-based interaction, but many real browser tasks depend on visual information: product images, colors, icons, visual layouts, screenshots supplied by the user, and images embedded in social or shopping pages. The paper asks how well current LLM and VLM agents can handle realistic visually grounded web tasks.

## Method
VisualWebArena extends the WebArena setup with self-hosted web environments and execution-based evaluation. It introduces 910 visually grounded tasks across Classifieds, Shopping, and Reddit-style sites; 25.2% of tasks include input images. Agents operate over browser actions such as click, type, scroll, goto, and stop. The evaluation uses text matching, LLM-based fuzzy matching, VQA-based checks, image-similarity checks, and final-page state locators. The paper benchmarks text-only LLM agents, caption-augmented agents, multimodal VLM agents, and a Set-of-Marks (SoM) visual-agent interface that labels interactable page elements with bounding boxes and IDs.

## Key Findings
- Humans solve the sampled benchmark tasks at 88.7% success, while the best main-table agent, GPT-4V with SoM, reaches 16.37%.
- Text-only GPT-4 reaches 7.25% success; adding image captions raises it to 12.75%, and direct multimodal GPT-4V reaches 15.05%.
- SoM improves GPT-4V overall from 15.05% to 16.37%, with the clearest gains on visually dense Classifieds and Reddit pages.
- GPT-4V + SoM performs worse on OCR-required tasks than non-OCR tasks, suggesting fine-grained text recognition remains a bottleneck.
- Appendix experiments with newer frontier models show GPT-4o at 19.78% overall, still far below human performance.

## Tags
`multimodal-agents`, `web-agents`, `visual-grounding`, `browser-automation`, `benchmark`, `vision-language-models`, `set-of-marks`, `webarena`

## Connections
- Extends **WebArena** by making every task visually grounded and adding visual evaluation primitives.
- Complements text-centric web-agent benchmarks such as **Mind2Web** and **WebShop** by stressing visual perception, image inputs, and page layout.
- Uses **Set-of-Marks** prompting as an action-grounding interface for VLM browser agents.
- Useful alongside multimodal GUI-agent work because it evaluates agents in reproducible websites rather than static screenshots only.
