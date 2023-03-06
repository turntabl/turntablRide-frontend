from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from loading import Loading
from kivymd.app import MDApp
from google_oauth import GoogleOAuth

class Authentication:
    '''
    This class provides authentication functionality using Google Oauth2.

    Notes
    -----
    This class only works with Desktop applications
    '''

    def __init__(self):
        # initialize_google(self.after_login, self.error_listener, os.environ["GOOGLE_CLIENT_ID"], os.environ["GOOGLE_CLIENT_SECRET"])
        self.__google_login = GoogleOAuth(self.after_login)
        self.__loading = Loading(self.__google_login.stop_server)

    def login(self):
        '''Method to call to start the login process.'''
        self.__loading.open()
        if self.__google_login.login():
            #call after login
            return 
        else:
            # call error handler
            self.error_listener()
            return

    def after_login(self, name, email, photo_uri):
        '''
        Is called after the login process is successful.

        Parameters
        ----------
        name : str
            The name of the user in Google
        email : str
            The google email of the user used to signin 
        photo_uri : str
            A url to the google profile of the user
        '''

        self.__loading.dismiss()
        MDApp.get_running_app().root.current = "login"

    def error_listener(self):
        '''Called whenever there is an error in the login process'''

        Snackbar(text="Error logging in. Check connection or try again.").open()
        Clock.schedule_once(lambda *args: self.__loading.dismiss())