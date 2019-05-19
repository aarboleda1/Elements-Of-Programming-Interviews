import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""A naive approach would be to generate all subsets of size k and then
select one at random from these, the time and space complexity would be
huge and it's not very trivial

The key to building a random subset of size k is to first build a subset of size
k - 1 and then adding 1 more element, select randomly from the rest.

It's pretty simple when k == 1. e.g.

A = [1,2,3,4,5]
Use a random index generator to select an index from 0 - len(A) - 1
random_value = A[random_index]

When k > 1, we begin by choosing one element between A[i]...A[n - 1] and then
storing the random value at A[i] and then repeat the same process with n - 1
element subarray A[1, n - 1]. Eventually the random subset will occupy slots
A[0, k - 1] and the remaining elements will be in n - k slots

EXAMPLE

A = [8, 2, 9, 1, 4]
k = 3
n = len(A)
1st iteration
- Let the random number between 0 and n be 1, swap with A[0], since i == 0
A now equals [1, 2, 9, 8, 4]

2nd iteration
- Let the random number between 1 and n be 8, swap with A[1], since i == 1
A now equals [1, 8, 9, 2, 4]

3rd iteration
- Let the random number between 2 and n be 4, swap with A[2], since i == 2
A now equals [1, 8, 4, 2, 9]

[ ATTEMPTED ] 5/19
"""

def random_sampling(k, A):

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


# Pythonic solution
def random_sampling_pythonic(k, A):
    A[:] = random.sample(A, k)


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))]
             for a in result], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("offline_sampling.py",
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
