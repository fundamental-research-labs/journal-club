# Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate

**Authors:** Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu
**arXiv:** 2305.19118
**Venue:** Preprint
**Date:** October 2024

## Problem
Self-reflection methods ask an LLM to refine its own output, but the paper argues that this can collapse into Degeneration-of-Thought (DoT): once the model becomes confident in an initial answer, it tends to repeat or defend that answer instead of producing genuinely new reasoning. This is especially harmful on tasks where intuitive surface readings are often wrong.

## Method
The paper proposes Multi-Agent Debate (MAD). Two debater agents take affirmative and negative roles, respond to the shared debate history in a tit for tat style, and a judge agent either stops the debate when a solution is found or extracts a final answer when the iteration limit is reached. Experiments use zero-shot prompting with GPT-3.5-Turbo, GPT-4, Vicuna-7B, and Vicuna-13B on two main testbeds: Common MT, a Chinese-to-English commonsense translation benchmark, and Counter-Intuitive Arithmetic Reasoning (CIAR), a 200-question arithmetic dataset built around intuitive traps.

## Key Findings
- MAD improves GPT-3.5-Turbo and Vicuna results on the Common MT ambiguity subsets, and GPT-3.5-Turbo with MAD is reported to outperform GPT-4 on the paper's Common MT metrics.
- On CIAR, MAD improves over GPT-3.5-Turbo, CoT, self-consistency, and self-reflection baselines, while still trailing GPT-4.
- The analysis links MAD's gains to lower commonsense translation bias and much higher answer diversity than self-reflection.
- Adaptive stopping matters: forcing debates to continue can reduce translation quality, while the judge's adaptive break often stops after a single useful round.
- More debaters are not automatically better, and the paper reports lower Common MT performance when increasing from two debaters to three or four in its tested setup.
- LLM judges can be biased toward outputs produced by the same backbone model, so mixed-model debate requires caution.

## Tags
`multi-agent`, `debate`, `divergent-thinking`, `self-reflection`, `reasoning`, `machine-translation`, `LLM-as-judge`

## Connections
- Useful counterpoint to self-reflection and Reflexion-style methods: iterative self-feedback can entrench an initially wrong stance.
- Related to multi-agent debate and cooperative reasoning papers, but this version emphasizes a judge with adaptive stopping and evaluates debate intensity.
- Relevant to LLM-as-judge work because the judge can prefer same-backbone debaters, affecting mixed-model debate outcomes.
- Connects to chain-of-thought and self-consistency as another way to elicit diverse reasoning paths without external human feedback.
