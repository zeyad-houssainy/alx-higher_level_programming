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
    with open(filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        return (json_data)
