import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from bst_node import BstNode
from test_framework.test_utils import enable_executor_hook

"""
Build a min height BST from a sorted array
5/14 - [SOLVED]
"""


def build_min_height_bst_from_sorted_array(A):
    def bst_builder(start, end):
        if start >= end:
            return None
        else:
            mid = (start + end) // 2
            root = BstNode(A[mid])
            root.left = bst_builder(start, mid)
            root.right = bst_builder(mid + 1, end)
        return root

    return bst_builder(0, len(A))


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
