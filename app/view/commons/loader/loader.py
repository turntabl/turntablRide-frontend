from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder


# used to load the kv file and make it available.


class Loader(MDDialog):
    """This is a custom Dialog widget showing a spinner and a button"""

    def __init__(self, stop_server, **kwargs):
        self.stop_server = stop_server
        cancel_btn = MDFlatButton(
            text="CANCEL",
            on_press=lambda *args: (self.stop_server(), self.dismiss()),
        )
        self.buttons = [cancel_btn]
        super().__init__(**kwargs)
