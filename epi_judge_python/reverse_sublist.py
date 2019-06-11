from test_framework import generic_test
from list_node import ListNode

"""7.2 Reverse a single sublist

Write a program which takes a singly linked list L and two integers s and f as
arguments, and reverses the order of the nodes from the sth node to the fth node
, inclusive. The numbering begins at 1, i.e. the head node is the first node. Do
allocate additional nodes

Hint: Focus on the successor fields which have to be updated

[ ATTEMPTED ] - 5/29
[ ATTEMPTED ] - 6/11

"""
def reverse_sublist(L, start, finish):
    pass


if __name__ == '__main__':
    L1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    L1 = reverse_sublist(L1, 2, 5)
    print(L1)

    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
