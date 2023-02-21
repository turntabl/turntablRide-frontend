from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
import os
from dotenv import load_dotenv
from loading import Loading
from kivyauth.google_auth import login_google, initialize_google
from kivymd.app import MDApp

load_dotenv()

class Authentication:
    def __init__(self):
        initialize_google(self.after_login, self.error_listener, os.environ["GOOGLE_CLIENT_ID"], os.environ["GOOGLE_CLIENT_SECRET"])
        self.__loading = Loading()

    def login(self):
        self.__loading.open()
        login_google()

    def after_login(self, name, email, photo_uri):
        self.__loading.dismiss()
        MDApp.get_running_app().root.current = "login"

    def error_listener(self):
        Snackbar(text="Error logging in. Check connection or try again.").open()
        Clock.schedule_once(lambda *args: self.__loading.dismiss())