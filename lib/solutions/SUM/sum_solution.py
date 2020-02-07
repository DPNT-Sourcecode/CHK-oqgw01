# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x > 100 or y > 100:
        raise ValueError("Too high value")
    return x + y