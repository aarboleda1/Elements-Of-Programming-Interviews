from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string
"""6.1 p.75 String Bootcamp
A string is a sequence of characters. A string may encode an integer e.g., "123"
encodes 123. In this problem, you are to implement methods that take a string
representing an integer and return the corresponding integer, and vice versa.
Your code should handle negative integers. You cannot use library functions like
int in Python

Implement an integer to string conversion function, and a string to integer
conversion function. For example, if the input to the first function is the
integer 314, it should return the string "314" and if the input to the
second function is the string "314" it should return the integer 314

[ ATTEMPTED ] 5/23
"""
def int_to_string(x):
    num = abs(x)
    s = []
    while True:
        rem = num % 10
        num = num // 10
        s.append(
            chr(ord('0') + rem)
        )
        if num == 0:
            break
    return ('-' if x < 0 else '') + ''.join(reversed(s))

def string_to_int(s):
    res = 0
    is_neg = s[0] == '-'
    start = 1 if is_neg else 0
    for i in range(start, len(s)):
        char = s[i]
        res = (res * 10) + string.digits.index(char)
    return res * -1 if is_neg else res

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    ret = string_to_int("-13")
    print(ret)
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
