from test_framework import generic_test

"""5.17 The Sudoku Checker Problem

The objective is to fill a 9 x 9 grid with digits subject to constraint that
each column , row, and each of the 3 x 3 sub-grids that compose the grid contains
unique integers from 1 to 9. The grid is initialized with a partial assignment of
integers

Check whether a 9x9 2D array representing a partially completed Sudoku is valid.
Speicifally, check that no row, column or 3x3 2D subarray contains duplicates.
A 0-value in the 2D array indicates that the entry is blank; every other entry
is from 1 to 9

[ ATTEMPTED ] - 5/19
"""

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != 0]
        return len(set(unit)) == len(unit)

    one_to_nine = [False] * 10
    # # check rows
    for row in partial_assignment:
        if not is_valid_unit(row):
            return False

    for col in zip(*partial_assignment):
        if not is_valid_unit(col):
            return False

    # find grids
    for row in range(0, 3, 6):
        for col in range(0, 3, 6):
            square = [
                partial_assignment[x][y]
                for x in range(row, row + 3)
                for y in range(col, col + 3)
            ]
            if not is_valid_unit(square):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
