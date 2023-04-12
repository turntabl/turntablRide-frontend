from kivymd.app import MDApp

class ChatScreenController(object):
    """Handles all logic related to the chat screen
    """
    def __init__(self):
        #self.id = id
        self.root = MDApp.get_running_app().root
        
    def send_message(self, *args):
        # Get the current text from the TextInput
        message = self.message_input.text
        
        # Clear the TextInput
        self.message_input.text = ""
        
        # Add the new message to the chat screen
        self.chat_label.text += f"\nUser: {message}"