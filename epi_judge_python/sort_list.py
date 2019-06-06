from sorted_lists_merge import merge_two_sorted_lists
from test_framework import generic_test
from list_node import ListNode
"""13.11 Implement a fast sorting algorithm for lists

Hint: In what respects are lists superior to arrays?
[ATTEMPTED] 6/5
"""
# def stable_sort_list(L):
#     pass
def stable_sort_list(L):
    dummy_head = ListNode(0, L)
    while L and L.next:
        if L.data > L.next.data:
            target = L.next
            pre = dummy_head
            while pre.next.data < target.data:
                pre = pre.next

            temp = pre.next
            pre.next = target
            L.next = target.next
            target.next = temp
        else:
            L = L.next
    return dummy_head.next
if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_list.py", "sort_list.tsv", stable_sort_list
        )
    )
