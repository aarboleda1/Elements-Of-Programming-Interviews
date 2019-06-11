from test_framework import generic_test
from heapq import heapify, heappop, heappush, heappushpop
"""11.8 Find the kth largest element

Design an algorithm for computing the kth largest element in an array

Hint: Use divide and conquer in conjunction with randomization
"""

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
"""
[3, 1, -1, 2]
k = 2
h -2

[-3]
"""
def find_kth_largest(k, A):
    h = []
    for el in A:
        if len(h) < k:
            heappush(h, el)
        else:
            if h[0] < el:
                heappop(h)
                heappush(h, el)
    return h[0]


if __name__ == '__main__':
    A = [3, 1, -1, 2]
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
