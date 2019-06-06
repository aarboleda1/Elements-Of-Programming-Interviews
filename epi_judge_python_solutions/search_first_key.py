import bisect

from test_framework import generic_test
"""
Basic algorithm: My first approach was to do a binary search and once
the first index where A[i] == k, iterate backwards to find the
first occurrence of that element. Binary search takes (log n), but traversing
backwards takes O(n)

Key Idea: In a binary search, the fundamental idea is to maintain a set of
candidate results. For the problem below, if we see an element at index i
which is equal to k, we don't know if it is the first element equal to k, but
we do know it no subsequent elements can be the first one. Therefore, we consider
all elements with index i - 1 or less from the candidates

[ ATTEMPTED ] - 6/5, Solved, but didn't get optimal time complexity
"""
def search_first_of_k(A, k):
    L, R, res = 0, len(A) - 1, -1
    while L <= R:
        mid = L + (R - L) // 2
        if A[mid] < k:
            L = mid + 1
        elif A[mid] == k:
            # In the worst case, this is O(N)
            while mid > -1 and A[mid] == k:
                mid -= 1
            return mid + 1
        else:
            R = mid - 1
    return res

def search_first_of_k(A, k):

    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
