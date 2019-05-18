import collections

from test_framework import generic_test

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
    - Note, for my solution, I constructed based on letter text, the solution
    below is better because it uses the smaller of the two, letter_text
    and checks if the chars in magazine_text can cover chars in the char_frequency_for_letter
"""
def is_letter_constructible_from_magazine(letter_text, magazine_text):

    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
            if not char_frequency_for_letter:
                # All characters for letter_text are matched.
                return True

    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter


# Pythonic solution that exploits collections.Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) -
            collections.Counter(magazine_text))
# 5/18 Pythonic solution that exploits collections.Counter. Note that the
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_counts = Counter(magazine_text)
    for l in letter_text:
        if l not in char_counts:
            return False

        char_counts[l] -= 1
        if char_counts[l] < 0:
            return False
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
