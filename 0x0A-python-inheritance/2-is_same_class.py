#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """check if an object is an instance of the main given class

    Args:
        obj: the object to be checked
        a_class (type): the original parent class that we want to compare with
    returns:
        return True if the Obect is instance of a_class
    """
    if obj.__name__ == a_class:
        return True
    return False
