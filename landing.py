from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import asyncio
from auth import LoginView

# from kivy.app import async_runTouchApp


Builder.load_file("kv_files/landing.kv")


class OurScreenManager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return OurScreenManager()


if __name__ == "__main__":
    asyncio.run(MyApp().async_run())
