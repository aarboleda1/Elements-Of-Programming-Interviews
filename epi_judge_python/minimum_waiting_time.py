from test_framework import generic_test


# O (n log n)
def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_time = 0
    for i, s in enumerate(service_times):
        num_times_left = len(service_times) - i - 1
        total_time += s * num_times_left
    return total_time


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_waiting_time.py",
            "minimum_waiting_time.tsv",
            minimum_total_waiting_time,
        )
    )
