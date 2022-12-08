#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, col in enumerate(row):
            s = ' '
            if index == len(row) - 1:
                s = ''
            print("{:d}".format(col, s), end=s)
        print("")
