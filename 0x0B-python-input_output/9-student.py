#!/usr/bin/python3
"""Student Class Module"""

class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes student
        Args:
            first_name (str): name
            last_name (str): name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        return self.__dict__ 