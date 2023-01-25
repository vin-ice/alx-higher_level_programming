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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be an integer")
        self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be an integer")
        self.__height = height

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
    
    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)