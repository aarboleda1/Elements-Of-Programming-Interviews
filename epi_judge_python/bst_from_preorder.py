from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence):
    def make(lower_bound, upper_bound):
        if index[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[index[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        index[0] += 1
        L = make(lower_bound, root)
        R = make(root, upper_bound)
        return BstNode(root, L, R)

    index = [0]
    return make(float("-inf"), float("inf"))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
