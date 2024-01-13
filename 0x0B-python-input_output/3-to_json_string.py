#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Return to JSON string representaion
    Args:
        myobj: object to examine

    Return:
        str: JSON Representation
    """

    return json.dumps(my_obj)
