from config import GCP_PROJECT_ID, GCP_PROJECT_LOCATION, GCS_BUCKET


from google.cloud import storage, firestore


def get_settings(gcs_client: bool = False, firestore_client: bool = False, model: bool = False):

    if gcs_client:
        gcs_client = storage.Client()
        gcs_bucket = gcs_client.bucket(GCS_BUCKET, GCP_PROJECT_ID)
        GoogleSettings.gcs_bucket = gcs_bucket
    
    if firestore_client:
        firestore_client = firestore.Client(project=GCP_PROJECT_ID)
        GoogleSettings.firestore_client = firestore_client
    
    if model:
        vertexai.init(project=GCP_PROJECT_ID, location=GCP_PROJECT_LOCATION)
        model = GenerativeModel("gemini-1.0-pro-vision-001")
        GoogleSettings.model = model

    return GoogleSettings