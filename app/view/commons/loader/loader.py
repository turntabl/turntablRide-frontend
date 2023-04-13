from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton

Builder.load_file("app/view/commons/loader/loader.kv")


class Loader(MDDialog):
    """This is a custom Dialog widget showing a spinner and a button"""

    def __init__(self, func=None, **kwargs):
        """
        parameters
        ----------
        func: func
            Extra function to pass to the button. By default value is None.
        kwargs: dict
            named keyword parameters that will be passed to the Parent of this
            class. (MDDialog)
        """

        cancel_btn = MDFlatButton(
            text="CANCEL",
            on_press=lambda *args: (
                func() if func is not None else None,
                self.dismiss(),
            ),
        )
        self.buttons = [cancel_btn]
        super().__init__(**kwargs)
