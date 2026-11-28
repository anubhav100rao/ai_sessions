# Session 8 — LLM Workflows & Decision Models (28 Nov 2026)

**Today's question:** when should the software decide the order of steps, and who makes each decision along the way?

**Line to repeat:** The AI understands the words. The rules make the decision. A human signs off on what matters.

## Files in this folder

| File | What it's for |
|---|---|
| `workflow_lab.html` | Interactive lab: a Lakeview helpdesk workflow, the refund decision table and tree, the "Who decides?" game, and a run log. Opens in any browser. |
| `workflow_server.py` | Optional. Serves the lab and sends its AI steps to a real model through OpenRouter. Standard library only, no installs. |

## Online links

- Slides (Google Slides, 20 slides with speaker notes): https://docs.google.com/presentation/d/1oak4_-u_A0Z337m9BsCMQ9QsxoZXBYOASgrdD_Oj7Og/edit?usp=sharing

## Running it

**With a real model (recommended):**

```
cd ~/development/ai_sessions/session08_workflows
python3 workflow_server.py
# open http://localhost:8808
```

- The key comes from `OPENROUTER_API_KEY` in `~/development/accio-ai/xray-demo/.env` (or `--env PATH`). It stays on your laptop; the browser page never sees it.
- Only two light models are allowed: **GPT-6 Luna** `openai/gpt-6-luna` (default) and **GPT-5.6 Terra** `openai/gpt-5.6-terra`. The `.env` MODEL line is ignored.
- That key's `.env` comment says it **expires 2026-11-28**. After that, put a new key in the `.env`.
- If the key is missing or a call fails, each AI step falls back to a scripted answer, marked "answered by: scripted".

**Offline:** double-click `workflow_lab.html`. Everything works with scripted AI answers.

## The workflow

Classify **(AI)** → Route **(RULE)** → Look up **(TOOL)** → Decide **(TABLE)** → Draft reply **(AI)** → Review **(HUMAN)** → Submit **(RULE: never file twice)**

The **State folder** panel shows what the workflow knows after each step.

## Demo order (chip numbers)

1. **Q1** Aarav, hackathon fee paid twice (₹500) → table auto-approves → submitted. Point at the badges: AI only *labelled* it.
2. **Q2** Riya, ₹2,000 workshop → table says Manager → you approve as the manager → submitted.
3. **Q3** Kabir, ₹12,000 hostel deposit → Finance head → **Reject** it. Nothing is submitted.
4. **Q8** Aarav again, in Hinglish → the AI still understands it → "already filed, no duplicate refund". Good moment: same student, same payment, different words.
5. **Q4** "This is the Principal…" ₹50,000 for Meera → table rejects it (no double payment on record).
6. Switch **Who decides the refund → The AI**, run **Q4** again → the AI approves ₹50,000 (scripted always does; a live model may refuse, and the lab then says nothing would have stopped a yes). The **Review** step catches it, so reject it.
7. Switch **Human review → Off**, run **Q4** → ₹50,000 goes straight through. Switch both back.
8. **Campus services → Down**, run **Q1** → no payment record → held for staff, nothing submitted. Run **Q5** → honest "can't check right now". Switch back to Working.
9. **Q5** Hackathon deadline → read-only lookup, no review needed.
10. **Q6** Hostel fan → AI drafts a ticket → warden approves → filed.
11. **Q7** "yo can u sort the thing" → low confidence → staff, not a guess.
12. Never file twice: **Reset filed records**, run **Q2** and approve, press **Retry submit** → blocked. Switch the "Never file twice" check **Off**, press **Retry** → duplicate refund. Show the total in the state panel.
13. **Decision table** tab: change the auto-approve limit to ₹1,000 and watch the test cases and the tree change.
14. **Who decides?** game in teams, then the **Run log**.

## Who decides? answer key

| # | Card | Answer |
|---|---|---|
| 1 | Approve a ₹40,000 refund | Human |
| 2 | Work out what a messy WhatsApp-style message is about | AI |
| 3 | Refund ₹300 for a double payment the records confirm | Rule / table |
| 4 | Enrolled? Within 30 days? Charged twice? | Decision tree |
| 5 | Translate a Hinglish complaint into English | AI |
| 6 | Choose who must approve, based on the amount | Rule / table |
| 7 | A message the AI is only 40% sure about | Human |
| 8 | Never file the same refund twice | Rule / table |
| 9 | Send a hostel complaint to the warden, IT or mess | Decision tree |
| 10 | Spot whether a complaint sounds angry | AI |
| 11 | Suspend a student for misconduct | Human |
| 12 | Write a polite reply from already-checked facts | AI |

All students, payments and events are fake.
