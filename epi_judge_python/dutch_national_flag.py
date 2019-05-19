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

[ ATTEMPTED ] 5/2/19
[ ATTEMPTED ] 5/19
"""

def dutch_flag_partition(pivot_index, A):
    # TODO
    return A


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
