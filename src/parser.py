import fitz  # PyMuPDF

def extract_candidate_sections(pdf_path):
    """
    Returns a list of dicts: {"text": <section text>, "page": N}
    - Splits each page into paragraphs by '\n\n'
    - Filters out very short paragraphs
    """
    doc = fitz.open(pdf_path)
    sections = []
    for page_no, page in enumerate(doc, start=1):
        text = page.get_text("text")
        for para in text.split("\n\n"):
            p = para.strip()
            if len(p) > 100:
                sections.append({"text": p, "page": page_no})
    return sections
