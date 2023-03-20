class PickupLocation(object):
    def __init__(self, pickup_location: str):
        self.pickup_location = pickup_location

    def get_pickup_location(self):
        return self.pickup_location

    def set_pickup_location(self, pickup_location):
        self.pickup_location = pickup_location

    def register_pickup_location(self):
        if not self.is_valid_pickup_location():
            return {"error": "Pickup is not valid"}

        return {"pickup_location": self.pickup_location}

    def is_valid_pickup_location(self):
        return False if len(self.pickup_location) == 0 else True
