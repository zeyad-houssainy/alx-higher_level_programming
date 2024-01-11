#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
from sys import argv
from json_module import load_from_json_file, save_to_json_file


try:
    json_list = load_from_json_file("add_item.json")
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, "add_item.json")
