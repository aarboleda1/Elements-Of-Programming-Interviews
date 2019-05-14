from test_framework import generic_test, test_utils

"""
Generate all subsets of size k

Write a program which computes all size k subsets of [1,2, ..., n], where k an
n are program inputs.

For example, if k = 2 and n = 5, then the result is the
following:

[[1,2], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]

- 4/24 [ATTEMPTED]
- 5/8/19 [ATTEMPTED]
- 5/12/19
"""
"""
k will be depth of the recursive tree
idx pointer to
[1] + [2]
[1] + [3]
[1] + [4]

[2] + [3]
[2] + [4]

[3] + [4]
"""
def combinations(n, k):
    all_subsets = []

    def recur(subset, start):
        if len(subset) == k:
            all_subsets.append(subset)
            return

        # while i <= n:
        #     recur(subset + [i], i + 1)
        #     i += 1
        for i in range(start, n + 1):
            recur(subset + [i], i + 1)

    recur([], 1)
    return all_subsets


if __name__ == '__main__':
    combinations(4, 2)
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
