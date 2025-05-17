from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def ingest():
    docs = []
    for file in os.listdir("data/manuals"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join("data/manuals", file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    texts = [doc.page_content for doc in split_docs]
    embeddings = model.encode(texts)

    faiss_store = FAISS.from_texts(texts, embedding=model)
    faiss_store.save_local("vector_store")

if __name__ == "__main__":
    ingest()
