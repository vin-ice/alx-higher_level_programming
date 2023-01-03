#!/usr/bin/python3
"""Module with a name printing function"""

def say_my_name(first_name, last_name=""):
    """Prints a pair of strings
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))