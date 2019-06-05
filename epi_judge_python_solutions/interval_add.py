import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

"""13.7 Merging Intervals

Suppose the time during the day that a person is busy is stored as a disjoint time
intervals. If an event is added to the person's calendar, the set of busy times
may need to be updated.

In the abstract, we want a way to add an interval to a set of disjoint intervals
and represent the new set as a set of disjoint intervals. For example, if the initial set of
intervals is [-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17] and then the
added interval is [1,8], the result is [-4, -1], [0, 9], [11, 12], [14,17]

[-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17]


[[-4,-1], [0, 9], [14,17]]

[ ATTEMPTED ] 6/4
Basic Algorithm: Use the sorted property to process intervals in the array.
Specifically, process the intervals in 3 different stages:
1) Iterate thru the intervals which appear complete before the interval
to be added. Directly add these to the result

2) Once we encounter an interval that intersects the new interval to be added,
compute its union with the interval to be added. This union itself is an interval
Keep iterating thru the intervals and as long as they intersect with the current
interval we are forming, keep computing the union.

3) Finally, iterate thru the rest of the intervals. Because the array was
originally sorted by start times, none of these can intersect the interval to be
added and we can just directly append them to result

Time Complexity: O(N)
Space Complexity: O(1), using no extra space
"""
def add_interval(disjoint_intervals, new_interval):

    i, result = 0, []

    # Processes intervals in disjoint_intervals which come before new_interval.
    while (i < len(disjoint_intervals)
           and new_interval.left > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_intervals which overlap with new_interval.
    while (i < len(disjoint_intervals)
           and new_interval.right >= disjoint_intervals[i].left):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1
    # Processes intervals in disjoint_intervals which come after new_interval.
    return result + [new_interval] + disjoint_intervals[i:]


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
