from kivymd.app import MDApp

class ChatScreenController(object):
    """Handles all logic related to the chat screen
    """
    def __init__(self):
        self.root = MDApp.get_running_app().root
        
    def send_message(self):
        message = self.ids.message_input.text

        if message.strip() == "":
            return

        # Add the message to the chat label
        self.ids.chat_label.text += f"[b][color=0080ff]You:[/color][/b] {message}\n"

        # Clear the message input field
        self.ids.message_input.text = ""