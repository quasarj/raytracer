from ray.color import Color
from ray.canvas import Canvas

@given(u'{var} ← canvas({width:d}, {height:d})')
def step_impl(context, var, width, height):
    setattr(context, var, Canvas(width, height))


@then(u'every pixel of {var} is color({r:g}, {g:g}, {b:g})')
def step_impl(context, var, r, g, b):
    canvas = getattr(context, var)
    color = Color(r, g, b)

    for pixel in canvas:
        assert pixel == color

@when(u'write_pixel({canvas}, {x:d}, {y:d}, {color})')
def step_impl(context, canvas, x: int, y: int, color):
    ca = getattr(context, canvas)
    co = getattr(context, color)

    ca[x, y] = co


@then(u'pixel_at({canvas}, {x:d}, {y:d}) = {color}')
def step_impl(context, canvas, x, y, color):
    ca = getattr(context, canvas)
    co = getattr(context, color)

    assert ca[x, y] == co


@when(u'{ppm} ← canvas_to_ppm({canvas})')
def step_impl(context, ppm, canvas):
    c = getattr(context, canvas)
    setattr(context, ppm, c.to_ppm())


@then(u'lines 1-3 of {ppm} are')
def step_impl(context, ppm):
    p = getattr(context, ppm)
    assert p.splitlines()[:3] == context.text.splitlines()

@then(u'lines 4-18 of {ppm} are')
def step_impl(context, ppm):
    p = getattr(context, ppm)

    a = p.splitlines()[3:18]
    b = context.text.splitlines()

    print(a)
    print(b)

    assert a == b

