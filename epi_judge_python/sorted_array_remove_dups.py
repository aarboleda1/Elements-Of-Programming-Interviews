import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
"""
6.6
Delete Duplicates from a Sorted Array
e.g. A = [2,3,5,5,5,6,6,7]
After deletion, the array is [2,3,5,6,7,5,6,7]

Write a program which takes a sorted array as input and updates it so that all
duplicates have been removed and the remaining elements have been shifted left
to fill the emptied indices. Return the number of valid elements after deletion
"""
def delete_duplicates(A):
    pass


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
