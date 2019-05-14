from bst_node import BstNode
from test_framework import generic_test
from collections import deque
"""
Rebuild a BST from pre-order sequence
[3, 2, 1, 5, 4, 6]


[3, 2, 1, 5, 4, 6]

        3  [2, 1, 5, 4, 6]
    2       5 [1, 5, 4, 6]
  1  None  4      [4, 6]
 None

      3
    2
  1

5/14 - [SOLVED]
"""
def rebuild_bst_from_preorder(preorder_sequence):
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




if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
