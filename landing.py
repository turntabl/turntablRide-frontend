from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("kv_files/landing.kv")


class WelcomeView(BoxLayout):
    pass


class DashBoardView(BoxLayout):
    pass


class MyApp(MDApp):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.screen_manager = ScreenManager()

        self.welcome_screen = Screen(name="welcome")
        self.welcome_screen.add_widget(WelcomeView())
        self.screen_manager.add_widget(self.welcome_screen)

        self.login_screen = Screen(name="login")
        self.login_screen.add_widget(DashBoardView())
        self.screen_manager.add_widget(self.login_screen)
        return self.screen_manager


if __name__ == "__main__":
    MyApp().run()
