import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

"""11.10 Find the duplicate and missing elements

If an array contains n - 1 integers, each between 0 and n - 1, inclusive, and
all number in the array are distinct, then it must be the case that exactly one
number between 0 and n - 1 is absent.

We can determine the missing number in O(n) time and O(1) space by computing
the sum of the elements in the array. Since the sum of all numbers from 0 to
n - 1, inclusive is (n - 1)n / 2, we can subtract the sum of the numbers from
(n - 1)n / 2 to get the missing number.

For example, if the array is [5,3,2,0,1,2], then n = 6. We subtract
(5 + 3 + 0 + 1 + 2) = 11 from 5(6)/2 = 15, and the result, 4, is the missing
number.

Similarly, if the array contains n + 1 integers, each between 0 and n - 1
inclusive, with exactly 1 element appearing twice, the duplicated integer
will be equal to the sum of the elements of the array minus (n - 1)n/2

Alternatively, for the 1st problem, we can compute the missing number by
computing the XOR of all integers from 0 to n - 1, inclusive, and XORing that
with the XOR of all the elements in the array. Every element in the array,
except for the missing element, cancels out with an integer from the first set.
Therefore, the resulting XOR equals the missing element. The same approach
works for the problem of finding the duplicated element. For example, the array
[5,3,0,1,2] represented in binary is
[(101) ^ 2, (011) ^ 2, (000) ^ 2, (001) ^ 2, (010) ^ 2]. The XOR of these
entries is (101) ^ 2. The XOR of all numbers form 0 to 5, inclusive is (001) ^ 2. T
The XOR of (101) ^ 2 and (001) ^ 2 and (001) ^ 2 and (100) ^ 2 = 4, which is the
missing number

We now turn to a related, though harder, problem.

You are given an array of n integers, each between 0 and n - 1, inclusive. Exactly
one element appears twice, implying that exactly one number between 0 and n - 1
is missing from the array. How would you compute the duplicate and missing numbers?

Hint: Consider performing multiple passes thru the array.
[0, 2, 1, 1] DupAndMis(1, 3)

i  A
0 [0, 2, 1, 1]
1 [0, 1, 2, 1]
2 [0, 1, 2, 1]
3 [0, 1, 2, 1]

"""
def find_duplicate_missing(A):
    pass


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    A = [0, 2, 0, 1]
    print(find_duplicate_missing(A), " dup: 0, missing: 3")
    A = [4, 3, 1, 1, 0]
    print(find_duplicate_missing(A), "dup: 1, missing: 2")
    A = [12, 14, 41, 74, 79, 22, 16, 11, 24, 76, 101, 27, 60, 31, 0, 13, 53, 90, 89, 1, 4, 85, 9, 77, 43, 93, 51, 86, 35, 5, 67, 71, 21, 46, 56, 95, 66, 19, 20, 44, 73, 91, 61, 69, 83, 34, 17, 29, 58, 78, 36, 49, 99, 38, 96, 40, 92, 37, 33, 15, 47, 5, 23, 3, 26, 64, 52, 81, 82, 8, 28, 25, 32, 65, 68, 70, 72, 94, 63, 7, 55, 10, 45, 100, 84, 2, 54, 98, 50, 39, 6, 88, 48, 97, 57, 59, 87, 62, 75, 30, 18, 42]
    print(find_duplicate_missing(A), "duplicate: 5, missing: 80")
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
