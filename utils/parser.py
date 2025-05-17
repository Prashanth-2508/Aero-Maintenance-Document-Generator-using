import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"[ERROR] Failed to parse PDF: {pdf_path} - {e}")
    return text

def extract_text_from_docx(docx_path):
    text = ""
    try:
        doc = docx.Document(docx_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"[ERROR] Failed to parse DOCX: {docx_path} - {e}")
    return text

def load_manuals_from_folder(folder_path="data/manuals"):
    documents = []
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if file.lower().endswith(".pdf"):
            content = extract_text_from_pdf(path)
        elif file.lower().endswith(".docx"):
            content = extract_text_from_docx(path)
        else:
            continue
        if content:
            documents.append({"filename": file, "content": content})
    return documents
