from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from loading import Loading
import config
from kivymd.app import MDApp
from google_auth import GoogleOAuth
from kivy.uix.boxlayout import BoxLayout


class LoginView(BoxLayout):
    """
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.google_auth = GoogleOAuth(
            config.CLIENT_ID,
            config.CLIENT_SECRET,
            self.after_login,
            self.error_listener,
        )
        self.loading = Loading()

    def login(self):
        """Method to call to start the login process."""
        self.loading.open()
        self.google_auth.login()

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
            resp = requests.get(
                config.BACKEND_SERVER + "/api/v1/demo", headers=header, timeout=2
            )
            root = MDApp.get_running_app().root
            status_code = resp.status_code
            if status_code == 200:
                Clock.schedule_once(lambda *args: (change_screen(root, resp),), 0)
            elif status_code == 401:
                Clock.schedule_once(
                    lambda *args: (
                        Snackbar(text="You don't have access to this screen").open(),
                    ),
                    0,
                )
            Clock.schedule_once(lambda *args: (self.loading.dismiss(),), 0)
        except requests.exceptions.RequestException:
            self.error_listener("Backend server is down")

    def error_listener(self, msg):
        """Called whenever there is an error in the login process"""

        Clock.schedule_once(
            lambda *args: (
                self.loading.dismiss(),
                Snackbar(text=msg).open(),
            ),
            0,
        )


def change_screen(root, resp):
    root.current = "dashboard"
    root.get_screen("dashboard").ids.dashboard.ids.welcome_text.text = resp.text
