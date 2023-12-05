#!/usr/bin/python3
"""Defines a JSON file-reading function."""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file to be loaded.
    :return: The Python object represented by the JSON file.
    """
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
