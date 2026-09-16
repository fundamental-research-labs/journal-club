# WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

**Authors:** Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
**arXiv:** 2401.13919
**Venue:** Preprint
**Date:** June 2024 (arXiv v4)

## Problem
Web agents are often evaluated in simplified simulators, static snapshots, or stepwise offline settings, which hides the difficulty of interacting with live websites. Text-only agents also lose the visual structure that web pages are designed to communicate through layouts, widgets, calendars, maps, and other rendered UI components.

## Method
WebVoyager is an end-to-end browser agent built around a large multimodal model. It uses Selenium to interact with live websites, observes marked-up screenshots plus auxiliary text from interactive elements, reasons in a ReAct-style loop, and chooses actions such as click, input, scroll, wait, back, search-engine jump, and answer. The paper also builds a 643-task benchmark across 15 common websites using self-instruct plus human verification, evaluates with human task-success labels, and studies GPT-4V as an automatic evaluator over saved trajectories.

## Key Findings
- On the 643-task benchmark, WebVoyager reaches 59.1% human-labeled task success, above GPT-4 (All Tools) at 30.8% and a WebVoyager text-only accessibility-tree setup at 40.1%.
- The benchmark covers 15 live websites, including shopping, travel, maps, search, news, code, education, recipes, and reference sites, with 40 to 45 tasks per site.
- GPT-4V trajectory evaluation reaches 85.3% agreement and 0.70 kappa with consolidated human labels when given the full trajectory.
- Vision helps most on visually complex sites such as Booking and Google Flights, while text-heavy sites expose limits of screenshot-first perception.
- The dominant failure category in the sampled error analysis is navigation getting stuck, followed by visual grounding issues, hallucination, and prompt misalignment.

## Tags
`web-agent`, `multimodal-agent`, `browser-automation`, `GPT-4V`, `web-navigation`, `set-of-mark`, `Selenium`, `trajectory-evaluation`, `benchmark`

## Connections
- Extends the line of WebGPT, Mind2Web, WebArena, and SeeAct from text-centric or constrained web navigation toward live multimodal browser control.
- Useful alongside agent benchmarks such as AgentBoard because it emphasizes end-to-end task completion rather than only stepwise action prediction.
- Connects to multimodal GUI-agent work: screenshots and element markings are treated as first-class state, not just as auxiliary context.
- Important for evaluation methodology because it proposes LMM-based automatic judging over web-agent trajectories while validating against human labels.
