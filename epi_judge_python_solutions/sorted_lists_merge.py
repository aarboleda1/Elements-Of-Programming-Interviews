from list_node import ListNode
from test_framework import generic_test

"""7.1 Merge two sorted lists

Basic Algorithm: Choose lesser of the two nodes and append them
to pointers. It's a good test of pointers and looping through a
linked list

- [ ATTEMPTED ] 5/29
"""
def merge_two_sorted_lists(L1, L2):

    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    retusrn dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
