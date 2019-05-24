from test_framework import generic_test, test_utils

"""The power set of a set S is the set of all subsets of S, including both
the empty set and S itself.

Write a function that takes as input a set and returns its powerset

input: [0, 1, 2]
output: [[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]]
- 5/21 [ SOLVED ]
- 5/13 [SOLVED] to review notes!
- 5/7 [ATTEMPTED]
"""


def generate_power_set(nums):
    powerset = []
    def recur(subset, i):
        if i == len(nums):
            powerset.append(subset)
        else:
            recur(subset, i + 1)
            recur(subset + [nums[i]], i + 1)
    recur([], 0)
    return powerset

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
