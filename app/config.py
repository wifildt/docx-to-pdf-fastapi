import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")

LIBREOFFICE_PATH = "/usr/lib/libreoffice/program"
