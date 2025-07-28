<!-- # AdobeHackathonProject-1b-
# Build
docker build -t persona-section-extractor .

# Run (CPU, no network, maps local files to container)
docker run --rm -v $(pwd):/app --network none persona-section-extractor -->

# 🧠 Adobe Hackathon 2025 – Round 1B  
**Persona-Based Intelligent Section Extractor for PDFs**

## 📌 Problem Statement

Develop a document intelligence system that:
- Accepts user-defined folders (collections) of PDFs.
- Reads a persona and job-to-be-done from a JSON file.
- Extracts and ranks the most relevant sections based on the persona/job.
- Runs **fully offline** and is **Dockerized**.

---

## ✅ Solution Overview

This system:
- Iterates over every `CollectionX` folder present (e.g., `Collection1`, `Collection2`, ...).
- Parses all PDFs inside the `PDFs/` subfolder.
- Extracts titles/headings/subsections that are contextually relevant.
- Ranks sections and outputs results to `challenge1b_output.json`.

---

## 📁 Folder Structure

```bash
project_root/
├── main.py                         # Entry point — runs processing for all collections
├── src/
│   └── processor.py                # Persona-based extraction and ranking logic
├── Collection1/
│   ├── PDFs/                       # Folder containing input PDFs
│   ├── challenge1b_input.json      # Persona & job definition
│   └── challenge1b_output.json     # Output written here after processing
├── Collection2/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Dockerfile                      # Offline Docker image
├── requirements.txt                # Python dependencies
├── README.md                       # This file
```

✅ You can create as many collections as needed — the script auto-detects and processes each one.

---

## 🧠 Input JSON Format — `challenge1b_input.json`

```json
{
  "persona": "Investment Analyst",
  "job": "Analyze revenue trends, R&D investments, and market positioning strategies"
}
```

---

## 📤 Output JSON Format — `challenge1b_output.json`

```json
{
  "metadata": {
    "input_documents": ["report1.pdf", "report2.pdf"],
    "persona": "Investment Analyst",
    "job_to_be_done": "Analyze revenue trends, R&D investments, and market positioning strategies",
    "processing_timestamp": "2025-07-15T12:00:00Z"
  },
  "extracted_sections": [
    {
      "document": "report1.pdf",
      "page_number": 3,
      "section_title": "Revenue Growth Breakdown",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "report1.pdf",
      "page_number": 3,
      "refined_text": "Revenue increased due to product diversification..."
    }
  ]
}
```

---

## 🐳 Running the Project with Docker (Offline)

### Step 1: Build the Docker Image

```bash
docker build -t persona-section-extractor .
```

### Step 2: Run the Container

#### ✅ On Linux/macOS (bash, zsh):
```bash
docker run --rm -v $(pwd):/app --network none persona-section-extractor
```

#### ✅ On Windows (PowerShell):
```bash
docker run --rm -v "${PWD}:/app" --network none persona-section-extractor
```

✅ This command:
- Mounts the current project directory into the container.
- Disables all internet access (`--network none`).
- Automatically processes all `CollectionX/` folders (e.g., `Collection1`, `Collection2`, ...).
- Writes output JSONs back into each respective collection directory.

---

## ⚙️ Dependencies

Everything is already included in the Docker image.

If you want to install dependencies locally:
```bash
pip install -r requirements.txt
```

---

## 🧪 Testing Your Setup

1. Add your own `CollectionX/` folder (e.g., `Collection4/`).
2. Add a few PDFs inside the `PDFs/` subfolder.
3. Add a `challenge1b_input.json` defining the persona/job.
4. Run the Docker container again.
5. Check `challenge1b_output.json` for results.

---

## 🧾 Example Collections

```bash
Collection1/      # Travel Planning
├── PDFs/
├── challenge1b_input.json
├── challenge1b_output.json

Collection2/      # Adobe Acrobat Learning
├── PDFs/
├── challenge1b_input.json
├── challenge1b_output.json

Collection3/      # Recipes
├── PDFs/
├── challenge1b_input.json
├── challenge1b_output.json
```

---

## 👩‍💻 Author

Salusha — Participant, Adobe Hackathon 2025  
GitHub: [https://github.com/salusha](https://github.com/salusha)

Snehal Taori — Participant, Adobe Hackathon 2025  
GitHub: [https://github.com/snehaltaori](https://github.com/snehaltaori)

Deepanshi Verma — Participant, Adobe Hackathon 2025  
GitHub: [https://github.com/DeepanshiiVerma](https://github.com/DeepanshiiVerma)


---
