import collections

from test_framework import generic_test
# Recursive solution
"""9.1 Test if a Binary Tree is height-balanced

A binary tree is said to be height balanced if for each node in the tree, the difference
in the height of its left and right subtrees is at most one. A perfect binary
tree is height-balanced, as is a complete binary tree. A height-balanced
binary tree doesn't have toe be perfect or complete

Write a program that takes as input the root of a binary tree and checks whether
the tree is height-balanced.

[ ATTEMPTED ] - 5/30 Make sure to read the wording correctly

Basic algorithm for iterative:
Use a stack, for postorder traversal, we want to process left, right then node.

Iteratively, we use the stack to tell us if the top of the stack's right side
has been processed yet or if it even has a right side.

In the case thathe right side has been explored already or there there is no
right side to explore, the current node is one where we can confirm the
difference between left heights and right sides are not greater than 1

If we do, we make sure to store last = node, so that when we find a future
right node, we don't process nodes twice
"""
# Iterative solution
def is_balanced_binary_tree(root):
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            # last == node.right for when we
            # traverse all the way down the right subtree, we'll now need to
            # process the root. think about postorder traversal, left, right,
            # then root
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True

# Simple recursive
def is_balanced_binary_tree(tree):
        def recur(root): # int
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return recur(tree) != -1

def is_balanced_binary_tree(tree):

    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # Base case.

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
