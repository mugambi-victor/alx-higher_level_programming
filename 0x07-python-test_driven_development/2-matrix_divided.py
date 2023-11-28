#!/usr/bin/python3

"""
Module: 2-matrix_divided

Contains a function to divide all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a specified divisor.

    Args:
    matrix (list): A list of lists containing integers or floats.
    Each inner list represents a row of the matrix.
    div (int or float): The divisor to divide all elements of the matrix.
    Returns:
    list: A new matrix with all elements divided by
    the specified divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or
    floats, or if each row of the matrix does not have the
    same size, or if the divisor is not a number.
    ZeroDivisionError: If the divisor is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix
