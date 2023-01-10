#!/usr/bin/python3
"""Module with dictionary descriptor"""

def class_to_json(obj):
    """retruns dict description with simple data struct
    Args:
        obj (object): Instance of a class
    """
    return obj.__dict__