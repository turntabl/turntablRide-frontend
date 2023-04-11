from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors
from kivymd.app import MDApp

class ChatScreenController(object):
    """Handles all logic related to the chat screen
    """
    def __init__(self, destination):
        self.destination = destination
        self.root = MDApp.get_running_app().root