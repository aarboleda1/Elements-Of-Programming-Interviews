import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.

# Let's take advantage of a BST property. That every left child is less than it's
# parent, and every right child is greater than it's parent. If you draw it out, you'll
# notice that at each node there will be 4 possibilites
# 1) If the roots key is the same at s or b, root is the LCA
# 2) If the key at s is smaller than the key at the root and the key at b
# is greater than the root, then root is LCA
# 3) If root.data < s.data, then the LCA is somehere in the right subtree
# 4) If root.data > b.data, then LCA is somewhere in the left subtree

#
def find_LCA(root, s, b):
    # If root == s.data or b.data, then don't even search
    while root.data < s.data or root.data > b.data:
        # If root.data < s.data, then the LCA is somehere in the right subtree
        while root.data < s.data:
            root = root.right
        # If root.data > b.data, then LCA is somewhere in the left subtree
        while root.data > b.data:
            root = root.left
    # Now, the s.data <= root.data <= b.data
    return root


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_LCA, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_in_bst.py",
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
