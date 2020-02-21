from ray.tuple import Tuple, Point, Vector, tuple
from ray.color import Color
from ray.util import equal

# make a tuple, of any kind
@given('{var} ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var, x: float, y: float, z: float, w: float):
    setattr(context, var, tuple(x, y, z, w))

# verify a parameter is set correctly
@then(u'{var}.{attr} = {x:g}')
def step_impl(context, var, attr, x: float):
    obj = getattr(context, var)
    assert getattr(obj, attr) == x

@then(u'{a} is a point')
def step_impl(context, a):
    assert getattr(context, a).is_point()

@then(u'{a} is not a vector')
def step_impl(context, a):
    assert not getattr(context, a).is_vector()

@then(u'{a} is not a point')
def step_impl(context, a):
    assert not getattr(context, a).is_point()

@then(u'{a} is a vector')
def step_impl(context, a):
    assert getattr(context, a).is_vector()

# make a point
@given(u'{var} ← point({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    setattr(context, var, Point(x, y, z))

# make a vector
@given(u'{var} ← vector({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    setattr(context, var, Vector(x, y, z))

# special rule for negating a tuple
@then(u'-{var:S} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var, x, y, z, w):
    obj = getattr(context, var)
    assert -obj == tuple(x, y, z, w)

#ensure a tuple is set
@then(u'{var:S} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var, x, y, z, w):
    assert getattr(context, var) == tuple(x, y, z, w)

@then('{var1} == {var2}')
def step_impl(context, var1, var2):
    assert getattr(context, var1) == getattr(context, var2)


@then(u'{var1} + {var2} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, var2, x, y, z, w):
    v1 = getattr(context, var1)
    v2 = getattr(context, var2)
    assert v1 + v2 == tuple(x, y, z, w)

@then(u'{var1} - {var2} = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, var1, var2, x, y, z):
    v1 = getattr(context, var1)
    v2 = getattr(context, var2)
    assert v1 - v2 == Vector(x, y, z)

@then(u'{var1} - {var2} = point({x:g}, {y:g}, {z:g})')
def step_impl(context, var1, var2, x, y, z):
    v1 = getattr(context, var1)
    v2 = getattr(context, var2)
    assert v1 - v2 == Point(x, y, z)


# scalar multiply
@then(u'{var1} * {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, scalar, x, y, z, w):
    obj = getattr(context, var1)
    assert obj * scalar == tuple(x, y, z, w)

# scalar divide
@then(u'{var1} / {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, var1, scalar, x, y, z, w):
    obj = getattr(context, var1)
    assert obj / scalar == tuple(x, y, z, w)


#sqrt rule
@then(u'magnitude({vector}) = √{scalar:g}')
def step_impl(context, vector, scalar):
    import math
    obj = getattr(context, vector)
    test_val = math.sqrt(scalar)
    assert obj.magnitude() == test_val


@then(u'magnitude({vector}) = {scalar:g}')
def step_impl(context, vector, scalar):
    obj = getattr(context, vector)
    assert obj.magnitude() == scalar

# normalization
@when(u'{var} ← normalize({vector_var})')
def step_impl(context, var, vector_var):
    v = getattr(context, vector_var)
    setattr(context, var, v.normalize())

@then(u'normalize({vector_var}) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, vector_var, x, y, z):
    v = getattr(context, vector_var)
    assert v.normalize() == Vector(x, y, z)

@then(u'normalize({vector_var}) = approximately vector({x:g}, {y:g}, {z:g})')
def step_impl(context, vector_var, x, y, z):
    v = getattr(context, vector_var)
    noramlized = v.normalize()

    assert equal(noramlized.x, x)
    assert equal(noramlized.y, y)
    assert equal(noramlized.z, z)

@then(u'dot({vec1}, {vec2}) = {scalar:g}')
def step_impl(context, vec1, vec2, scalar: float):
    v1 = getattr(context, vec1)
    v2 = getattr(context, vec2)

    assert v1.dot(v2) == scalar

@then(u'cross({vec1}, {vec2}) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, vec1, vec2, x, y, z):
    v1 = getattr(context, vec1)
    v2 = getattr(context, vec2)

    assert v1.cross(v2) == Vector(x, y, z)
    
@given(u'{var} ← color({x:g}, {y:g}, {z:g})')
def step_impl(context, var, x, y, z):
    setattr(context, var, Color(x, y, z))

@then(u'{color1} * {scalar:g} = color({x:g}, {y:g}, {z:g})')
def step_impl(context, color1, scalar, x, y, z):
    c1 = getattr(context, color1)
    assert c1 * scalar == Color(x, y, z)
    

# test various color operations
@then(u'{color1} {op} {color2} = color({x:g}, {y:g}, {z:g})')
def step_impl(context, color1, op, color2, x, y, z):
    c1 = getattr(context, color1)
    c2 = getattr(context, color2)
    test_color = Color(x, y, z)

    if op == "+":
        assert c1 + c2 == test_color
    if op == "-":
        assert c1 - c2 == test_color
    if op == "*":
        assert c1 * c2 == test_color
