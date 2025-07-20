import os
import json
from datetime import datetime
from src.processor import analyze_documents
from src.write_output import write_output  # ✅ Corrected import

def process_all_collections():
    for folder in os.listdir():
        if folder.startswith("Collection") and os.path.isdir(folder):
            input_json = os.path.join(folder, "challenge1b_input.json")
            pdf_dir = os.path.join(folder, "PDFs")
            output_json = os.path.join(folder, "challenge1b_output.json")

            if os.path.exists(input_json) and os.path.isdir(pdf_dir):
                with open(input_json, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                result = analyze_documents(pdf_dir, config)
                result["metadata"]["processing_timestamp"] = datetime.utcnow().isoformat()

                # ✅ Use your actual writer function
                write_output(output_json, result, output_json)

                print(f"[✓] Processed {folder}")
            else:
                print(f"[!] Skipping {folder} — Missing PDFs or input JSON")

if __name__ == "__main__":
    process_all_collections()
