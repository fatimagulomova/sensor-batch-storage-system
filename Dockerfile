FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python3 scripts/clean_csv.py

CMD ["python", "scripts/load_script.py"]
