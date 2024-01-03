#!/usr/bin/python3
"""8-rectangle.py
"""


from 7-base_geometry import BaseGeometry

test = BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ Constructor"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height


r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))