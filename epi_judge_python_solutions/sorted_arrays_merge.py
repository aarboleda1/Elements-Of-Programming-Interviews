import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):

    min_heap = []
    # Builds a list of iterators for each array in sorted_arrays.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap.
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

# TC: O(N), SC: O(N)
def merge_sorted_arrays(sorted_arrays):
    res, heap = [], []
    for i, arr in enumerate(sorted_arrays):
        heappush(heap, (arr[0], 0, i))
    while heap:
        (val, idx, idx_in_sorted_arrays) = heappop(heap)
        res.append(val)
        if idx < len(sorted_arrays[idx_in_sorted_arrays]) - 1:
            heappush(
                heap,
                (sorted_arrays[idx_in_sorted_arrays][idx + 1],
                idx + 1,
                idx_in_sorted_arrays)
            )
    return res
# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
