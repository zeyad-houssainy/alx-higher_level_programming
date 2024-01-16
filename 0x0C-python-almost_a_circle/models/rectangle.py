#!/usr/bin/python3
"""Module for the Rectangle class"""
from base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = x
        super().__init__(id)

    @property
    def width(self):
        """Getter for the width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.validate_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for the width parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for the X parameter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X"""
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the Y parameter"""
        return self.__y

    @width.setter
    def y(self, value):
        """Setter for Y"""
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        """Validation for integer positive values"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive number 'number > 0'")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
