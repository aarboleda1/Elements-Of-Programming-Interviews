from test_framework import generic_test


"""11.4 Compute the integer square root

Write a program which takes a nonnegative integer and returns the larger integer
whose square root is less than or equal to the given integer. For example,
if the input is 16, return 4; if the input is 300, return 17, since 17^2 =
289 < 300 and 18^2 = 324 > 300

Hint: Look out for corner cases

[ ATTEMPTED ] 6/6
"""


def square_root(k):
    pass


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
