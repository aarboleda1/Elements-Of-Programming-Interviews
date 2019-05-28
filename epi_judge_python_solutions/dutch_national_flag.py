import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

"""
3 basic strategies:
1) create 3 separate arrays
    lo []
    med []
    hi []
    Append to list and concat them
2) forwards scan then a backwards scan
    if less than, move to front,
3) While loop to meet condition
- Attempted 5/3/19: Still needs work, understand the variant in the comment
    Score: 6/10
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
        this middle group should show you the condition
        while equal <
    # unclassified group: A[equal:larger].
    # top group: A[larger:].


"""
# O(N) time with O(1) space
# Make 2 passes,
# 1) Move all elements < pivot_value to the beginning in the first pass
# 2) Move all elements > pivot_value to end of the array
def dutch_flag_partition(pivot_index, A):
    pivot_val = A[pivot_index]
    write_idx = 0
    # Write all elements less than pivot_value to front
    for i in range(len(A)):
        if A[i] < pivot_val:
            A[i], A[write_idx] = A[write_idx], A[i]
            write_idx += 1
    # Write all elements greater than pivot_value to end
    write_idx = len(A) - 1
    for i in range(len(A) - 1, -1, -1):
        if A[i] >= pivot_val:
            A[i], A[write_idx] = A[write_idx], A[i]
            write_idx -= 1
    return A


def dutch_flag_partition(pivot_index, A):

    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


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
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
