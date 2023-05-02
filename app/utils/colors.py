class Colors(object):
    """
    Application colors
    Usages: import into main class and use it directly
    then in your kivy file or anywhere call it like this; for example using the ErrorColor
        app.COLORS.ErrorColor.get("BackgroundColor")

    You may add your own colors here if need be
    """

    def __init__(self):
        self.LightColor = {
            "StatusBar": "E0E0E0",
            "AppBar": "#202020",
            "Background": "#2E3032",
            "CardsDialogs": "#FFFFFF",
            "FlatButtonDown": "#CCCCCC",
        }
        self.WhiteColor = {"BackgroundColor": "#FFFFFF", "TextColor": "#FFFFFF"}
        self.GreyColor = {
            "BackgroundColor": [135, 135, 135, 0.92],
            "TextColor": [135, 135, 135, 0.92],
        }
        self.BlueColor = {"BackgroundColor": "#4285F4", "TextColor": "#4285F4"}
        self.RedColor = {"BackgroundColor": "#F44336", "TextColor": "#F44336"}
        self.BordersColor = {"BlueBorder": "#4285F4", "GreyBorder": "#F0F1F1"}
        self.BlackColor = {"TextColor": "#000000", "BackgroundColor": "#000000"}
        self.ErrorColor = {"BackgroundColor": "#B00020", "TextColor": "#B00020"}
        self.SuccessColor = {"BackgroundColor": "#4BB543", "TextColor": "#B00020"}
