"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""


def findMedianSortedArrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        return findMedianSortedArrays(B, A)

    lo, hi, half_len = 0, m, (m + n + 1) // 2
    while lo <= hi:
        # partition with smaller array and do a binary search
        # use i as a midpoint and perform binary search logic
        # on this partitioned array
        i = (lo + hi) / 2
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            lo = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            hi = i - 1
        else:
            # i is perfect, we now need to calculate
            # the median based on i and j

            # if i == 0, then treat A[i - 1], which will
            # be an out of bound index, to be -infinity
            # do the same for j == 0 and B[j - 1]
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            # if i == m, then treat A[i], which will
            # be an out of bound index, to be infinity
            # do the same for j == n and B[j - 1]
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
