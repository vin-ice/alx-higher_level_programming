#!/usr/bin/python3
"""Module file I/O operation"""

def append_write(filename="", text=""):
    """appends text to file
    Args:
        filename (str): pathname
        text (str): text to append
    Return:
        count of characters entered
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        count = file.write(text)
    file.close()
    return count
