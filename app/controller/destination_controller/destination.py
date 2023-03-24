from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors
from kivymd.app import MDApp

class DestinationController(object):
    """Control and validate the user provided destination and return to model if valid 
    or back to user if not valid

    """
    def __init__(self, destination: str):
        self.destination = destination
        self.root = MDApp.get_running_app().root

    def get_destination(self) -> str:
        return self.destination

    def set_destination(self, destination: str) -> None:
        self.destination = destination

    def register_destination(self) -> None:
        if self.is_valid_destination():
            Toaster(message="Destination is not valid", bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
             
        # TODO send data to model or cache and proceed to next scrren
        self.root.current = "CarRegistrationScreen"
        self.root.transition.direction = "left"
        Toaster(message= f"destination {self.destination}", bg_color=Colors().SuccessColor.get("BackgroundColor"),font_size=14).toast()
          

    def is_valid_destination(self) -> bool:
        return len(self.destination) == 0
