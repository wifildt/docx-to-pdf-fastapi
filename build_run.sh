docker build --no-cache -t docx-to-pdf-fastapi .
docker run --env-file .env -p 8000:8000 docx-to-pdf-fastapi

