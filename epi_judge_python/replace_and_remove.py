import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""6.4 Replace and remove

Consider the following two rules that are applied to an array of characters.

- Replace each 'a' by two 'd's
- Delete each entry containing b

For example, applying these rules to the array [a, c, d, b, b, c, a] results
in the array [d, d, c, d, c, d, d]

Write a program which takes as input an array of characters, and removes each 'b'
and replaces each 'a' by two 'd's. Specifically, along with the array, you are
provided an integer-valued size. Size denotes the number of entries of the
array that the operation is to be applied to. You do not have to worry about
preserving subsequent entries. For example, if the array is [a, b, c, a, c, _]
and the size is 4, you can return [d,d,d,d,c]. You can assume there is enough
space in the array to hold final result

- Replace each 'a' by two 'd's
- Delete each entry containing b

Hint: consider performing multiple passes on s
[ ] 5/27
[ ATTEMPTED ] - 5/25
"""
def replace_and_remove(size, s):
    pass

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    replace_and_remove(4, ['a', 'b', 'c', 'b'])
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
