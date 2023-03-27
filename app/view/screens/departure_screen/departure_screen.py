from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file("app/view/screens/departure_screen/departure_screen.kv")

class DepartureScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.departure = ObjectProperty(None)
