from __future__ import annotations
import math
from .util import equal

class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self: Tuple) -> bool:
        return equal(self.w, 1.0)

    def is_vector(self: Tuple) -> bool:
        return equal(self.w, 0.0)

    def magnitude(self: Tuple) -> float:
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2 +
            self.w ** 2
        )

    def normalize(self: Tuple) -> Tuple:
        mag = self.magnitude()
        return tuple(self.x / mag,
                     self.y / mag,
                     self.z / mag,
                     self.w / mag)

    def dot(self: Tuple, other: Tuple) -> float:
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z +
            self.w * other.w
        )

    def cross(self: Tuple, other: Tuple) -> Tuple:
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __eq__(self: Tuple, other: Tuple) -> bool:
        return (equal(self.x, other.x) and
                equal(self.y, other.y) and
                equal(self.z, other.z) and
                equal(self.w, other.w))

    def __add__(self: Tuple, other: Tuple) -> Tuple:
        return tuple(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z,
                     self.w + other.w)
                
    def __sub__(self: Tuple, other: Tuple) -> Tuple:
        return tuple(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z,
                     self.w - other.w)

    def __neg__(self: Tuple) -> Tuple:
        return tuple(0, 0, 0, 0) - self

    # allow multiplying by a scalar only
    def __mul__(self: Tuple, other) -> Tuple:
        if isinstance(other, Tuple):
            return tuple(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
                self.w * other.w
            )
        else:
            return tuple(self.x * other,
                         self.y * other,
                         self.z * other,
                         self.w * other)

    def __truediv__(self: Tuple, scalar: float) -> Tuple:
        return tuple(self.x / scalar,
                     self.y / scalar,
                     self.z / scalar,
                     self.w / scalar)

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

class Point(Tuple):
    def __init__(self, x, y, z):
        super(Point, self).__init__(x, y, z, 1)

class Vector(Tuple):
    def __init__(self, x, y, z):
        super(Vector, self).__init__(x, y, z, 0)


# shortcuts
def tuple(x: float, y: float, z: float, w: float) -> Tuple:
    """Create a Vector or a Point, depending on w"""

    if equal(w, 1.0): return Point(x, y, z)
    if equal(w, 0.0): return Vector(x, y, z)
    return Tuple(x, y, z, w)
