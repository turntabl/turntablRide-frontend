import os
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton
from kivy.lang import Builder
from kivy.core.window import Window

dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(dir, "adding_riders_screen.kv"))


class AddingRidersScreen(MDScreen):
    driver_name = StringProperty("Kelvin Mills")
    
    def open_riders_section(self):
        print(self.ids)
        print("Connecting to the riders section...")