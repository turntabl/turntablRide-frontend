"""
This module contains global variables to be used within the package.
These varibales may or may not be constants.
"""

PORT = 9004
HOST = "localhost"
CALLBACK_URL = f"https://127.0.0.1:{PORT}/"
google_endpoints = {
    "AUTHORIZATION_ENDPOINT": "https://accounts.google.com/o/oauth2/v2/auth",
    "TOKEN_ENDPOINT": "https://oauth2.googleapis.com/token",
    "USERINFO_ENDPOINT": "https://openidconnect.googleapis.com/v1/userinfo",
}
