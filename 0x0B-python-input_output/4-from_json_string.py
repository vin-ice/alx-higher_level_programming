#!/usr/bin/python3
"""Module with character encoding exchange function"""
import json

def from_json_string(my_str):
    """returns an object represented by a json string
    Args:
        my_str (str): JSON String 
    """

    return  json.loads(my_str)