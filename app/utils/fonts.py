from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
resource_add_path('assets/fonts/')
class Fonts(object):
    """
    Application Fonts
    Usages: import into main class and use it directly
    then in your kivy file or anywhere call it like this; for example
        app.Fonts().fonts.get("jakarta")
    """
    def __init__(self):

        LabelBase.register(name="jakarta",
                            fn_regular ="PlusJakartaSans-Regular.ttf", 
                            fn_italic="PlusJakartaSans-Italic.ttf",
                             fn_bold="PlusJakartaSans-Bold.ttf", 
                             fn_bolditalic="PlusJakartaSans-BoldItalic.ttf")
        self.fonts = {
                        "jakarta_normal": "PlusJakartaSans-Italic.ttf"
                        }
        self.weight = {
                        "weight_700": 700
                        }
        
