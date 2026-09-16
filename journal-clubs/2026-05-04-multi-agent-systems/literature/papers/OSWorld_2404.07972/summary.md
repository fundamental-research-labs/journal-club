# OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**Authors:** Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
**arXiv:** 2404.07972
**Venue:** Preprint
**Date:** May 2024

## Problem
Digital agents are increasingly expected to operate real computers, but prior benchmarks often use static demonstrations, single domains, simplified action spaces, or web/mobile-only environments. That makes it hard to measure whether multimodal agents can complete realistic open-ended tasks involving arbitrary desktop applications, files, GUI and CLI interactions, and multi-application workflows.

## Method
OSWorld is a VM-based real computer environment for agent evaluation and learning. It initializes task states through configuration files, exposes screenshots, accessibility trees, and optional streams as observations, accepts raw mouse and keyboard actions through `pyautogui`-style code plus WAIT/FAIL/DONE actions, and evaluates final states with task-specific execution scripts. The benchmark built on this environment contains 369 Ubuntu tasks across OS, Office, Daily, Professional, and Workflow categories, plus a 43-task Windows analytic set. Tasks include intermediate initial states, required files, and custom evaluators for checking files, app state, accessibility trees, cookies, and other artifacts.

## Key Findings
- OSWorld emphasizes realistic computer use: 369 Ubuntu tasks include 268 single-app tasks, 101 multi-app workflow tasks, 30 infeasible tasks, 302 distinct initial states, and 134 execution-based evaluation functions.
- Human annotators completed 72.36% of the benchmark, with a median operation time of 111.94 seconds, indicating that the tasks are substantially harder than simple web-navigation examples.
- Reported LLM/VLM agents remain far below humans: the best overall success rate in Table 5 is 12.24%, and screenshot-only VLM settings are around the mid-single digits.
- Workflow tasks are especially difficult for agents; reported workflow success remains single-digit across the evaluated baselines and settings.
- Accessibility trees, screenshot plus accessibility-tree inputs, and Set-of-Mark prompting can help some models, but their effects are inconsistent and can introduce noise or misguidance.
- The error analysis points to GUI grounding and operational knowledge as central bottlenecks, including mouse-click inaccuracies, repeated failed actions, poor handling of noisy windows, and weak knowledge of app-specific procedures.

## Tags
`computer-use-agents`, `multimodal-agents`, `desktop-automation`, `GUI-grounding`, `execution-based-evaluation`, `benchmark`, `accessibility-tree`, `Set-of-Mark`, `workflow-tasks`

## Connections
- Extends web and mobile GUI-agent benchmarks such as WebArena, VisualWebArena, Mind2Web, Android-in-the-Wild, and MiniWoB++ by moving to controllable real computer environments with arbitrary desktop applications.
- Complements static GUI datasets such as OmniACT by emphasizing executable interaction loops and final-state evaluation rather than only next-action prediction.
- Useful context for coding-agent and software-assistant work because it evaluates end-to-end computer operation, including VS Code, terminals, files, spreadsheets, documents, browsers, and multi-app workflows.
- Related to multimodal grounding methods such as Set-of-Mark prompting, but shows that desktop-scale UI density and high-resolution screenshots make grounding harder than many prior image or web settings.
