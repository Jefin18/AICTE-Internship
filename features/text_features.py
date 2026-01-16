from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def encode_sentences(sentences):
    return embedder.encode(sentences, convert_to_tensor=True)
