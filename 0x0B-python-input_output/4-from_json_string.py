#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Function that returns the JSON data into Data-structure type
    Args:
        my_str: given data

    Returns:
        Data structure type
    """

    return json.loads(my_str)
