from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors

class DestinationController(object):
    """Control and validate the user provided destination and return to model if valid 
    or back to user if not valid
    
    """
    def __init__(self, destination: str):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def register_destination(self):
        if self.is_valid_destination():
            # {"status": "success", "message": {"destination": self.destination}}
            return Toaster(message="Destination is not valid", bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
             
        # {"status": "error", "message": "Destination is not valid"}
        return Toaster(message= f"destination {self.destination}", bg_color=Colors().SuccessColor.get("BackgroundColor"),font_size=14).toast()
          

    def is_valid_destination(self):
        return len(self.destination) == 0
