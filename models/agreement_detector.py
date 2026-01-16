import torch
from features.text_features import encode_sentences

AGREEMENT_PHRASES = [
    "I agree",
    "Exactly",
    "That's right",
    "Absolutely",
    "Yes, correct"
]

agreement_vectors = encode_sentences(AGREEMENT_PHRASES)

def detect_agreement(segments, threshold=0.75):
    events = []

    texts = [s["text"] for s in segments]
    embeddings = encode_sentences(texts)

    for i, emb in enumerate(embeddings):
        sims = torch.cosine_similarity(emb, agreement_vectors)
        if torch.max(sims).item() >= threshold:
            events.append({
                "type": "Agreement",
                "timestamp": segments[i]["start"],
                "text": segments[i]["text"]
            })

    return events
