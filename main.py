import os, sys, json
from src.parser import extract_candidate_sections
from src.scorer import rank_sections
from src.generator import assemble_output

def process_collection(col_name):
    base = os.path.join("input", col_name)
    with open(os.path.join(base, "challenge1b_input.json"), "r", encoding="utf-8") as f:
        inp = json.load(f)
    docs = [d["filename"] for d in inp["documents"]]
    persona = inp["persona"]["role"]
    job = inp["job_to_be_done"]["task"]
    query = persona + " — " + job

    # Collect all candidate sections across docs
    candidates = []
    for fn in docs:
        pdf = os.path.join(base, "PDFs", fn)
        for sec in extract_candidate_sections(pdf):
            sec.update({"filename": fn})
            candidates.append(sec)

    # Rank top sections
    top_secs = rank_sections(candidates, query, top_k=len(docs)*2)

    # For subsections, you could re‑rank sentences within each top section.
    # Here, we’ll simply reuse top_secs as rough subsections:
    top_subs = top_secs

    assemble_output(os.path.join("output", col_name),
                    docs, persona, job, top_secs, top_subs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <CollectionName>")
        sys.exit(1)
    os.makedirs(os.path.join("output", sys.argv[1]), exist_ok=True)
    process_collection(sys.argv[1])
