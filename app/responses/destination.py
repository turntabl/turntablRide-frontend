class Destination(object):
    def __init__(self, destination: str):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def register_destination(self):
        if self.is_valid_destination():
           return {"status": "success", "message": {"destination": self.destination}}
            
        return  {"status": "error", "message": "Destination is not valid"}

    def is_valid_destination(self):
        return len(self.destination) == 0
