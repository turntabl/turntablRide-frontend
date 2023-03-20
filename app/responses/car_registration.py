class CarRegistration(object):
    def __init__(self, car_number: str, car_capacity: int):
        self.car_number = car_number
        self.car_capacity = car_capacity

    def is_valid_car_number(self):
        return False if len(self.car_number) <= 3 else True

    def is_valid_car_capacity(self):
        return False if int(self.car_capacity) == 0 or self.car_capacity == "" else True

    def get_car_number(self):
        return self.car_number

    def get_car_capacity(self):
        return self.car_capacity

    def set_car_number(self, car_number):
        self.car_number = car_number

    def set_car_capacity(self, car_capacity):
        self.car_capacity = car_capacity

    def register_car(self):
        if not self.is_valid_car_number():
            return {"status": "error", "message": "Car number must be greater than 3 characters"}
        if not self.is_valid_car_capacity():
            return {"status": "error", "message": "Car capacity cannot zero or less than zero"}

        return {"status": "success", "message": {"car_number": self.car_number, "car_capacity": self.car_capacity}}
