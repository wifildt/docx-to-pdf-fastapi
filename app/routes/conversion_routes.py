import os
import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.s3_service import download_file_from_s3, upload_file_to_s3
from app.services.converter_service import convert_docx_to_pdf
from app.config import S3_BUCKET

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Initialize API router
router = APIRouter()


class ConvertRequest(BaseModel):
    key: str


"""
Converts a DOCX file from S3 to PDF and uploads it back to S3.
"""
@router.post("/convert")
async def convert_docx(request: ConvertRequest):
    try:
        docx_key = request.key
        docx_local_path = f"/tmp/{os.path.basename(docx_key)}"
        pdf_key = docx_key.replace(".docx", ".pdf")
        pdf_local_path = docx_local_path.replace(".docx", ".pdf")

        # Step 1: Download DOCX from S3
        try:
            download_file_from_s3(S3_BUCKET, docx_key, docx_local_path)
        except Exception:
            raise HTTPException(status_code=500, detail="Failed to download DOCX from S3")

        # Step 2: Convert DOCX to PDF
        try:
            convert_docx_to_pdf(docx_local_path)
        except Exception:
            raise HTTPException(status_code=500, detail="Failed to convert DOCX to PDF")

        # Step 3: Upload PDF to S3
        try:
            pdf_s3_url = upload_file_to_s3(pdf_local_path, S3_BUCKET, pdf_key)
        except Exception:
            raise HTTPException(status_code=500, detail="Failed to upload PDF to S3")

        # Cleanup local files
        os.remove(docx_local_path)
        os.remove(pdf_local_path)

        return {"message": "Conversion successful!", "pdf_s3_path": pdf_s3_url}

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Unexpected system error")
