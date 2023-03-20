from kivy.lang import Builder
from kivy_garden.mapview import MapMarker
from kivy.animation import Animation

Builder.load_file("kiv/commons/gps_blinker.kv")


class GpsBlinker(MapMarker):
    current_lat = 5.614818
    current_lon = -0.205874
    def blink(self):
        # Animation that changes the blink size and opacity
        anim = Animation(outer_opacity=0, blink_size=50)

        # When the animation completes, reset the animation, then repeat
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self, *args):
        self.outer_opacity = 1
        self.blink_size = self.default_blink_size
        self.blink()
