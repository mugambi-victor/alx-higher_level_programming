#!/usr/bin/python3
"""
Module: 3-say_my_name

Contains a function to print a formatted
string with the given first and last names.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or"
                        "last_name must be a string")

    full_name = first_name + " " + last_name if last_name else first_name
    print("My name is {}".format(full_name))
