#!/usr/bin/python3
"""Module with a text formatter"""


def text_indentation(text):
    """replaces end-line symbols with two breaklines 
    and prints formatted text
     
    Args:
        text (str): Text to format
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    seps = [': ', '? ', '. ', '.', '?', ':']

    for sep in seps:
        text = text.replace(sep, '\n\n').strip()
    print("{}".format(text))