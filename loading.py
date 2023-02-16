from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivyauth.utils import stop_login
from kivy.lang import Builder


Builder.load_file("loading.kv")

class Loading(MDDialog):

    def __init__(self, **kwargs):
        cancel_btn = MDFlatButton(text="CANCEL", on_release=lambda *args: (stop_login(), self.dismiss()))
        self.buttons = [cancel_btn]
        super().__init__(**kwargs)