import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))
"""12.7 pg 183

Write a program that takes 2 arrays of strings, and returns the indices of the
starting and ending index of the shortest subarray of the first array (the
"paragraph" array) that "sequentially covers", i.e., contains all the strings
in the second array (the "keywords" array), in the order in which they appear in
the keywords array. You can assume all keywords are distinct.

For example, let the paragraph array be [apple, banana, cat, apple] and the
keywords array be [banana, apple]. The paragraph subarray starting at index 0
and ending at index 1 does not fulfill the specification, even though it contains
all the keywords, since they don't appear in the specified order. On the other
hand, the subarray starting at index 1 and ending at index 3 does fulfill the
specification.

BASIC IDEA: The brute force approach is to iterate thru all subarrays of the
paragraph array. To check whether a subarray of a paragraph array sequentially
covers the keyword array, search the first occurence of the 1st keyword. Next
search 1st occur of the second keyword. No earlier occurrence o the second keyword
is relevant, since those keywords don't satisy the correct ordering of the keyword
array. This leads to an O(N) time algorithm for testing whether a subarray
fulfills the specification, where n is the length of the paragraph array. Since
there are O(N ^ 2) subarrays of the paragraph array, this leads to the time complexity
of O(N^2 * N) == O(N^3)

Although the brute force algorithm works, we can use a hash table to map keywords
to their most recent occurrences in the paragraph array as we iterate through
it, and a hash table mapping each keyword to the length of the shortest
subarray ending at the most recent occurrence of that keyword.

[ ATTEMPTED ] -
"""

def find_smallest_sequentially_covering_subset(paragraph, keywords):

    # Maps each keyword to its index in the keywords array.
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}

    # Since keywords are uniquely identified by their indices in keywords
    # array, we can use those indices as keys to lookup in an array.
    latest_occurrence = [-1] * len(keywords)
    # For each keyword (identified by its index in keywords array), the length
    # of the shortest subarray ending at the most recent occurrence of that
    # keyword that sequentially cover all keywords up to that keyword.
    shortest_subarray_length = [float('inf')] * len(keywords)

    shortest_distance = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:  # First keyword.
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = (
                    i - latest_occurrence[keyword_idx - 1])
                #
                shortest_subarray_length[keyword_idx] = (
                    distance_to_previous_keyword +
                    shortest_subarray_length[keyword_idx - 1])
            latest_occurrence[keyword_idx] = i

            # Last keyword, for improved subarray.
            if (keyword_idx == len(keywords) - 1
                    and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)
    return result


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
