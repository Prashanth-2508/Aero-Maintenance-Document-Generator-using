import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
INDEX_PATH = "vector.index"
META_PATH = "vector_meta.pkl"

def build_faiss_index(text_chunks):
    embeddings = MODEL.encode(text_chunks, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open(META_PATH, "wb") as f:
        pickle.dump(text_chunks, f)

    faiss.write_index(index, INDEX_PATH)


def search_faiss(query, top_k=5):
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        chunks = pickle.load(f)

    query_vec = MODEL.encode([query])
    _, indices = index.search(query_vec, top_k)
    return "\n".join([chunks[i] for i in indices[0]])
