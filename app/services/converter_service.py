import os
import subprocess
import logging

from app.config import LIBREOFFICE_PATH

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure LibreOffice paths are set
os.environ["UNO_PATH"] = LIBREOFFICE_PATH
os.environ["PATH"] += os.pathsep + LIBREOFFICE_PATH

def convert_docx_to_pdf(docx_path: str) -> str:
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"File not found: {docx_path}")

    pdf_path = docx_path.replace(".docx", ".pdf")

    try:
        logger.info(f"Converting DOCX to PDF: {docx_path} → {pdf_path}")
        subprocess.run(["unoconv", "-f", "pdf", "-o", pdf_path, docx_path], check=True)
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF conversion failed, file not found: {pdf_path}")

        logger.info("Conversion successful!")
        return pdf_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running unoconv: {e}")
        raise
