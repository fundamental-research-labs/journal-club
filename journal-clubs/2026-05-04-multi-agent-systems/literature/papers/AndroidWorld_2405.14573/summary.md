# AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents

**Authors:** Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, Oriana Riva
**arXiv:** 2405.14573
**Venue:** ICLR 2025
**Date:** April 2025

## Problem
Computer-use agents need online evaluation in realistic environments with reliable outcome rewards. Existing UI-agent benchmarks are often static demonstrations, web-only environments, or Android datasets without executable rewards, which makes them weak proxies for agents that must operate real mobile apps under varied task conditions.

## Method
AndroidWorld is a fully functional Android benchmark built on the Android Emulator, AndroidEnv, and Android Debug Bridge. It defines 116 programmatic tasks across 20 Android apps, with per-task initialization, success checking, and teardown logic. Tasks are parameterized from controlled random seeds, so the same template can generate many natural-language goals and state configurations. Rewards are mostly computed from durable device state such as files, app databases, settings, and messages, with UI-state checks where needed. The paper also integrates 92 MiniWoB++ tasks into Android as MobileMiniWoB++ and evaluates M3A, a zero-shot Android agent using ReAct-style action selection and Reflexion-style summaries.

## Key Findings
- AndroidWorld provides interactive, device-state evaluation for 116 Android tasks across 20 apps, plus 92 MobileMiniWoB++ tasks.
- The best reported AndroidWorld baseline, M3A with GPT-4 Turbo and the accessibility tree, reaches 30.6% success, well below the 80.0% human success rate.
- An adapted web-navigation agent, SeeAct, transfers weakly to AndroidWorld, reaching 15.5% success in the reported setup.
- Richer prompting and reflection help on AndroidWorld: M3A with GPT-4 Turbo improves over M3A-Simple, while screenshot Set-of-Mark input is not uniformly better than text accessibility-tree input.
- Parameter variation matters: the same agent varies across random seeds, and task parameters can expose hidden interaction requirements such as scrolling to unseen options.

## Tags
`android`, `mobile-ui-agents`, `computer-control`, `interactive-benchmark`, `device-state-rewards`, `task-parameterization`, `multimodal-agents`, `robustness`

## Connections
- Complements **WebVoyager** and other web-agent benchmarks by moving online UI-agent evaluation to real Android apps rather than desktop web pages.
- Related to **AgentBoard** as a benchmark contribution, but AndroidWorld emphasizes executable environments, parameterized tasks, and ground-truth success checks.
- Useful alongside MiniWoB++ work because it ports MiniWoB-style parameterization into Android while adding realistic native-app tasks.
- Relevant to multimodal agent evaluation: the paper shows that screenshots and Set-of-Mark overlays are helpful in some settings but do not automatically outperform accessibility-tree observations on native Android apps.
