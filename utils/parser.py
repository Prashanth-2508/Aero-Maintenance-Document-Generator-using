# utils/parser.py

import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using PyMuPDF (fitz).
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"[ERROR] Failed to parse PDF: {pdf_path} – {str(e)}")
    return text


def extract_text_from_docx(docx_path):
    """
    Extracts text from a .docx file using python-docx.
    """
    text = ""
    try:
        doc = docx.Document(docx_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"[ERROR] Failed to parse DOCX: {docx_path} – {str(e)}")
    return text


def load_manuals_from_folder(folder_path="data/manuals"):
    """
    Iterates through the folder and extracts text from all PDF and DOCX files.
    """
    documents = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.lower().endswith(".pdf"):
            content = extract_text_from_pdf(file_path)
        elif file.lower().endswith(".docx"):
            content = extract_text_from_docx(file_path)
        else:
            print(f"[WARN] Skipping unsupported file format: {file}")
            continue

        if content.strip():
            documents.append({"filename": file, "content": content.strip()})

    return documents
