import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

"""9.10 Compute the successor
Compute the succesor in a tree using in order traversal, assume the node
stores its parent

Brute Force: A inorder walk, stopping immediately at the first node to be visited
after the given node.

A closer look, for an in order traversal there are 2 options for a given node
1. A node does have right subtree.
    - For this case, the next node is the left most node of the right subtree
2. A node has no right subtree, therefore it will be one of the parents pointers
    - If the node is it's parents left child, the parent will be the next node
    we visit: Example, node is 2 in tree below, next node is 3
    - If the node is it's parents right child, then we have already visited
    the parent, traverse up, we stop the traversal when we come from a
    left subtree
     6
   3
 2   1


"""
def find_successor(node):

    if node.right:
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:
            node = node.left
        return node

    # Find the closest ancestor whose left subtree contains node.
    while node.parent and node.parent.right is node:
        node = node.parent

    # A return value of None means node does not have successor, i.e., node is
    # the rightmost node in the tree.
    return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("successor_in_tree.py",
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
