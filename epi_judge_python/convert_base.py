from test_framework import generic_test

"""6.2 Base Conversion

In the decimal number system, the position of a digit is used to signify the
power of 10 that digit is to be multiplied with. For example "314" denotes the
number with 3 x 100 + 1 x 10 + 4 x 1. The base b number system generalizes
the decimal number system: the string "ak - 1 ak - 2... a1a0", where 0 <= a < b
denotes the base-b integer

Write a program that performs base conversion. The input is a string, an integer
b1, and another integer b2. The string represents an integer in b1. The output
should be the string representing the integer in b2. Assume 2 <= b1 and
b2 <= 16. Use "A" to represent 10, "B" for 11, ... and "F for 15, for"

[ ATTEMPTED ]  - 5/25
"""
def convert_base(num_as_string, b1, b2):
    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
