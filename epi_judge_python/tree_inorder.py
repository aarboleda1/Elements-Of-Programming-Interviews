from test_framework import generic_test

# Perform an inorder traversal without recursion
# Time Complexity: O(N), Space Complexity: O(h), where h is the height of the tree
def inorder_traversal(tree):
    res, s = [], []
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            res.append(tree.data)
            tree = tree.right
    return res
"""
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
