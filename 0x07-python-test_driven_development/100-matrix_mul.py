#!/usr/bin/python3

"""
Module: 6-matrix_mul

Contains a function that  multiplies two matrices.

"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of
        lists, or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty or if
        the matrices can't be multiplied.

    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    # Validate m_a
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
