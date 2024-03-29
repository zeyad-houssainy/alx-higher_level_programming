#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """checks if object is instance or inherited from a base class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if object is instance or inherited from a base class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
