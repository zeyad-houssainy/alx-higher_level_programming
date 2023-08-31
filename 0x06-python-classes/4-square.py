#!/usr/bin/python3
"""define an empty class square"""


class Square:
    """square class is generated"""

    def __init__(self, size=0):
        """initiate attributes"""
        self.size = size

    def size(self):
        """Getter for private __size"""
        return (self.__size)

    def size(self, value):
        """setter for private __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of the square.size"""
        return (self.size * self.size)


###############################################
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
