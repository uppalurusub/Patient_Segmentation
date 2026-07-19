import os

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
REQUEST_TIMEOUT = int(os.getenv("API_REQUEST_TIMEOUT", "30"))
