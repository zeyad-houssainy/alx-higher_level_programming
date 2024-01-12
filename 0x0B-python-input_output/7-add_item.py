#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
from sys import argv

"""access commandline arguments"""
load_file = __import__("6-load_from_json_file").load_from_json_file
"""create object from JSON file"""
save_file = __import__("5-save_to_json_file.py").save_to_json_file
"""writes an object to text file, using JSON representation"""

try:
    json_list = load_file("add_item.json")
except:
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_file(json_list, "add_item.json")
