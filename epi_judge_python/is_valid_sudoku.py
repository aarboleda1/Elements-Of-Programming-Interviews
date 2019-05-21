from test_framework import generic_test

"""5.17 The Sudoku Checker Problem

The objective is to fill a 9 x 9 grid with digits subject to constraint that
each column, row, and each of the 3 x 3 sub-grids that compose the grid contains
unique integers from 1 to 9. The grid is initialized with a partial assignment of
integers

Check whether a 9x9 2D array representing a partially completed Sudoku is valid.
Speicifally, check that no row, column or 3x3 2D subarray contains duplicates.
A 0-value in the 2D array indicates that the entry is blank; every other entry
is from 1 to 9
matrix = [
    [1,2,0,0,3,0,0,0,8],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [2,0,0,4,0,9,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
result: True
 [
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 9, 0, 0, 0, 0, 0],
 [0, 3, 2, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [9, 0, 4, 5, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 7, 0, 0, 6],
 [0, 0, 0, 6, 0, 5, 2, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 3, 0],
 [0, 0, 0, 0, 6, 2, 0, 0, 0]
]

[ SOLVED ] 5/21
[ ATTEMPTED ] - 5/19
"""
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    pass

if __name__ == '__main__':
    matrix = [
        [1,2,0,0,3,0,0,0,8],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,4,0,9,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    bad_matrix_row = [
        [1,2,0,0,3,0,8,0,8],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,4,0,9,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    bad_matrix_col = [
        [1,2,0,0,3,0,0,0,8],
        [0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,4,0,9,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    bad_matrix_grid = [
        [1,2,0,0,3,0,0,0,8],
        [0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,4,0,9,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    bad_matrix_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 8, 0, 9, 0, 0, 5, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 5, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 6, 0, 3, 0]
    ]
    assert is_valid_sudoku(matrix) is True
    assert is_valid_sudoku(bad_matrix_row) is False
    assert is_valid_sudoku(bad_matrix_col) is False
    assert is_valid_sudoku(bad_matrix_grid) is False
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
