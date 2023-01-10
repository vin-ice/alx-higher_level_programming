#!/usr/bin/python3
"""Module with file I/O operation"""

def write_file(filename="", text=""):
    """writes text to a file
    Args:
        filename (str): path to file to write to
        text (str): text to write
    Return:
        count of characters printed
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        count = file.write(str(text))
    file.close()
    return count
