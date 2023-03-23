from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

from app.utils.colors import Colors


class Toaster(object):
    """ Customized snackbar as app Toaster, extending from BaseSnackbar . This Toaster has been created to handle all customized user errors.
    The Toaster comes with two functionalities.

    1. 
        A simple Toaster with message
        To use this toast, just import it into your class and use. You may not need to instantiate.
        for example:

            `` Toaster(message="Message to display on Toster", bg_color= self.colors.ErrorColor.get("BackgroundErrorColor"), font_size=14).toast() ``
        
        Note: You must call .toast() on Toaster in other to display it.
        i.e:
            Toaster(...).toast()
        just like above example

    2. 
        A simple Toaster with message and buttons.
        To use, just import it into your class and use. You may not need to instantiate.
        for example:

            `` Toaster(message="Message to display on Toster", bg_color=self.colors.ErrorColor.get("BackgroundErrorColor"), font_size=14).toast_with_buttons(2,["Cancel", "ok"], ["#F44336", "#F44336"],[lambda *args: 2,lambda *args: 4]) ``
        
        Note: You must call .toast_with_buttons() on Toaster in other to display and use the buttons.
        i.e:
            Toaster(...).toast_with_buttons(...)

        TODO: Fix misalignment of button in toast
    """
    def __init__(self,
                 message: str = "Pass your own message here",
                 bg_color: str = "BlueColor",
                 font_size: int = 14,
                 duration: int = 3,
                 auto_dismiss: bool = True):
        self.message = message
        self.colors = Colors()
        self.bg_color = self.colors.BlueColor.get("BackgroundColor") if bg_color == "BlueColor" else bg_color
        self.font_size = font_size
        self.duration = duration
        self.auto_dismiss = auto_dismiss

        self.toaster = Snackbar(
            snackbar_x=dp(10),
            snackbar_y=dp(10),
            text=self.message,
            bg_color=self.bg_color,
            font_size=sp(self.font_size),
            duration=self.duration,
            auto_dismiss=self.auto_dismiss,
            radius= [10, 10, 10, 10]
            )
        self.toaster.size_hint_x = (Window.width - (self.toaster.snackbar_x * 2)) / Window.width

    def toast(self) -> "Toaster":
        """Call this method to display toast or to cause the toast to open and show.
        This doesn't show any buttons on toast. Use @toast_with_buttons method to use buttons

        :return: Opens the Toaster to toast
        :rtype: Toaster
        """
        return self.toaster.open()

    def toast_with_buttons(self, number_of_buttons: int, text: list[str], text_color: list[str], on_release_action:
    list[object]):
        """Extra functionality with the toast. Call this method to add buttons to the Toaster.
        The text,  text_color and on_release_action must be a list even if it a single button to display on Toaster
        NB: IT CURRENTLY HAS A BUG OF ALIGNMENT OF BUTTON COMPONENT
        
        For example to show a single button
        number_of_buttons = 1
        text = ["Cancel"]
        text_color = ["#FFFFFF"]
        on_release_action = [do_cancel_action]
        ----------------------------------------------
        For example to show 2 buttons
        number_of_buttons = 2
        text = ["Cancel", "Dismiss"]
        text_color = ["#FFFFFF", " #F44336"]
        on_release_action = [do_cancel_action, do_dismiss_action]
        So for each button would match 
        MDFlatButton(
                text = "Cancel",
                text_color = "#FFFFFF",
                on_release = do_cancel_action,
            )
            etc
        TODO: Fix misalignment of button in toast
        :param number_of_buttons: The number of buttons you wish to appear on toast
        :type number_of_buttons: int
        :param text: A List of the label names on each button
        :type text: list[str]
        :param text_color: a List of the color names on each button
        :type text_color: list[str]
        :param on_release_action: The callback action on release on the button
        :type on_release_action: list[function]. You may anonymous functions here (lamda)
        :return: a full Toaster with buttons
        :rtype: Toaster
        """

        self.toaster.buttons = [
            MDFlatButton(
                text=text[each_button].strip(),
                text_color=text_color[each_button].strip(),
                on_release=on_release_action[each_button],
            )
            for each_button in range(number_of_buttons) if number_of_buttons is not None]
        return self.toast()

