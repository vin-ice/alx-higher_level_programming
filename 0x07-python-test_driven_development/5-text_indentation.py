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

    seps = [": ", "? ", ". "]
    reps = [":\n\n", "?\n\n", ".\n\n"]

    for index, sep in enumerate(seps):
        text = text.replace(sep, reps[index]).strip()
    print("{}".format(text))