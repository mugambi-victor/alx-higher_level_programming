#!/usr/bin/python3
# 1-square.py
"""Define a class Square."""
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
