#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
