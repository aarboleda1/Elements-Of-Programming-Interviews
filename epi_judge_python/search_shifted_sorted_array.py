from test_framework import generic_test

"""11.3 Search a cyclically sorted array

An array is said to be cyclically sorted if it is possible to cyclically shift
its entries so that it becomes sorted. For example, array below

378, 478, 550, 631, 103, 203, 220, 234, 279, 368

Design an O(log n) algorithm for finding the position of the smallest element
in a cyclically sorted array. Assume all elements are distinct. For example,
for the array above, the algorithm should return 4

378, 478, 550, 631, 103, 203, 220, 234, 279, 368 -> 4

550, 631, 103, 203, 220, 234, 279, 368 -> 2
L          M     R

478, 550, 631, 103, 203 -> 3
                 L    R
                 M
1000, 478, 550, 631, 900, 1001 -> 2
1, 2, 3, 4 -> 0

[3, 1, 2]
L   M  R
- [ATTEMPTED] 6/5
"""
def search_smallest(A):
    pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
