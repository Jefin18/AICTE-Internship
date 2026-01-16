DISAGREEMENT_MARKERS = [
    "I disagree",
    "not true",
    "don't agree",
    "however",
    "but I think"
]

def detect_disagreement(segments):
    events = []

    for s in segments:
        text = s["text"].lower()
        if any(marker in text for marker in DISAGREEMENT_MARKERS):
            events.append({
                "type": "Disagreement",
                "timestamp": s["start"],
                "text": s["text"]
            })

    return events
