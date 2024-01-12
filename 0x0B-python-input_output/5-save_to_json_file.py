#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Function that returns the JSON data into Data-structure type
    Args:
        my_str: given data
        filename: file that will write data on,
        will create new file if not exists

    Returns:
        file contain JSON data
    """
    with open(filename, "w", encoding="utf-8") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
        f.close()
