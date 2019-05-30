from list_node import ListNode
from test_framework import generic_test

"""7.7  Remove kth last element from a list | delete_kth_last_from_list.py
Given a singly linked list and an integer k, write a program to remove the kth last
element from the list. Your algorithm cannot use more than a few words of
storage, regardless of the length of the list. In particular, you cannot assume
that it is possible to record the length of the list

Basic Algorithm:
Use 2 iterators to traverse the list. Advance the first iterator by k steps,
and then the two iterators can advance in tandem. When the 1st iterator
reaches the tail, the 2nd iterator is at the (k + 1)th last node, and then
simply remove the kth node
[ SOLVED ] - 5/29
"""
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):

    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
