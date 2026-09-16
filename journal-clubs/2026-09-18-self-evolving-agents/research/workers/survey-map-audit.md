# Survey-map audit: self-evolving agents and recursive improvement

**Audit date/cutoff:** 2026-09-16. I inspected the current arXiv metadata/abstracts and version histories for three requested sources. Surveys are navigation aids; their taxonomies are not independent empirical evidence. Quantitative claims below are abstract-level leads pending primary-paper verification.

## 1. A Survey of Self-Evolving Agents

**Gao et al., arXiv:2507.21046.** Canonical: https://arxiv.org/abs/2507.21046. Submitted July 28, 2025 (v1); latest v4 January 16, 2026. The arXiv page labels it *Transactions on Machine Learning Research* (01/2026), 77 pages, and exposes a Creative Commons license link. Authors: Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou, Shaokun Zhang, Jiayi Zhang, Jinyu Xiang, Yixiong Fang, Qiwen Zhao, Dongrui Liu, Qihan Ren, Cheng Qian, Zhenghailong Wang, Minda Hu, Huazheng Wang, Qingyun Wu, Heng Ji, Mengdi Wang.

**Taxonomy/navigation value.** Organizes systems by what evolves (models, memory, tools, architecture), when (intra-test-time vs inter-test-time), and how (scalar rewards, textual feedback, single- vs multi-agent). It also maps evaluation metrics/benchmarks and safety, scalability, and co-evolution challenges. This is a useful map for ensuring the session covers weight/model adaptation, context/memory, procedural skills/tools, workflow/topology, and environment co-evolution.

**Audit finding.** The survey’s important methodological warning is that many benchmarks reset state between tasks, which cannot test accumulation, forgetting, or cross-task transfer. The session already addresses this with AgentStream, WikiSkill, Library Drift, and memory benchmarks. The survey should be cited as a taxonomy and gap statement, not as evidence that any mechanism works or that RSI is near ASI. Its broad ASI framing is a motivation/roadmap claim, not a measured result.

## 2. Self-Evolving Coding Agents

**Zhou et al., arXiv:2608.03392.** Canonical: https://arxiv.org/abs/2608.03392. Submitted August 4, 2026 (v1); v2 August 20; latest v3 August 29, 2026. Authors on v3: Hao Zhou, Haichuan Hu, Tianyu Luo, Ye Shang, Chunrong Fang, Zhenyu Chen, Liang Xiao, Quanjun Zhang. Subject is Software Engineering (cs.SE); arXiv exposes a Creative Commons license link. Companion collection: https://github.com/zhouhao1024/Awesome-Self-Evolving-Coding-Agents (license not checked).

**Taxonomy/navigation value.** Centers the object updated by evolution: agent framework, memory, skills/tools, model, workflow/topology, and environment/context. It adds two orthogonal axes: timing of evolution and software-specific evidence signals. The coding domain’s distinctive signals are executable tests, repository-level context, dependency/repository change, and trajectories from repair attempts.

**Audit finding.** This map makes consequential missing families visible for the main session: repository/framework self-rewrite and search; repair-experience memory; tool creation/mastery; coder-verifier or self-play model updates; multi-agent workflow/topology adaptation; and environment/dependency adaptation. These are mechanisms, not results. The survey’s cross-literature conclusions—feedback reliability, benchmark overfitting, reversibility, maintenance, safety, cost, and generalization—align with the session’s existing concern about regressions and should motivate screening of coding-specific primary work. Add the survey as navigation only; screen its repository for primary sources such as coding-harness evolution, Recuris/PILOT, and evaluator/verifier loops.

## 3. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

**Duan et al., arXiv:2609.11873v2.** Canonical: https://arxiv.org/abs/2609.11873. Submitted September 10, 2026 (v1); latest v2 September 15, 2026, within the September 16 cutoff. Authors: Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, Yumou Liu, Bangrui Xu, Yukai Wu, Sidi Chen, Yuhan Zhou, Haoyu Wang, Xiaoyou Yu, Shaokun Han, Xuzhou Zhu, Le Zhou, Bolin Lu, Wei Zhou, Jiachen Liu, Nuozhou Fang, Jiaxin Tian, Ruoyu Chen, Yuxuan Li, Kai Zuo, Kaiyan Zhang, Qianyu Yang, Zijie Wang, Jiantao Qiu, Conghui He, Guoliang Li, Bowen Zhou, Zhiyuan Liu, Zhoufutu Wen, Jihua Kang, Xuanhe Zhou, Fan Wu. Subjects cs.LG/cs.AI/cs.CL; arXiv exposes a Creative Commons license link.

**Conceptual contribution.** Proposes a five-level RSI roadmap: (1) autonomy over improvement execution, (2) autonomy over improvement strategy, (3) autonomy over experience acquisition, (4) autonomy over environment adaptation, and (5) recursive meta-improvement. It introduces a Headroom-Closed Index (HCI) for diagnosing remaining improvement headroom and discusses scientific discovery, embodied intelligence, and software engineering.

**Evidence audit.** The abstract says it draws on industry practice and preliminary empirical evidence but gives no reproducible experiment, sample, comparator, uncertainty, or held-out transfer result. Treat HCI and the five-level roadmap as proposed framing; inspect v2 full text before any numerical or “genuine RSI” claim. This is a consequential September frontier source for conceptual framing, but not a replacement for controlled evidence from WikiSkill, AgentStream, Library Drift, or the primary mechanisms.

## Missing or newly salient mechanism families

The two taxonomies together suggest four gaps worth screening in the existing corpus:

1. **Framework/self-rewrite and workflow-topology search.** The current materials cover harness evolution but should explicitly distinguish changing a prompt/skill library from changing the agent’s scaffold, delegation graph, or communication protocol.
2. **Executable-feedback coding loops.** Tests and repository state provide verifiable signals, but can overfit benchmark suites and create irreversible repository/tool changes. Coding-specific primary work should be screened for held-out repositories, rollback, and maintenance cost.
3. **Environment/dependency co-evolution.** Tool/API/interface drift is represented by EvoHarnessBench and Library Drift, but environment adaptation deserves a separate axis from memory retention: an agent can preserve a correct skill while the interface changes.
4. **Meta-improvement autonomy.** The RSI roadmap distinguishes executing a fixed improvement recipe from choosing the recipe, acquiring experience, and changing the environment. Existing positive results mostly establish lower levels; claims of recursive improvement should state which level is actually demonstrated.

The strongest consequential source to add to screening is **Self-Evolving Coding Agents v3**, because it supplies a coding-specific taxonomy and points to repository-level primary work. **The Last AI Built by Humans v2** should be added as a dated frontier/conceptual source with explicit “preliminary evidence” qualification. **Gao v4** should remain a foundational map and benchmark-gap citation, not an empirical source.

## Access and limitations

All three sources were inspected through arXiv metadata and abstracts, with version histories verified. No full-text methods/results were read in this audit, and no local copies were retained. The arXiv pages expose license links, but the exact license terms were not transcribed; download/retention should be checked before saving PDFs. The coding survey’s GitHub collection is a discovery index rather than a peer-reviewed evidence source. No source should support a quantitative claim until its cited primary paper and evaluation protocol are read.
