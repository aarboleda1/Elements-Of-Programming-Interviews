from test_framework import generic_test


"""6.5 Test Palindromicity

For the purpose of this problem, define a palindromic string to be a string
which when all nonalphanumeric are removed it reads the same front to back
ignoring case. For example, "A man, a plan, a canal, Panama" and "Able
was I, ere I saw Elba" are palindromic, but "Ray a Ray" is not.

Implement a function which takes as input a string s and returns true if s is a
palindromic string

[ATTEMPTED] 5/25
"""


def is_palindrome(s):

    return True


if __name__ == "__main__":
    is_palindrome("A man, a plan, a canal, Panama.")
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
