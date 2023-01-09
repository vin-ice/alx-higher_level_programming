#!/usr/bin/python3
"""Module with a custom base class"""

class BaseGeometry:
    """Base Class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")