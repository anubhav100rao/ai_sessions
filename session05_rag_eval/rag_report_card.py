"""
Session 5: Improving and evaluating RAG, the "RAG Report Card"
=================================================================
A tiny RAG assistant plus a grader, in plain Python. You need no libraries
and no API key.

Run it:   python3 rag_report_card.py

What happens:
  1. CUT     the documents into small pieces ("chunks")
  2. FIND    the pieces that best match the question ("retrieval")
  3. ANSWER  from those pieces, with a citation, or say "I don't know"
  4. GRADE   every answer against an answer key (the TEST SET)
  5. EXPERIMENT: change one setting at a time and watch the score move

The "AI" here is deliberately simple: it picks the best-matching sentence
from the retrieved pieces. A real system would hand the pieces to an LLM
(see `ask_real_llm` at the bottom). The way we grade it stays the same.
"""

import re
from lakeview_data import DOCUMENTS, TEST_SET

STOPWORDS = set("""a an the is are was were be to of in on for at by with and or
if i my me we you your it its this that what when how can do does will
many much any as from into up per who which there their they them not no
get""".split())


def words(text):
    """Lower-case words, without punctuation or filler words."""
    found = re.findall(r"[a-z0-9:]+", text.lower())
    return [w.rstrip("s") if len(w) > 3 else w for w in found if w not in STOPWORDS]


# ---------------------------------------------------------------- 1. CUT
def make_chunks(chunk_size, include_archived=True):
    """Cut every document into pieces of about `chunk_size` words."""
    chunks = []
    for doc in DOCUMENTS:
        if doc["status"] == "archived" and not include_archived:
            continue  # FIX for outdated answers: leave old versions out of the library
        tokens = doc["text"].split()
        for start in range(0, len(tokens), chunk_size):
            piece = " ".join(tokens[start:start + chunk_size])
            chunks.append({"doc": doc["id"], "status": doc["status"], "text": piece})
    return chunks


# ---------------------------------------------------------------- 2. FIND
def score(question, chunk_text):
    """How many of the question's words appear in this piece?"""
    q = set(words(question))
    c = set(words(chunk_text))
    return len(q & c)


def retrieve(question, chunks, top_k):
    ranked = sorted(chunks, key=lambda ch: score(question, ch["text"]), reverse=True)
    return ranked[:top_k]


# ---------------------------------------------------------------- 3. ANSWER
MIN_MATCH = 2  # if the best piece matches fewer words than this -> "I don't know"


def answer(question, retrieved):
    best_sentence, best_doc, best_score = None, None, 0
    for ch in retrieved:
        for sentence in re.split(r"(?<=[.!?])\s+", ch["text"]):
            s = score(question, sentence)
            if s > best_score:
                best_sentence, best_doc, best_score = sentence, ch, s
    if best_score < MIN_MATCH:
        return {"text": "I don't know. The documents don't say.", "cited": None, "status": None}
    return {"text": best_sentence, "cited": best_doc["doc"], "status": best_doc["status"]}


# ---------------------------------------------------------------- 4. GRADE
def grade(test, retrieved, reply):
    """Four checks, the same ones the students use on paper."""
    answerable = test["source"] is not None
    abstained = reply["cited"] is None
    checks = {}
    if answerable:
        checks["found_right_doc"] = any(ch["doc"] == test["source"] for ch in retrieved)
        checks["correct"] = (not abstained) and all(k in reply["text"] for k in test["must_contain"])
        checks["citation_ok"] = reply["cited"] == test["source"]
        checks["fresh"] = reply["status"] != "archived"
    else:
        checks["said_dont_know"] = abstained
    checks["PASS"] = all(checks.values())
    return checks


SYNONYMS = {  # FIX for "same meaning, different words": rewrite the question
    "medical": "illness",
    "certificate": "documented",
}


def rewrite(question):
    """Add the words the documents actually use (a simple 'query rewrite')."""
    extra = [SYNONYMS[w] for w in re.findall(r"[a-z]+", question.lower()) if w in SYNONYMS]
    return question + " " + " ".join(extra)


