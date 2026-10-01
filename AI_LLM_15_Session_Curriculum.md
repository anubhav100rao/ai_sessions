# Applied AI & LLM Engineering

## A practical curriculum for final-year B.Tech Computer Science students

**Format:** 15 sessions × 60 minutes, every Saturday  
**Dates:** 10 October 2026 – 16 January 2027  
**Total live instruction:** 15 hours  
**Level:** Short fundamentals refresher, followed by intermediate application engineering  
**Recommended project format:** Pairs or teams of three

This curriculum develops the ability to build, evaluate, and deploy useful LLM applications. Students progress from a model call to document retrieval, connected tools, workflows, and bounded agents. Demos and small coding exercises are part of every teaching session.

**Scheduling assumption:** October 10 means October 10, 2026. All 15 dates below are Saturdays, with no breaks. The schedule includes December 26 and January 2; adjust for the university's holiday and examination calendar before announcing it.

## 1. Curriculum design

### What changes from the tentative outline

| Original area | Recommended treatment |
|---|---|
| LLM basics, tokenization, embeddings, inference | One focused refresher. Revisit embeddings and inference later through practical implementation. |
| RAG, MCP, connectors | Teach these separately first: RAG supplies evidence, connectors integrate systems, and MCP standardizes an interface for context and tools. |
| LLM workflows and agentic demos | Build tool calling and a predictable workflow before introducing model-directed execution. |
| Agents and the agent loop | Implement one bounded agent, then cover state, memory, failure recovery, and evaluation. |
| Local LLMs and deployment | Include model selection, quantization, resource constraints, serving, and application deployment. |
| Examples and demos | Use one evolving project, with a visible failure case and a small student modification each week. |
| Additional topics | Add structured outputs, context management, evaluation, cost and latency measurement, security, and a practical introduction to fine-tuning. |

Only Session 1 is primarily foundational: **1 of 15 hours, or approximately 7%**. The remaining time covers applied topics, engineering practice, and project demonstrations. A few minutes of refresher material can appear when a later concept needs it.

### Expected learning outcomes

By the end, students should be able to:

1. Explain the token-generation loop and distinguish it from an agent's tool-use loop.
2. Build an LLM feature with a clear prompt, structured response, and validation.
3. Implement semantic search and a RAG pipeline that returns traceable citations.
4. Diagnose retrieval failures separately from answer-generation failures.
5. Connect an application to external data and tools through direct integrations and MCP.
6. Choose between a fixed workflow and an agent, and justify that choice.
7. Implement limits, permissions, state management, and failure handling around tool use.
8. Compare hosted and local inference using measured quality, latency, and resource use.
9. Explain when prompting, retrieval, or fine-tuning is appropriate.
10. Package an application for a reproducible demo and report its measured limitations.

### Prerequisites

- Python: functions, dictionaries, packages, and basic exception handling.
- Basic HTTP APIs, JSON, Git, and command-line familiarity.
- Basic understanding of vectors and similarity; no advanced linear algebra required.
- Prior exposure to a chatbot or generative AI tool.

Deep learning implementation, transformer mathematics, CUDA, and prior agent-framework experience are not prerequisites.

### Workload and teaching approach

The live course is exactly 15 hours. A polished portfolio project also benefits from **45–60 minutes of optional practice between sessions**. These extensions are identified separately and are not extra live classes.

For students attending only the live sessions, provide working starter code and completed checkpoints. Their goal is to understand, modify, and evaluate the supplied application. For the project track, students extend the same application between classes; they do not build a new project each week.

Most teaching sessions follow this rhythm:

| Time | Activity | Purpose |
|---|---|---|
| 0–5 minutes | Retrieval question or previous failure case | Connect to the preceding session. |
| 5–20 minutes | Focused concepts | Introduce only what the day's implementation needs. |
| 20–40 minutes | Instructor demo with visible inputs and outputs | Make the mechanism and a failure mode observable. |
| 40–55 minutes | Guided exercise using a prepared checkpoint | Make one meaningful change and inspect its effect. |
| 55–60 minutes | Questions and exit check | Confirm understanding and introduce optional practice. |

Keep setup and large downloads outside class. Run full benchmarks and training jobs beforehand; inspect representative results live. Stretch topics should be omitted when discussion or debugging needs the time.

## 2. Schedule at a glance

