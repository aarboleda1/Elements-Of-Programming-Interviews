import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

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

Basic Algorithm: Brute force algorithm, for each endpoint, compute the number of
events that contain it. The maximum of this quantity over all endpoints. If there
are n endpoints, then we'll have to scan over the array n times, which would make this
algorithm O(n ^ 2)

The problem with this solution, is it does not take into account of locality.
When we move from 1 point to the next, we know 2 things, if it's a start and its
value. If we sort all endpoints, and we have 3 events that happen in a row,
without their endtimes being seen, then that means there are 3 events in a row

example: [(0,3), (1, 5), (2, 3)]
If we sort this into something into a tuple containing, (value, is_start),
We check each event and keep a count of how many events are going on at the same time.
You break ties between event times by putting start times first depending on
whether the interviewer will have start_times and end times being equal if
that is considered "overlapping"

sorted_array = [
    (0, True), (1, True), (2, True), (3, False), (3, False), (5, False)
]
num_events 1       2         3          2           1            0
From this we can see that there are at max 3 events going on at the same time

[ ATTEMPTED ] - 6/3
"""
# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

# O(N) time and O(N) space
def find_max_simultaneous_events(A):
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

# O(N) time and O(N) space
def find_max_simultaneous_events(A):

    # Builds an array of all endpoints.
    E = [
        p for event in A for p in (Endpoint(event.start, True),
                                   Endpoint(event.finish, False))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
