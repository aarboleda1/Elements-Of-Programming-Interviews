import collections
import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""9.3 Compute the lowest common ancestor in a binary tree

Design an algorithm for computing the LCA of two nodes in a binary tree in which
nodes do not have a parent field

Basic Algorithm: Traverse thru the tree and search for node0 and node1. Return
to the caller the result of the search and handle the cases
1) When you traverse, the first node you find, if it's equal to n1 or n2. You
can always return that node consider the case:
If we are looking for 3,2, the first encounter with node 3, we can return early
because w
     Tree
       1
   3        5
2
2) You've found both nodes, then current_node is the root
3) You've found 1 of the nodes
4) You've found none of the nodes
[ ATTEMPTED ] 5/31
[ ATTEMPTED ] 6/14

Watch this video if you can't solve it and reason about it properly
https://www.youtube.com/watch?v=py3R23aAPCA
"""

def lca(tree, node0, node1):
    def search(cur_node, node0, node1):
        if cur_node is None:
            return None
        # Found the node we've been looking for, return myself
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
        return cur_node  # Both children nodes have been found, this is the LCA!

    return search(tree, node0, node1)

def lca(tree, node0, node1):

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes +
            (node0, node1).count(tree))
        return Status(num_target_nodes, tree
                      if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
