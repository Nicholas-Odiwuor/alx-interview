#!/usr/bin/python3
"""
Rotates a 2D matrix 90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

