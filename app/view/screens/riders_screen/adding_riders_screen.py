import os
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

dir = os.path.dirname(__file__)
Builder.load_file(os.path.join(dir, "adding_riders_screen.kv"))

class AddingRidersScreen(MDScreen):
    pass