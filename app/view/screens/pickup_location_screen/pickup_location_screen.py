from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from app.controller.pickup_location_controller.pickup_location import PickupLocationController


Builder.load_file("app/view/screens/pickup_location_screen/pickup_location_screen.kv")


class PickupLocationScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pick_up = ObjectProperty()

    def get_pickup_location_details(self):
        register = PickupLocation(self.pick_up.text)
        return register.register_pickup_location()