| Session | Saturday | Topic | Student checkpoint |
|---|---|---|---|
| 1 | 10 Oct 2026 | LLM essentials and the generation loop | Trace one model request and its output. |
| 2 | 17 Oct 2026 | Prompting, context, and structured outputs | Validate a structured response. |
| 3 | 24 Oct 2026 | Embeddings and semantic search | Retrieve relevant passages from a small corpus. |
| 4 | 31 Oct 2026 | Build a RAG application | Answer questions with source references. |
| 5 | 07 Nov 2026 | Improve and evaluate RAG | Compare two retrieval configurations. |
| 6 | 14 Nov 2026 | Tool calling and connectors | Execute a validated, permission-scoped tool call. |
| 7 | 21 Nov 2026 | MCP in practice | Expose and call a tool through an MCP server. |
| 8 | 28 Nov 2026 | LLM workflows with connected tools | Run a predictable multi-step workflow. |
| 9 | 05 Dec 2026 | Agents and the agent loop | Implement a bounded tool-using agent. |
| 10 | 12 Dec 2026 | Agent state, memory, and reliability | Recover from a tool failure and inspect a trace. |
| 11 | 19 Dec 2026 | Inference, local LLMs, and model selection | Compare local and hosted inference. |
| 12 | 26 Dec 2026 | Model adaptation and fine-tuning | Make an evidence-based adaptation decision. |
| 13 | 02 Jan 2027 | Serving, deployment, and observability | Run the application as a service. |
| 14 | 09 Jan 2027 | End-to-end evaluation and hardening | Produce a release candidate and quality report. |
| 15 | 16 Jan 2027 | Capstone demos and engineering review | Present the system, evidence, and trade-offs. |

## 3. Running project: Campus Knowledge Assistant

### Student-facing use case

Build an assistant that can answer questions about a fictional university, retrieve supporting documents, look up events, calculate relevant values, and prepare a helpdesk ticket for approval.

Example requests:

- “What are the project submission requirements? Cite the relevant section.”
- “Find next week's technical events and show their registration deadlines.”
- “The policy does not explain my situation. Prepare a helpdesk ticket for me to review.”
- “The event service is unavailable. Tell me what you could verify and what is missing.”

### Instructor-provided data

- Approximately 15–25 short, synthetic or public documents: project guidelines, academic FAQs, lab rules, and event notices.
- A prepared text extraction of those documents, so PDF parsing does not consume the RAG session.
- A small events database or mock API.
- A local helpdesk store with draft and approved states.
- Sample users and access roles, with no real student records.
- Development questions, known failure examples, and a separate final evaluation set.

### How the project grows

| Stage | Capability added |
|---|---|
| Sessions 1–2 | Model request, prompt template, validated answer format. |
| Sessions 3–5 | Search, RAG, citations, and an initial evaluation report. |
| Sessions 6–7 | Direct tools, connector adapter, and an MCP interface. |
| Sessions 8–10 | Workflow, bounded agent, session state, and failure recovery. |
| Sessions 11–12 | Model comparison and adaptation recommendation. |
| Sessions 13–14 | Service deployment, monitoring, and final quality checks. |
| Session 15 | Demo, architecture explanation, and measured results. |

### The two loops students must distinguish

```text
Generation loop within a language model:
Context → next-token scores → token selection → append token → repeat until stopping

Tool-use loop managed by an application:
User task → model response → validated tool request → tool execution
         → tool result added to context → next model response → stop or repeat
```

The generation process produces tokens. The application controls whether a requested tool runs, what data it receives, and when execution stops. A tool request is not permission to execute it.

## 4. Detailed session plans

### Session 1 — LLM essentials: what happens between a prompt and a response

**Date:** Saturday, 10 October 2026  
**Guiding question:** What does an LLM actually do when we call it?

**Learning outcomes**

- Trace tokenization, model inference, token selection, and stopping.
- Distinguish training from inference and model weights from supplied context.
- Explain why plausible text can still be incorrect.

**Core coverage**

- A brief map of AI, machine learning, generative AI, and LLMs; maximum three minutes.
- Tokens, vocabulary, context windows, and token budgets.
- Transformer intuition: attention uses context; no architectural derivation.
- Next-token generation, sampling, output limits, and streaming.
- Token embeddings inside a model versus passage embeddings used for retrieval.
- One-minute preview of the complete Campus Knowledge Assistant.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Diagnose prior knowledge with three questions; show the final project preview. |
| 5–20 | Explain the request lifecycle and generation loop. |
| 20–40 | Inspect tokens for English, code, and multilingual text; stream a response and inspect usage. |
| 40–55 | Students change one input or supported generation setting and compare outputs. |
| 55–60 | Exit check: explain why adding a document to a prompt does not retrain the model. |

**Demo and failure case:** Ask about a fictional campus rule that was never provided, then supply the relevant paragraph. Compare the answers and identify their evidence. If the model correctly declines the first request, discuss that result rather than expecting a hallucination.

**Checkpoint:** An annotated request-response trace with input tokens, output tokens, elapsed time, and one limitation.

**Optional practice — 45 minutes:** Run five prompt variations and record which changes affect response length, quality, and time.

