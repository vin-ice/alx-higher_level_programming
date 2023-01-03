#!/usr/bin/python3
'''
Module of a Square class
'''

class Square:
    """Defines a square by dimensions
    Attributes:
        size: size of square
    """
    
    def __init__(self, size=0):
        """"Sets instance size att
        Args:
            size: size of square
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")