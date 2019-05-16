from test_framework import generic_test

"""
Given two BST's, it is straightforward to create a BST containing the union of
their keys: traverse one, and insert its keys into the other

Design an algorithm that takes as input two BST's and merges them to form a
balanced BST. For any node, you can update its left and right subtree fields,
but cannot change its key. Your solution can dynamically allocate no more
than a few bytes

[ ] 5/14
"""
def merge_two_bsts(A, B):
    pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_merge.py", 'bst_merge.tsv',
                                       merge_two_bsts))
