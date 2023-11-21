#!/usr/bin/python3
# 102-sqaure.py
"""Define a class Square."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (number): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (number): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (number): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator."""
        return self.area() >= other.area()
