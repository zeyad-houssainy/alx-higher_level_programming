#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get/set width if rectangle"""
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
        """get/set height if rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if value < 0:
            raise TypeError("width must be an integer")
        elif not isinstance(value, int):
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(self.__height):
            for k in range(self.__width):
                rect.append("#")
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
