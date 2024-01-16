#!/usr/bin/python3
"""Module for the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value

    @property
    def height(self):
        """Getter for the width parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for the X parameter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X"""
        self.__x = value

    @property
    def y(self):
        """Getter for the Y parameter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        self.__y = value
