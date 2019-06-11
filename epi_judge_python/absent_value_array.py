from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""11.9 Find the missing IP address

The storage capacity of hard drives dwards that of RAM. This can lead to interesting
space-time trade-offs.

Suppose you were given a file containing roughly one billion IP addresses, each
of which is a 32-bit quantity. How would you programmatically find an IP address
that is not in the file? Assume you have unlimited drive space but only a few
megabytes of RAM at your disposal.

Hint: Can you be sure tehre is an address which is not in the file?
"""
def find_missing_element(stream):
    # TODO - you fill in here.
    return 0


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
