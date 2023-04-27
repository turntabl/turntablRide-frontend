from kivymd.app import MDApp
from kivy.clock import Clock

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
        
    def get_ride_chat_name(self, driver):
        return f"{driver.first_name} Ride Chat"
        
    # def start_or_end_ride(self, ride):
    #     if ride.start == False:
    #         ride.start = True
    #         return "Ride Started"
    #     else:
    #         ride.start = False
    #         return "Ride Ended"   
        
    
    def get_ride_details(self, ride):
        rider = f"{ride.driver.first_name} ' ' {ride.driver.last_name}" 
        car_number = ride.car_number
        start_location = ride.start_destination
        end_location = ride.end_location
        set_off_time = ride.set_off_time
        wait_time = ride.max_wating_time
        
        context = {"Name": rider,
                   "Car Number": car_number,
                   "From": start_location,
                   "To": end_location,
                   "Set-Off Time": set_off_time,
                   "Wait time": wait_time
                   }
        return context
    
    def go_back(self):
        pass