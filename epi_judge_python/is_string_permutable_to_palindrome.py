from test_framework import generic_test
from collections import Counter
"""A palindrome is a string that reads the same forwards and backwards, e.g.,
"level", "rotator", and "foobaraboof"

Write a program to test whether the letters forming a string can be permuted
to form a palindrome. For example, "edified" can be formed to form "deified"

Hint: Find a simple characterization of strings that can be permuted to form a
palindrome

- [ SOLVED ] 5/18 Time complexity: O(N), Space is O(N)
"""
def can_form_palindrome(s):
    hash_table = {}
    has_odd_char = False
    for char in s:
        val = hash_table.get(char, 0)
        hash_table[char] = val + 1
    for k, count in hash_table.items():
        is_odd = count % 2 == 1
        if has_odd_char and is_odd:
            return False
        elif is_odd:
            has_odd_char = True
    return True




if __name__ == '__main__':
    assert can_form_palindrome("level") == True
    assert can_form_palindrome("abx") == False
    assert can_form_palindrome("dad") == True
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
