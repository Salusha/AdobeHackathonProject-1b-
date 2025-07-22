import json
from datetime import datetime

def assemble_output(collection_path, docs, persona, job, top_sections, top_subsections):
    out = {
        "metadata": {
            "input_documents": docs,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": [
            {
                "document": sec["filename"],
                "page_number": sec["page"],
                "section_title": sec["text"][:80],
                "importance_rank": sec["importance_rank"]
            }
            for sec in top_sections
        ],
        "subsection_analysis": [
            {
                "document": sub["filename"],
                "page_number": sub["page"],
                "refined_text": sub["text"][:500]
            }
            for sub in top_subsections
        ]
    }
    out_path = f"{collection_path}/challenge1b_output.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("Wrote:", out_path)
