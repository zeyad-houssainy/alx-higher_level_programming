#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class define properties of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Create instances of a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(self.__class__.__name__, self.id,
                   self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size parameter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.validate_integer("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update values for the square parameters"""
        if args is not None and len(args) != 0:
            list_atrr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list_atrr[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
