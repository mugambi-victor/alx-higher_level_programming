#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from each tuple
    a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    # Perform addition for each element
    result_tuple = (a1 + b1, a2 + b2)

    return result_tuple
