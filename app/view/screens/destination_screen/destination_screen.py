from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from app.controller.destination_controller.destination import DestinationController

from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors
Builder.load_file("app/view/screens/destination_screen/destination_screen.kv")

class DestinationScreen(MDScreen):
    """ Most of the contents for the destination screen is auto-injected from "app/view/screens/destination_screen/destination_screen.kv"
    Other logics from the destination screen can be added here.

    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destination = ObjectProperty()
        self.destination_controller = DestinationController
        
