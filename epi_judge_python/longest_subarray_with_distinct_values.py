from test_framework import generic_test

"""Write a program that takes an array and returns the length of the longest
subarray with the property that all its elements are distinct. For example,
if the array is [f,s,f,e,t,w,e,n,w,e] then a longest subarray all
of whose elements are distinct is [s,f,e,t,w]
{
    f: 0,
    s: 1
}

- HISTORY LOG
[ ATTEMPTED ] 5/15
"""


def longest_subarray_with_distinct_entries(A):
    most_recent_occ = {}
    start_idx_sub_arr_without_dup = res = 0
    for i, el in enumerate(A):
        if el in most_recent_occ:
            if most_recent_occ[el] >= start_idx_sub_arr_without_dup:
                dup_idx = most_recent_occ[el]
                res = max(i - start_idx_sub_arr_without_dup, res)
                start_idx_sub_arr_without_dup = dup_idx + 1
        most_recent_occ[el] = i
    return max(res, len(A) - start_idx_sub_arr_without_dup)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
