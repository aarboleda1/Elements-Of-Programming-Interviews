from test_framework import generic_test
from list_node import ListNode
"""7.7  Remove kth last element from a list | delete_kth_last_from_list.py
Given a singly linked list and an integer k, write a program to remove the kth last
element from the list. Your algorithm cannot use more than a few words of
storage, regardless of the length of the list. In particular, you cannot assume
that it is possible to record the length of the list

[ SOLVED ] - 5/29
"""
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
