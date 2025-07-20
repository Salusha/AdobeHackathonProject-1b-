import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

# Load embedding model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_sections_from_pdf(pdf_path, persona, job):
    query = f"{persona}. {job}".strip()
    query_emb = model.encode(query)

    doc = fitz.open(pdf_path)
    candidates = []

    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if not text:
            continue

        # Simple assumption: each page is a potential section
        candidates.append({
            "document": os.path.basename(pdf_path),
            "page_number": i + 1,
            "title": f"Page {i + 1}",
            "text": text
        })

    # Compute relevance score
    scored = []
    for sec in candidates:
        sec_emb = model.encode(sec["text"])
        score = util.cos_sim(query_emb, sec_emb).item()
        scored.append((score, sec))

    # Sort by similarity score descending
    scored.sort(reverse=True, key=lambda x: x[0])
    top_sections = scored[:5]  # take top 5 matches

    # Format section data
    extracted_sections = [
        {
            "document": sec["document"],
            "page_number": sec["page_number"],
            "section_title": sec["title"],
            "importance_rank": i + 1
        }
        for i, (score, sec) in enumerate(top_sections)
    ]

    # Format subsection analysis
    subsection_analysis = [
        {
            "document": sec["document"],
            "page_number": sec["page_number"],
            "refined_text": sec["text"]
        }
        for _, sec in top_sections
    ]

    return extracted_sections, subsection_analysis


def analyze_documents(pdf_dir, config):
    input_docs = []
    sections = []
    subsections = []

    for file in sorted(os.listdir(pdf_dir)):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            input_docs.append(file)

            persona = config.get("persona", {}).get("role", "")
            job = config.get("job_to_be_done", {}).get("task", "")
            sec, sub = extract_sections_from_pdf(path, persona, job)

            sections.extend(sec)
            subsections.extend(sub)

    return {
        "metadata": {
            "input_documents": input_docs,
            "persona": config.get("persona", {}),
            "job_to_be_done": config.get("job_to_be_done", {}).get("task", ""),
            "processing_timestamp": None  # You can fill this in main.py
        },
        "extracted_sections": sections,
        "subsection_analysis": subsections
    }
