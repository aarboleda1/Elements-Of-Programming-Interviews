from test_framework import generic_test


# my solution
# Time complexity: O(m + n)
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


def merge_two_sorted_arrays(A, m, B, n):

    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


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
