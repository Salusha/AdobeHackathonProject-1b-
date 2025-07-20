import sys
import os
import json
from datetime import datetime
from PyPDF2 import PdfReader

def extract_sections(pdf_path, keywords):
    sections = []
    try:
        reader = PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue
            for kw in keywords:
                if kw.lower() in text.lower():
                    section_title = text.split('\n')[0][:80]
                    sections.append({
                        "document": os.path.basename(pdf_path),
                        "section_title": section_title,
                        "importance_rank": 1,
                        "page_number": i + 1
                    })
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return sections

def extract_subsections(pdf_path, keywords):
    subsections = []
    try:
        reader = PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue
            for kw in keywords:
                if kw.lower() in text.lower():
                    refined_text = text[:500]
                    subsections.append({
                        "document": os.path.basename(pdf_path),
                        "refined_text": refined_text,
                        "page_number": i + 1
                    })
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return subsections

def process_collection(collection_name):
    collection_path = os.path.join(os.getcwd(), collection_name)
    input_json = os.path.join(collection_path, "challenge1b_input.json")
    output_json = os.path.join(collection_path, "challenge1b_output.json")
    pdf_folder = os.path.join(collection_path, "PDFs")

    with open(input_json, 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    keywords = [
        "city", "things to do", "cuisine", "restaurant", "hotel", "tips", "culture", "adventure", "nightlife", "packing", "water sports"
    ]

    extracted_sections = []
    subsection_analysis = []

    for doc in input_data["documents"]:
        pdf_path = os.path.join(pdf_folder, doc["filename"])
        extracted_sections.extend(extract_sections(pdf_path, keywords))
        subsection_analysis.extend(extract_subsections(pdf_path, keywords))

    for idx, section in enumerate(extracted_sections):
        section["importance_rank"] = idx + 1

    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": input_data["persona"]["role"],
            "job_to_be_done": input_data["job_to_be_done"]["task"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"Output JSON generated at {output_json}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <CollectionFolder>")
        sys.exit(1)
    process_collection(sys.argv[1])