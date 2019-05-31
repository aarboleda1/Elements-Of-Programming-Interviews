from collections import deque

from test_framework import generic_test


"""9.1 Test if a binary tree is symmetric
[ ATTEMPTED ]
"""


def is_symmetric(tree):

    return check_symmetric(tree, tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
