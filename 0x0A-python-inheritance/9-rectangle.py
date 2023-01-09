#!/usr/bin/python3
"""Module with a custom base class"""

BaseGeometry = __import__('8-rectangle').BaseGeometry

class Rectangle(BaseGeometry):
    """Inherits from Base Geometry"""
    def __init__(self, width, height):
        """Instantiates with width and height value
        Args:
            width (int): size of wideness
            height (int): measure of length
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Returns area"""
        return self.__height * self.__width

    def __str__(self):
        """returns string rep of the Rectangle"""

        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
