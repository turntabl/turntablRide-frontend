from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from app.utils.colors import Colors
from app.utils.fonts import Fonts


class LoginScreen(MDScreen):
    pass



class WindowManager(MDScreenManager):
    pass


class Run(MDApp):

    def __init__(self, **kwargs):
        super().__init__()
        self.COLORS = Colors()
        self.Fonts = Fonts()

    def on_start(self):
        Window.size = (360, 640)
        
        self.theme_cls.theme_style = "Light"


if __name__ == '__main__':
    Run().run()
