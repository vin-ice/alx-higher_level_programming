#!/usr/bin/python3
"""Module with object inspection functionality"""

def lookup(obj):
    """Returns a list of available attributes 
    and methods of an object
    Args:
        obj (obj): Instance of a class
    """

    return dir(obj)