# generate_doc.py
# Core RAG Orchestrator

from utils.vectorstore import search_faiss
from utils.llama_rag import generate_from_context
from utils.doc_writer import save_to_doc
import argparse

def main(query: str):
    print("[INFO] Searching relevant content from manuals...")
    context = search_faiss(query)

    print("[INFO] Generating response using LLaMA...")
    response = generate_from_context(query, context)

    print("[INFO] Saving to DOCX...")
    doc_path = save_to_doc(response)

    print(f"[SUCCESS] Maintenance document saved at: {doc_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Maintenance Docs using LLaMA + RAG")
    parser.add_argument("--query", type=str, required=True, help="Maintenance issue or instruction")

    args = parser.parse_args()
    main(args.query)
