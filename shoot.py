from ray.tuple import Vector, Point
from ray.canvas import Canvas
from ray.color import Color

from typing import NamedTuple

class Enviornment(NamedTuple):
    gravity: Vector
    wind: Vector

class Projectile(NamedTuple):
    position: Point
    velocity: Vector



def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


start = Point(0, 1, 0)
velocity = Vector(1, 1.8, 0).normalize() * 11.25

p = Projectile(start, velocity)

gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)
e = Enviornment(gravity, wind)
c = Canvas(900, 550)


while p.position.y > 0:
    x = int(p.position.x)
    y = int(p.position.y)

    print(x, y)

    # flip y
    y_f = c.height - y
    c[x, y_f] = Color(1, 1, 1)

    p = tick(e, p)


with open("out.ppm", "w") as outfile:
    outfile.write(c.to_ppm())
