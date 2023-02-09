from kivymd.app import MDApp
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from kivy.uix.image import Image
from kivyauth.utils import stop_login
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivyauth.google_auth import initialize_google, login_google


class WelcomeView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        initialize_google(self.after_login, self.error_listener, os.environ["GOOGLE_CLIENT_ID"], os.environ["GOOGLE_CLIENT_SECRET"])
        self.orientation = "vertical"
        self.add_widget(Label(text="turntablRide", color=(0, 0, 0), bold=True, font_size=35,
                              size_hint=(1.0, 0.2)))
        # Create an image widget
        image = Image(source='images/landing_big.png')
        # Add the Image widget
        self.add_widget(image)
        # Adding button
        btn_box = BoxLayout(orientation="horizontal", size_hint=(0.3, 0.1), pos_hint={"x": 0.35})
        google_icon = Image(source='images/google_icon.png', size_hint=(0.3, 1.0))
        login_btn = Button(text="Login with Google", bold=True, font_size=18,
                           background_color=[0.234, 0.59, 0.965, 1],
                           background_normal="", on_press=self.login)
        btn_box.add_widget(google_icon)
        btn_box.add_widget(login_btn)
        self.add_widget(btn_box)
        self.padding = [0, 0, 0, 100]

        cancel_btn = MDFlatButton(text="CANCEL")
        cancel_btn.bind(on_release=lambda *args: (stop_login(), self.dialog.dismiss()))

        self.dialog = MDDialog(
            title="",
            size_hint_x=None,
            size_hint_y=None,
            width="250dp",
            type="custom",
            auto_dismiss=False,
            content_cls=Content(),
            buttons=[cancel_btn],
            )

    def login(self, instance):
        login_google()
        self.dialog.open()
        print("successfull")

    def after_login(self, name, email, photo_uri):
        self.dialog.dismiss()
        MDApp.get_running_app().root.current = "login"

    def error_listener(self):
        Snackbar(text="Error logging in. Check connection or try again.").open()
        Clock.schedule_once(lambda *args: self.dialog.dismiss())


class LoginView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Welcome Back", color=(0, 0, 0),
                              bold=True, size_hint=(0.3, 0.12), pos_hint={"x": 0.35}))


class Content(BoxLayout):
    pass


class MyApp(MDApp):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        from kivy.uix.screenmanager import ScreenManager, Screen
        self.screen_manager = ScreenManager()

        self.welcome_screen = Screen(name="welcome")
        self.welcome_screen.add_widget(WelcomeView())
        self.screen_manager.add_widget(self.welcome_screen)

        self.login_screen = Screen(name="login")
        self.login_screen.add_widget(LoginView())
        self.screen_manager.add_widget(self.login_screen)
        return self.screen_manager


if __name__ == "__main__":
    MyApp().run()
