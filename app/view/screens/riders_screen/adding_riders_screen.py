import os

from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.animation import Animation

dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(dir, "adding_riders_screen.kv"))


class AddingRidersScreen(MDScreen):
    driver_name = StringProperty("Kelvin Mills")
    
    def open_riders_section(self, widget):
        Animation(pos_hint={"x": 0}, duration=0.2).start(widget)

    def hide_riders_section(self, widget):
        Animation(pos_hint={"x": 1.01}, duration=0.2).start(widget)
