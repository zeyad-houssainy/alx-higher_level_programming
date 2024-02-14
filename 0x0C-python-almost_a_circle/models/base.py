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
        """that returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""
        file_name = f"{cls.__name__}.json"
        list_dic = []
        for i in list_objs:
            list_dic.append(i.to_json_string)
        with open(file_name, "w") as file:
            file.write(list_dic)
