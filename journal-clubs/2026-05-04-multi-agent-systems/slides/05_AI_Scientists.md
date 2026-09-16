---
marp: true
theme: default
paginate: true
style: |
  section { font-size: 24px; }
  h1 { font-size: 36px; color: #2d3436; }
  h2 { font-size: 28px; color: #636e72; }
---

# AI Scientists Produce Results Without Reasoning Scientifically
**Rios-Garcia, Alampara, Gupta, Mandal, Mannan, Aghajani, Krishnan, Jablonka -- FSU Jena, IIT Delhi**

- **Question**: Do LLM-based "AI scientist" agents actually reason scientifically, or do they just execute workflows? Evaluated through 25,000+ agent runs across 8 scientific domains
- **Two evaluation lenses**: (i) performance decomposition (what explains success?) and (ii) epistemological trace analysis (what cognitive operations does the agent actually perform?)
- **Setup**: 3 frontier models (GPT-4o, Claude Sonnet 4.5, GPT-OSS-120B) x 2 scaffolds (ReAct, structured tool-calling) x 8 domains spanning workflow execution (molecular sim, surface construction, ML, AFM) to hypothesis-driven inquiry (spectroscopy, qualitative analysis, circuit inference)
- **Key finding**: The base model accounts for **41.4%** of explained variance in performance; the scaffold accounts for only **1.5%**. Scaffold engineering is nearly irrelevant compared to model capability

---

# Key Results

- **Reasoning breakdowns dominate across all domains**:
  - Evidence ignored in **68%** of traces
  - Beliefs never updated in **71%** of traces
  - Refutation-driven belief revision in only **26%**
  - Convergent multi-test evidence (multiple independent lines on one hypothesis) in only **7%**
  - Untested claims in **53%** overall, **63%** in hypothesis-driven domains
- **Agents don't adapt reasoning to task type**: evidence non-uptake is 82% in workflow domains, 66% in strategic reasoning, 60% in hypothesis-driven -- the same undisciplined pattern everywhere
- **Trace interventions**: Injecting near-complete successful trajectories helps for workflow tasks (where 1-2 steps suffice) but only near-complete trajectories (steps n-2 or n-1) help for hypothesis-driven tasks. Partial context doesn't rescue reasoning
- **Reliability compounds**: Pass^k (all k trials succeed) drops below 0.05 by k=4-6 for hypothesis-driven domains. Repeated attempts don't yield consistent success
- **IRT analysis**: reasoning ability gap between strongest and weakest model exceeds 5.3 standard units in qualitative analysis; knowledge gap alone doesn't explain failures

---

# Open Questions & Discussion

- **"Reasoning as a training target"**: The paper's core recommendation -- but how? RLHF optimizes for answer quality, not epistemic process. Would training on annotated reasoning traces (H -> T -> E -> U cycles) actually change base model behavior?
- **The scaffold irrelevance finding is striking**: 1.5% of variance means prompt engineering and orchestration barely matter. This challenges a lot of current "agent framework" work. Counter-argument: they only tested ReAct vs tool-calling -- more exotic scaffolds (tree search, explicit hypothesis tracking) might matter more
- **Human scientists also reason poorly** -- confirmation bias, p-hacking, etc. The bar for "scientific reasoning" is whether the *process* justifies the *result*, not perfection. But 68% evidence non-uptake is extreme
- **Connection to multi-agent design**: If you're building a multi-agent research system, adding a "reviewer" agent that enforces epistemic norms (did you test that hypothesis? did you incorporate that evidence?) might compensate for what the base model lacks. This is essentially the SGS Guide idea applied to scientific reasoning
- **Practical takeaway**: Outcome-based eval (did the agent get the right answer?) is insufficient. For any high-stakes domain, you need process-based eval -- and current agents fail process eval badly
