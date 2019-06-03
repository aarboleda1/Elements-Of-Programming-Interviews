import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""6.4 Replace and remove p. 78

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

Hint: consider performing multiple passes on s

Basic Idea:
We should think about this in two parts, first, replace all b's. This will
give you the size of the final string.
Next part is to count the number of a's int he string. Since, for each a we encounter
we'll also have to replace it with a d and add another

Final string length is write_idx + a_count

Then replace all the a's. Do this by iterating backwards and writing the d's

Remove
[ SOLVED ] 6/2
[ ATTEMPTED ] - 5/27
[ ATTEMPTED ] - 5/25
"""

def replace_and_remove(size, s):

    # Forward iteration: remove 'b's and count the number of 'a's.
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            # Remove the b's and write the cur char
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # Backward iteration: replace 'a's with 'dd's starting from the end.
    cur_idx = write_idx - 1
    write_idx += a_count - 1

    # The final size is the array with all b's removed plus
    # the array with number of a's
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
