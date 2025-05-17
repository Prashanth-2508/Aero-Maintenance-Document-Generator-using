import streamlit as st
from utils.vectorstore import search_faiss
from utils.llama_rag import generate_from_context
from utils.doc_writer import save_to_doc

st.set_page_config(layout="centered")
st.title("🛠️ Aerospace Maintenance Document Generator")

query = st.text_area("Enter maintenance issue or logs")

if st.button("Generate Document"):
    with st.spinner("Fetching relevant info from manuals..."):
        context = search_faiss(query)
        response = generate_from_context(query, context)
        path = save_to_doc(response)

        with open(path, "rb") as f:
            st.download_button("Download DOCX", f, file_name="maintenance_report.docx")
