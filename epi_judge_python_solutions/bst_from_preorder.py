from bst_node import BstNode
from test_framework import generic_test
from collections import deque
"""
History Log
- 5/14 [SOLVED]: Very similar to the way you serialize a Binary Tree
in the serialize/deserialize problem
"""
def rebuild_bst_from_preorder(preorder_sequence):

    if not preorder_sequence:
        return None

    transition_point = next((i for i, a in enumerate(preorder_sequence)
                             if a > preorder_sequence[0]),
                            len(preorder_sequence))
    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:]))

# My Solution O(N) as we will touch each node once, and the amount of word in
# each node is constant
def rebuild_bst_from_preorder_my_version(preorder_sequence):
    if not preorder_sequence:
        return None
    preorder_sequence = deque(preorder_sequence)

    def rebuild_bst_helper(lo, hi):
        if not preorder_sequence:
            return None

        data = preorder_sequence[0]
        # satisfy bst property
        if data > hi or data < lo:
            return None

        root = BstNode(data)
        preorder_sequence.popleft()
        root.left = rebuild_bst_helper(lo, data)
        root.right = rebuild_bst_helper(data, hi)
        return root
    return rebuild_bst_helper(float("-inf"), float("inf"))
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
