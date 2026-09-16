# Practitioner discovery: self-evolving agents

**Run date/cutoff:** 2026-09-16 (America/Los_Angeles). **Lane:** first-party
engineering blogs, repositories, talks/experiments, researcher posts, and
negative/failure evidence. Existing coverage already includes autoresearch, Reef,
SoL-Pi, Hermes, LangChain, NVIDIA NemoClaw, Hyperagents, and related notes; this
pass searched for additional artifacts and did not duplicate those families.

## Top five additions

1. **Shopify Sidekick continual-learning loop** — strongest new candidate. A
   first-party production account describes a complete loop from random production
   samples and human rubric calibration, through harness search and self-healing
   trajectories, to SFT/GRPO updates and prompt compression. It reports up to 2,000
   GraphQL-agent requests/minute, 96% estimated serving-cost reduction, 19% lower
   time-to-first-token and 38% lower end-to-end latency in a 350-request/minute load
   test, plus throughput changes. These are company-reported figures in one article;
   no independent replication, confidence intervals, traffic denominator, or public
   code/data was located.
2. **ArcFusion self-improving document parser** — useful small-company case study
   with an explicit automated prompt-optimization loop and a claimed 86%→99.8%
   accuracy change. The post says no manual prompt edits occurred after launch, but
   the task distribution, test-set isolation, sample size, judge, and raw traces are
   not supplied in the inspected article. Treat as a reproducibility lead, not a
   general result.
3. **BetterForAll/self-improving-agents** — runnable progression from deterministic
   score loops to a four-agent arena, with benchmark and judge configuration visible
   in the repository. This is an inspectable teaching/research artifact, not evidence
   of broad capability improvement; no run was executed in this pass.
4. **Agent Improvement Loop (Postsyntax)** — a detailed practitioner argument for
   converting each production failure into a permanent regression test, retaining
   prompt/retrieval/tool/workflow state and classifying root causes before fixing.
   It supplies a concrete operational loop but no measured deployment study.
5. **Hyperstruck engineering blog series** — first-party, failure-oriented notes on
   experience accumulation, forgetting, deduplication, false success, and secret
   leakage. The posts are useful negative-design evidence and terminology, but the
   inspected pages expose no controlled benchmark or public evaluation corpus.

## Candidate evidence families

### Shopify Sidekick's continual learning loop

