import heapq
import itertools

from test_framework import generic_test
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

Basic Algorithm: We want to take advantage of the partiall sortedness. Iterate
thru the array, and for each element, we ask, what are the potential candidates?
Well, they can only be k indices away. We also note that we want the smallest
item from the i to k + 1. So for each element we gather all candidates
A[i]..A[i + (k + 1)]. Then when we pop from the heap, we write to i - k


NOTE create your own test case, the test cases here aren't correct
"""
def sort_approximately_sorted_array(A, k):
    min_heap = []
    heap = A[:k + 1]
    heapq.heapify(heap)
    write_index = 0
    for i in range(k + 1, len(A)):
        smallest = heapq.heappop(heap)
        A[write_index] = smallest
        heapq.heappush(heap, A[i])
        write_index += 1
    return A
# Incorrect
def sort_approximately_sorted_array(sequence, k):

    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
