import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


RED, WHITE, BLUE = range(3)

"""5.1 The Dutch National Flag Problem

Write a program that takes an array A and index i into A, and
rearranges the elements such that all elements less han A[i] appear first,
followed by elements equal to the pivot followed by elements greater than the
pivot.
[ ATTEMPTED ] 6/6/19
[ ATTEMPTED ] 5/2/19
[ ATTEMPTED ] 5/19

[1,3,0,9,10,3] pivot_index = 2
[0,3,1,9,10,3] mid = 3, = 1
[0,9,1,3,10,3] mid = 4, lo = 2
[0,9,10,3,1,3] mid = 5, lo = 3
"""

def dutch_flag_partition(pivot_index, A):
    pass


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
