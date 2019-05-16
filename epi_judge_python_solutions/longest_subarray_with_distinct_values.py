from test_framework import generic_test
"""
12.8
HISTORY LOG
- [ATTEMPTED] 5/15

As stated in the hash_table and the array bootcamp notes, we can save indices
of arrays and then use them as information when working with subsets. For
this particular example, the logic is as so:

Initialize a left_idx, this will represent the start of a subarray that
contains no duplicates. Each time we encounter an element, check the hash table
table to see if it has been seen before. If it has, and it's index is larger
than the left_idx, this means there is a duplicate in our current subarray.

Now, we can seee that there is a potential for the result, in that the current
index - left_idx will give us a duplicate free set. we can also assign
left_idx to be duplicate_idx + 1 so we can check for non-duplicate subarrays
starting at dup_idx + 1
"""

def longest_subarray_with_distinct_entries(A):

    # Records the most recent occurrences of each entry.
    most_recent_occurrence = {}
    longest_dup_free_subarray_start_idx = result = 0
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate.
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current
            # subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i
    return max(result, len(A) - longest_dup_free_subarray_start_idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
