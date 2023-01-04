#!/usr/bin/python3
"""Module with matrix multiplication functionality"""
import numpy as np
 

def lazy_matrix_mul(m_a, m_b):
    """multipleis two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    """
    
    return (np.matmul(m_a, m_b)) 
