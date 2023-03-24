"""Call methods from the view and model"""
from app.model.login_auth_model.login_auth import Authentication
from app.view.screens.login_screen.login_screen import LoginScreen


class LoginAuthenticationController:
    """
    The `LoginAuthenticationController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self) -> None:
        self.view = LoginScreen()
        self.model = Authentication(self.after_login, self.view.show_error_toast)

    def login(self):
        self.view.show_loader()
        self.model.login_user()

    def after_login(self, token):
        code, msg = self.model.fetch_data(token)
        self.view.dismiss_loader()
        if code == 200:
            self.view.go_to_main_screen(msg)
        else:
            self.view.show_error_toast(msg)
