import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


RED, WHITE, BLUE = range(3)

"""
5/2/19
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
