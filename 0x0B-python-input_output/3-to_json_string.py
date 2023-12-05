#!/usr/bin/python3
"""Defines a string-to-JSON function."""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    :param my_obj: The object to be converted to a JSON string.
    :return: The JSON representation of the object as a string.
    """
    import json
    return json.dumps(my_obj)
