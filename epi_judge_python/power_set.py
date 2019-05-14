from test_framework import generic_test, test_utils

"""The power set of a set S is the set of all subsets of S, including both
the empty set and S itself.

Write a function that takes as input a set and returns its powerset

input: [0, 1, 2]
output: [[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]]

- 5/7 [ATTEMPTED]
- 5/13 [SOLVED] to review notes!
"""


def generate_power_set(nums):
    pass

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
