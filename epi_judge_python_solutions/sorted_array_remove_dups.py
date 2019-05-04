import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
The brute force solution to this would be to create an auxilary array
everytime we see a new number add it to that array

We don't really need this. Because we know the array is sorted, we know that
A[i - 1] must not equal A[i]. So, by this intuition, we need to look for
numbers that we have not seen yet.

Iterate thru the array. We should also se a write_index which, we know
that if A[write_index - 1] != A[i], then, that write to write_index.

[1,2,3,3,3,4,5], e.g. for A[write_index] = 3, and i = 5, write to write_index
and the array will then be [1,2,3,4,3,4,5]

- 5/3, some out of bounds indices with arrays. Need to retry
"""
# Returns the number of valid entries after deletion.
def delete_duplicates(A):

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

# Another implementation
def delete_duplicates_v2(A):
    if not A:
        return 0

    i, write_index, n = 0, 1, len(A)
    while i < n:
        if A[i] != A[write_index - 1]:
            A [write_index] = A[i]
            write_index += 1
        i += 1
    return write_index

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
