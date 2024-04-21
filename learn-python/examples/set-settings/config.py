import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_PROJECT_LOCATION = os.getenv("GCP_PROJECT_LOCATION")
GCS_BUCKET = os.getenv("GCS_BUCKET")