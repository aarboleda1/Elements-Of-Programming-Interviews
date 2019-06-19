from test_framework import generic_test
import heapq
import itertools
"""10.3 Sort an almost-sorted array

Often data is almost-sorted, for example a server receives timestamped stock
quotes and earlier quotes may arrive slightly after later quotes because of
differences in server loads and network routes. In this problem we address
efficient ways to sort such data.

Write a program which takes as input a very long sequence of numbers and prints
the numbers in sorted order. Each number is at most k away from its correctly
sorted position. (Such an array is sometimes referred to as being k-sorted).
For example, no number in the sequence [3,-1,2,6,4,5,8] is more than 2 away
from its final sorted position

Hint: How many numbers must you read after reading the ith number to be sure
you can place it in the correct location?

NOTE create your own test case, the test cases here aren't correct
(ATTEMPTED, 6/18)
"""
def sort_approximately_sorted_array(A, k):
    pass


# def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    # return []


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    A, k = [3,-1,2,6,4,5,8], 2
    sort_approximately_sorted_array(A, k)
    # exit(
        # generic_test.generic_test_main(
            # "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            # sort_approximately_sorted_array_wrapper))
