import functools
import string

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""6.1 p.75
A string is a sequence of characters. A string may encode an integer e.g., "123"
encodes 123. In this problem, you are to implement methods that take a string
representing an integer and return the corresponding integer, and vice versa.
Your code should handle negative integers. You cannot use library functions like
int in Python

Implement an integer to string conversion function, and a string to integer
conversion function. For example, if the input to the first function is the
integer 314, it should return the string "314" and if the input to the
second function is the string "314" it should return the integer 314

Basic algorithm:
    char_str = '2'
    char_int = string.digits.index(c)
    char_int = 2

[ ATTEMPTED ] 5/23
[ ATTEMPTED ] 5/26
"""

def int_to_string(x):

    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
