from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from app.commons.toast import Toaster
from app.responses.car_registration import CarRegistration
from app.utils.colors import Colors

Builder.load_file("kiv/screens/car_registration_screen.kv")


class CarRegistrationScreenContent(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.IS_DRIVING = True
        self.car_registration_number = ObjectProperty()
        self.car_capacity = ObjectProperty()
        self.driving_car_btn = ObjectProperty()
        self.not_driving_car_btn = ObjectProperty()

    def is_driving(self):
        self.IS_DRIVING = True

    def is_not_driving(self):
        self.IS_DRIVING = False

    def get_car_details(self):
        register_car = CarRegistration(self.car_registration_number.text, self.convert_capacity_value_to_int())
        response = register_car.register_car()
        if response["status"] == "error" and self.IS_DRIVING:
            Toaster(message=response["message"], bg_color=Colors().ErrorColor.get("BackgroundColor"),font_size=14).toast()
        return response

    def convert_capacity_value_to_int(self):
        return 0 if self.car_capacity.text == "" else self.car_capacity.text

    def activate_is_not_driving_fields(self):
        # Set IS_DRIVING attribute to False
        self.is_not_driving()

        # Disable car registration number and capacity input fields, and reduce opacity
        self.car_registration_number.disabled = True
        self.car_capacity.disabled = True
        self.car_registration_number.opacity = 0.4
        self.car_capacity.opacity = 0.4

        # Change UI properties of buttons to indicate user is not driving
        self.driving_car_btn.md_bg_color = "#F0F1F1"  # set background color to light gray
        self.driving_car_btn.line_color = "#F0F1F1"  # set line color to light gray
        self.driving_car_btn.text_color = "#000000"  # set text color to black
        self.not_driving_car_btn.md_bg_color = "#4285F4"  # set background color to blue
        self.not_driving_car_btn.line_color = "#4285F4"  # set line color to blue
        self.not_driving_car_btn.text_color = "#FFFFFF"  # set text color to white

    def activate_is_driving_fields(self):
        self.is_driving()
        self.car_registration_number.disabled = False
        self.car_capacity.disabled = False
        self.car_registration_number.opacity = 1
        self.car_capacity.opacity = 1
        self.not_driving_car_btn.md_bg_color = "#F0F1F1"
        self.not_driving_car_btn.line_color = "#F0F1F1"
        self.not_driving_car_btn.text_color = "#000000"
        self.driving_car_btn.md_bg_color = "#4285F4"
        self.driving_car_btn.line_color = "#4285F4"
        self.driving_car_btn.text_color = "#FFFFFF"
