from config import get_google_config, client_google
import socket
import webbrowser
import threading
from queue import Queue
from server import oauth_server, run_server

q = Queue()

token_server = oauth_server(q)

def start_login():
    print("start_login called")
    if is_connected():
        # prepare consent page
        consent_page = prepare_consent_page()
        #open browser 
        webbrowser.open(consent_page, 1, False)
        # start server in another thread/ process
        t = threading.Thread(target=run_server, args=(token_server,q))
        t.start()
        # name = input("enter your name")
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
    auth_endpoint = get_google_config()["authorization_endpoint"]
    consent_page = client_google.prepare_request_uri(
        auth_endpoint,
        redirect_uri="https://127.0.0.1:9004/",
        scope=["openid", "email", "profile"],
    )
    return consent_page
