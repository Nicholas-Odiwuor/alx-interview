#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of height n.
    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        # build the new row: start & end with 1, middle elements are sums of neighbors
        row = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
        triangle.append(row)

    return triangle

