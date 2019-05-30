from list_node import ListNode
from test_framework import generic_test

"""7.2 Reverse a single sublist

Write a program which taeks a singly linked list L and two integers s and f as
arguments, and reverses the order of the nodes from the sth node to the fth node
, inclusive. The numbering begins at 1, i.e. the head node is the first node. Do
allocate additional nodes

Hint: Focus on the successor fields which have to be updated
Basic Algorithm: First, we start by identifying the sth node using iteration.
Once we reach the sth node, we start the reversing process and keep counting
finish - start number of times. Once we reach the f'th node, stop the reversion
process and link the reverted section with the unreverted sections
[ ATTEMPTED ] - 5/29
"""
def reverse_sublist(L, start, finish):

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
