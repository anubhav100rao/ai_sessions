# Velora Support: RAG Demo Questions

**Data:** [Velora support tickets and policies (Google Sheet)](https://docs.google.com/spreadsheets/d/19XNwzLrUo0RJciMEhlVEwomDcmOaDNIMZw_rzxLjfEI/edit)

- **Tickets** tab: 30 customer support tickets, 1 Oct to 6 Nov 2026
- **Policies** tab: 13 store rules (returns, refunds, late delivery, priorities)

Velora is a made-up online store. All customer and order IDs are invented.

**Setup:** in NotebookLM, choose *Add source → Google Drive* and pick the sheet. If Sheets isn't offered, download it as a PDF (*File → Download → PDF*) and upload that.

Questions assume **today is 7 Nov 2026**.

---

## 1. Simple lookups

The AI should get these right.

| # | Question | Expected answer |
|---|---|---|
| 1.1 | What did the customer want in T-5014, and what did we do? | A refund of a ₹1,000 price drop on an air fryer. Declined, because price drops aren't refunded. |
| 1.2 | What's the status of order ORD-89912? | Diwali gift hamper, P1, still open, out for delivery on 7 Nov. |
| 1.3 | Which tickets are still open or escalated? | T-5017, T-5023, T-5026, T-5028, T-5029 (5 tickets). |
| 1.4 | What was the smartphone problem in T-5017? | It heats up and keeps restarting. Escalated, with a brand technician visit booked for 9 Nov. |

## 2. Traps

The AI needs to read carefully to get these right.

| # | Question | Expected answer | What it tests |
|---|---|---|---|
| 2.1 | What happened with customer C-2047's earbuds? | First a replacement (T-5002), then a full ₹2,499 refund after a second defect (T-5006). | One order spread across two tickets |
| 2.2 | Did customer C-7330 get a full refund? | No. A partial refund of ₹1,150 on a ₹2,299 order. | Reading the refund column instead of assuming |
| 2.3 | Why does C-6650 have two tickets? | The same complaint twice (T-5027, T-5028). The return was declined because the mouse was delivered on 20 Oct, past the 7-day window. | Duplicate tickets |
| 2.4 | Can a personalised item be returned? | The policy says no, but T-5012 was reprinted free because the seller made the printing error. | An exception inside a policy |

## 3. Questions that need both tabs

The answer needs a ticket and a policy together.

| # | Question | Expected answer |
|---|---|---|
| 3.1 | A customer's headphones were delivered 20 days ago and are faulty. Can they return them? | No. Electronics have a 7-day return window, so they go to the brand's service centre under warranty, as in T-5007. |
| 3.2 | C-2047's charger isn't working (T-5023). Should we refund it, as we did for the earbuds? | No. It's a different order, so it's a first defect, and that gets one free replacement. |
| 3.3 | When should C-9015 expect the refund for the sneakers? | It was a cash-on-delivery order, so the refund is a bank transfer in 7 to 10 working days from 4 Nov: roughly 13 to 18 Nov. |
| 3.4 | Does the hamper customer (T-5029) get late-delivery credit? | Only if it arrives more than 3 days after the promised 5 Nov, i.e. after 8 Nov. If it's delivered on 7 Nov, no credit. |
| 3.5 | When does C-6120's ₹100 wallet credit expire? | It was added on 17 Oct and lasts 90 days, so it expires on 15 Jan 2027. |

## 4. Counting and totals

RAG fetches only some rows at a time, so it may well get these wrong. After asking, check each answer live in the sheet with a filter.

| # | Question | Expected answer |
|---|---|---|
| 4.1 | How many tickets came in during October? | 22 (and 8 in November) |
| 4.2 | How much have we refunded in total? | ₹21,641 across 11 tickets |
| 4.3 | How many different customers raised tickets? | 17 (30 tickets in total, because some customers raised more than one) |
| 4.4 | What's the average satisfaction (CSAT) score? | 3.36 out of 5, from 25 rated tickets |
| 4.5 | Which product category has the most tickets? | Fashion (11), then Electronics (9) |

**Teaching point:** RAG is good for looking things up and unreliable for counting or adding across a whole table. For totals, use a spreadsheet filter or formula.

## 5. Not in the data

A good answer says the data doesn't contain this.

| # | Question | Why it can't be answered |
|---|---|---|
| 5.1 | What's customer C-1182's phone number? | No contact details are stored. |
| 5.2 | Which courier company delivers the hamper? | Courier names aren't recorded. |
| 5.3 | Is the hamper customer a Velora Plus member? | The policy gives members ₹200 credit, but membership isn't recorded in the sheet. |

---

**Exit question:** "The assistant gave a wrong answer. Was the information missing, did it fetch the wrong rows, or did it misread what it fetched?"
