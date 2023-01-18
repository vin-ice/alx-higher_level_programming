#!/usr/bin/python3
"""Module with a class"""

Base = __import__('base').Base

class Rectangle(Base):
    """Template defining shape: rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes values of the instance
        Args:
            width (int): value of attr width
            height (int): value of attr height
            x (int): value of attr x
            y (int): value of attr y
            id (int): value of instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the instance att width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the instance att width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the instance att width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the instance att height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the instance att x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter for the instance att x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the instance att y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter for the instance att y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def display(self):
        """Prints out a schema of the specified shape"""
        print("\n" * self.__y, end="")
        print("\n".join([((" " * self.__x) + ("#" * self.__width)) for row in range(self.__height)]))

    def __str__(self):
        """returns rectangle's desc"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns argument to each att
        Args:
            args: list of varied arguments
            kwargs: list of dictionaries
        """
        if args and len(args) > 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.width = args[idx]
                if idx == 2:
                    self.height = args[idx]
                if idx == 3:
                    self.x = args[idx]
                if idx == 4:
                    self.y = args[idx]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Shape"""

        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}