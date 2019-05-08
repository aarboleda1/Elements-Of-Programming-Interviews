from test_framework import generic_test, test_utils

"""
- 5/8/19
"""
def combinations(n, k):
    all_subsets = []
    def recur(subset, offset):
        if len(subset) == k:
            all_subsets.append(subset)
            return
        num_rem = k - len(subset)
        i = offset
        while i <= n and num_rem <= n - i + 1:
            recur(subset + [i], i + 1)
            i += 1
    recur([], 1)
    return all_subsets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
