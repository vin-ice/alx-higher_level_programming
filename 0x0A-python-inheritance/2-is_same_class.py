#!/usr/bin/python3
"""Module with class subscription assertion"""

def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of a class
    Args:
        obj (object): instance of a class
        a_class: said class
    Return:
        True if exact instance
    """

    return obj.__class__ == a_class
