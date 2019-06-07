import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook


Interval = collections.namedtuple("Interval", ("left", "right"))

"""13.7 Merging Intervals

Suppose the time during the day that a person is busy is stored as a disjoint time
intervals. If an event is added to the person's calendar, the set of busy times
may need to be updated.

In the abstract, we want a way to add an interval to a set of disjoint intervals
and represent the new set as a set of disjoint intervals. For example, if the initial set of
intervals is [-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17] and then the
added interval is [1,8], the result is [-4, -1], [0, 9], [11, 12], [14,17]

[-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17]
new_interval = [1,8]

1) [-4, -1] # not overlapping because i.end < new_interval.start
# overlappers
2) while i.start < new_interval.end
3) [10, 12] # not overlapping because i.start > new_interval.end

[[-4,-1], [0, 9], [14,17]]

[ SOLVED ] 6/6
[ ATTEMPTED ] 6/4
Time Complexity:
Space Complexity
"""


def add_interval(disjoint_intervals, new_interval):
    pass


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals, Interval(*new_interval))
    )


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            "interval_add.tsv",
            add_interval_wrapper,
            res_printer=res_printer,
        )
    )
