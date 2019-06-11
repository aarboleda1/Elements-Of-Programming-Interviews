import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import heapq
"""13.6 Render a calendar
Consider the problem of designing an online calendaring application. One
component of the design is to render the calendar, i.e. display it visually

Suppose each day consist of a number of events, where an event is specified as a
start time and finish time. Individual events for a day are to be rendered as
nonoverlapping rectangular regions whose sides are parallel to the X- and Y-axes
. Let the X-axis correspond to time. If an event starts at time b and ends at
time e, the upper and lower sides of its corresponding rectangle must be at b and
e, respectively.

Suppose the y-coordinates for each day's events must lie between 0 and L ( a
pre-specified constant), and each event's rectangle must have the same "height"
(distance between the sides parallel to the X-axis). Your task is to compute the
maximum height an event rectangle can have. In essence, this is equivalent to
the following problem.

Write a program that takes a set of events, and determines the maximum number of
events that take place concurrently.

[ ATTEMPTED ] - 6/3
"""
# Event is a tuple (start_time, end_time)
Event = collections.namedtuple("Event", ("start", "finish"))
# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
"""
0, 3
2, 5
"""
def find_max_simultaneous_events(A):
    if not A:
        return 0
    A.sort(key=lambda e:e.start)
    res, h = 0, [A[0].finish]
    for event in A[1:]:
        if h[-1] > event.start:
            res += 1
        heapq.heappush(h, event.finish)
    return res


    """

    """
def find_max_simultaneous_events_(A):
    starts = sorted([e.start for e in A])
    ends = sorted([e.finish for e in A])
    num_sim_events = 0
    i, j = 0, 0
    while i < len(starts):
        if starts[i] > ends[j]:
            num_sim_events -= 1
            j += 1
        num_sim_events += 1
        i += 1
    return num_sim_events

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events, events))


if __name__ == "__main__":
    events = [Event(0, 3), Event(2, 5)]
    r = find_max_simultaneous_events(events)
    print(r)

    events = [Event(0, 2), Event(2, 5)]
    r = find_max_simultaneous_events(events)
    print(r)

    events = [Event(0, 1), Event(2, 5)]
    r = find_max_simultaneous_events(events)
    print(r)

    events = [Event(0, 1), Event(2, 5), Event(3,9), Event(4,6)]
    r = find_max_simultaneous_events(events)
    print(r)
    # exit(
        # generic_test.generic_test_main(
            # "calendar_rendering.py",
            # "calendar_rendering.tsv",
            # find_max_simultaneous_events_wrapper,
        # )
    # )
