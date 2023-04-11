from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from app.controller.chat_screen_controller.chat_screen import ChatScreenController

Builder.load_file("app/view/screens/chat_screen/chat_screen.kv")

class ChatScreen(MDScreen):
    """Most of the chat screen contents is auto-injected from the loaded "app/view/screens/chat_screen.kv" file"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = ChatScreenController()
