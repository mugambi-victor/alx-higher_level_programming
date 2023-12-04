#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Args:
    - obj: Object to be checked.
    - a_class: Class to check against.

    Returns:
    - True if obj is an instance of a class that inherited from a_class,
      False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
