# What's Included:

Parsing hundreds of aerospace manuals (PDF/DOCX)

Chunking and vector storage using FAISS

Querying using vector similarity

Answer generation using LLaMA model locally (no OpenAI)

Output formatting into DOCX

 📁 All required code modules, scripts, and instructions have been created in the project structure above. You can now:

# How to Run

 1. Place your manuals into data/manuals/ folder
2. Run vector indexing:
    python ingest_manuals.py
 3. Generate document:
    python generate_doc.py --query "Hydraulic leak troubleshooting for Model ZX-250"

# Notes
- This uses a local LLaMA model for free inference (adjust model_id if needed)
- You can containerize this easily for batch or API use
- Handles hundreds of manuals and performs chunk-based RAG retrieval
