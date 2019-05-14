from test_framework import generic_test, test_utils

"""
Similar approach to the the power_set. The key here is to notice that
there are 2 possibilities when generating a given subset.

1. The subset does not contain 1
2. The subset does contain 1

For the first case, we genreate and return all subsets of size k of [2,3,...n].
For the second case, we compute all k - 1 sized subsets of [2,3,...n] and then
add 1 to each subset

History Log:
- 5/8, [ATTEMPTED] Didn't get. Still needs more work on the case analysis
- 5/13 [ATTEMPTED] I'd say i mostly solved, but had an off by one error, that I
didn't catch until i ran and looked thru it in the tests
"""
def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return

        # Generate remaining combinations over {offset, ..., n - 1} of size
        # num_remaining.
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return result


def combinations_pythonic(n, k):
    result = [[]]
    for _ in range(k):
        result = [[i] + c for c in result
                  for i in range(1, c[0] if c else n + 1)]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
