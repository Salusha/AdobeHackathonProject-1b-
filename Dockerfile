# Use slim Python 3.10
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# System packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential git \
 && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install CPU‑only PyTorch (>=2.1) and friends
RUN pip install --prefer-binary --no-cache-dir \
    torch==2.1.0+cpu \
    torchvision==0.16.0+cpu \
    torchaudio==2.1.0+cpu \
    -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt

# Pre‑download the SBERT model for offline use
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Copy your application code
COPY . .

# Run the pipeline
ENTRYPOINT ["python", "main.py"]
