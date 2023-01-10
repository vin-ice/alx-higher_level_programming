#!/usr/bin/python3
"""Module with a function for serialized data to a text file"""

import json

def save_to_json_file(my_obj, filename):
    """Writes serailized data to a text file
    Args:
        my_obj: python object to serialized
        filename (str): path of file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)
    file.close()