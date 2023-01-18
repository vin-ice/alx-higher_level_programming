#!/usr/bin/python3

"""Module for the shape: square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square module
        Args:
            size: length and width
            x: horizontal displacement
            y: vertical displacement
            id: Unique identifier of instance
        """
        super().__init__(id = id, width = size, height = size, x = x, y = y)

    @property
    def size(self):
        """Public getter for the attr width/height"""
        return self.width
    @size.setter
    def size(self, value):
        """Public setter of width/height
        Args:
            value (int): Value of width/height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """upadtes square attributes"""
        if args and len(args) > 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.size = args[idx]
                if idx == 2:
                    self.x = args[idx]
                if idx == 3:
                    self.y = args[idx]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def __str__(self):
        """returns rectangle's desc"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """returns the dictionary representation of a Shape"""

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
