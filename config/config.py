import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
BACKEND_SERVER = "http://localhost:8080"
PREFERRED_WINDOW_SIZE = (360, 640)
APP_TITLE = "TurntablRide"
APP_ICON = "assets/images/favicon.png"
SERVICE_NAME = os.getenv("SERVICE_NAME")
CURRENT_USER = os.getenv("CURRENT_USER")
EXPIRY = os.getenv("EXPIRY")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
