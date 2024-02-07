#!/usr/bin/python3
'''Module for Rectangle class.'''
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
        self.validate_integer("width", self.__width)
        self.validate_integer("height", self.__height)
        self.validate_integer("x", self.__x)
        self.validate_integer("y", self.__y)

    @property
    def width(self):
        """Getter for the width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for the height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for the X parameter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for X"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the Y parameter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value):
        """Validation for integers and values"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """returns area for the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display a representation for the Recatngle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """returns a presentation for the class"""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """update the values for the object"""
        if args:
            # if *args are existing
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_2 = {
            "id": self.__id,
            "x": self.__x,
            "y": self.__y,
            "width": self.__width,
            "height": self.__height,
        }
        return dict_2
