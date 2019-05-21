import collections
import math

from test_framework import generic_test

"""
5.17 The Sudoku Checker Problem

The objective is to fill a 9 x 9 grid with digits subject to constraint that
each column, row, and each of the 3 x 3 sub-grids that compose the grid contains
unique integers from 1 to 9. The grid is initialized with a partial assignment of
integers

Check whether a 9x9 2D array representing a partially completed Sudoku is valid.
Speicifally, check that no row, column or 3x3 2D subarray contains duplicates.
A 0-value in the 2D array indicates that the entry is blank; every other entry
is from 1 to 9

Basic Idea:
Check the rows, columns and valid grid, use a helper function and for each of
these units, make sure that there are no duplicates.

One clever solution in my solution is that to get all values in a column-wise
fashion in python you can do

matrix = [
    [1,3],
    [2,4]
]
for col in zip(*matrix):
    print(col)

would print
    (1,2)
    (2,4)
"""

def is_valid_unit(alist):
    alist = [val for val in alist if val != 0]
    return len(set(alist)) == len(alist)

def is_valid_rows(matrix):
    for row in matrix:
        if not is_valid_unit(row):
            return False
    return True

def is_valid_columns(matrix):
    for col in zip(*matrix):
        if not is_valid_unit(col):
            return False
    return True

def is_valid_grids(matrix):
    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            unit = [
                matrix[row][col] for row in range(i, i + 3)
                for col in range(j, j + 3)
            ]
            if not is_valid_unit(unit):
                return False
    return True

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    return (
        is_valid_columns(partial_assignment) and
        is_valid_rows(partial_assignment) and
        is_valid_grids(partial_assignment)
    )

"""Given solution, not very intuitive
"""
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):

    # Return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col] contains any
    # duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return
    # False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (
            I + 1)) for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
        collections.Counter(k for i, row in enumerate(partial_assignment)
                            for j, c in enumerate(row) if c != 0
                            for k in ((i, str(c)), (str(c), j),
                                      (i / region_size, j / region_size,
                                       str(c)))).values(),
        default=0) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
