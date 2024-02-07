#!/usr/bin/python3
"""Module for the base class"""
import json


class Base:
    """A representation of the base of our OOP hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the base model object
        Attributes:
            id (int): case for the ID for the constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """that returns the JSON string representation"""