def run(chunk_size=40, top_k=3, include_archived=True, rewrite_query=False, show=False):
    chunks = make_chunks(chunk_size, include_archived)
    passed = 0
    for test in TEST_SET:
        q = rewrite(test["question"]) if rewrite_query else test["question"]
        retrieved = retrieve(q, chunks, top_k)
        reply = answer(q, retrieved)
        result = grade(test, retrieved, reply)
        passed += result["PASS"]
        if show:
            mark = "PASS" if result["PASS"] else "FAIL"
            print(f"[{mark}] Q: {test['question']}")
            print(f"        A: {reply['text']}   (source: {reply['cited']})")
            failed = [k for k, v in result.items() if k != "PASS" and not v]
            if failed:
                print(f"        failed checks: {', '.join(failed)}")
    return round(100 * passed / len(TEST_SET))


def retrieval_stats(chunk_size=40, top_k=3):
    """Two numbers about FINDING, before any answer is written:
       hit rate = how often the right document is among the pieces we hand over
       noise    = what share of the handed-over pieces are irrelevant"""
    chunks = make_chunks(chunk_size)
    answerable = [t for t in TEST_SET if t["source"]]
    hits, noise = 0, 0.0
    for t in answerable:
        got = retrieve(t["question"], chunks, top_k)
        hits += any(ch["doc"] == t["source"] for ch in got)
        noise += sum(ch["doc"] != t["source"] for ch in got) / len(got)
    return round(100 * hits / len(answerable)), round(100 * noise / len(answerable))


# ---------------------------------------------------------------- 5. EXPERIMENT
if __name__ == "__main__":
    print("=" * 72)
    print("BASELINE: chunk_size=40 words, top_k=3, old documents still in library")
    print("=" * 72)
    base = run(chunk_size=40, top_k=3, include_archived=True, show=True)
    print(f"\nREPORT CARD SCORE: {base}%\n")

    print("=" * 72)
    print("EXPERIMENT 1: piece size (top_k=3)")
    print("=" * 72)
    for size in [8, 15, 40, 100]:
        print(f"  chunk_size={size:>3} words -> score {run(chunk_size=size, top_k=3)}%")

    print("\n" + "=" * 72)
    print("EXPERIMENT 2: how many pieces we hand to the AI (chunk_size=15)")
    print("=" * 72)
    print("  More pieces -> more likely the right page is included (hit rate),")
    print("  but more of what the AI reads is irrelevant (noise).")
    for k in [1, 2, 3, 5, 10]:
        hit, noise = retrieval_stats(chunk_size=15, top_k=k)
        print(f"  top_k={k:>2} -> hit rate {hit:>3}%   noise {noise:>3}%")

    print("\n" + "=" * 72)
    print("EXPERIMENT 3: archive the old 2023 attendance policy")
    print("=" * 72)
    fixed = run(chunk_size=40, top_k=3, include_archived=False, show=True)
    print(f"\nREPORT CARD SCORE: {base}%  ->  {fixed}%")

    print("\n" + "=" * 72)
    print("EXPERIMENT 4: archive old docs AND rewrite the question with synonyms")
    print("=" * 72)
    best = run(chunk_size=40, top_k=3, include_archived=False, rewrite_query=True)
    print(f"REPORT CARD SCORE: {base}%  ->  {fixed}%  ->  {best}%")


# ---------------------------------------------------------------- optional
def ask_real_llm(question, retrieved):
    """
    How a real system would answer. Not run by default.
    Requires: pip install anthropic   and an ANTHROPIC_API_KEY.
    """
    import anthropic
    context = "\n\n".join(f"[{ch['doc']}] {ch['text']}" for ch in retrieved)
    prompt = (
        "Answer the question using ONLY the documents below. "
        "Cite the document name in square brackets. "
        "If the documents do not contain the answer, say \"I don't know\".\n\n"
        f"DOCUMENTS:\n{context}\n\nQUESTION: {question}"
    )
    client = anthropic.Anthropic()
    msg = client.messages.create(model="claude-haiku-5-5", max_tokens=300,
                                 messages=[{"role": "user", "content": prompt}])
    return msg.content[0].text
