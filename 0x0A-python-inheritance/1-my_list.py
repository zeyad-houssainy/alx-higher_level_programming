#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """class for this list"""
    
    def print_sorted(self):
        """print sorted output"""
        print(sorted(self))
