# Claims

## Claim 1
**Claim:** AndroidWorld turns Android UI automation into an executable, parameterized benchmark rather than a static action-matching dataset.

**Evidence:** The benchmark contains 116 tasks across 20 Android apps. Each task has initialization, success-checking, teardown, and seed-controlled parameter generation, allowing many goal variants from the same task template.

**Caveats/Scope:** The app suite is limited to open-source apps and built-in system apps that can run without login and keep relevant state locally.

**Source pointers:** `paper.pdf`, Abstract; Section 3.3; Table 1; Appendix D/Table 4

## Claim 2
**Claim:** Device-state inspection provides more durable rewards for mobile app tasks than superficial UI matching alone.

**Evidence:** AndroidWorld uses adb to inspect and manipulate app/system state such as files, SQLite databases, SMS messages, settings, and UI elements where appropriate. Table 2 gives validators for calendar events, SMS messages, files, timers, and composite tasks.

**Caveats/Scope:** Reward logic is manually authored and app-specific; some tasks still require UI-element validation when system-state inspection is impractical.

**Source pointers:** `paper.pdf`, Sections 3.4-3.5; Table 2; Appendix D.2-D.3

## Claim 3
**Claim:** Current baseline agents are far from human-level performance on AndroidWorld.

**Evidence:** In Table 3, the best AndroidWorld baseline is M3A with GPT-4 Turbo and accessibility-tree input at 30.6% success, compared with 80.0% human success. SeeAct, adapted from web navigation, reaches 15.5%.

**Caveats/Scope:** These numbers use the paper's evaluated models, seed 30, temperature 0, and per-task step limits; they should not be read as a current leaderboard for newer agents.

**Source pointers:** `paper.pdf`, Table 3; Section 4.2

## Claim 4
**Claim:** M3A's Android-specific prompting and reflection improve task success, but multimodal screenshot marking is not uniformly better than accessibility-tree input.

**Evidence:** With GPT-4 Turbo on AndroidWorld, M3A reaches 30.6% success with accessibility-tree input versus 19.8% for M3A-Simple. The GPT-4 Turbo Set-of-Mark variant reaches 25.4% on AndroidWorld but 67.7% on MobileMiniWoB++, showing different input modalities help in different task suites.

**Caveats/Scope:** The paper does not isolate every prompting component independently, and the modality comparison depends on benchmark, model, and accessibility-tree quality.

**Source pointers:** `paper.pdf`, Sections 4.1-4.2; Table 3; Appendix E

## Claim 5
**Claim:** Parameterized task variants reveal robustness failures that single static test instances can hide.

**Evidence:** Across three random seeds, M3A with GPT-4 Turbo and accessibility-tree input varies from 26.3% to 33.2% success. The robustness analysis shows task parameters can change required UI interaction patterns, such as needing horizontal scrolling to select hidden expense categories.

**Caveats/Scope:** The detailed robustness study uses a representative subset of tasks and 20 trials per task due to compute constraints.

**Source pointers:** `paper.pdf`, Section 5; Figure 3; Appendix E.4-E.5

## Claim 6
**Claim:** Web-oriented computer-use agents do not transfer cleanly to mobile app control.

**Evidence:** The authors adapt SeeAct to Android by adding mobile actions and using the accessibility tree instead of the DOM, but it underperforms M3A on AndroidWorld and struggles with mobile-specific actions, grounding, memory-intensive tasks, and recovery.

**Caveats/Scope:** This is evidence from one adapted web-agent baseline, not a general impossibility result for all web-agent architectures.

**Source pointers:** `paper.pdf`, Sections 4.1.2, 4.2, and 4.3; Table 3; Appendix E.6
