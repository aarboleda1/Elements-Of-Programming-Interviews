import bintrees
from test_framework import generic_test

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    i, j, k = 0, 0, 0
    arr1, arr2, arr3 = sorted_arrays
    min_dist_so_far = float('inf')
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        min = min(arr1[i], arr2[j], arr3[k])
        max = min(arr1[i], arr2[j], arr3[k])
        min_dist_so_far = min(max - min, min_dist_so_far)
        if min_dist_so_far == 0:
            return min_dist_so_far
        if arr1[i] == min:
            i += 1
        elif arr2[j] == min:
            j += 1
        else:
            k += 1
    return min_dist_so_far

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    min_dist_so_far = float('inf')
    iters = bintrees.RBTree()
    # you need i, to tell you what idx you're coming from down below
    for i, sorted_arr in enumerate(sorted_arrays):
        it = iter(sorted_arr)
        first_min = next(it, None)
        if first_min is not None:
            it.insert((first_min, i), it)
    while True:
        min_val, min_idx = iters.min_key()
        max_val = iters.max_key()[0]
        min_dist_so_far = min(max_val - min_val, min_dist_so_far)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        # if one is done, you've already exhausted finding the min between the 3
        if next_min is None:
            return min_dist_so_far
        iters.insert((next_min, min_idx), it)
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
