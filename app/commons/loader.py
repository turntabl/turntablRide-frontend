from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from app.google_auth.server import trigger_server_stop


# used to load the kv file and make it available.
Builder.load_file("kiv/commons/loader.kv")


class Loading(MDDialog):
    """This is a custom Dialog widget showing a spinner and a button"""

    def __init__(self, **kwargs):

        cancel_btn = MDFlatButton(
            text="CANCEL",
            on_press=lambda *args: (trigger_server_stop(), self.dismiss()),
        )
        self.buttons = [cancel_btn]
        super().__init__(**kwargs)
