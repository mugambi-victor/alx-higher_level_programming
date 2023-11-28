#!/usr/bin/python3
"""The 0-add_integer module."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Default is 98.

    Returns:
    int: The sum of a and b as an integer.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if isinstance(a, bool):
        raise TypeError("a must be an integer or float")
    if isinstance(b, bool):
        raise TypeError("b must be an integer or float")
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    a = round(float(a))
    b = round(float(b))
    return a + b
