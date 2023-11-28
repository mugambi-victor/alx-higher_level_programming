#!/usr/bin/python3
import numpy as np

"""
Module: 101-lazy_matrix_mul

Contains a function  that multiplies two matrices using NumPy..

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (numpy.ndarray): The first matrix.
    - m_b (numpy.ndarray): The second matrix.

    Returns:
    numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(m_a, m_b)

