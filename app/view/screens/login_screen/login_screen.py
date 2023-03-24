from kivymd.uix.screen import MDScreen
from app.controller.auth_controller.login_auth import LoginAuthenticationController
from kivy.lang import Builder

Builder.load_file("app/view/screens/login_screen/login_screen.kv")



class LoginScreen(MDScreen):
    """ Most of the contents for the login screen is auto-injected from 
        `` app/view/screens/login_screen/login_screen.kv ``

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = LoginAuthenticationController()

