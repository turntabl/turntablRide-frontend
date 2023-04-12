import time
import keyring
from config.config import (
    SERVICE_NAME,
    CURRENT_USER,
    REFRESH_TOKEN,
    EXPIRY,
    CLIENT_ID,
    CLIENT_SECRET,
)
from app.lib.google_auth import refresh


def save_credentials(token):
    keyring.set_password(SERVICE_NAME, CURRENT_USER, token["id_token"])
    keyring.set_password(SERVICE_NAME, REFRESH_TOKEN, token["refresh_token"])
    keyring.set_password(SERVICE_NAME, EXPIRY, token["expires_at"])


def delete_credentials():
    keyring.delete_password(SERVICE_NAME, CURRENT_USER)
    keyring.delete_password(SERVICE_NAME, REFRESH_TOKEN)
    keyring.delete_password(SERVICE_NAME, EXPIRY)


def get_credentials():
    id_token = keyring.get_password(SERVICE_NAME, CURRENT_USER)
    expiry = keyring.get_password(SERVICE_NAME, EXPIRY)
    refresh_token = keyring.get_password(SERVICE_NAME, REFRESH_TOKEN)
    return {"id_token": id_token, "refresh_token": refresh_token, "expires_at": expiry}


def refresh_credentials(refresh_token):
    data = refresh(refresh_token, CLIENT_ID, CLIENT_SECRET)
    if data is None:
        return data
    credentials = {
        "refresh_token": refresh_token,
        "id_token": data["id_token"],
        "expires_at": int(data["expires_in"]) + time.time(),
    }
    save_credentials(credentials)
    return credentials
