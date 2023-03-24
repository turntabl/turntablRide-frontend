import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
BACKEND_SERVER = "http://localhost:8080"
PREFERRED_WINDOW_SIZE = (360, 640)
