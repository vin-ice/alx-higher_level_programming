#!/usr/bin/python3
"""Module for an add operation"""

def add_integer(a, b=98):
    """Adds two integers and return the sum.
    Args:
        a (int/float): First operand
        b (int/float): Second Operand

    Returns:
        a + b (int): sum of operands
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))