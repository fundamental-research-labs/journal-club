# Claims

## Claim 1
**Claim:** Multi-SWE-bench extends issue-resolving evaluation beyond Python with a human-validated multilingual benchmark.

**Evidence:** The benchmark contains 1,632 issue-resolving tasks from 39 repositories across Java, TypeScript, JavaScript, Go, Rust, C, and C++. The final set is produced after automated candidate filtering and manual verification.

**Caveats/Scope:** The benchmark targets seven non-Python languages and selected GitHub repositories with viable CI/build environments; it is not a comprehensive sample of all software ecosystems.

**Source pointers:** `paper.pdf`: Abstract; Sec. 3 "Multi-SWE-bench"; Sec. 3.2; Table 1.

## Claim 2
**Claim:** The dataset construction emphasizes executable, test-grounded instances rather than raw issue-PR pairs.

**Evidence:** The pipeline selects maintained repositories with CI/CD support, builds Docker environments, filters PRs by test-transition patterns such as Any->FAILED->PASSED, discards regressions or ambiguous transitions, and then applies dual annotation plus cross-review. The paper reports 2,456 automatically retained candidates and 1,632 final instances after manual verification by 68 annotators, with an internal QA team checking annotation quality.

**Caveats/Scope:** The quality standard depends on test availability, successful environment reconstruction, and annotator judgments; repositories without workable CI or clear tests are excluded.

**Source pointers:** `paper.pdf`: Sec. 3.1.1-3.1.5; Figure 2; Table 3.

## Claim 3
**Claim:** Current SWE-bench-oriented agents show limited generalization from Python to other programming languages.

**Evidence:** Table 4 reports consistently higher Python resolved rates than non-Python rates. For example, Claude-3.7-Sonnet with MopenHands resolves 52.20% of Python issues, versus 21.88% Java, 2.23% TypeScript, 5.06% JavaScript, 7.48% Go, 15.90% Rust, 8.59% C, and 14.73% C++.

**Caveats/Scope:** The comparison uses the paper's multilingual adaptations of Agentless, SWE-agent, and OpenHands; stronger language-specific tools or future agents may change the gap.

**Source pointers:** `paper.pdf`: Sec. 6.1.1; Table 4; Table 5.

## Claim 4
**Claim:** Agent workflow matters, but no single adapted method dominates all models and languages.

**Evidence:** The paper compares MagentLess, MSWE-agent, and MopenHands and reports that MopenHands is strongest in most language-level comparisons, while MSWE-agent and MagentLess still win selected cases. Table 4 shows the best Java result under MSWE-agent with Claude-3.7-Sonnet (23.44%) but the best C++ result under MopenHands with Claude-3.7-Sonnet (14.73%).

**Caveats/Scope:** These method rankings are based on resolved-rate tables for the tested model set and the authors' specific multilingual adaptations.

**Source pointers:** `paper.pdf`: Sec. 5.1; Sec. 6.1.2; Table 4; Table 5.

## Claim 5
**Claim:** Difficulty, patch length, and cross-file edits are major drivers of benchmark failure.

**Evidence:** The paper defines easy, medium, and hard using human estimated resolution time and reports that resolved rates decrease sharply as difficulty increases, with hard issues often near zero. It also finds that longer ground-truth fix patches and patches modifying more files correlate with lower resolved rates across methods.

**Caveats/Scope:** Patch length and file count are measured from ground-truth fixes, so they are retrospective explanatory factors rather than information normally available to an agent before solving.

**Source pointers:** `paper.pdf`: Sec. 3.2; Sec. 6.1.1; Sec. 6.2.3; Table 2; Table 5; Figures 13-14.

## Claim 6
**Claim:** Multi-SWE-RL is a related but separate scaling effort for RL data, not the same artifact as the manually verified benchmark.

**Evidence:** The paper releases 4,723 containerized issue-resolving instances across 76 repositories and the same seven languages as an initial Multi-SWE-RL community dataset. It explicitly says this release uses the same construction pipeline as Multi-SWE-bench but excludes the manual verification phase.

**Caveats/Scope:** The RL release is meant for scalable training-data creation and community contribution; its quality guarantees are weaker than the final Multi-SWE-bench benchmark.

**Source pointers:** `paper.pdf`: Abstract; Sec. 4; Sec. 7.
