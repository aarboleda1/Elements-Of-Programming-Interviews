from test_framework import generic_test, test_utils

"""The power set of a set S is the set of all subsets of S, including both
the empty set and S itself.

Write a function that takes as input a set and returns its powerset
- 5/7 [HARD]
"""


def generate_power_set(nums):
    res = [[]]
    for num in nums:
        res += [
            item + [num] for item in res
        ]
    return res

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
