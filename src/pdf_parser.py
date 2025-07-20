import fitz  # PyMuPDF
import os

def extract_sections(pdf_dir):
    sections = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            doc = fitz.open(path)
            for page_num, page in enumerate(doc):
                text = page.get_text()
                if len(text.strip()) < 100: continue
                # For now: treat each page as one section (improve later with heading detection)
                sections.append({
                    "doc_name": file,
                    "page": page_num + 1,
                    "title": "Page Summary",
                    "text": text.strip()
                })
    return sections
