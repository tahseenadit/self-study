from settings import GoogleSettings
from utils import get_settings

firestore_client = GoogleSettings.firestore_client
if firestore_client is None:
    get_settings(firestore_client = True)