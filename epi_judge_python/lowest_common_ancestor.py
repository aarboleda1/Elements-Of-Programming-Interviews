import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""9.3 Compute the lowest common ancestor in a binary tree

Design an algorithm for computing the LCA of two nodes in a binary tree in which
nodes do not have a parent field

[ ATTEMPTED ] 5/31
"""


def lca(tree, node0, node1):
    def search(cur_node, node0, node1):
        if cur_node is None:
            return None
        if cur_node == node0 or cur_node == node1:
            return cur_node

        # Perform search, if both searches come back positive,
        # then we are sitting at the LCA
        left = search(cur_node.left, node0, node1)
        right = search(cur_node.right, node0, node1)
        if not right:
            return left
        if not left:
            return right
        return cur_node  # we've found node on both sides

    return search(tree, node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
