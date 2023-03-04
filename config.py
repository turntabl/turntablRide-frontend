import os
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv
import requests

load_dotenv()
client_google = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))

def get_google_config():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()