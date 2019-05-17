import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import Counter
Subarray = collections.namedtuple('Subarray', ('start', 'end'))

"""
When you type keywords in a search engine, the search engine will return results,
and each result contains a digest of the web page, i.e., highlighting
within that page of keywords that you searched for. For example, a search for the
keywords "Union" and "save" in the text, would return the covering set between
***"save the Union"***

"My paramount object in this strugle is to save the Union, and is not either to
save or to destroy slavery. If I could save the Union without"

Write a program which takes an array of strings and a set of strings, and
returns the indices of the starting and ending index of a shortest subarray of
the given array that "covers" the set, i.e., contains all the strings in the set

[ ATTEMPTED ] 5/14
[ SOLVED ] 5/15
[ ATTEMPTED ]
Input:
    paragraph:["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a"]
                                                        r
    keywords: ["b", "c", "e"]
Output:
left_idx = 0
left_id
{
    b: 2,
    c: 2,
    e: 1
}

"""


def find_smallest_subarray_covering_set(paragraph, keywords):
    word_counts = {}
    left_idx = 0
    res = Subarray(-1, -1)
    num_rem = len(keywords)
    for right_idx, word in enumerate(paragraph):
        if word in keywords:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
            # we've just seen this word
            if word_counts[word] == 1:
                num_rem -= 1
        # covering
        while num_rem == 0:
            if res == (-1, -1) or res[1] - res[0] > right_idx - left_idx:
                res = Subarray(left_idx, right_idx)

            # check to see if we are still coverint all letters in set
            if paragraph[left_idx] in keywords:
                word_counts[paragraph[left_idx]] -= 1
                if word_counts[paragraph[left_idx]] == 0:
                    num_rem += 1
            left_idx += 1
    return res
"""
 {b: 1, c: 1, e: 1}
"""

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    p = ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]
    kw = ["b", "c", "e"]
    res = find_smallest_subarray_covering_set(p, kw)
    print(res)
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
