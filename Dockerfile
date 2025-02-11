FROM python:3.9-slim-bullseye

# Install LibreOffice, unoconv, and Python-UNO bindings
RUN apt-get update && apt-get install -y \
    libreoffice \
    libreoffice-writer \
    unoconv \
    python3-uno \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install fastapi boto3 uvicorn python-dotenv

# Set LibreOffice environment variables
ENV UNO_PATH="/usr/lib/libreoffice/program"
ENV PYTHONPATH="/usr/lib/python3/dist-packages"
ENV PATH="${UNO_PATH}:${PATH}"

# Set working directory
WORKDIR /app
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
