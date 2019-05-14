from test_framework import generic_test

"""
Write a program that teaks input as a binary tree and checks if the tree satisfies
the BST property
- 5/14 [SOLVED]
"""

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    def is_bst_recur(root, lo, hi):
        if not root:
            return True
        elif root.data < lo or root.data > hi:
            return False
        return (
            is_bst_recur(root.left, lo, root.data) and
            is_bst_recur(root.right, root.data, hi)
        )
    return is_bst_recur(tree, low_range, high_range)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
