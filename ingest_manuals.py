# Parses all aerospace manuals, chunks them, and stores embeddings into FAISS

from utils.parser import load_manuals_from_folder
from utils.chunker import chunk_text
from utils.vectorstore import build_faiss_index

if __name__ == "__main__":
    print("[INFO] Loading aerospace manuals...")
    manuals = load_manuals_from_folder("data/manuals")

    print("[INFO] Chunking documents...")
    chunks = []
    for manual in manuals:
        chunks.extend(chunk_text(manual["content"]))

    print(f"[INFO] Total chunks created: {len(chunks)}")

    print("[INFO] Building FAISS index...")
    build_faiss_index(chunks)
    print("[SUCCESS] Vector store saved!")
