#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file
    (UTF8) and return the number of characters added.

    :param filename: The name of the file to be appended.
    :param text: The string to be appended to the file.
    :return: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
