#!/usr/bin/python3
"""Rectangle class Module"""

class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes variables
        Args:
            width (int/float): Value of width
            height (int/float): value of height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private att width
        Return:
            Value of att width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for the private att width
        Args:
            value (int/float): Value for att width
        """ 
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private att height
        Return:
            Value of att height
        """

        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for the private att height
        Args:
            value (int/float): Value for att height
        """ 
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value