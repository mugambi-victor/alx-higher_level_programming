#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    LockedClass: A class that restricts the
    creation of new instance attributes,
    except for 'first_name'.

    Attributes:
    - first_name (str): The first name
    attribute allowed for dynamic creation.
    """

    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """
        Set the value of an attribute.

        Args:
        - name (str): The name of the attribute.
        - value: The value to be assigned.

        Raises:
        - AttributeError: If the attribute name is not 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
