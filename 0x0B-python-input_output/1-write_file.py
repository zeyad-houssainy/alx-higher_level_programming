#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """function to write a file"""

    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))
