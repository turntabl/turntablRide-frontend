from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from app.utils.colors import Colors
from app.utils.fonts import Fonts
from config.config import PREFERRED_WINDOW_SIZE, APP_TITLE, APP_ICON


class WindowManager(MDScreenManager):
    """Manages and switches the applications to different screens.
    Actual implementation is found in the ` run.kv ` file

    :param MDScreenManager: Screen manager. This is the main class that will control your ~kivymd.uix.screen.MDScreen stack and memory
    :type MDScreenManager: ~kivymd.uix.screenmanager.MDScreenManager
    """

    pass


class Run(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = APP_TITLE
        self.icon = APP_ICON
        Window.size = PREFERRED_WINDOW_SIZE
        self.COLORS = Colors()
        self.Fonts = Fonts()
        self.load_all_kv_files(self.directory)

    def on_start(self) -> None:
        self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    Run().run()
