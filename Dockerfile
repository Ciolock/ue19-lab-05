FROM python:3.10-slim

WORKDIR /app
COPY . .

# Patch pip vulnerabilities
RUN pip install --upgrade pip

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
