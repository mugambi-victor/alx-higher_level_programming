#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains a function to print the input text
with 2 new lines after each '.', '?', and ':' characters.

"""


def text_indentation(text):
    """
    Print the input text with 2 new lines
    after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters to check for indentation
    indentation_chars = ['.', '?', ':']
    current_line = ""

    # Iterate through each character in the input text
    for char in text:
        # Check if the current character is one of the indentation characters
        if char in indentation_chars:
            # Print the current line without leading or trailing spaces
            print(current_line.strip())
            # Reset the current line to an empty string
            current_line = ""
            # Print new line after encountering the symbol
            print("\n", end="")
        else:
            # Otherwise, add the character to the current line
            current_line += char

    # Print the last line if there is any remaining text
    if current_line:
        print(current_line.strip())
    print("\n\n", end="")
