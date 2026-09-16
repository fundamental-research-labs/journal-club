# Claims

## Claim 1
**Claim:** AutoGen's main abstraction is the "conversable agent," a reusable agent interface that can receive messages, maintain conversational context, and respond using LLMs, humans, tools, or combinations of those capabilities.

**Evidence:** Section 2.1 defines conversable agents and describes built-in `ConversableAgent`, `AssistantAgent`, and `UserProxyAgent` classes. Figure 2 illustrates unified `send`, `receive`, and `generate_reply` interfaces plus configurable human input and code execution.

**Caveats/Scope:** This is a framework design claim, not evidence that any particular agent configuration is optimal. Actual behavior depends on the underlying LLM, tools, prompts, and application-specific settings.

**Source pointers:** `paper.pdf`, Abstract; Section 2.1; Figure 2.

## Claim 2
**Claim:** Conversation programming lets developers express both static and dynamic multi-agent workflows using a mix of natural-language control and programming-language control.

**Evidence:** Section 2.2 defines conversation-centric computation and conversation-driven control flow, then describes auto-reply mechanisms, custom reply functions, termination conditions, tool execution logic, function calls, and `GroupChatManager` for dynamic group chat.

**Caveats/Scope:** The paper demonstrates flexibility through examples rather than a formal expressiveness or developer-usability study.

**Source pointers:** `paper.pdf`, Section 2.2; Figures 2 and 3; Section 3.

## Claim 3
**Claim:** AutoGen's built-in two-agent pattern can be an effective out-of-the-box setup for autonomous math problem solving.

**Evidence:** In the MATH experiments using GPT-4 and a `sympy` execution environment, AutoGen reports 69.48% accuracy on the full MATH test set versus 55.18% for vanilla GPT-4. On 120 randomly selected level-5 problems, AutoGen is also the highest reported method among the compared systems.

**Caveats/Scope:** The comparison uses 2023-era systems and selected configurations; some baselines were not run on the full dataset because of manual effort or prior underperformance.

**Source pointers:** `paper.pdf`, Section 3 A1; Figure 4a; Appendix D, A1; Table 2.

## Claim 4
**Claim:** Interactive retrieval in AutoGen's Retrieval-augmented Chat improves QA performance over a non-interactive retrieval variant in the reported Natural Questions setup.

**Evidence:** The paper reports 25.88 F1 and 66.65 recall for Retrieval-augmented Chat with interactive retrieval, compared with 22.79 F1 and 62.59 recall without interactive retrieval and 15.12 F1 and 58.56 recall for DPR. Appendix D says about 19.4% of Natural Questions queries triggered an `UPDATE CONTEXT` operation.

**Caveats/Scope:** Results depend on the selected corpus, retriever, prompting, and GPT-3.5-turbo setup; the paper attributes some advantage over DPR to retriever differences, not only the conversation mechanism.

**Source pointers:** `paper.pdf`, Section 3 A2; Figure 4b; Appendix D, A2; Figure 8.

## Claim 5
**Claim:** AutoGen's modular agent design makes it straightforward to add a grounding agent that improves ALFWorld decision-making performance.

**Evidence:** The two-agent ALFChat setup matches ReAct at 54% average success, while adding a grounding agent raises average success to 69% and best-of-3 success to 77% in Table 3. The appendix case study attributes the gain to avoiding repeated commonsense action loops.

**Caveats/Scope:** The grounding agent is evaluated on ALFWorld's synthetic household tasks, so the result should not be generalized to all online decision-making environments.

**Source pointers:** `paper.pdf`, Section 3 A3; Figure 4c; Appendix D, A3; Table 3; Figure 10.

## Claim 6
**Claim:** AutoGen can reduce orchestration code and manual effort in multi-agent coding workflows that need separate writer, executor, and safeguard roles.

**Evidence:** In the OptiGuide reimplementation, the paper reports reducing core workflow code from over 430 lines to 100 lines. It also reports roughly 3x user-time savings in a 10-question coffee supply-chain study, 3x to 5x fewer user interactions across 2000 questions, and unsafe-code F1 gains of 8% with GPT-4 and 35% with GPT-3.5-turbo for the multi-agent design.

**Caveats/Scope:** The strongest manual-effort evidence is from one OptiGuide setting with an expert programmer and domain-specific dependencies; broader software-engineering generalization is not established here.

**Source pointers:** `paper.pdf`, Section 3 A4; Figure 4d; Appendix D, A4; Figure 11; Table 4.
