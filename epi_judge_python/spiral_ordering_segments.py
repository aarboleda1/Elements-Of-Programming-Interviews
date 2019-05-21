from test_framework import generic_test

"""5.18 Compute the spiral ordering of a 2D array
A 2D array can be written as a sequence in several orders - the most natural
ones being row-by-row or column-by-column. In this problem we explore the
problem of writing the 2D array in spiral order. For example, the spiral ordering
for the 2D, in Example 1 below is [1,2,3,6,9,8,7,4,5] and the spiral ordering
for Example 2 is [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

Example 1:
M = [
 [1,2,3],
 [4,5,6],
 [7,8,9],
]
spiral_ordering = [1,2,3,6,9,8,7,4,5]

Example 2:
[
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16],
]
spiral_ordering = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

HISTORY LOG
[ SOLVED ] 5/21
[ATTEMPTED ] 5/19
"""
def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []
    ret = []
    left, right = 0, len(square_matrix) - 1
    top, bottom = 0, len(square_matrix[0]) - 1
    while left < right and top < bottom:
        # left -> right
        for i in range(left, right):
            val = square_matrix[top][i]
            ret.append(val)
        # top -> bottom
        for i in range(top, bottom):
            val = square_matrix[i][right]
            ret.append(val)

        # right -> left
        for i in range(right, left, -1):
            val = square_matrix[bottom][i]
            ret.append(val)

        # bottom -> top
        for row in range(bottom, top, -1):
            val = square_matrix[row][left]
            ret.append(val)
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    if top == bottom and left == right:
        ret.append(square_matrix[top][left])
    return ret


if __name__ == '__main__':
    M = [
     [1,2,3],
     [4,5,6],
     [7,8,9],
    ]
    spiral_ordering = matrix_in_spiral_order(M)
    print(spiral_ordering)
    assert spiral_ordering == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
