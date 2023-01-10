#!/usr/bin/python3
"""Module with Json to object conversion functionality"""
import json

def load_from_json_file(filename):
    """creates an object from a JSON file
    Args:
        filename (str): path to file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        json_value = file.read()
    file.close()
    return json.loads(json_value)