#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if 0 <= idx < len(my_list):
        my_list[idx] = new_element
    return my_list
