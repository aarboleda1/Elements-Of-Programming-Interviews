import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

"""12.7 pg 183

Write a program that takes 2 arrays of strings, and return the indices of the
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

word_counts_and_orders: Dict[word: Tuple(count, mostRecentIndex)] {
    apple: (2, 3),
    banana: (1, 1),
}
keywords = [banana, apple]
rem_to_cover = 0
left = 0

# HISTORY LOG
[  ] - 5/15
"""


def is_ordered(words_info, keywords):
    for i in range(1, len(keywords)):
        prev = keywords[i - 1]
        cur = keywords[i]
        (_, prev_idx) = words_info[prev]
        (_, cur_idx) = words_info[cur]
        if prev_idx > cur_idx:
            return False
    return True

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    # keyword: (count, mostRecentlySeenIndex)
    words_info = {kw: (0, -1) for kw in keywords}
    num_rem_to_cover = len(keywords)
    left, res = 0, Subarray(0, 0)
    for i, word in enumerate(paragraph):
        if word in keywords:
            cur_count, idx = words_info[word]
            if cur_count == 0:
                num_rem_to_cover -= 1
            # update to most recently seen index
            words_info[word] = (cur_count + 1, i)
        while num_rem_to_cover == 0 and is_ordered(words_info, keywords):
            if res == Subarray(0, 0) or i - left < res[1] - res[0]:
                res = Subarray(left, i)

            left_word = paragraph[left]
            if left_word in keywords:
                (count, cur_idx) = words_info[left_word]
                new_count = count - 1
                # We need this to make sure that the current subarr
                # covers all words in the keywords
                if new_count == 0:
                    words_info[left_word] = (new_count, -1)
                    num_rem_to_cover += 1
                else:
                    words_info[left_word] = (new_count, cur_idx)
            left += 1
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
