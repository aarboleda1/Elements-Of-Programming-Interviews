import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

"""
[ SOLVED ] 5/15
[ find_smallest_subarray_covering_set ] 5/17
TOPICS
- 2 pointer, hash table

This problem is tricky in the sense that you need to be aware of
- Is this keyword covered? What if there are multiple instances of the same
keyword. If we are looking for the smallest subarray, then it makes most
sense to have a dictionary which tells us the # of times we've seen a word. If
it is not in the current set, then we need to decrement our counter object
- The 2 pointer concept comes in that we have found a subarray that covers all
keywords, aka num_rem_to_cover == 0. Once we know this, we can begin looking
for smaller subarrays that still satisfies this condition. Increment the left
pointer forward

SC: O(K) where the size of the keywords
Time Complexity: O(P) where P is the len of paragraph

Example
      RightPointer
aaaabbc
   ^
   LeftPointer
"""
def find_smallest_subarray_covering_set(paragraph, keywords):

    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result

# On 5/15
def find_smallest_subarray_covering_set_my_version(paragraph, keywords):
    word_counts = {kw: 0 for kw in keywords}
    left, num_rem = 0, len(keywords)
    res = Subarray(-1, -1)
    for idx, word in enumerate(paragraph):
        if word in keywords:
            if word_counts[word] == 0:
                num_rem -= 1
            word_counts[word] += 1
        while num_rem == 0:
            if res == (-1, -1) or res[1] - res[0] > idx - left:
                res = Subarray(left, idx)

            # check to see if we are still coverint all letters in set
            if paragraph[left] in keywords:
                word_counts[paragraph[left]] -= 1
                if word_counts[paragraph[left]] == 0:
                    num_rem += 1
            left += 1

    return res

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
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
