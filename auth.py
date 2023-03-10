from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from loading import Loading
import os
from dotenv import load_dotenv
from kivymd.app import MDApp
from google_oauth import GoogleOAuth

load_dotenv()


class Authentication:
    """
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    """

    def __init__(self):
        self.__google_login = GoogleOAuth(
            os.getenv("GOOGLE_CLIENT_ID"),
            os.getenv("GOOGLE_CLIENT_SECRET"),
            self.after_login,
        )
        self.__loading = Loading(self.__google_login.stop_server)

    def login(self):
        """Method to call to start the login process."""
        self.__loading.open()
        if not self.__google_login.login():
            self.error_listener()

    def after_login(self, token):
        """
        Is called after the login process is successful.

        Parameters
        ----------
        token : str
            used to access resources on the backend not google resources
        """
        root = MDApp.get_running_app().root
        import requests

        header = {"Authorization": "Bearer " + token}

        try:
            resp = requests.get("http://localhost:8080/api/v1/demo", headers=header)

            status_code = resp.status_code
            self.__loading.dismiss()
            if status_code == 200:
                root.current = "dashboard"
                root.get_screen(
                    "dashboard"
                ).ids.dashboard.ids.welcome_text.text = resp.text
            elif status_code == 401:
                Snackbar(text="You don't have access to this page").open()
                root.current = "login"
        except requests.exceptions.RequestException:
            self.__loading.dismiss()
            Snackbar(text="Server is down. Try agian later.").open()
            root.current = "login"

    def error_listener(self):
        """Called whenever there is an error in the login process"""

        Snackbar(text="Error logging in. Check connection or try again.").open()
        Clock.schedule_once(lambda *args: self.__loading.dismiss())
