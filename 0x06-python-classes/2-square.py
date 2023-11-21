#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
