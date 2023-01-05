#!/usr/bin/python3
"""Module with a function for printing square"""

def print_square(size):
    """Prints square of given size

    Args:
        size (int): Size of square
    """
   
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for row in range(int(size)):
        for cell in range(int(size)):
            print("#", end="")
        print()