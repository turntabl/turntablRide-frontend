import requests
import multitasking
from config.config import CLIENT_SECRET, CLIENT_ID, BACKEND_SERVER
from app.lib.google_auth import GoogleOAuth


class Authentication:
    """
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    """

    observers = []

    def __init__(self):
        self.google_auth = GoogleOAuth(CLIENT_ID, CLIENT_SECRET)

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = None if value == "error" else value
        if value == "error":
            self.notify_error("No internet connection")
        else:
            self.notify_success(value)

    @multitasking.task
    def login_user(self):
        """Method to call to start the login process."""
        self.credentials = self.google_auth.login()

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
            resp = requests.get(BACKEND_SERVER + "/api/v1/demo", headers=header)
            status_code = resp.status_code
            if status_code == 200:
                return (status_code, resp.text)
            elif status_code == 401:
                return (status_code, "You don't have access to this screen")
        except requests.exceptions.RequestException:
            return (0, "Backend server is down")

    def notify_error(self, msg):
        for observer in self.observers:
            observer.on_error(msg)

    def notify_success(self, data):
        for observer in self.observers:
            observer.on_success(data)
