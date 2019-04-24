from heapq import heappop, heappush, heappushpop

from test_framework import generic_test
"""
Design an algorithm for computing the running median of a sequence
sequence = [1,0,3,5,2,0,1]
ans = [1,.5.1,2,2,1.5,1]
"""


def online_median(sequence):
    max_heap, min_heap = [], []
    medians = []
    for n in sequence:
        # balance, make sure the min_heap is smaller thean the right heap
        heappush(max_heap, -heappushpop(min_heap, n))
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))
        # get the median
        median = (
            min_heap[0]
            if len(min_heap) != len(max_heap)
            else 0.5 * (min_heap[0] + (-max_heap[0]))
        )
        medians.append(median)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
