
EPSILON = 0.00001
def equal(a, b):
    if abs(a - b) < EPSILON:
        return True
    else:
        return False

