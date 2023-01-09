#!/usr/bin/python3
"""Module with a custom base class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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

