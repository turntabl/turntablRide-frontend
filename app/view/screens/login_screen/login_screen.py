from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from app.view.commons.loader.loader import Loader
from app.lib.google_auth import trigger_server_stop
from app.view.commons.toast.toast import Toaster
from app.controller.auth_controller.login_auth import LoginAuthenticationController

Builder.load_file("app/view/screens/login_screen/login_screen.kv")


class LoginScreen(MDScreen):
    """Most of the contents for the login screen is auto-injected from
    `` app/view/screens/login_screen/login_screen.kv ``
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = LoginAuthenticationController(self)
        self.app = MDApp.get_running_app()
        self.loader = Loader(func=trigger_server_stop)

    def show_loader(self):
        self.loader.open()

    def dismiss_loader(self):
        self.loader.dismiss()

    def go_to_main_screen(self, data):
        """
        Screen to go after the login process is done and no error occured.

        Parameters
        ----------
        data : Any
            The data to be used to populate the next screen.
        """
        pass

    def show_error_toast(self, msg):
        Clock.schedule_once(
            lambda *args: (
                Toaster(
                    message=msg,
                    bg_color=self.app.COLORS.ErrorColor.get("BackgroundColor"),
                    font_size=14,
                ).toast(),
            ),
            0,
        )
