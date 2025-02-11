import boto3
import logging
import os
from app.config import AWS_REGION

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load AWS credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Initialize S3 client with explicit credentials (if set)
if AWS_ACCESS_KEY and AWS_SECRET_KEY:
    logger.info("Using AWS credentials from environment variables.")
    s3_client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
else:
    logger.info("Using default AWS credentials (IAM roles or AWS config).")
    s3_client = boto3.client("s3", region_name=AWS_REGION)


def download_file_from_s3(bucket: str, key: str, local_path: str):
    """
    Downloads a file from S3 to a local directory.
    """
    try:
        logger.info(f"Downloading from S3: s3://{bucket}/{key} → {local_path}")
        s3_client.download_file(bucket, key, local_path)
        logger.info("Download successful.")
        return local_path
    except Exception as e:
        logger.error(f"S3 download error: {e}")
        raise


def upload_file_to_s3(local_path: str, bucket: str, key: str):
    """
    Uploads a local file to S3.
    """
    try:
        logger.info(f"Uploading to S3: {local_path} → s3://{bucket}/{key}")
        s3_client.upload_file(local_path, bucket, key)
        logger.info("Upload successful.")
        return f"s3://{bucket}/{key}"
    except Exception as e:
        logger.error(f"S3 upload error: {e}")
        raise
