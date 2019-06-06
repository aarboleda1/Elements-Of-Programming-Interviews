from test_framework import generic_test
"""11.3 Search a cyclically sorted array

An array is said to be cyclically sorted if it is possible to cyclically shift
its entries so that it becomes sorted. For example, array below

378, 478, 550, 631, 103, 203, 220, 234, 279, 368

Design an O(log n) algorithm for finding the position of the smallest element
in a cyclically sorted array. Assume all elements are distinct. For example,
for the array above, the algorithm should return 4

[ATTEMPTED] 6/5

Basic Idea:
The brute force approach is to iterate thru the array, comparing the running
minimum with the current entry. Time complexity is O(n)

This approach does not take advantage of the properties of the array.

1) For example, for any m if A[m] > A[n - 1] where n is the len(A), then
the minimum value must be an index in the range from m + 1 to n - 1.
2) Conversely, if A[m] < A[n - 1], then no index in the range from m+1 to n-1
can be the index of the minimum value. These two observations lead us to
the binary search algorithm

e.g.

[5,3,1,2]
if m equals 0, A[0] > A[n], therefore the min must be from 0..n

"""
def search_smallest(A):

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid
    # Loop ends when left == right.
    return left

# Wrong
def search_smallest(A):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = left + (right - left)) // 2
        if mid > 0 and A[mid] < A[mid - 1]:
            return mid
        elif A[mid] > A[left]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
