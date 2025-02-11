import logging
from fastapi import FastAPI
from app.routes.conversion_routes import router

# Configure logger
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI
app = FastAPI(title="DOCX to PDF Converter API", version="1.0")

# Include API routes
app.include_router(router, prefix="/api")
