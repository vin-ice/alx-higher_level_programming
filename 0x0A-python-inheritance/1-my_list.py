#!/usr/bin/python3
"""Module with custom classes implementing inheritance"""

class MyList(list):
    """Custom class inheriting from list"""

    def print_sorted(self):
        """prints the ordered list"""
        print(sorted(self)) 