#!/usr/bin/python3
"""Module with a custom inheriting class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Inherits from a subclass"""

    def __init__(self, size):
        """Inititializes size
        Args:
            size (int): sides
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns area of shape"""
        return self.__size ** 2

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle", self.__size, self.__size))