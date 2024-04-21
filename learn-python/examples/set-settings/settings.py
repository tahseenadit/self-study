from dataclasses import dataclass
from typing import Any


@dataclass
class GoogleSettings:
    gcs_bucket: Any = None
    firestore_client: Any = None
    model: Any = None