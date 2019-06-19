import functools
import math

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
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars, k):
    # TODO - you fill in here.
    return []


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
