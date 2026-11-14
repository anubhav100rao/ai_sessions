# Session 5 — Improving & Evaluating RAG (14 Nov 2026)

**Today's question:** our assistant gives answers with sources. How do we tell whether it's actually *good*?

## Files in this folder

| File | What it's for |
|---|---|
| `rag_report_card_lab.html` | Interactive lab for the live demo. Open it in any browser; it works offline. Move the five knobs and watch the score change. |
| `Lakeview_Student_Handbook_Session5.pdf` | Upload to NotebookLM for the team exercise. It includes both the 2023 and 2026 attendance policies, unlabeled: that's the freshness trap. |
| `rag_report_card.py` + `lakeview_data.py` | A tiny RAG assistant plus grader in plain Python, with no installs or API key. Run `python3 rag_report_card.py`. |

## Online links

- Slides (Claude): https://claude.ai/artifact/4sqzs5sfjG5D691cr8s7YQ
- Slides (Google Slides): https://docs.google.com/presentation/d/1XWxV_qifHtnB-31vLK8vB43BMbtP6wiVW2Soe8i0KRQ/edit?usp=sharing
- RAG Report Card Lab (hosted): https://claude.ai/artifact/HSsSTgPKVWmwPPytwe89RL
- Team report card sheet: https://claude.ai/artifact/T77WcQrFYRiQBNmiMBxdMQ. Share it with edit access; each team duplicates the "Report card" tab.

## The score story (same numbers in the lab, the script and the slides)

| Setting | Score |
|---|---|
| Baseline: 40-word pieces, 3 pieces, old docs searchable | 82% |
| + Archive old documents | 91% |
| + Rewrite questions (medical → illness) | 100% |
| Pieces cut to 15 words | 55% (answers lose their ending) |
| "Say I don't know" rule off | 64% (bot guesses on unanswerable questions) |

## Demo order (lab)

1. Baseline: 82%. Click a red attendance row to show that the old 2023 policy won.
2. Set piece size to 15: 55%. The re-exam answer comes out as "The re-exam fee is…". Set it back to 40.
3. Archive old documents: 91%.
4. Rewrite questions: 100%.
5. Untick the "I don't know" rule: 64%. Tick it back on.
6. Open the "How many pieces?" tab and compare hit rate with noise for 1–10 pieces.
