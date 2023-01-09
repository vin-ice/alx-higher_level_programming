#!/usr/bin/python3
"""Module with a custom base class"""

class BaseGeometry:
    """Base Class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates input
        Args:
            name (str): name of input
            value (int): integer value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))