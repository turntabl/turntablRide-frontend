from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from loading import Loading
import os
import threading
from dotenv import load_dotenv
from kivymd.app import MDApp
from google_auth import GoogleOAuth

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
            self.error_listener,
        )
        self.login_thread = threading.Thread(target=self.__google_login.login)
        self.login_thread.daemon = True
        self.__loading = Loading(self.__google_login.stop_tok_server)

    def login(self):
        """Method to call to start the login process."""
        self.__loading.open()
        self.login_thread.start()

    def after_login(self, token):
        """
        Is called after the login process is successful.

        Parameters
        ----------
        token : str
            used to access resources on the backend not google resources
        """
        import requests

        header = {"Authorization": "Bearer " + token}

        try:
            resp = requests.get("http://localhost:8080/api/v1/demo", headers=header)
            root = MDApp.get_running_app().root
            status_code = resp.status_code
            if status_code == 200:
                Clock.schedule_once(lambda *args: (change_screen(root, resp),), 0)
            elif status_code == 401:
                Clock.schedule_once(
                    lambda *args: (
                        Snackbar(text="You don't have access to this page").open(),
                    ),
                    0,
                )
            Clock.schedule_once(lambda *args: (self.__loading.dismiss(),), 0)
        except requests.exceptions.RequestException:
            self.error_listener("Backend server is down")

    def error_listener(self, msg):
        """Called whenever there is an error in the login process"""

        Clock.schedule_once(
            lambda *args: (
                self.__loading.dismiss(),
                Snackbar(text=msg).open(),
            ),
            0,
        )


def change_screen(root, resp):
    root.current = "dashboard"
    root.get_screen("dashboard").ids.dashboard.ids.welcome_text.text = resp.text
