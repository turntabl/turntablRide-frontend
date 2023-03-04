import os
import socket
import threading
import webbrowser
from oauthlib.oauth2 import WebApplicationClient

from server import start_server
import requests
client_google = WebApplicationClient(os.getenv("GOOGLE_CLIENT_ID"))
google_provider_cfg = requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

def start_login():
    print("start_login called")
    if is_connected():
        # prepare consent page
        consent_page = prepare_consent_page()
        #open browser 
        webbrowser.open(consent_page, 1, False)
        # start server in another thread/ process
        thread = threading.Thread(target=start_server)
        thread.start()
        # wait for token
        return True
    else:
        print("cannot connect internet")
        return False




def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def prepare_consent_page():
    auth_endpoint = google_provider_cfg["authorization_endpoint"]
    client_google.client_id = os.getenv("GOOGLE_CLIENT_ID")
    consent_page = client_google.prepare_request_uri(
        auth_endpoint,
        redirect_uri="http://127.0.0.1:9004/loginGoogle/callbackGoogle",
        scope=["openid", "email", "profile"],
    )
    return consent_page


# @server.route("/loginGoogle/callbackGoogle")
# def callback():
#     return "<h2>Return back to application to proceed</h2>"