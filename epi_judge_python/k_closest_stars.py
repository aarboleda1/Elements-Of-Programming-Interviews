import functools
import heapq
import math
import random
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""10.4 Compute k closest stars

Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0).
Model stars as points, and assume distances are in light years. The Milky Way
consists of approximately 10^12 stars, and their coordinates are stored in
a file.

How would you compute the k stars which are closest to Earth?

Hint: Suppose you know the k closest stars in the first n stars. If the (n + 1)th
star is to be added to the set of k closest stars, which element in that set
should be acheived?

() - 6/18
"""


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

"""
4, 2, 0, 9, 3

0,2
"""
# use 1st item as pivot
def partition(stars, start, end, partition_idx): # int (index)
    # swap
    A[partition_idx], A[end] = A[end], A[partition_idx]
    star = stars[partition_index]
    distance = star.distance
    j = start
    for i in range(start, end):
        if stars[i].distance < distance:
            j += 1
        else:
            A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    return j

def find_closest_k_stars(stars, k):
    start, end, n = 0, len(stars) - 1, len(stars)
    while start < end:
        random_idx = random.randint(start, end)
        index_from_partition = partition(stars, start, end, random_idx)

        if index_from_partition == n - k:
            return stars[index_from_partition]
        elif index_from_partition > n - k:
            end = index_from_partition - 1
        else:
            start = index_from_partition + 1
    return -1





def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d) for s, d in zip(sorted(output), expected_output)
    )


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_closest_stars.py",
            "k_closest_stars.tsv",
            find_closest_k_stars_wrapper,
            comp,
        )
    )
