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
