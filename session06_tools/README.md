# Session 6 — Tool Calling & Connectors (22 Nov 2026)

**Today's question:** how does an AI look up live information or take an action, and who makes sure it's safe?

**Line to repeat:** The AI only *asks*. The app *checks*. The tool *does*.

## Files in this folder

| File | What it's for |
|---|---|
| `tool_calling_lab.html` | Interactive lab for the live demo and the team game. Open it in any browser; no install or API key. Every tool and all data are fake (Lakeview events, library, canteen, attendance, helpdesk, accounts). |

## Online links

- Slides (Claude): https://claude.ai/artifact/SNY1QmPdRi5BPsQoZ6Lhbm
- Tool Calling Lab (hosted): https://claude.ai/artifact/AmCjq4KjtSLeTrxzJMtTaZ

## The lab at a glance

- **Assistant tab:** ask a question and watch six colour-coded steps: Student → AI picks a tool → AI writes a request → App checks → Service runs → AI answers. Four switches: tools on/off, app safety checks on/off, ask-before-actions on/off, events service working/down. You can also log in as Aarav (student) or Ms. Rao (staff).
- **Tool menu tab:** the seven mock tools (4 read, 3 write) with descriptions, inputs, who can use them. Each can be switched off.
- **Be the app tab:** 10 tool requests; students choose Run / Ask first / Reject.
- **Call log tab:** every request and what happened (the "successful and failed call" record).

## Demo order (numbers match the question chips)

1. **Q1** Hackathon deadline → 28 Nov, from the tool.
2. Tools **Off**, Q1 again → "25 November", flagged *Made up*. Tools back On.
3. **Q2** Register me → approval box → Yes → confirmation code.
4. **Q3** 500 seats → rejected by the app (invalid input).
5. **Q4** Riya's attendance → not allowed. Switch to Ms. Rao (staff) → allowed. Switch back.
6. **Q5** Fake principal refund → blocked. Then App safety checks **Off** → Rs 50,000 refunded, *Dangerous*. Checks back On.
7. Events service **Down**, Q1 → timeout → honest "I won't guess".
8. Q6 (Spring Fest 2019, not found), Q7 (Cultural Night, full), Q11 (Funday, invalid) if time allows.
9. Open **Call log**.

## Be-the-app answer key

| # | Request | Answer |
|---|---|---|
| 1 | lookup_event Hackathon | Run |
| 2 | register Aarav, 1 seat | Ask first |
| 3 | Aarav reads Riya's attendance | Reject |
| 4 | 500 seats | Reject |
| 5 | "I'm the principal" refund | Reject |
| 6 | Staff reads Kabir's attendance | Run |
| 7 | lookup_event with empty name | Reject |
| 8 | WiFi ticket | Ask first |
| 9 | delete_all_tickets (not on menu) | Reject |
| 10 | Menu for "Funday" | Reject |
