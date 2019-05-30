from list_node import ListNode
from test_framework import generic_test

"""7.10 Implement Even-Odd Merge
Consider a singly linked list whose nodes are numbered starting at 0. Define
the even-odd merge of the list to be the list consisting of the even-numbered
nodes followed by the odd-numbered nodes. The even-odd merge is illustrated

Basic algorithm: Iterate thru the list and append even elements to an even
list and od elements to another list. Use an indiciator variable, 0 and 1 or True
and False to tell us which list to append to.Finally, append the odd list
to the even list

**Gotchas: Remember to remove pointers from odd list
"""
def even_odd_merge(L):
    if not L:
        return L
    even_iter = even_head = ListNode(-1)
    odd_iter = odd_head = ListNode(-1)
    cur = L
    turn = 0
    while L:
        if turn == 0:
            even_iter.next = L
            even_iter = even_iter.next
        else:
            odd_iter.next = L
            odd_iter = odd_iter.next
        L = L.next
        turn ^= 1
    # Make sure to detach the tail
    odd_iter.next = None
    even_iter.next = odd_head.next
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
