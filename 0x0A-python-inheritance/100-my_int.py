#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    MyInt class inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverted == operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted != operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
