#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Load existing items from the file, if it exists
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
