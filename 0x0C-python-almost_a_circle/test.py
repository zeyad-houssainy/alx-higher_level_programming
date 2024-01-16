from models.base import Base
def test_function(var1, *argv):
    print(f"Variable Number 1: {var1}")
    count = 2
    for items in argv:
        print(f"Variable number {count}: {items}")
        count += 1

test_function("Mohamed", "Zeyad", "Habiba","Rana", "Sarah")

print("$$$$$$$$$$$$$$$$$$$$")

dict = {"name": "Zeyad", "Age": 29, "Hobbies": ["Games", "Programming"]}
# print(dict)

# for key, value in dict.iteritems():
#     print(f"{key} >>> {value}")

def test_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key} >>> {value}")


test_kwargs(name = "Hi i'm zeyad")


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print (f"{key} == {value}")
greet_me(name = "Raneem", age = 26)


#!/usr/bin/python3
'''Module for Rectangle class.'''


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
