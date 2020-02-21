from __future__ import annotations
from math import ceil
from .tuple import Tuple

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

# Math is already defined on Tuple, so re-use it for colors
class Color(Tuple):
    def __init__(self, red, green, blue) -> Color:
        super(Color, self).__init__(red, green, blue, 0)

    def __str__(self):
        r = ceil(self.red * 255)
        g = ceil(self.green * 255)
        b = ceil(self.blue * 255)

        r = clamp(0, r, 255)
        g = clamp(0, g, 255)
        b = clamp(0, b, 255)

        return f"{r} {g} {b}"

    
    @property
    def red(self):
        return self.x

    @property
    def green(self):
        return self.y

    @property
    def blue(self):
        return self.z
