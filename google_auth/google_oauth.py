import socket
import requests
import webbrowser
import threading
from google_auth.server import oauth_server, run_server
from google_auth import global_var as glob
from oauthlib.oauth2 import WebApplicationClient


class GoogleOAuth:
    """
    Provide Google OAuth2 to kivy apps.

    Notes
    -----
    Currently working for only web applications that require OAuth using Google.
    """

    def __init__(
        self, client_id, client_secret, success_listener, error_listener, **kwargs
    ):
        """
        Creates an object of GoogleOAuth with parameters provided.

        Parameters
        ----------
        client_id : str
            The client ID of the application provided by Google on the cloud
            console of the application.
        client_secret : str
            The client secret of the application provided by Google on the cloud
            console of the application.
        success_listener : func
            A function to be called the user is authenticated. Function should
            accept one parameter which is the token received.
        """
        self.succ_listener = success_listener
        self.err_listener = error_listener
        self.client_id = client_id
        self.__client_secret = client_secret
        self.web_client = WebApplicationClient(client_id, **kwargs)

    def login(self):
        """
        Function to initiate the login process. Redirects user to consent page
        for authentication.

        Return
        ------
        True if consent page was being able to open for user
        False if there was no internet connection.
        """
        if self.is_connected():
            consent_page = self.__prepare_consent_page()
            self.__token_server = oauth_server(self, self.__client_secret)
            t = threading.Thread(target=run_server, args=(self.__token_server,))
            t.daemon = True
            t.start()
            webbrowser.open(consent_page, 1, False)
        else:
            self.err_listener("No internet Connection")

    def stop_tok_server(self):
        """
        Function to stop the token server.
        """
        glob.stop_thread = True
        self.__token_server.shutdown()

    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

    def __prepare_consent_page(self):
        """
        Prepares the consent page for the user. This page is what the
        user is redirected to for authentication from google.

        Return
        ------
        consent_page : str
            A Url in a string format
        """
        self.oauth_endpoints = self.__get_google_auth_endpoints()
        auth_endpoint = self.oauth_endpoints["authorization_endpoint"]
        consent_page = self.web_client.prepare_request_uri(
            auth_endpoint,
            redirect_uri="https://127.0.0.1:9004/",
            scope=["email", "profile"],
        )
        return consent_page

    def __get_google_auth_endpoints(self):
        """
        Function to return the google endpoints needed for authorization
        and authentication of the user.

        Return
        ------
        A json encoded content.
        """
        return requests.get(
            "https://accounts.google.com/.well-known/openid-configuration"
        ).json()
