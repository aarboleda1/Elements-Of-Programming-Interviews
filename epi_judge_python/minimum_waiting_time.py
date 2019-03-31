from test_framework import generic_test

# O (n log n)
def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_wait_time = 0
    for i, st in enumerate(service_times):
        n_remaining_q = len(service_times) - (i + 1)
        total_wait_time += n_remaining_q * st
        print(total_wait_time)
    return total_wait_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
