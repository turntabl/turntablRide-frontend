from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from app.controller.car_registration_controller.car_registration import CarRegistrationController

from app.view.commons.toast.toast import Toaster
from app.utils.colors import Colors

Builder.load_file("app/view/screens/car_registration_screen/car_registration_screen.kv")


class CarRegistrationScreen(MDScreen):
    """ Most of the contents for the CarRegistrationScreen screen is auto-injected from "app/view/screens/card_registration_screen/card_registration_screen.kv"
    Other logics from the CarRegistrationScreen screen can be added here.

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.IS_DRIVING = True
        self.car_registration_number = ObjectProperty()
        self.car_capacity = ObjectProperty()
        self.driving_car_btn = ObjectProperty()
        self.not_driving_car_btn = ObjectProperty()
        self.car_registration_controller = CarRegistrationController

    def is_driving(self) -> None:
        """Activate driving"""
        self.IS_DRIVING = True

    def is_not_driving(self) -> None:
        """Deactivate drving"""
        self.IS_DRIVING = False

    def get_car_details(self)  -> None:
        """Get input car details to controller"""
        if self.IS_DRIVING:
            self.car_registration_controller(self.car_registration_number.text, self.convert_capacity_value_to_int()).register_car()

        Toaster(message="Thank you. You are not driving today", bg_color=Colors().SuccessColor.get("BackgroundColor"),font_size=14).toast()

    def convert_capacity_value_to_int(self) -> int:
        """ Convert the type of car capacity when empty from str to int
        """
        return 0 if self.car_capacity.text == "" else self.car_capacity.text

    def activate_is_not_driving_fields(self) -> None:

        # Set IS_DRIVING attribute to False
        self.is_not_driving()

        # Disable car registration number and capacity input fields, and reduce opacity
        self.car_registration_number.disabled = True
        self.car_capacity.disabled = True
        self.car_registration_number.opacity = 0.4
        self.car_capacity.opacity = 0.4

        # Change UI properties of buttons to indicate user is not driving
        self.driving_car_btn.md_bg_color = Colors().GreyColor.get("BackgroundColor")  # set background color to light gray
        self.driving_car_btn.line_color = Colors().GreyColor.get("BackgroundColor")  # set line color to light gray
        self.driving_car_btn.text_color = Colors().BlackColor.get("BackgroundColor")  # set text color to black
        self.not_driving_car_btn.md_bg_color = Colors().BlueColor.get("BackgroundColor")  # set background color to blue
        self.not_driving_car_btn.line_color = Colors().BlueColor.get("BackgroundColor")  # set line color to blue
        self.not_driving_car_btn.text_color = Colors().WhiteColor.get("BackgroundColor")  # set text color to white

    def activate_is_driving_fields(self) -> None:
        """Activate driving fields. That is registration and capacity input fields"""
        self.is_driving()
        self.car_registration_number.disabled = False
        self.car_capacity.disabled = False
        self.car_registration_number.opacity = 1
        self.car_capacity.opacity = 1
        self.not_driving_car_btn.md_bg_color = Colors().GreyColor.get("BackgroundColor")
        self.not_driving_car_btn.line_color = Colors().GreyColor.get("BackgroundColor")
        self.not_driving_car_btn.text_color = Colors().BlackColor.get("BackgroundColor")
        self.driving_car_btn.md_bg_color = Colors().BlueColor.get("BackgroundColor")
        self.driving_car_btn.line_color = Colors().BlueColor.get("BackgroundColor")
        self.driving_car_btn.text_color = Colors().WhiteColor.get("BackgroundColor")
