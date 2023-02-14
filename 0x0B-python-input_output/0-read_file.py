#!/usr/bin/python3
"""Module with file I/O operation"""

def read_file(filename=""):
    """reads text from a file and prints out to stdout
    Args:
        filename (str): Path to file
    """
    with open(filename, encoding="utf-8") as file:
        text = file.read()
        print("{}".format(text), end="\n")
    file.close()