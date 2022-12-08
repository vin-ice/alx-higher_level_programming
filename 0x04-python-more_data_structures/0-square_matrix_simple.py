#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[row[cell] ** 2 for cell in range(3)] for row in matrix]
    return squares