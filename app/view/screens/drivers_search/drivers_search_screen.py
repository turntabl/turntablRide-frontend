from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from app.controller.drivers_search_controller.drivers_search import DriversSearchController


Builder.load_file("app/view/screens/drivers_search/drivers_search_screen.kv")


class DriversSearchScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drivers_search = ObjectProperty()


