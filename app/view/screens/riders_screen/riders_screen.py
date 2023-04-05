from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("app/view/screens/riders_screen/riders_screen.kv")

class RidersScreen(MDScreen, MDFloatLayout):
    pass