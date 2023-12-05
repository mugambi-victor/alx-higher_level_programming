#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    :param filename: The name of the file to be read.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
