from test_framework import generic_test
from list_node import ListNode

def reverse_sublist(L, start, finish):
    dummy_head = cur = ListNode(0, L)
    count = 0
    while count < start:
        cur = cur.next
        count += 1

    count = 0
    cur = cur.next
    prev = cur
    while count < (finish - start):
        tmp = cur.next
        cur.next = tmp.next
        prev = cur
        cur = tmp
        count += 1
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
