from config import get_google_config, client_google
import socket
import webbrowser
import threading
from queue import Queue
from server import oauth_server, run_server


class GoogleOAuth:

    def __init__(self, success_listener):
        self.success_listener = success_listener
        self.__queue = Queue()
        self.__token_server = oauth_server(self.__queue, self.success_listener)
# q = Queue()

# token_server = oauth_server(q, after_login)

    def login(self):
        print("start_login called")
        if self.is_connected():
            # prepare consent page
            consent_page = self.prepare_consent_page()
            #open browser 
            webbrowser.open(consent_page, 1, False)
            # start server in another thread/ process
            t = threading.Thread(target=run_server, args=(self.__token_server, self.__queue))
            t.start()
            # wait for token
            return True
        else:
            print("cannot connect internet")
            return False


    def stop_server(self):
        self.__token_server.shutdown()



    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def prepare_consent_page(self):
        auth_endpoint = get_google_config()["authorization_endpoint"]
        consent_page = client_google.prepare_request_uri(
            auth_endpoint,
            redirect_uri="https://127.0.0.1:9004/",
            scope=["openid", "email", "profile"],
        )
        return consent_page
