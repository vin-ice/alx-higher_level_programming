#!/usr/bin/python3
"""Module with a division operation for a matrix"""

def matrix_divided(matrix, div):
    """Divides elements of a matrix
    Args:
        matrix (list): matrix
        div (int/float): dividor
    
    Returns:
        matrix_p (list): new list
    """

    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(cell, (int, float)) for row in matrix for cell in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[float("{:.2f}".format(cell / div)) for cell in row] for row in matrix]