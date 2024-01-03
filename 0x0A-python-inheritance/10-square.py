#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self, size):
        if (self.integer_validator("size", size)):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
