# Claims

## Claim 1
**Claim:** AutoAgent provides a zero-code path from natural-language requirements to executable tools, agents, and workflows.

**Evidence:** The framework uses profiling and editor agents to produce structured XML forms, create required tools, compose agents, validate constraints, and retry after parser or execution errors. The paper demonstrates this on a DaVinci image agent, a Financial Agent, and a majority-voting math workflow.

**Caveats/Scope:** The evidence is strongest for the reported examples and implementation design. The paper does not include a controlled study showing that non-programmers can reliably use the system without help.

**Source pointers:** `paper.pdf`, Abstract; Sec. 3.4; Sec. 4.3; Appendix Sec. 6.6; Listings 18 and 20; Table 6

## Claim 2
**Claim:** The core system is a modular generalist multi-agent stack centered on an orchestrator with web, coding, and local-file specialists.

**Evidence:** Section 3.1 defines the Orchestrator Agent and the Web, Coding, and Local File agents, including handoff tools, BrowserGym-based browsing, Docker-sandboxed code execution, and markdown-based file browsing. Table 4 lists the system-level tools exposed to these agents.

**Caveats/Scope:** The architecture is presented as a general foundation, but robustness depends on the underlying LLM, tool implementations, sandbox, and task environment.

**Source pointers:** `paper.pdf`, Fig. 2; Sec. 3.1; Appendix Sec. 6.1; Table 4

## Claim 3
**Claim:** AutoAgent reports strong GAIA validation performance relative to listed open-source generalist agents.

**Evidence:** Table 1 reports AutoAgent at 55.15 average success on GAIA validation, above the listed open-source baselines such as Langfun Agent v2.0 at 54.55, Magentic-1 at 36.97, and FRIDAY at 34.55. It also reports 71.70 on Level 1 tasks.

**Caveats/Scope:** The comparison uses published GAIA leaderboard results rather than a fully uniform rerun of every baseline. AutoAgent is below h2oGPTe Agent v1.6.8 overall, and its Level 3 score is not best in the table.

**Source pointers:** `paper.pdf`, Sec. 4.1; Table 1

## Claim 4
**Claim:** AutoAgent's file system supports agentic RAG by converting local files into vector-database collections and exposing retrieval/answering tools.

**Evidence:** Section 3.3 describes automatic conversion of uploaded text files, archives, and folders into text chunks stored in a vector database, with tools such as `save_raw_docs_to_vector_db`, `query_db`, and `answer_query`. Table 4 gives the tool descriptions.

**Caveats/Scope:** The design is primarily described for text documents and text-convertible files. Retrieval quality still depends on chunking, embeddings, indexing, and the LLM used for final answers.

**Source pointers:** `paper.pdf`, Sec. 3.3; Appendix Sec. 6.1; Table 4

## Claim 5
**Claim:** On MultiHop-RAG, AutoAgent outperforms the paper's chunk-based, graph-based, and LangChain agentic RAG baselines.

**Evidence:** Table 2 reports AutoAgent at 73.51% accuracy and 14.20% error. The closest agent-based baseline, LangChain, is reported at 62.83% accuracy and 20.50% error; LightRAG is reported at 58.18% accuracy and 35.40% error.

**Caveats/Scope:** The experiment uses one RAG benchmark with gpt-4o-mini, text-embedding-3-small, 256-token chunks, and top-6 retrieval. The result should not be generalized to all RAG corpora or retrieval settings without additional evaluation.

**Source pointers:** `paper.pdf`, Sec. 4.2; Table 2

## Claim 6
**Claim:** AutoAgent can generate a simple multi-model reasoning workflow that modestly improves over the best single model reported in the paper's MATH-500 comparison.

**Evidence:** The system generates a majority-voting workflow that runs GPT-4o, Claude 3.5 Sonnet, and DeepSeek-v3 solvers in parallel and aggregates their answers. Table 3 reports 75.6 pass@1 for the workflow versus 74.2 for DeepSeek-v3 and 66.4 for both GPT-4o and Claude 3.5 Sonnet.

**Caveats/Scope:** The improvement over the best single model is small, and the paper does not provide a broad cost, latency, or ablation analysis for workflow generation.

**Source pointers:** `paper.pdf`, Sec. 4.3; Table 3; Appendix Sec. 6.7.3; Listing 20; Table 5
