import threading
from kivy.clock import Clock

from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors
from app.view.commons.loader.loader import Loader
import config.config as config
from kivymd.app import MDApp
from app.lib.google_auth import GoogleOAuth




class Authentication:
    """
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    """

    def __init__(self):
        self.google_login = GoogleOAuth(
            config.CLIENT_ID,
            config.CLIENT_SECRET,
            self.after_login,
            self.error_listener,
        )
        self.login_thread = threading.Thread(target=self.google_login.login)
        self.login_thread.daemon = True
        self.loading = Loader(self.google_login.stop_tok_server)

    def login(self) -> None:
        """Method to call to start the login process."""
        self.loading.open()
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
            resp = requests.get(config.BACKEND_SERVER + "/api/v1/demo", headers=header)
            root = MDApp.get_running_app().root
            status_code = resp.status_code
            if status_code == 200:
                Clock.schedule_once(lambda *args: (change_screen(root, resp),), 0)
            elif status_code == 401:
                Clock.schedule_once(
                    lambda *args: (
                        Toaster(message="You don't have access to this screen", bg_color=Colors().ErrorColor.get("BackgroundColor"),
                    font_size=14).toast(),
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
                Toaster(message=msg, bg_color=Colors().ErrorColor.get("BackgroundColor"),
                    font_size=14).toast(),
            ),
            0,
        )


    def login_and_register_user(self):
        """Custom login response to hold user return responses"""
        return Authentication().login()
    
def change_screen(root, resp):
    root.current = "dashboard"
    root.get_screen("dashboard").ids.dashboard.ids.welcome_text.text = resp.text