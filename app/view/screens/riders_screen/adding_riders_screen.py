from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("app/view/screens/riders_screen/adding_riders_screen.kv")
class AddingRidersScreen(MDScreen, MDFloatLayout):
    pass