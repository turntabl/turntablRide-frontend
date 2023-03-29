import requests
import config.config as config
from app.lib.google_auth import GoogleOAuth


class Authentication:
    """
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    """

    def __init__(self, after_login, error_listener):
        self.google_auth = GoogleOAuth(
            config.CLIENT_ID, config.CLIENT_SECRET, after_login, error_listener
        )

    def login_user(self):
        """Method to call to start the login process."""
        self.google_auth.login()

    def fetch_data(self, token):
        """
        Function called to get some data from the backend server

        Parameters
        ----------
        token : str
            used to access resources on the backend not google resources
        """

        header = {"Authorization": "Bearer " + token}

        try:
            resp = requests.get(config.BACKEND_SERVER + "/api/v1/demo", headers=header)
            status_code = resp.status_code
            if status_code == 200:
                return (status_code, resp.text)
            elif status_code == 401:
                return (status_code, "You don't have access to this screen")
        except requests.exceptions.RequestException:
            return (0, "Backend server is down")
