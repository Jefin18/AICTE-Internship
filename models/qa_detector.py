import re

QUESTION_WORDS = ["what", "why", "how", "when", "where", "do", "does", "is", "are"]

def is_question(sentence):
    if sentence.strip().endswith("?"):
        return True
    return any(sentence.lower().startswith(w) for w in QUESTION_WORDS)

def detect_qa_events(segments, max_gap=5.0):
    qa_events = []

    for i in range(len(segments) - 1):
        s1 = segments[i]
        s2 = segments[i + 1]

        if is_question(s1["text"]):
            time_gap = s2["start"] - s1["end"]
            if time_gap <= max_gap:
                qa_events.append({
                    "type": "Question-Answer",
                    "timestamp": s1["start"],
                    "question": s1["text"],
                    "answer": s2["text"]
                })

    return qa_events
