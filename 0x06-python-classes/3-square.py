#!/usr/bin/python3
'''
Module of a Square class
'''


class Square:
    '''A simple class that defines a square
    Attributes:
        size: The size of the square
    '''
    
    def __init__(self, size=0):
        '''Initialization method for the Square class
        Args:
            size(int): The size of the square
        '''
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        '''Finds the area of the Square
        Returns:
            The area of the square
        '''
        return self.__size ** 2