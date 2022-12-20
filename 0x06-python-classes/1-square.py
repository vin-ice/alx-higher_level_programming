#!/usr/bin/python3
'''
Module of a Square Class
'''


class Square:
    """Defines a square by dimensions
    Attributes:
        size: The size of the square
    """
    
    def __init__(self, size):
        """"Sets instance size att
        Attributes:
            size: size of square
        """
        self.__size = size