from sorted_lists_merge import merge_two_sorted_lists
from test_framework import generic_test


def stable_sort_list(L):
    # base case: L is empty or single node
    if not L or not L.next:
        return L

    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None
    left = stable_sort_list(L)
    right = stable_sort_list(slow)
    return merge_two_sorted_lists(left, right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_list.py", "sort_list.tsv", stable_sort_list
        )
    )
