from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from app.commons.toast import Toaster
from app.responses.destination import Destination
from app.utils.colors import Colors
Builder.load_file("kiv/screens/destination_screen.kv")

class DestinationScreenContent(MDScreen):
    """ Most of the contents for the destination screen is auto-injected from "kiv/screens/destination_screen.kv"
    Other logics from the destination screen can be added here.

    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destination = ObjectProperty()
        

    def destination_details(self) -> dict[str: str]:
        """Get the user provided destination details from UI

        :return: validated object
        :rtype: dict
        """
        register = Destination(self.destination.text)
        response = register.register_destination()
        if response["status"] == "error":
            Toaster(message=response["message"], bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
        return response
