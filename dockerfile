FROM python:3.10-slim

WORKDIR /app

# #(MariaDB client para python-mariadb)
RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY . .

#Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8055

CMD ["python", "app.py"]