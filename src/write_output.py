import json
from datetime import datetime

def write_output(metadata, result, output_path):
    output = {
        "metadata": metadata,
        # "extracted_sections": result["extracted_sections"],
        # "sub_section_analysis": result["sub_section_analysis"]
        "extracted_sections": result.get("extracted_sections", []),
        "sub_section_analysis": result.get("sub_section_analysis", [])
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
