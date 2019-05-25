import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""6.6 Reverse all words in a sentence

Given a string containing a set of words separated by whitespace, we would
like to transform it to a string in which the words appear in the reverse order.
For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not keep
the original string

Implement a function for reversing words in a string s

Hint: It's difficult to solve this with one pass

[ ATTEMPTED ] - 5/25
"""
# Assume s is a string encoded as c.
def reverse_words(s):
    pass



@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    reverse_words(bytearray(b'alice likes bob'))
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
