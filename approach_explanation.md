# Approach Explanation

For Round 1B we needed a **generic**, **offline**, **CPU‑only** system that
can ingest any 3–10 PDFs plus a persona + job, then output the most
relevant sections and refined sub‑sections ranked by importance.

## 1. Candidate Section Extraction
We use **PyMuPDF** to read each page’s full text, which is
split into paragraphs by blank lines. Paragraphs longer than 100 chars
are treated as “candidate sections” to cover arbitrary document types.

## 2. Semantic Scoring & Ranking
We combine the persona role and job-to-be-done into a single  
query string. Using the **all‑MiniLM‑L6‑v2** sentence‑transformer
(~80 MB), we embed both the query and each candidate section.
Cosine similarity then provides a relevance score.  
We sort by descending score and pick the top 2×(#docs) sections
to ensure breadth across all PDFs.

## 3. Sub‑section Refinement
For each top section, we reuse its text as a “refined_text”—  
in a full system you might split into sentences and re‑rank,
but for time and size constraints this simple approach
still surfaces the key passages.

## 4. Output Assembly
We write a JSON with:
1. **metadata**: input filenames, persona, job, timestamp  
2. **extracted_sections**: document, page, truncated title, rank  
3. **subsection_analysis**: document, page, truncated text

## 5. Compliance & Performance
- **Offline**: no network calls  
- **CPU‑only**: pure Python + PyMuPDF + a small transformer  
- **Model size**: ~80 MB (< 1 GB)  
- **Speed**: Embeddings and ranking for 5 documents run in < 60 s  
  on 8‑core, 16 GB RAM.

This modular structure makes the system
easy to extend (e.g., using real heading detection
from Round 1A) or swap in lighter TF‑IDF scoring if desired.
