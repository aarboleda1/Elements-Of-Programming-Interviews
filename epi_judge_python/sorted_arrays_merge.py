from test_framework import generic_test
from heapq import heappush, heappop
"""10.1 Merge sorted files

This problem is motivated by the following scenarios. You are given 500 files,
each containing stock trade information for an S&P 500 company. Each trade
is encoded by a line in the following format 1232111, AAPPL, 345.12

The 1st number is the time of the trade expressed as the number of milliseconds
since the start of the day's trading. Lines within each file are sorted in
increasing order of time. The remaining values are the stock symbol, number of
shares, and price. You are to create a csingle file containing all the trades
from the 500 files, sorted in order of increasing trade times. The individual
files are in the order of 5 - 100 megabytes; the combined file will be the
order of 5 gigabytes. In the abstract we are trying to solve the following
problem.

Write a program that takes as input a set of sorted sequences and computes
the union of these sequences a sorted sequence. For example, if the input
is [3,5,7] [0,6] [0,6,28], then the output is [0,0,3,5,6,6,7,28]

Hint: Which part of the sequence is significant as the algorithm executes?

(SOLVED, 6/18)
"""

def merge_sorted_arrays(sorted_arrays):
    pass


if __name__ == '__main__':
    print(merge_sorted_arrays([[-1, 0], [-2]]), [-2, -1, 0])
    print(merge_sorted_arrays([[-1, 0], [-2], [3,5]]), [-2, -1, 0, 3, 5])
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
