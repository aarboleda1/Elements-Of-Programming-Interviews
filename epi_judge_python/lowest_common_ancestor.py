import collections
import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""9.3 Compute the lowest common ancestor in a binary tree

Design an algorithm for computing the LCA of two nodes in a binary tree in which
nodes do not have a parent field
[ ATTEMPTED ] 5/31
[ ATTEMPTED ] 5/31


1) Am I one of the nodes
2) Of the left and right, have I found one of the nodes?

If I am one of the nodes, always return myself
1) I am a node, return myself, whetehr I cover or not
2) left or right cases
3) left and right cases but I'm not a node
ans = C
  C
B


left = B
right = None

ans = A
     Z
   A
 B   C


ans = D

     D
   A   C
 B

    G
  F   B
        C

"""

result_tuple = collections.namedtuple("ResultTuple", ("num_nodes", "node"))


def lca(tree, node0, node1):
    pass


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
