from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from app.utils.colors import Colors
from app.view.commons.loader.loader import Loader
from app.lib.google_auth import trigger_server_stop
from app.view.commons.toast.toast import Toaster
from app.controller.auth_controller.login_auth import LoginAuthenticationController


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
        root = self.app.root
        root.current = "dashboard"
        root.get_screen("dashboard").ids.dashboard.ids.welcome_text.text = data

    def show_error_toast(self, msg):
        Clock.schedule_once(
            lambda *args: (
                Toaster(
                    message=msg,
                    bg_color=Colors().ErrorColor.get("BackgroundColor"),
                    font_size=14,
                ).toast(),
            ),
            0,
        )
