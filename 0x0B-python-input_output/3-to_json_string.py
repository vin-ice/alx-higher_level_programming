#!/usr/bin/python3
"""Module with character format manipulation function"""
import json

def to_json_string(my_obj):
    """returns JSON representation of an object
    Args:
        my_obj (obj): Object
    """
    return json.dumps(my_obj)