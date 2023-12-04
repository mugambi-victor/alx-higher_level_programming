#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
