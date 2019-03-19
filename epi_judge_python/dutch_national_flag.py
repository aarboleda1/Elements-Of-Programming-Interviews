import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# TC: O(N) SC: O(1)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, mid, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while mid < larger:
        # A[equal] is the incoming unclassified element.
        if A[mid] < pivot:
            A[smaller], A[mid] = A[mid], A[smaller]
            smaller, mid = smaller + 1, mid + 1
        elif A[mid] == pivot:
            mid += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[mid], A[larger] = A[larger], A[mid]
    print(smaller, mid, larger)
    # pivot = A[pivot_index]
    #
    # sm = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[sm] = A[sm], A[i]
    #         sm += 1
    #
    # right = len(A) - 1
    # for j in range(len(A) - 1, -1, -1):
    #     if A[j] > pivot:
    #         A[j], A[right] = A[right], A[j]
    #         right -= 1



@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    A = [9, -1, 2, 0, 9, 2, 2, 2]
    dutch_flag_partition(3, A)
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
