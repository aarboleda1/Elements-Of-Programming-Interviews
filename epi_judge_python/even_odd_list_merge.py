from test_framework import generic_test
from list_node import ListNode
"""7.10 Implement Even-Odd Merge
Consider a singly linked list whose nodes are numbered starting at 0. Define
the even-odd merge of the list to be the list consisting of the even-numbered
nodes followed by the odd-numbered nodes. The even-odd merge is illustrated

Write a program that computes the even-odd merge

[ SOLVED ] 5/30 read gotchas
"""
def even_odd_merge(L):
    pass

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
