#!/usr/bin/python3


def pascal_triangle(n):
    """Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle
