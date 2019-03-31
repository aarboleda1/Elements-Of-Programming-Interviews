import collections

from test_framework import generic_test


PairedTasks = collections.namedtuple("PairedTasks", ("task_1", "task_2"))


def optimum_task_assignment(task_durations):
    task_durations.sort()
    lo, hi = 0, len(task_durations) - 1
    opt_assignment = []
    while lo < hi:
        opt_assignment.append((task_durations[lo], task_durations[hi]))
        lo += 1
        hi -= 1
    return opt_assignment


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "task_pairing.py", "task_pairing.tsv", optimum_task_assignment
        )
    )
