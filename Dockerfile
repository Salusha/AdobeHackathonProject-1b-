FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure we don’t use network and process everything from current directory
CMD ["python", "main.py"]
