from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer

def search_faiss(query: str, top_k=3):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    vectordb = FAISS.load_local("vector_store", embedding=model)

    docs = vectordb.similarity_search(query, k=top_k)
    return "\n".join([doc.page_content for doc in docs])
