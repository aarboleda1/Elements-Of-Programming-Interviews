from test_framework import generic_test


"""13.2 Merge two sorted arrays
Suppose you are given two sorted arrays of integers. If one has enough empty
entries at its end, it can be used to store the combined entries of two arrays in
sorted order. For example, consider [3,13,17, , , , ] and [3,7,11,19]. Then
the combined entries can be stored in the first array as [3,3,7,11,13,17,19]

Write a program which takes as input two sorted arrays of integers, and
updates the first to the combined entries of the two arrays in sorted order.
Assume the first array has enough empty entries at its end to hold the result

[ SOLVED ] 6/3
"""


def merge_two_sorted_arrays(A, m, B, n):
    write_index = len(A) - 1
    a, b = m - 1, n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1
        write_index -= 1
    while a >= 0:
        A[write_index] = A[a]
        write_index -= 1
        a -= 1
    while b >= 0:
        A[write_index] = B[b]
        write_index -= 1
        b -= 1
    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
