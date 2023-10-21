#!/usr/bin/python3
"""
0-main
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascals triangle of n.

    Args:
        n: The number of rows in the Pascals triangle.

    Returns:
        An empty list if n <= 0, otherwise a list of lists of 
        integers representing the Pascals triangle of n.
    """

    if n <= 0:
        return []

    # Initialize the Pascals triangle.
    pascal_triangle = [[1]]

    # Iterate over the rows starting from the second row.
    for i in range(1, n):
        # Initialize the current row.
        current_row = []

        # Add the first element of the current row, which is always 1.
        current_row.append(1)

        # Calculate the remaining elements of the current row.
        for j in range(1, i):
            current_row.append(
                pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            )

        # Add the last element of the current row, which is always 1.
        current_row.append(1)

        # Add the current row to the Pascals triangle.
        pascal_triangle.append(current_row)

    return pascal_triangle
