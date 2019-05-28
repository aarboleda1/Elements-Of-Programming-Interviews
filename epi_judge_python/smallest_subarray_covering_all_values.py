import collections
import functools

from test_framework import generic_test
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


# HISTORY LOG
[ ATTEMPTED ] - 5/19
[ ATTEMPTED ] - 5/17
[ ATTEMPTED ] - 5/15
"""

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    res = Subarray(-1, -1)
    found_words = {keyword: 0 for keyword in keywords}
    keywords_to_find = len(keywords)
    left = 0
    for right in range(len(paragraph)):
        if paragraph[right] in keywords:
            found_words += 1
            keywords_to_find -= 1

        # found all, find a shorter!
        if keywords_to_find == 0:
            if res == (-1, -1) or res[1] - res[0] > right - left:
                res = Subarray(left, right)
            if paragraph[left] not keywords:
                left += 1
            else:
                found_words[paragraph[left]] -= 1

            if found_words[paragraph[left]] == 0:
                keywords_to_find += 1
    return res








    return res







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
    res = find_smallest_sequentially_covering_subset(
        ["apple", "banana", "cat", "apple"],
        ["banana", "apple"]
    )
    start, end = res
    assert start == 1 and end == 3
    print("success!!!")

    start, end = find_smallest_sequentially_covering_subset(["a", "b"], ["a", "b"])
    print(start, end, 'are start and end')

    # exit(
    #     generic_test.generic_test_main(
    #         "smallest_subarray_covering_all_values.py",
    #         'smallest_subarray_covering_all_values.tsv',
    #         find_smallest_sequentially_covering_subset_wrapper))
