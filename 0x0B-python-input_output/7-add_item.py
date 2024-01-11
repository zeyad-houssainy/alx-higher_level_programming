#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
from sys import argv


load_file = __import__("6-load_from_json_file").load_from_json_file
save_file = __import__("5-save_to_json_file.py").save_to_json_file

try:
    json_list = load_file()
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_file(json_list, "add_item.json")
