"""Call methods from the view and model"""
from app.model.login_auth_model.login_auth import Authentication
from app.utils.credentials import save_credentials


class LoginAuthenticationController:
    """
    The `LoginAuthenticationController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, view) -> None:
        self.view = view
        self.model = Authentication(self.success, self.on_error)

    def login(self):
        self.view.show_loader()
        self.model.login_user()

    def success(self, token):
        save_credentials(token)
        code, msg = self.model.fetch_data(token["id_token"])
        self.view.dismiss_loader()
        if code == 200:
            self.view.go_to_main_screen(msg)
        else:
            self.view.show_error_toast(msg)

    def on_error(self, msg):
        self.view.dismiss_loader()
        self.view.show_error_toast(msg)
