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
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance())
    size, matrix_p = 0, []
    for row in matrix:
        if not isinstance(row, list) or all(not isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if size: 
            if size != len(row): 
                raise TypeError("Each row of the matrix must have the same size")
        else:
            size = len(row)
       
        matrix_pp = []
        for cell in row:
            matrix_pp.append(round(cell / div, 2))
        matrix_p.append(matrix_pp)
    return matrix_p
