import webbrowser
import requests
import urllib.parse
from app.lib.google_auth.server import get_oauth_server
from app.lib.google_auth.globals import CALLBACK_URL, google_endpoints
from app.lib.google_auth.utils import is_connected
from oauthlib.oauth2 import WebApplicationClient


class GoogleOAuth:
    """
    Provide Google OAuth2 to kivy apps.
    Notes
    -----
    Currently working for only desktop applications that require OAuth using Google.
    """

    def __init__(self, client_id, client_secret, **kwargs):
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
        error_listener : func
            A function that is called when there is an error during the login process.
            Must accept one argument
        kwargs : dict
            Key values parameters passed to WebApplicationClient
        """
        self.client_id = client_id
        self._client_secret = client_secret
        self.web_client = WebApplicationClient(client_id, **kwargs)
        self._consent_page = self._prepare_consent_page()

    def login(self):
        """
        Function to initiate the login process. Redirects user to consent page
        for authentication.
        """
        if is_connected():
            return self._start_login()
        else:
            res = "error"
        return res

    def _start_login(self):
        token_server = get_oauth_server(self, self._client_secret)
        webbrowser.open(self._consent_page, 1, False)
        token_server.handle_request()
        token_server.server_close()
        return self.web_client.token

    def _prepare_consent_page(self):
        """
        Prepares the consent page for the user. This page is what the
        user is redirected to for authentication from google.
        Return
        ------
        consent_page : str
            A Url in a string format
        """
        consent_page = self.web_client.prepare_request_uri(
            google_endpoints["AUTHORIZATION_ENDPOINT"],
            redirect_uri=CALLBACK_URL,
            scope=["email", "profile"],
            access_type="offline",
        )
        return consent_page


def refresh(refresh_token, client_id, client_secret):
    url = google_endpoints["TOKEN_ENDPOINT"]
    header = {"content-type": "application/x-www-form-urlencoded"}
    body = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
    ).encode("utf-8")
    try:
        res = requests.post(
            url, headers=header, data=body, auth=(client_id, client_secret)
        )
        return res.json()
    except requests.exceptions.ConnectionError:
        return None
