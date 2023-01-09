#!/usr/bin/python3
"""Module with functionality that
 determines class subscription of an object"""

def is_kind_of_class(obj, a_class):
    """Determines whether an 
    object is an instance of a class or a subclass
    Args:
        obj (object): instance
        a_class: Class of said instance
    Return:
        True if it belongs to either else False 
    """

    return isinstance(obj, a_class)