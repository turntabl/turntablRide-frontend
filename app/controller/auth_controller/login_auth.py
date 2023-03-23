"""Call methods from the view and model"""
from app.model.login_auth_model.login_auth import Authentication


class LoginAuthenticationController:
    """
    The `LoginAuthenticationController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self) -> None:
        pass

    def verify_user(self):
        return Authentication().login_and_register_user()
