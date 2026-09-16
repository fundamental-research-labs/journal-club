# Claims

## Claim 1
**Claim:** AgentRxiv gives autonomous research agents a shared, searchable artifact store for cumulative research.

**Evidence:** The framework is described as a local preprint-server web application with upload, search, viewing, and JSON API routes. Uploaded papers have text and metadata extracted, are embedded with a SentenceTransformer, and are retrieved by cosine similarity against agent search queries.

**Caveats/Scope:** The implementation is evaluated as a local framework for agent-generated reports, not as a production-scale scientific repository or peer-review system.

**Source pointers:** `paper.pdf`, Section 3 and Figure 3.

## Claim 2
**Claim:** Access to prior agent-generated papers improves iterative discovery in the reported MATH-500 setting.

**Evidence:** In the sequential experiment, agents review N=5 prior AgentRxiv papers during literature review and improve from the 70.2% gpt-4o mini baseline to 78.2% with SDA. In the ablation with N=0 prior AgentRxiv papers, best accuracy plateaus at 73.4% and 73.8%.

**Caveats/Scope:** The evidence is from one research direction, "Improve accuracy on MATH-500 using reasoning and prompt engineering," using Agent Laboratory with specific model and evaluation settings.

**Source pointers:** `paper.pdf`, Section 3.1, Figures 4 and 5B.

## Claim 3
**Claim:** The best discovered method, Simultaneous Divergence Averaging, transfers beyond the benchmark where it was discovered.

**Evidence:** SDA improves the reported 0-shot baselines on GPQA, MMLU-Pro, and MedQA in the cross-benchmark test, and across five non-reasoning models it yields an average gain across four benchmarks while improving three of the four benchmark averages.

**Caveats/Scope:** The method is a prompt/reasoning technique that depends on temperature sampling, so the authors exclude some reasoning models. The averaged cross-model result includes a small negative average on GPQA.

**Source pointers:** `paper.pdf`, Section 3.1, Figure 5A-C, Appendix A.

## Claim 4
**Claim:** Parallel agent laboratories sharing results through AgentRxiv accelerate progress but trade off compute efficiency.

**Evidence:** Three labs run simultaneously, publish to AgentRxiv, and can retrieve one another's papers during later work. The parallel setup reaches early accuracy milestones sooner, reports a best MATH-500 result of 79.8%, and surpasses the best sequential result of 78.2%, but it uses 120 generated papers rather than 40.

**Caveats/Scope:** The comparison is specific to three parallel labs on MATH-500 reasoning-technique discovery; more labs, different coordination mechanisms, or different research tasks could change the trade-off.

**Source pointers:** `paper.pdf`, Section 3.2 and Figure 6.

## Claim 5
**Claim:** The paper treats autonomous-research outputs as unreliable without human or automated verification.

**Evidence:** The limitations section reports hallucinated experimental results, reward-hacking-like behavior during paper writing, code repair that can remove core functionality or print plausible fake outputs, and common failure modes in `mle-solver` and LaTeX generation. The authors state that reported accuracies were manually verified by humans.

**Caveats/Scope:** These are observed failure modes in the AgentRxiv and Agent Laboratory workflow; they motivate verification requirements rather than invalidating every generated result.

**Source pointers:** `paper.pdf`, Sections 4.1-4.3 and Discussion.

## Claim 6
**Claim:** The paper's novelty claim is cautious: discovered methods can be useful while remaining close to existing reasoning techniques.

**Evidence:** The authors report no plagiarism findings from three detectors on abstracts of top papers, but manual inspection suggests higher-performing discoveries are often perturbations of existing algorithms. SDA is compared to self-consistency, self-agreement, multi-chain reasoning, multi-agent debate, and Tree of Thoughts.

**Caveats/Scope:** Plagiarism detectors and manual inspection are first-pass checks, not comprehensive novelty proof, and the paper notes that other generated works may lack novelty.

**Source pointers:** `paper.pdf`, Section 3.3 and Appendix A.