- **Canonical:** [Shopify Engineering, “Sidekick's continual learning loop”](https://shopify.engineering/sidekicks-continual-learning-loop)
- **Authors/org:** Cody Mazza-Anthony and Andrew McNamara, Shopify.
- **Type/date:** first-party engineering blog; published 2026-08-05 (date shown on
  page; accessed 2026-09-16).
- **Evidence family:** Sidekick/GraphQL agent, internal training/evaluation pipeline.
- **What was inspected:** full HTML article, including rubric/calibration,
  autoresearch-style harness optimization, self-healing pipeline, SFT/GRPO, and
  GraphQL-agent deployment sections.
- **Reported measurements:** production service “up to 2,000 requests per minute”;
  frontier-vs-specialized serving estimate of about $27M/year versus $1M/year
  (96% reduction); roughly 6,000→1,500 prompt tokens; at 350 requests/minute,
  about 19% lower time-to-first-token, 38% lower end-to-end latency, 16% more
  requests/sec, 12% more output tokens/sec, and about 14% fewer GPUs. The article
  also claims the specialized model surpasses the frontier baseline, but gives no
  table, confidence interval, task count, baseline model identifier, or public
  evaluation set in the inspected text.
- **Interpretation:** This is the clearest practitioner description found of a
  multi-level update target (harness, trajectories, weights, and prompt compression)
  operating in production. It supports the existence of an engineering loop and
  company-reported operational outcomes, not a causal or independently verified
  claim that self-improvement is generally reliable.
- **Access/copy:** Full public HTML read. No download needed; article images are
  hosted by Shopify CDN. Redistribution/license basis for a local capture is not
  established; retain canonical link only. No public code or raw logs located.
- **Suggested role:** concrete practitioner complement to autoresearch and NVIDIA;
  discussion of metric validity, judge alignment, data leakage, and weight-update
  regressions.

### ArcFusion self-improving document parser

- **Canonical:** [“The Agent That Learns: How We Built a Self-Improving AI Loop”](https://www.arcfusion.ai/blog/the-agent-that-learns)
- **Author/org:** Napat Dollapavijit, ArcFusion.
- **Type/date:** first-party engineering case study; published 2026-04-30; accessed
  2026-09-16.
- **Evidence family:** ArcFusion document-parsing product and prompt optimizer.
- **What was inspected:** full public article. It describes an orchestrator that
  evaluates outputs, rewrites prompts, versions candidates, and retains changes.
- **Reported claim:** document-parsing accuracy increased from 86% to 99.8% after
  the loop started, with no manual prompt edit thereafter. The post does not expose
  sample size, task mix, holdout construction, metric definition, number of trials,
  cost, or a before/after table. This is a company-selected case study, not a
  controlled estimate of general self-improvement.
- **Access/copy:** Full public HTML read. No public code or downloadable dataset
  found. Keep canonical URL; local retention permission not established.
- **Suggested role:** illustrative example of optimization-loop claims; pair with a
  checklist asking what must be disclosed before accepting a large gain.

### BetterForAll self-improving-agents repository

- **Canonical:** [GitHub repository](https://github.com/BetterForAll/self-improving-agents)
- **Author/org:** BetterForAll.
- **Type/date:** open-source code/educational experiment; repository page accessed
  2026-09-16; exact initial publication date and current commit were not verified in
  this pass.
- **Evidence family:** deterministic score loop, autoresearch-style loop, and
  four-agent arena examples.
- **What was inspected:** README and repository landing page. It exposes an initial
  solution, benchmark script, deterministic score option, optional LLM judge/rubric,
  and an arena loop with multiple agents.
- **Evidence status:** inspectable mechanism and reproducibility lead; no execution,
  run logs, seed aggregation, or independent evaluation performed. LLM-judge mode
  is especially vulnerable to rubric/judge drift unless separately validated.
- **Access/copy/license:** public GitHub source; license was not confirmed from the
  landing page, so do not retain a copy in this session. Canonical code link only.
- **Suggested role:** hands-on artifact for showing how “self-improvement” can mean
  search over programs, judge-mediated selection, or agent tournaments, with each
  meaning requiring different controls.

### Postsyntax: Agent Improvement Loop

- **Canonical:** [The Agent Improvement Loop: Turning Production Failures into Regression Tests](https://postsyntax.substack.com/p/the-agent-improvement-loop-turning)
- **Author:** Rafay A.; first-party practitioner essay, published 2026-07-01;
  accessed 2026-09-16.
- **Evidence family:** production-agent reliability and regression testing.
- **What was inspected:** full public HTML. It proposes preserving the failed prompt,
  retrieved documents, tool sequence, workflow state, expected behavior, and
  observed failure as a permanent regression case; it recommends failure taxonomy,
  human review labels, and continuous evaluation before deployment.
- **Evidence status:** operational design guidance, not a measured experiment. The
  article contains no deployment sample, benchmark, ablation, or replication.
- **Access/copy:** full public HTML read; no downloadable artifact or stated
  redistribution license located. Keep canonical link only.
- **Suggested role:** negative/operational counterweight: an agent can appear to
  improve while silently reintroducing old failures unless the evaluation corpus
  itself evolves and runs in CI.

### Hyperstruck experience and failure blog series

- **Canonical:** [Hyperstruck blog index](https://hyperstruck.com/blog/)
- **Author/org:** Hyperstruck.
- **Type/date:** first-party engineering blog series; index accessed 2026-09-16.
  Relevant posts are dated 2026-05-27 through 2026-07-20, including “Most of What
  Your Agent Learns Is Garbage,” “Agents Need to Forget,” “Stopping Agents From
  Reporting False Success,” “Sharing Learnings Without Leaking Secrets,” and
  “Plausible Is Not Proven.”
- **Evidence family:** production memory/learning operations and failure modes.
- **What was inspected:** index and post titles/snippets; individual posts were not
  all full-text reviewed in this pass. Therefore these are discovery leads with
  limited access depth, not verified findings.
- **Evidence status:** useful first-party negative-result agenda (garbage learnings,
  stale beliefs, false success, leakage), but no measured benchmark was established.
- **Access/copy:** public HTML links; no local copies retained; license/permission
  basis unknown.
- **Suggested role:** follow-up primary reading if the discussion needs forgetting,
  provenance, or security failure modes beyond benchmark gains.

### Additional leads screened out or retained as lower-priority

- **ClosedLoop AI blog:** [index](https://closedloopai.co/blog/). First-party posts
  dated July 2026 discuss failure clustering and drift, but the inspected search
  result exposed marketing-level summaries without reproducible measurements. Keep
  as a lead, not evidence.
- **RememberLoop:** [“How to build continuously improving agents”](https://blog.rememberloop.com/p/how-to-build-continuously-improving),
  2026-06-15. A personal engineering narrative about silent degradation and scheduled
  checks; no controlled result found in the inspected page. Lower priority than
  Postsyntax because the concrete loop was less fully specified.
- **Zeltrex “The Living Agent”:** [PDF](https://zeltrex.com/papers/the-living-agent-2026.pdf).
  Search discovery reports 280+ tasks across 10+ autonomous days at $0.24/task, but
  this claim was not full-text verified in the pass and the provenance/independence
  are unclear. Do not use numerically without primary inspection.
- **Self-improving-agent survey and Awesome list:** [survey site](https://self-improving-agent.com/),
  [repository](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents).
  Useful citation expansion and vocabulary, but secondary synthesis rather than
  practitioner evidence; existing research lanes already cover the major papers.

## Search queries, coverage, and gaps

Queries used on 2026-09-16 (Google/Bing-style web search, then first-party follow-up):

1. `site:github.com self improving agent benchmark 2026 adaptive coding agent experiment`
2. `site:blog.* self evolving agent 2026 experiment loop`
3. `self-improving coding agent technical report 2026 repository`
4. `agent learns from failures continual improvement engineering blog 2026`
5. `production continual learning loop agent weights 2026 engineering blog`
6. `self improving agent accuracy before after case study 2026`
7. `agent regression tests production failures self improvement blog`
8. `self evolving agent forgetting false success security leakage blog`
9. `site:shopify.engineering agent continual learning Sidekick`
10. `site:arcfusion.ai self-improving agent loop accuracy`
11. `site:hyperstruck.com/blog agent learns forget`
12. `site:github.com/BetterForAll/self-improving-agents`
13. `self-improving agents negative results production drift`
14. `researcher X self-improving agent production failures 2026`
15. `agent self improvement talk slides 2026 production`
16. `agent self modification security failure 2026 first party`

Coverage reached public first-party blogs, open-source experiment repositories, and
failure-oriented engineering writing. Direct X/Twitter posts and talks/slides did
not produce a verifiable new artifact in this pass; search snippets were not treated
as evidence. No new source was retained locally because public access did not establish
redistribution permission. No code was installed or executed.

Open gaps:

- Shopify's article needs primary artifacts or an author follow-up with task counts,
  model/version identifiers, held-out evaluation, judge calibration results, and
  ablations separating harness changes, data curation, and weight updates.
- ArcFusion and Zeltrex need raw datasets, held-out protocols, failure counts, and
  cost accounting before their headline gains can be compared with papers.
- BetterForAll needs pinned commit/date and reproducible seeded runs; the role of
  LLM judges and benchmark overfitting is unresolved.
- Hyperstruck's individual posts should be read in full before any claim about
  forgetting, leakage, or false-success rates is used.
- Social and talk coverage remains limited by searchability and access; no claim of
  exhaustive practitioner coverage is made.
