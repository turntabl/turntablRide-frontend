from app.utils.colors import Colors
from app.view.commons.toast.toast import Toaster
from kivymd.app import MDApp

class CarRegistrationController(object):
    def __init__(self, car_number: str, car_capacity: int):
        self.car_number = car_number
        self.car_capacity = car_capacity
        self.root = MDApp.get_running_app().root

    def is_valid_car_number(self) -> bool:
        return False if len(self.car_number) <= 3 else True

    def is_valid_car_capacity(self) -> bool:
        return False if int(self.car_capacity) == 0 or self.car_capacity == "" else True

    def get_car_number(self) -> str:
        return self.car_number

    def get_car_capacity(self) -> int:
        return self.car_capacity

    def set_car_number(self, car_number: str) -> None:
        self.car_number = car_number

    def set_car_capacity(self, car_capacity: int) -> None:
        self.car_capacity = car_capacity

    def register_car(self) -> None:
        if not self.is_valid_car_number():
            Toaster(message="Car number must be greater than 3 characters", bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
        if not self.is_valid_car_capacity():
            Toaster(message="Car capacity cannot zero or less than zero", bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
        
        self.root.current = "CarRegistrationScreen"
        Toaster(message=f"car_number : {self.car_number}, car_capacity: {self.car_capacity}", bg_color=Colors().SuccessColor.get("BackgroundColor"),font_size=14).toast()
