#!/usr/bin/python3
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    and return the number of characters written.

    :param filename: The name of the file to be written.
    :param text: The string to be written to the file.
    :return: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
