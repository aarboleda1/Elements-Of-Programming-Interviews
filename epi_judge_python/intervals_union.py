import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


Endpoint = collections.namedtuple("Endpoint", ("is_closed", "val"))

Interval = collections.namedtuple("Interval", ("left", "right"))

"""13.8 Compute the union of intervals

In this problem we consider sets of intervals with integer endpoints; the
intervals may be open or closed at either end. We want to compute the union of
intervals in such sets. A concrete example is given in 13.2 on the facing page

Design an algorithm that takes as input a set of intervals and ouputs their union
expressed as a set of disjoin intervals

[ SOLVED ] - 6/4
"""


def union_of_intervals(intervals):
    pass


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [
        (i.left.val, i.left.is_closed, i.right.val, i.right.is_closed) for i in result
    ]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intervals_union.py", "intervals_union.tsv", union_of_intervals_wrapper
        )
    )
