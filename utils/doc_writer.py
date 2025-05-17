from docx import Document
import uuid

def save_to_doc(text):
    doc = Document()
    doc.add_heading("Maintenance Document", level=1)
    doc.add_paragraph(text)

    path = f"output/{uuid.uuid4()}.docx"
    doc.save(path)
    return path
