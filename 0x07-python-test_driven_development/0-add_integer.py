#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """return adding the integer a and b
    
    >>> add_integer(1,1)
    2
    >>> print(add_integer(1, 2))
    3
    >>> print(add_integer(100, -2))
    98
    >>> print(add_integer(2))
    100
    >>> print(add_integer(100.3, -2))
    98
    >>> print(add_integer(4, "School"))
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> print(add_integer(None))
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer(float('nan'))
    Traceback (most recent call last):
    >>> add_integer(2, float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer
    >>> add_integer(float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a)+int(b))
