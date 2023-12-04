#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    MyList class extends the built-in list class with additional functionality.

    Public Methods:
    - print_sorted(): Prints the elements
    of the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.

        Returns:
        None
        """
        print(sorted(self, key=str))
