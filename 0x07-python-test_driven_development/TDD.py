from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("Number shouldn't be negative, Chose a positive value")
    return (pi*(r**2))
