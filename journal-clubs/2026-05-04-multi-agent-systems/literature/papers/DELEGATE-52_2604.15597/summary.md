# LLMs Corrupt Your Documents When You Delegate

**Authors:** Philippe Laban, Tobias Schnabel, Jennifer Neville
**arXiv:** 2604.15597
**Venue:** CoLM 2026 (submitted)
**Date:** April 2025

## Problem
As LLMs are increasingly used for "delegated work" (e.g., vibe coding), users trust them to edit documents without introducing errors. But how reliably do LLMs preserve document content over long-horizon editing workflows across diverse professional domains?

## Method
The authors introduce DELEGATE-52, a benchmark with 310 work environments across 52 professional domains (coding, crystallography, music notation, accounting, etc.). Each environment has real seed documents (2-5k tokens), 5-10 reversible editing tasks, and distractor context (8-12k tokens). They evaluate using a "round-trip relay" method: apply a forward edit then its inverse, and measure how well the original document is reconstructed. By chaining 10 such round-trips (20 interactions), they simulate long-horizon delegated workflows without needing reference annotations. Domain-specific parsing and similarity functions (not generic metrics) measure reconstruction quality.

## Key Findings
- Even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) corrupt an average of 25% of document content after 20 interactions; average across all 19 models is 50% degradation
- Python is the only domain (out of 52) where most models achieve near-lossless delegation (RS@20 >= 98%)
- The best model (Gemini 3.1 Pro) is "ready" for delegated work in only 11 of 52 domains
- Agentic tool use (file read/write + code execution) makes things worse, adding ~6% additional degradation on average
- Degradation compounds multiplicatively: larger documents and longer interactions amplify errors (each additional 1k tokens costs ~0.7% after 2 interactions but ~3.6% after 20)
- Sparse critical failures (10+ point drops in a single round-trip) account for ~80% of total degradation; models don't fail via many small errors but via occasional severe ones
- Weaker models degrade primarily through content deletion; frontier models degrade through content corruption
- Short-term performance (2 interactions) is not predictive of long-horizon performance (20 interactions)
- Models perform better in programmatic/structured domains and worse in natural language/niche domains
- Extending to 100 interactions shows continued degradation with no sign of plateauing
- Image editing models degrade far more severely than text models (best models: 28-30% final score vs 70-80% for text)

## Tags
`delegation`, `document-editing`, `benchmark`, `long-horizon`, `degradation`, `multi-domain`, `agentic-tool-use`, `vibe-coding`

## Connections
- Directly relevant to **SingleAgentOutperforms** and **WhyMultiAgentFail**: DELEGATE-52 finds that agentic tool use does not help (and actually hurts), echoing findings that more complex agent setups don't automatically improve performance
- Related to **SlopCodeBench**: both study quality degradation in AI-generated/edited artifacts, though SlopCodeBench focuses on code quality while DELEGATE-52 spans 52 domains
- Complements **CooperBench**: both benchmark LLM capabilities in realistic collaborative/delegated work scenarios beyond simple QA
- Connects to **ScienceOfScaling**: DELEGATE-52 shows that scale helps (GPT 4o at 14.7% vs GPT 5.4 at 71.5% over 16 months) but is far from sufficient for most domains
- Relevant to **AgentScalingDiversity**: both examine how agent capabilities vary across diverse task domains, with DELEGATE-52 showing a "jagged frontier" where models excel in some domains but fail in others
- Tangential to **MaAS** and **MemMA**: while those focus on multi-agent architectures and memory, DELEGATE-52's finding that errors compound over long interactions is relevant to any system where LLMs iteratively modify shared artifacts
