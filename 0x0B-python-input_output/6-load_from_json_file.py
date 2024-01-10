#!/usr/bin/python3
"""Turn Json data to the code"""
import json


def load_from_json_file(filename):
    """Function that returns the JSON data into Data-structure type
    Args:
        filename: file with json data

    Returns:
        JSON data
    """
    with open(filename, "r", encoding="utf-8"):
        json_data = json.load(filename)
        return (json_data)
