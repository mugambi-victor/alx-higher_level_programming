#!/usr/bin/python3
"""Defines a JSON-to-object function."""


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    :param my_str: The JSON string to be converted to a Python object.
    :return: The Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
