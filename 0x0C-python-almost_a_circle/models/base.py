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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: jason string representation.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
