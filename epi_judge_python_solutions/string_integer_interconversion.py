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
For both, you want to make sure the numberes are in base10, then you can use
modulus and division operators to break down and build up the string or int

int_to_string basic algorithm: Use modulo operator to get the remainder of a
number and divide the number by 10. Get the remainder and add it to a stack,
string or queue.
Check out these 3 iterations
1) 314 % 10 = 4, 314 // 10 = 31, add 4 to alist, alist = [4]
2) 31 % 10 = 1, 31 // 10 = 1, add 1 to alist, alist = [4,1]
3) 3 % 10 = 3, 3 // 10 = 0, add 3 to alist, alist = [4,1,3]

The reversed and joined value of alist will be 314

Do the same thing but in reverse for string_to_int


[ SOLVED ] 6/3
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
# my own personal implementation
def string_to_int(s):
    is_negative = s[0] == "-"
    start = 1 if is_negative else 0
    running_sum = 0
    for i in range(start, len(s)):
        running_sum = (running_sum * 10) + string.digits.index(s[i])
    return running_sum * (-1 if is_negative else 1)

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
