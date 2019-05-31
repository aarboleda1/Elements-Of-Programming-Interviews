from test_framework import generic_test

"""9.1 Test if a Binary Tree is height-balanced

A binary tree is said to be height balanced if for each node in the tree, the difference
in the height of its left and right subtrees is at most one. A perfect binary
tree is height-balanced, as is a complete binary tree. A height-balanced
binary tree doesn't have toe be perfect or complete

Write a program that takes as input the root of a binary tree and checks whether
the tree is height-balanced.

[ ATTEMPTED ] - 5/30 Make sure to read the wording correctly. Recursive solution
is pretty trivial, see if you can do an iterative solution!
"""
def is_balanced_binary_tree(root):
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
