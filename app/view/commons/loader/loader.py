from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

Builder.load_file("app/view/commons/loader/loader.kv")


class Loader(MDDialog):
    """This is a custom Dialog widget showing a spinner and a button"""
