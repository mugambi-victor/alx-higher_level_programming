#!/usr/bin/python3
def no_c(my_string):
    chars = list(my_string)
    i = 0
    while i < len(chars):
        if chars[i] == 'c' or chars[i] == 'C':
            del chars[i]
        else:
            i += 1
    return ''.join(chars)
