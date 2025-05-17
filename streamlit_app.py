import streamlit as st
from utils.vectorstore import search_faiss
from utils.llama_rag import generate_from_context
from utils.doc_writer import save_to_doc
import base64

def generate_download_link(file_path, link_text="Download Result"):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path.split("/")[-1]}">{link_text}</a>'
    return href

st.set_page_config(page_title="Aerospace Maintenance Generator", layout="centered")
st.title("🛠️ Aerospace Maintenance Document Generator")

query = st.text_area("Enter maintenance issue/query:", height=100, placeholder="e.g. Troubleshoot landing gear hydraulic leak")

if st.button("Generate Document") and query.strip():
    with st.spinner("Searching documents and generating response..."):
        context = search_faiss(query)
        result = generate_from_context(query, context)
        file_path = save_to_doc(result)

    st.success("Document generated successfully!")
    st.markdown(generate_download_link(file_path, "📥 Download Generated DOCX"), unsafe_allow_html=True)
    st.text_area("Generated Response:", result, height=250)

st.markdown("---")
st.caption("Built using LLaMA + RAG + Streamlit")
