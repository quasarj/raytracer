from ray.tuple import point, vector, Vector, Point
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


p = Projectile(position=point(0, 1, 0), 
               velocity=vector(1, 2, 0).normalize())

e = Enviornment(vector(0, -0.1, 0), vector(-0.01, 0, 0))


while p.position.y > 0:
    print(p.position.x, p.position.y, p.position.z)
    p = tick(e, p)

