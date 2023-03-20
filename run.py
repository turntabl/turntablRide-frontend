from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from app.utils.colors import Colors
from app.utils.fonts import Fonts

""" The run.py would contain all the screens of the application as well as the Screen Manager.
    All new developed screens must be included here. As shown below (LoginScreen class) is included as a screen
    which would be managed by the WindowManager class.
    The contents and stylying of the screens goes into app/screens/ and kiv/screens/ respectively
"""

class LoginScreen(MDScreen):
    """Holds the login screen of the app


    :param MDScreen: A a component of MDScreenManager  
    :type MDScreen: ~kivymd.uix.screenmanager.MDScreenManager
    """
    pass



class WindowManager(MDScreenManager):
    """ Manages and switches the applications to different screens

    :param MDScreenManager: Screen manager. This is the main class that will control your ~kivymd.uix.screen.MDScreen stack and memory  
    :type MDScreenManager: ~kivymd.uix.screenmanager.MDScreenManager
    """
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
