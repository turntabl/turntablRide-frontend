from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from app.responses.login_auth import Authentication

Builder.load_file("kiv/screens/login_screen.kv")


class LoginScreenContent(MDScreen):
    """ Most of the contents for the login screen is auto-injected from "kiv/screens/login_screen.kv"
    Other logics from the login screen can be added here. eg: button responses and validations

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def login_with_google(self) -> dict[str: str]:
        login_responses = Authentication().login_and_register_user()

        # if login_responses["status"] == "error":
        #     Toaster(message=response["message"], bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
        return login_responses
