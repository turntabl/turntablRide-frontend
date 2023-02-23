from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivyauth.utils import stop_login
from kivy.lang import Builder

# used to load the kv file and make it available.
Builder.load_file("kv_files/loading.kv")

class Loading(MDDialog):
    '''This is a custom Dialog widget showing a spinner and a button'''

    def __init__(self, **kwargs):
        cancel_btn = MDFlatButton(text="CANCEL", on_release=lambda *args: (stop_login(), self.dismiss()))
        self.buttons = [cancel_btn]
        super().__init__(**kwargs)