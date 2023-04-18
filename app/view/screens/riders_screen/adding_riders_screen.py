import os
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(dir, "adding_riders_screen.kv"))

class AddingRidersScreen(MDScreen):
    driver_name = StringProperty("Kelvin Mills")
    
    def open_riders_section(self):
        print("Connecting to the riders section...")