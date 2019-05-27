"""
K-Messed Array Sort/Nearly Sorted Array

Back to Back SWE: https://www.youtube.com/watch?v=yQ84lk-EXTQ
https://www.geeksforgeeks.org/nearly-sorted-algorithm/

Given an array of integers arr where each element is at most k places away from
its sorted position, code an efficient function sortKMessedArray that sorts arr.
For instance, for an input array of size 10 and k = 2, an element belonging to
index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in
the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

1 ≤ k ≤ 20
[output] array.integer

Basic Algorithm:
- Create a min-heap of size k from index 0 to k.

*****Add and place, add and place, add and place.******
We already added values from 0 to k, so now from k to n - 1, add A[i] and then
write to A[write_idx]
A[i]

n = len(arr)
Time: O(N * log(k)) we iterate over n elements and perform a log(k) insertion
to our min-heap
Space: The min-heap will be at most O(log (k))
"""
from heapq import heappush, heappop

def sort_k_messed_array(arr, k):
    heap = []
    n = len(arr)
    for i in range(min(len(arr), k)):
        heappush(heap, arr[i])
    read_idx = k
    write_idx = 0
    while read_idx < n:
        heappush(heap, arr[read_idx])
        read_idx += 1

        arr[write_idx] = heappop(heap)
        write_idx += 1

    while heap:
        arr[write_idx] = heappop(heap)
        write_idx += 1
    return arr
res = sort_k_messed_array([3, 1, 8, 7, 0], 2)
print(res)
assert res == [1,3,0,7,8]
