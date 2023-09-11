#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if value < 0:
            raise TypeError("width must be an integer")
        elif not isinstance(value, int):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if value < 0:
            raise TypeError("width must be an integer")
        elif not isinstance(value, int):
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(self.__height):
            for k in range(self.__width):
                rect.append("#")
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
