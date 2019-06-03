import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


"""9.10 Compute the successor
Compute the succsor in a tree using in order traversal, assume the node
has a parent pointer
[ ATTEMPTED ] 6/2
[ ATTEMPTED ] 5/31
"""


def find_successor(node):
    while node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "successor_in_tree.py", "successor_in_tree.tsv", find_successor_wrapper
        )
    )
