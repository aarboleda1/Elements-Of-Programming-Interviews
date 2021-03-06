import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""9.4 Compute the LCA when nodes have parent pointers

Algorithm using a set: A brute force is to store nodes on the search path from
node0 to root in a hash table or set, since we can traverse up the tree
by using the parent pointer. Then traverse up from 2nd node. If the current node
is inside the hash_table, it is the LCA because it's the first node
we've seen in both paths

Algorithm using depths: We can save space by using the node depths. If we were
traverse up in tandem, the first node where node0 != node1 will be our LCA
1) Get depths of both nodes
2) Find depth difference
3) Traverse up the tree the depth difference to put nodes in the same level
4) Traverse in tandem and find the first node that has both as a parent

- [ATTEMPTED] 6/1
"""
# Solution using node depths
def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth
    depth0 = get_depth(node0)
    depth1 = get_depth(node1)
    # make node0 the deeper node for simplification in the code
    if depth1 > depth0:
        node0, node1 = node1, node0

    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0

# Solution using a hash table
def lca(node0, node1):

    iter0, iter1 = node0, node1
    nodes_on_path_to_root = set()
    while iter0 or iter1:
        # Ascend tree in tandem for these two nodes.
        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent
    raise ValueError('node0 and node1 are not in the same tree')


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
