#!/usr/bin/python3
"""Defines a JSON file-writing function."""


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    :param my_obj: The object to be written to the file.
    :param filename: The name of the file to be created or overwritten.
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
