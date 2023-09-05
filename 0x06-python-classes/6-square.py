#!/usr/bin/python3
"""define an empty class square"""


class Square:
    """square class is generated"""

    def __init__(self, size=0, position=None):
        """initiate attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for private __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position"""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or (isinstance(value, tuple) and len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")                    
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
