import socket
import requests
import webbrowser
import threading
from server import oauth_server, run_server
from oauthlib.oauth2 import WebApplicationClient


class GoogleOAuth:
    def __init__(self, client_id, client_secret, success_listener, **kwargs):
        self.succ_listener = success_listener
        self.client_id = client_id
        self.__client_secret = client_secret
        self.web_client = WebApplicationClient(client_id, **kwargs)

    def login(self):
        print("start_login called")
        if self.is_connected():
            # prepare consent page
            consent_page = self.__prepare_consent_page()

            self.__token_server = oauth_server(self, self.__client_secret)

            # start server in another thread/ process
            t = threading.Thread(target=run_server, args=(self.__token_server,))
            t.start()
            # open browser
            webbrowser.open(consent_page, 1, False)
            return True
        else:
            print("cannot connect internet")
            return False

    def stop_server(self):
        self.__token_server.shutdown()
        print("shutdown server")

    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def __prepare_consent_page(self):
        self.oauth_endpoints = self.__get_google_auth_endpoints()
        auth_endpoint = self.oauth_endpoints["authorization_endpoint"]
        consent_page = self.web_client.prepare_request_uri(
            auth_endpoint,
            redirect_uri="https://127.0.0.1:9004/",
            scope=["email", "profile"],
        )
        return consent_page

    def __get_google_auth_endpoints(self):
        return requests.get(
            "https://accounts.google.com/.well-known/openid-configuration"
        ).json()