**Reading:** Selected introductory sections of the [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) and its [text generation documentation](https://huggingface.co/docs/transformers/main/en/llm_tutorial).

### Session 2 — Prompting, context engineering, and structured outputs

**Date:** Saturday, 17 October 2026  
**Guiding question:** How do we turn a model response into something software can use?

**Learning outcomes**

- Design an instruction with a task, relevant context, examples, and an output contract.
- Validate structured responses and handle invalid or missing fields.
- Explain why valid JSON does not imply a correct answer.

**Core coverage**

- Clear instructions, few-shot examples, and separation of instructions from input data.
- Context engineering: selecting relevant content, ordering it, and managing the budget.
- Schema-constrained output where supported; application-side validation in all cases.
- Missing information, refusal responses, bounded retries, and error paths.
- Prompt versions and a tiny repeatable evaluation set.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Review a fluent answer that is difficult to use in an application. |
| 5–20 | Introduce context selection and output schemas. |
| 20–40 | Convert a campus query into structured fields; show validation and one rejected response. |
| 40–55 | Students add a required field and an explicit missing-information case. |
| 55–60 | Exit check: distinguish a schema error from a factual error. |

**Demo and failure case:** Extract `topic`, `requested_action`, and `missing_information` from a helpdesk request. A malformed or incomplete response must take a visible error path instead of silently entering the application.

**Checkpoint:** A structured-output helper and five development examples.

**Optional practice — 45 minutes:** Compare two prompt versions on the same examples. Report validation success separately from content correctness.

### Session 3 — Embeddings and semantic search

**Date:** Saturday, 24 October 2026  
**Guiding question:** How can we find relevant text when the question uses different words?

**Learning outcomes**

- Embed documents and queries using a compatible retrieval model.
- Retrieve top-k passages and inspect their relevance.
- Identify cases where keyword search is useful.

**Core coverage**

- Passage embeddings, vector dimensions, and cosine similarity.
- Query/document compatibility, including model-specific encoding conventions.
- Keyword versus semantic search: exact course codes versus paraphrased questions.
- Chunk identifiers, metadata, and the purpose of an index.
- Similarity scores as ranking signals, not probabilities that an answer is true.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Compare an exact keyword query with a paraphrased question. |
| 5–20 | Explain embeddings and nearest-neighbor retrieval. |
| 20–40 | Search a prepared corpus and inspect the top results, scores, and metadata. |
| 40–55 | Students change top-k and compare one keyword query with one paraphrase. |
| 55–60 | Exit check: explain why unrelated embedding models cannot be mixed in one index. |

**Demo and failure case:** Search for “When must we submit the final project?” against a passage titled “Capstone delivery deadline.” Then test an exact identifier where a lexical match may work better.

**Checkpoint:** A search function returning passage text, source ID, and score.

**Optional practice — 45 minutes:** Label relevant passages for ten questions. Preserve this set for RAG evaluation.

**Reading:** [Sentence Transformers: Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html).

### Session 4 — Build a RAG application with citations

**Date:** Saturday, 31 October 2026  
**Guiding question:** How do we make an answer depend on retrievable evidence?

**Learning outcomes**

- Connect ingestion, retrieval, prompt assembly, and answer generation.
- Attach source references to answers and inspect whether they support the claims.
- Handle questions the document collection cannot answer.

**Core coverage**

- Retrieval-augmented generation: ingest → chunk → embed → index → retrieve → generate.
- Offline indexing versus online query processing.
- Chunk boundaries, overlap, source metadata, and context limits.
- Evidence-grounded instructions and traceable citations.
- Abstention and the limits of retrieval: RAG does not guarantee correctness.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Recall the search function built in Session 3. |
| 5–20 | Draw the RAG pipeline and separate indexing from answering. |
| 20–40 | Build a cited answer using retrieved passages; inspect its assembled context. |
| 40–55 | Students add one document and test one answerable and one unanswerable question. |
| 55–60 | Exit check: locate a failure in ingestion, retrieval, or generation. |

**Demo and failure case:** Compare model-only and RAG responses to a fictional project-policy question. Include a document whose relevant sentence is split across an unhelpful chunk boundary.

**Checkpoint:** A minimal RAG assistant that exposes retrieved passages alongside the answer.

**Optional practice — 60 minutes:** Add five short documents and answer the ten labeled questions. Mark unsupported statements even when the response contains citations.

### Session 5 — RAG quality: retrieval improvements and evaluation

**Date:** Saturday, 7 November 2026  
**Guiding question:** How do we tell whether a retrieval change actually helped?

**Learning outcomes**

- Score retrieval and generated answers separately.
- Compare a baseline with one targeted improvement.
- Diagnose irrelevant, outdated, or incomplete evidence.

**Core coverage**

- Retrieval hit rate at k; recall at k when all relevant passages are labeled.
- Answer correctness, evidence support, citation accuracy, and appropriate abstention.
- Metadata filters, hybrid lexical/vector retrieval, and reranking.
- Document versioning and freshness.
- Development versus held-out evaluation questions.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Inspect one incorrect answer and its retrieved evidence. |
| 5–20 | Define the scorecard and explain the candidate improvements. |
| 20–40 | Compare baseline retrieval with a prepared reranking pipeline on the same questions. |
| 40–55 | Students change one setting and inspect two improved or regressed cases. |
| 55–60 | Exit check: explain why increasing top-k can make an answer worse. |

**Demo and failure case:** Retrieve both an old and a current version of a policy. Show how version metadata affects relevance; then inspect a paraphrased query where reranking changes the order.

**Checkpoint:** A small comparison table with quality, latency, and representative failures. Hybrid search is a conceptual or prepared-code extension; students need not implement every improvement in this hour.

**Optional practice — 60 minutes:** Test one chunking or retrieval change across the development questions. Keep it only if the evidence supports the change.

**Reading:** [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html).

### Session 6 — Tool calling and connectors

**Date:** Saturday, 14 November 2026  
**Guiding question:** How does a model ask an application to retrieve data or perform an action?

**Learning outcomes**

- Define a tool's name, description, arguments, and result format.
- Execute a tool request only after validation and permission checks.
- Explain what a connector contributes beyond a model call.

**Core coverage**

- Tool-call lifecycle: model request → validate → execute → return result → respond.
- Direct API integrations and connectors to files, databases, and services.
- Read versus write tools, scoped credentials, and server-side authorization.
- Timeouts, API errors, and tool-result size limits.
- Approval before consequential actions; credentials remain outside model context.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Compare answering from a static document with looking up a current event. |
| 5–20 | Explain tool schemas and application-controlled execution. |
| 20–40 | Call `lookup_event` through a connector to a mock service and return its result to the model. |
| 40–55 | Students add argument validation and test a timeout or invalid identifier. |
| 55–60 | Exit check: identify which component is responsible for authorization. |

**Demo and failure case:** The assistant must use an event lookup result instead of inventing a registration deadline. A deliberately malformed request is rejected by application code.

**Checkpoint:** One validated read tool, with a recorded successful and failed call. Show a draft-ticket tool as a prepared extension.

**Optional practice — 45 minutes:** Wrap one additional synthetic data source and add two error cases. Keep all credentials in the application environment.

### Session 7 — MCP: connect tools through a standard interface

**Date:** Saturday, 21 November 2026  
**Guiding question:** How can different AI applications discover and use the same integration?

**Learning outcomes**

- Identify an MCP host, client, and server in a running example.
- Expose an existing function through an MCP server.
- Distinguish tools, resources, and prompts.

**Core coverage**

- MCP as an integration protocol; connectors may use MCP or a direct API.
- Host/client/server responsibilities and tool discovery.
- Tools for callable operations, resources for contextual data, prompts for reusable templates.
- Local stdio versus remote Streamable HTTP at a conceptual level.
- Explicit permissions and data boundaries; using MCP does not automatically make a tool safe.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Revisit the direct event integration from Session 6. |
| 5–20 | Map its responsibilities to MCP components. |
| 20–40 | Run a prepared local server, discover its tools, and call it from a compatible client. |
| 40–55 | Students modify one tool description or argument schema and inspect the result. |
| 55–60 | Exit check: explain why MCP and RAG solve different problems. |

**Demo and failure case:** Expose `search_campus_docs` and `lookup_event`. Show a denied call outside an allowed data scope. Use a supplied server scaffold so setup remains short.

**Checkpoint:** A working MCP tool with documented inputs, outputs, and allowed access.

**Optional practice — 60 minutes:** Expose the existing document search function and document how the host reaches the underlying data.

**Reading:** The official [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture). Match the SDK and protocol version to the instructor's tested environment.

### Session 8 — LLM workflows using connected tools

**Date:** Saturday, 28 November 2026  
**Guiding question:** When should software decide the sequence of steps?

**Learning outcomes**

- Implement a workflow with explicit stages and routing rules.
- Pass validated state between stages.
- Add a review gate before a write action.

**Core coverage**

- Prompt chaining and routing, with parallel execution as an optional illustration.
- Deterministic control flow around probabilistic model outputs.
- Workflow state, branching, error paths, and bounded retries.
- Connecting retrieval, event lookup, and ticket drafting.
- Human review and preventing duplicate writes after retries.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Decompose a student-support request into explicit steps. |
| 5–20 | Explain workflow state and routing. |
| 20–40 | Run classify → retrieve or look up → draft → validate → request review. |
| 40–55 | Students add one routing branch or a missing-information path. |
| 55–60 | Exit check: explain which decisions belong in code. |

**Demo and failure case:** A mock connector times out. The workflow reports the missing result and offers a draft for review. It must not submit a ticket merely because a model requested submission.

**Checkpoint:** A workflow diagram and one end-to-end run with observable intermediate state.

**Optional practice — 45 minutes:** Add one recovery path and compare it against an unstructured single-prompt attempt.

**Reading:** The workflow/agent distinction in [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).

### Session 9 — Agents and the agentic loop

**Date:** Saturday, 5 December 2026  
**Guiding question:** When should the model choose the next action?

**Learning outcomes**

- Implement a small model/tool/result loop using supplied helpers.
- Explain the trade-off between flexible execution and predictability.
- Enforce stopping rules independently of model instructions.

**Core coverage**

- Agent components: task, model, tools, state, execution policy, and stop conditions.
- Dynamic tool selection compared with Session 8's fixed workflow.
- Maximum steps, elapsed-time limits, token budgets, and tool allowlists.
- Handling “no tool needed,” missing information, and unsuccessful tasks.
- Observable calls and results as debugging evidence; private model reasoning is not required.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Show a request requiring a variable sequence of lookups. |
| 5–20 | Walk through the bounded agent loop. |
| 20–40 | Run the same request through a fixed workflow and a small agent. |
| 40–55 | Students add a step limit and a repeated-call stop condition. |
| 55–60 | Exit check: give one task for which a workflow is preferable. |

**Demo and failure case:** The agent searches documents, looks up an event, and prepares an answer. A tool then returns an inconclusive result; the agent must stop or request clarification rather than loop indefinitely.

**Checkpoint:** An agent with a small allowed tool set and a trace showing its stopping condition.

**Optional practice — 60 minutes:** Compare workflow and agent behavior on five tasks, recording task success, tool calls, time, and usage.

**Stretch only:** Discuss when independent subtasks could justify multiple agents. Multi-agent implementation is outside the required course scope.

### Session 10 — Agent state, memory, and reliability

**Date:** Saturday, 12 December 2026  
**Guiding question:** What must an application remember, and what should it discard?

**Learning outcomes**

- Separate conversation history, task state, and persistent memory.
- Recover from a tool failure without duplicating a write.
- Evaluate the actual task result rather than only the final message.

**Core coverage**

- Structured state, context truncation, and summarization trade-offs.
- Session isolation and explicit retention or deletion choices.
- Checkpoints, bounded retries, and idempotency for writes.
- Trace inspection: tool names, arguments, results, timings, and final state.
- Task success, unnecessary tool calls, failure recovery, and repeated trials.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Inspect a failed or repeated action from an agent trace. |
| 5–20 | Explain state boundaries and recovery rules. |
| 20–40 | Resume a prepared interrupted run and verify the mock helpdesk record. |
| 40–55 | Students fix one state-handling bug and rerun a failure case. |
| 55–60 | Exit check: explain why “ticket created” is not proof that it exists. |

**Demo and failure case:** A mock service creates a ticket but its response is lost. Replaying the approved operation with the same idempotency key returns the existing record instead of creating another.

**Checkpoint:** One recoverable execution trace and a check against the resulting application state.

**Optional practice — 60 minutes:** Add failure scenarios for a timeout, empty result, and repeated call. Try selected tasks multiple times and report variation.

**Reading:** Selected sections of [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

### Session 11 — Inference, local LLMs, and model selection

**Date:** Saturday, 19 December 2026  
**Guiding question:** What changes when we run the model ourselves?

**Learning outcomes**

- Call a local model through a prepared endpoint.
- Explain major resource and latency trade-offs.
- Compare models against the same application tasks.

**Core coverage**

- Hosted API versus self-hosted model; open weights and model licensing.
- Prefill versus decoding, time to first token, and output tokens per second.
- Model weights, KV cache, context length, and runtime memory.
- Quantization: smaller weight storage with potential quality trade-offs.
- Model capability checks: language, structured outputs, tools, and context needs.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Inspect the same task answered by two different models. |
| 5–20 | Explain inference stages and memory constraints. |
| 20–40 | Run a pre-downloaded local model and compare it with the hosted baseline. |
| 40–55 | Students run three prepared prompts or inspect supplied benchmark records. |
| 55–60 | Exit check: explain why smaller model files do not determine total runtime memory. |

**Demo and failure case:** A compact local model answers a simple extraction task but fails a more demanding tool task. Assess whether it is suitable for a narrower application role.

**Checkpoint:** A comparison of quality, first-token delay, completion time, and observed memory for a specified environment.

**Optional practice — 45 minutes:** Repeat the development questions against the local endpoint and recommend which tasks it can support.

**Delivery note:** Use an instructor machine or shared endpoint when student hardware is insufficient. A GPU is not required for course participation. Keep CPU examples small and provide recorded measurements as a fallback.

**Reading:** [Ollama Quickstart](https://docs.ollama.com/quickstart) for local execution; [vLLM Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/) as an optional serving reference.

### Session 12 — Model adaptation: prompting, RAG, and fine-tuning

**Date:** Saturday, 26 December 2026  
**Guiding question:** When does changing the model make more sense than changing its context?

**Learning outcomes**

- Select an adaptation method for a clearly stated problem.
- Describe supervised fine-tuning and LoRA at a practical level.
- Detect basic dataset leakage and misleading improvement claims.

**Core coverage**

- Prompting for instructions and examples; RAG for retrievable knowledge.
- Supervised fine-tuning for learned behavior, task patterns, or output style.
- LoRA: train small adapter updates while freezing base-model weights.
- QLoRA as a brief extension using a quantized base model.
- Dataset quality, training/validation/test separation, and held-out comparison.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Sort three application problems by likely adaptation approach. |
| 5–20 | Explain supervised adaptation and the LoRA concept. |
| 20–40 | Walk through a prepared notebook, training logs, and base-versus-adapter outputs. |
| 40–55 | Students inspect sample records for leakage, inconsistency, or poor labels. |
| 55–60 | Exit check: justify one case where fine-tuning would be unnecessary. |

**Demo and failure case:** Compare a base model, a stronger prompt, and a pre-trained adapter on synthetic helpdesk classification. Inspect a case where apparent improvement disappears on held-out examples.

**Checkpoint:** A short adaptation recommendation supported by evaluation results and data requirements.

**Optional practice — 45 minutes:** Curate twenty training examples and a separate small evaluation set. Training is an optional GPU exercise, not a completion requirement; this small dataset is for learning the process, not demonstrating production readiness.

**Scope boundary:** Do not train a model from scratch or wait for fine-tuning to finish during class. Fine-tuning and RAG can be combined, and neither guarantees factual accuracy.

**Reading:** [Hugging Face PEFT: LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora).

### Session 13 — Serving, deployment, and observability

**Date:** Saturday, 2 January 2027  
**Guiding question:** What does the application need beyond a working notebook?

**Learning outcomes**

- Run the assistant behind an application API.
- Distinguish application deployment from model serving.
- Capture useful performance and failure information.

**Core coverage**

- UI → application API → retrieval/tools → hosted or local model endpoint.
- Configuration, secrets, dependency pinning, and persistent indexes.
- Request timeouts, rate limits, concurrency limits, and basic authentication.
- Structured logs with request IDs, tool spans, latency, token usage, and errors.
- Container packaging and a reproducible start procedure.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Trace a request through the complete application. |
| 5–20 | Explain service boundaries and essential operational controls. |
| 20–40 | Start a prepared FastAPI service and simple UI; inspect one request's logs. |
| 40–55 | Students add a health check or one useful measurement and simulate an unavailable dependency. |
| 55–60 | Exit check: explain what should happen when the model endpoint times out. |

**Demo and failure case:** Run the assistant as a local service or private lab deployment. Stop a dependency and verify that the user sees a useful failure message and the operator sees a correlated error.

**Checkpoint:** A runnable service with a health check, example request, and basic logs. Show a prepared container build; students are not expected to learn all of Docker in this session.

**Optional practice — 60 minutes:** Start the project on a second environment using its README. Record setup failures and fix the instructions.

**Delivery note:** A reproducible local deployment satisfies the core requirement. Public cloud deployment is optional and depends on institutional accounts and budget.

**Reading:** [FastAPI: Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/).

### Session 14 — End-to-end evaluation, security, and release readiness

**Date:** Saturday, 9 January 2027  
**Guiding question:** What evidence would make us comfortable letting someone else use this?

**Learning outcomes**

- Run an end-to-end evaluation with a documented baseline.
- Test an indirect prompt-injection attempt and an authorization boundary.
- Identify unresolved limitations and make a release decision.

**Core coverage**

- Component tests versus task-level evaluations.
- Code-based checks, human rubrics, and the limitations of model-based judges.
- Untrusted instructions in documents and tool results.
- Application-enforced access control, output handling, and approved writes.
- Quality, latency, usage, and regression reporting.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Review the release criteria and known development failures. |
| 5–20 | Explain the evaluation report and attack boundaries. |
| 20–40 | Inspect a prepared full-suite report and run selected failure cases live. |
| 40–55 | Students fix one development failure or strengthen one enforcement check. |
| 55–60 | Exit check: state one remaining limitation and its user-visible consequence. |

**Demo and failure case:** Insert a malicious instruction into a synthetic retrieved document. Check whether the assistant follows it and whether application permissions prevent an unauthorized action. Discuss residual risk; a prompt telling the model to ignore attacks is not a complete defense.

**Checkpoint:** A release candidate, development evaluation report, and limitations list. Freeze the candidate before the instructor runs the held-out set; report those results without tuning on the hidden cases.

**Optional practice — 60 minutes:** Prepare the final demo and reproduce the reported results. If the candidate changes after final evaluation, label the old score as belonging to the earlier version and arrange a fresh evaluation.

**Reading:** [OWASP: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/).

### Session 15 — Capstone showcase and engineering review

**Date:** Saturday, 16 January 2027  
**Guiding question:** Can we demonstrate a useful system and explain why it behaves as it does?

**Learning outcomes**

- Explain the architecture using a real request.
- Demonstrate success, a failure path, and a permission boundary.
- Defend design choices using measurements rather than feature count.

**60-minute plan**

| Minutes | Activity |
|---|---|
| 0–5 | Introduce the review rubric and demonstration format. |
| 5–41 | Six team demos of six minutes each: four-minute demo and two-minute review. |
| 41–51 | Compare architectures, results, and recurring failure patterns. |
| 51–57 | Individual architecture questions and short exit assessment. |
| 57–60 | Explain portfolio packaging and suitable next learning steps. |

**Required demo sequence**

1. Show the user problem and trace one request through the architecture.
2. Answer a question with supporting evidence.
3. Execute a tool-backed task with visible state and permission handling.
4. Demonstrate an unanswerable question or failed dependency.
5. Show one measured improvement and one unresolved limitation.

**Cohort scaling:** The live schedule supports six teams. For larger cohorts, collect a short recording from every team before class, review those outside the live hour, and select six contrasting projects for live discussion. Preserve equal assessment criteria for all teams.

**Final checkpoint:** Repository, runnable application, evaluation report, architecture diagram, and short demo recording.

## 5. Recommended teaching stack

Use one consistent stack throughout. Introduce abstractions only after students have seen the underlying request, retrieval step, or tool loop.

| Layer | Recommended default | Teaching choice |
|---|---|---|
| Language | Python, using one instructor-tested version | Reuse students' existing programming skills. |
| Model access | One hosted provider through a small application wrapper | Avoid changing SDKs every week. Verify structured-output and tool support before class. |
| Output validation | Pydantic or JSON Schema validation | Make the output contract explicit. |
| Embeddings | One compact Sentence Transformers retrieval model | Keep document and query encodings compatible. |
| Search | NumPy similarity for the first small demo; one prepared persistent index thereafter | Teach ranking before database administration. |
| Tools and data | Python functions, a mock REST service, and SQLite | Keep integrations inspectable and reproducible. |
| MCP | Official Python SDK and a compatible test client or inspector | Use a pinned, tested combination. |
| Orchestration | Plain Python control flow | Make routing, state, and stop conditions visible. |
| Local inference | Ollama on the instructor machine or a shared endpoint | Let students use the same application with another model backend. |
| Adaptation | Prepared Transformers/PEFT notebook and adapter | Keep GPU work out of the critical classroom path. |
| Application | FastAPI plus a small prepared UI | Focus the lesson on system behavior. |
| Evaluation | Versioned cases, assertions, and a CSV/JSON score report | Keep criteria understandable without introducing another platform. |

Optional frameworks can be introduced as a brief mapping exercise after the plain-Python implementation. Do not require students to learn several orchestration frameworks, vector databases, and cloud platforms within these 15 hours.

Model names, software releases, service limits, and pricing change. Select and test exact versions before the course; record model identifiers and relevant configuration in each experiment. No particular paid subscription or commercial connector is required by this curriculum.

## 6. Capstone scope and assessment

### Minimum project scope

- A clearly stated user problem and a small documented corpus.
- RAG with source references and an insufficient-evidence path.
- At least two tools, including one exposed through MCP.
- A working bounded agent plus the earlier workflow checkpoint for comparison.
- Explicit state and server-side permission handling.
- At least one simulated write that requires review and avoids duplicate execution.
- A reproducible local service or private hosted demo.
- An evaluation report covering quality, latency, usage, and known limitations.

Students may choose a workflow as their final application's default if their comparison supports that decision. Preserve the bounded-agent exercise as evidence that they understand both designs. Fine-tuning, a public deployment, a local model, and multiple agents are not mandatory capstone components.

Equivalent project themes include a public-document research assistant, an open-source repository assistant, or a synthetic IT helpdesk assistant. Keep the same retrieval, tool, evaluation, and permission requirements.

### Suggested course assessment

If this is an assessed course, use the following optional weighting:

| Component | Weight | Evidence |
|---|---:|---|
| Weekly checkpoints | 35% | Small working modifications and brief observations. |
| Individual concept checks | 15% | Explain loops, evidence, state, and architecture choices. |
| Team capstone | 50% | Runnable project, report, demonstration, and individual contribution. |
| **Total** | **100%** | |

For a non-credit workshop series, use the same criteria as feedback without assigning grades. Evaluate AI-assisted code by whether students can explain it, modify it, and verify its behavior.

### Capstone rubric

| Criterion | Weight |
|---|---:|
| Problem definition and architecture choices | 15% |
| Retrieval, answer quality, and supporting evidence | 20% |
| Tool integration, workflow/agent behavior, and reliability | 20% |
| Evaluation quality and justified comparisons | 20% |
| Permissions, failure handling, and data boundaries | 10% |
| Reproducibility, documentation, and demo clarity | 15% |
| **Total** | **100%** |

Do not reward extra agents, integrations, or frameworks merely for increasing complexity.

## 7. Evaluation plan students can actually use

### Test set

Grow the development set from five examples in Session 2 to twenty by Session 10. The instructor supplies ten additional held-out cases for final evaluation. Distribute the thirty cases approximately as follows, with each case assigned one primary category:

| Category | Cases | What to verify |
|---|---:|---|
| Document questions | 12 | Relevant retrieval, correct answer, supporting citations. |
| Tool-backed requests | 6 | Correct tool, valid arguments, correct resulting state. |
| Multi-step tasks | 4 | Completion, justified calls, and stopping behavior. |
| Missing or ambiguous information | 4 | Abstention or clarification instead of unsupported certainty. |
| Adversarial or permission-boundary cases | 4 | No unauthorized action or cross-user data access. |
| **Total** | **30** | |

Include a mix of categories in both development and held-out sets. Keep duplicate and near-duplicate questions from leaking between them. This is a classroom diagnostic set, not enough to establish production reliability.

### Scorecard

| Metric | Practical definition |
|---|---|
| Retrieval hit rate at k | Fraction of answerable retrieval questions with at least one labeled relevant passage in the top k. |
| Retrieval recall at k | Retrieved relevant passages divided by all labeled relevant passages, per question; use only when relevance labels are sufficiently complete. |
| Answer correctness | Human score: 0 = wrong, 1 = partly correct, 2 = correct against the reference. |
| Evidence support | Whether each material factual claim is supported by the supplied sources. |
| Citation correctness | Whether the cited passage supports the associated claim. |
| Appropriate abstention | Correct handling of questions that cannot be answered from available evidence. |
| Task success | Whether the requested, authorized result exists in the application state. |
| Permission enforcement | Whether denied reads and unapproved writes are blocked by application code. |
| Efficiency | Tool calls, input/output tokens, and elapsed time per task. |
| Repeatability | Variation across repeated runs of selected agent tasks. |

For hosted calls, estimate cost from actual usage and the provider's recorded rates at evaluation time. Include tool, retrieval, and hosting charges where applicable. For local execution, report hardware and runtime separately; zero API fees do not mean zero operating cost.

Use code assertions for schemas, permissions, and database state. Use a short human rubric for nuanced answers. Any model-based grader is an aid that needs human calibration. These complementary grading approaches are discussed in [Anthropic's agent evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

### Final comparison

Each team should present at least one controlled comparison, such as:

- Baseline retrieval versus reranking.
- Fixed workflow versus bounded agent.
- Hosted versus local model.
- Baseline prompt versus improved prompt or prepared adapter.

Keep the questions and scoring method fixed, change one main factor, report regressions as well as improvements, and identify the exact system version evaluated.

## 8. Instructor preparation and delivery notes

### Before Session 1

1. Send a short diagnostic on Python, APIs, vectors, and prior LLM exposure. Provide targeted refresher reading to students who need it.
2. Supply a tested environment, setup instructions, a sample model call, and a no-credentials fallback notebook with recorded outputs.
3. Prepare starter and completed checkpoints for each session. Clearly mark student TODOs so each live exercise fits into fifteen minutes.
4. Prepare the synthetic corpus, mock services, access roles, and development/held-out cases.
5. Choose a hosted model, embedding model, and local model appropriate to available hardware and permitted usage.
6. Benchmark the demos, pre-download assets, and save short recordings for service or network outages.
7. Set a course usage budget after a rehearsal. Use scoped student access or an instructor-controlled gateway rather than distributing a shared secret key.
8. Confirm the university's calendar, team count, and presentation format.

### During each session

- State the user problem before introducing a framework or technical term.
- Show the prompt/context, retrieved sources, or tool calls so students can see what caused the output.
- Include one failure case and ask students to locate the failing component.
- Change one variable at a time when comparing behavior.
- End with a small checkpoint, not a second full assignment.
- If setup fails, switch to the completed checkpoint or recorded trace and preserve discussion time.

### Suggested repository organization

```text
campus-assistant/
├── README.md
├── requirements.txt          # Pinned, tested dependencies
├── .env.example             # Variable names only; no secrets
├── data/                    # Synthetic/public source documents
├── notebooks/               # Short concept demonstrations
├── checkpoints/             # Starter and completed session versions
├── app/                     # UI/API, retrieval, and orchestration
├── tools/                   # Validated service integrations
├── mcp_server/              # MCP exposure of existing tools
├── evals/                   # Development cases and grading helpers
├── reports/                 # Metrics, traces, and comparisons
└── deployment/              # Container and startup configuration
```

Keep the instructor's held-out evaluation cases outside the student repository until assessment is complete.

### Topics intentionally reserved for follow-on courses

- Full transformer derivations, backpropagation, and pretraining from scratch.
- Distributed training and large-scale GPU infrastructure.
- Detailed reinforcement learning and preference optimization.
- Complex multi-agent coordination and autonomous computer-use systems.
- Graph RAG, advanced multimodal pipelines, and custom embedding training.
- Large-scale production operations, Kubernetes, and enterprise authentication implementation.

These are suitable next steps after students can build and evaluate a small end-to-end LLM application. The outcome of this course is a working, explainable prototype with measured limitations and a clear path for further improvement.

---

**Reference note:** Linked resources are primary documentation or first-party engineering guidance, checked on 1 October 2026. Session sequencing, exercises, assessment weights, and time allocations are curriculum recommendations. The instructor should recheck API examples and compatibility before delivery.
