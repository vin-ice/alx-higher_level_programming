#!/usr/bin/python3
"""Module for a matrix multiplication operation"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices
    
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not all(isinstance(row_a, list) for row_a in m_a):
        raise TypeError("m_a must be a list of lists")
    elif all(len(row_a) < 1 for row_a in m_a):
        raise ValueError("m_a can't be empty")
    elif not all(isinstance(num_a, (int, float)) for num_a in [cell_a for row_a in m_a for cell_a in row_a]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(len(row_a) == len(m_a[0]) for row_a in m_a):
         raise TypeError("each row of m_a must be of the same size")
    
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(row_b, list) for row_b in m_b):
        raise TypeError("m_b must be a list of lists")
    elif all(len(row_b) < 1 for row_b in m_b):
        raise ValueError("m_b can't be empty")
    elif not all(isinstance(num_b, (int, float)) for num_b in [cell_b for row_b in m_b for cell_b in row_b]):
        raise TypeError("m_b should contain only integers or floats")
    elif not all(len(row_b) == len(m_b) for row_b in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_ab = []
    for row_na in range(len(m_a)):
        m_abr = []
        for col_na in range(len(m_a[row_na])):
            cell_ab = 0 
            for cell_na in range(len(m_a[row_na])):
                cell_ab += m_a[row_na][cell_na] * m_b[cell_na][col_na]
            m_abr.append(cell_ab)
        m_ab.append(m_abr)
    return m_ab