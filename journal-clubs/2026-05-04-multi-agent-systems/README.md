# Multi-agent systems: coordination, scaling, and limits

Directory date: **May 4, 2026**, the creation date of `gyyang/Literature`, as requested. This is an archival date; the actual meeting date is not established.

Imported from [gyyang/Literature](https://github.com/gyyang/Literature/blob/faf6d2c7b982e5dfcedda018d0a0cca2d40229e2/README.md), revision `faf6d2c7b982e5dfcedda018d0a0cca2d40229e2`, on September 16, 2026. This preserves the existing May 2026 materials rather than updating the research to the import date.

## Materials

- [Complete Literature repository](literature/README.md): the full manuscript, paper corpus, slides, research records, and tooling. This is the canonical full import; the materials below are the earlier journal-club subset.
- [Review paper PDF](literature/manuscript/multi-agent-review-draft/build/index.pdf): *Scaling Test-Time Compute with Multi-Agent LLM Systems*, 27 pages, dated May 8, 2026.
- [Editable manuscript](literature/manuscript/multi-agent-review-draft/README.md).
- [Full import record and tooling commands](FULL_IMPORT.md).
- [Main presentation](slides/presentation.html): 29 Reveal.js slides, “When Multi-Agent Helps and When It Doesn't.” The HTML is the editable source and presentation artifact.
- [Executive summary and discussion questions](executive-summary.md).
- Editable Marp mini-decks: [CAID](slides/01_CAID.md), [MemMA](slides/02_MemMA.md), [DELEGATE-52](slides/03_DELEGATE52.md), [SlopCodeBench](slides/04_SlopCodeBench.md), [AI scientists](slides/05_AI_Scientists.md).
- [Import provenance and validation](IMPORT.md).
- [Figure sources](slides/figures/README.md).

Open the HTML in a browser, or serve this directory:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000/slides/presentation.html`. Use arrow keys to advance. The presentation loads Reveal.js 5.1.0 from jsDelivr and requires internet access. The mini-decks use Marp front matter; no rendered mini-deck exports were present in the source.

## Selected papers

| Paper | Local research materials |
| --- | --- |
| [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805) | [Summary](papers/AI_Scientists_Dont_Reason_2604.18805/summary.md) · [Notes](papers/AI_Scientists_Dont_Reason_2604.18805/notes.md) · [Claims](papers/AI_Scientists_Dont_Reason_2604.18805/claims.md) |
| [Effective Strategies for Asynchronous Software Engineering Agents](https://arxiv.org/abs/2603.21489) | [Summary](papers/CAID_2603.21489/summary.md) · [Notes](papers/CAID_2603.21489/notes.md) · [Claims](papers/CAID_2603.21489/claims.md) |
| [LLMs Corrupt Your Documents When You Delegate](https://arxiv.org/abs/2604.15597) | [Summary](papers/DELEGATE-52_2604.15597/summary.md) · [Notes](papers/DELEGATE-52_2604.15597/notes.md) · [Claims](papers/DELEGATE-52_2604.15597/claims.md) |
| [MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution](https://arxiv.org/abs/2603.18718) | [Summary](papers/MemMA_2603.18718/summary.md) · [Notes](papers/MemMA_2603.18718/notes.md) · [Claims](papers/MemMA_2603.18718/claims.md) |
| [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://arxiv.org/abs/2603.24755) | [Summary](papers/SlopCodeBench_2603.24755/summary.md) · [Notes](papers/SlopCodeBench_2603.24755/notes.md) · [Claims](papers/SlopCodeBench_2603.24755/claims.md) |
| [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) | [Summary](papers/WhyMultiAgentFail_2503.13657/summary.md) · [Notes](papers/WhyMultiAgentFail_2503.13657/notes.md) · [Claims](papers/WhyMultiAgentFail_2503.13657/claims.md) |
| [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) | [Summary](papers/ScienceOfScaling_2512.08296/summary.md) · [Notes](papers/ScienceOfScaling_2512.08296/notes.md) · [Claims](papers/ScienceOfScaling_2512.08296/claims.md) |
| [CooperBench: Why Coding Agents Cannot be Your Teammates Yet](https://arxiv.org/abs/2601.13295) | [Summary](papers/CooperBench_2601.13295/summary.md) · [Notes](papers/CooperBench_2601.13295/notes.md) · [Claims](papers/CooperBench_2601.13295/claims.md) |
| [Multi-agent Architecture Search via Agentic Supernet](https://arxiv.org/abs/2502.04180) | [Summary](papers/MaAS_2502.04180/summary.md) · [Notes](papers/MaAS_2502.04180/notes.md) · [Claims](papers/MaAS_2502.04180/claims.md) |
| [Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets](https://arxiv.org/abs/2604.02460) | [Summary](papers/SingleAgentOutperforms_2604.02460/summary.md) · [Notes](papers/SingleAgentOutperforms_2604.02460/notes.md) · [Claims](papers/SingleAgentOutperforms_2604.02460/claims.md) |
| [Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity](https://arxiv.org/abs/2602.03794) | [Summary](papers/AgentScalingDiversity_2602.03794/summary.md) · [Notes](papers/AgentScalingDiversity_2602.03794/notes.md) · [Claims](papers/AgentScalingDiversity_2602.03794/claims.md) |

The earlier subset above uses external paper links. The [full import](literature/README.md) also includes all tracked paper PDFs and source trees from Literature. Imported claims and bibliographic metadata have not been independently revalidated against current paper versions.
