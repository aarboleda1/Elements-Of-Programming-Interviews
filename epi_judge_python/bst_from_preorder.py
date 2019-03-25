from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence):
    root_idx = [0]

    def rebuild_bst_from_preorder_on_value_range(lo, hi):
        if root_idx[0] == len(preorder_sequence):
            return None

        val = preorder_sequence[root_idx[0]]
        # keeps the variant of a BST tree that parent is greater than left
        # and less than right child
        if not lo <= val <= hi:
            return None

        root_idx[0] += 1
        root = BstNode(val)
        root.left = rebuild_bst_from_preorder_on_value_range(lo, val)
        root.right = rebuild_bst_from_preorder_on_value_range(val, hi)
        return root

    return rebuild_bst_from_preorder_on_value_range(float("-inf"), float("inf"))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
