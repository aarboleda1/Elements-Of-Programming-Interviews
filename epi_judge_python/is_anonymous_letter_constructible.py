from test_framework import generic_test
from collections import Counter
"""12.1 Is an anonymous letter constructible?

Write a program which takes text for an anonymous letter and text for a
magazine and determines if it's possible to write the anonymous letter using
the magazine. The anonymous letter can be written using the magazine if for each
character in the anonymous letter, the number of times it appears in the
anonymous letter is no more than the number of times it appears in the magazine

letter_text = "abc"
magazine_text = "aabc"

True, because "a" appears once, "b" appears once and "c" appears once

letter_text = "aabc"
magazine_text = "abc"

[ SOLVED ] - 5/18 SC: O(N) where N is the len of magazine_text and same for TC
"""
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    pass

if __name__ == '__main__':
    assert is_letter_constructible_from_magazine("abc", "aabc") is True
    assert is_letter_constructible_from_magazine("aaabc", "abc") is False
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
