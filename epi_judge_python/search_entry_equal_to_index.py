import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""11.2 Search a sorted array for entry equal to its index

Design an efficient algorithm that takes a sorted array of distinct integers,
and returns an index i, such that the element at index i equals i. For example,
when the input is [-2,0,2,3,6,7,9] your algorithm should return 2 or 3

[ ] 6/5

[-2,0,2,3,6,7,9] -> 7
res = 3
left = 2, right = 2
mid = 1
[0,2,3,6,7,9] -> 0
[-1,-2,-3,3] -> 3

[ATTEMPTED] 6/5, no need to code this out fully, make sure to remember Order
of operations!!!!
"""
def search_entry_equal_to_its_index(A):
    pass


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(
        functools.partial(search_entry_equal_to_its_index, A))
    if result != -1:
        if A[result] != result:
            raise TestFailure("Entry does not equal to its index")
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure("There are entries which equal to its index")


if __name__ == '__main__':
    res = search_entry_equal_to_its_index([-2,0,2,3,6,7,9])
    print(res)
    # exit(
        # generic_test.generic_test_main(
            # "search_entry_equal_to_index.py",
            # 'search_entry_equal_to_index.tsv',
            # search_entry_equal_to_its_index_wrapper))
