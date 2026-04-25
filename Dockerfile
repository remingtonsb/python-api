FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta padrão do OpenShift
EXPOSE 8080

# Usa Gunicorn para produção em vez do servidor de dev do Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
