#!/usr/bin/python3
"""Rectangle class Module"""

class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes variables
        Args:
            width (int/float): Value of width
            height (int/float): value of height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1 
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
        """Returns area of rectangular"""
        return self.__height * self.__width
    
    def perimeter(self):
        """Returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns a schema of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for row in range(self.__height)])

    def __repr__(self):
        """returns string representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """destructor method"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1