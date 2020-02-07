# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x > 100 or y > 100:
        raise ValueError("Too high value")
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Error")
    return x + y
