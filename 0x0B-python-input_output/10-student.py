#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class to define Students attributes
    Attributes:
        first_name (str) : First name for the student
        last_name (str) : Last name for the student
        age (int) : age of student
    """

    def __init__(self, first_name, last_name, age):
        """Create public instace if Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation to JSON"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            try:
                for items in attrs:
                    new_dict[items] = self.__dict__[items]
            except Exception:
                pass
            return new_dict
