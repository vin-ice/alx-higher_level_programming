#!/usr/bin/python3
"""Module to check object subscription"""

def inherits_from(obj, a_class):
    """Checks if object belongs to a class or a subclass
    Args:
        obj (object): instance
        a_class: suspected class or superclass
    """
    
    return issubclass(type(obj), a_class) and not type(obj) is a_class
