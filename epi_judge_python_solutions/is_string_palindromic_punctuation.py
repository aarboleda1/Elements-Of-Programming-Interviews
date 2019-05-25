from test_framework import generic_test

"""6.5 Test Palindromicity

For the purpose of this problem, define a palindromic string to be a string
which when all nonalphanumeric are removed it reads the same front to back
ignoring case. For example, "A man, a plan, a canal, Panama" and "Able
was I, ere I saw Elba" are palindromic, but "Ray a Ray" is not.

Implement a function which takes as input a string s and returns true if s is a
palindromic string

Basic Algorithm: Start and end pointers to find chars. Only subtlety is if
s[start] or s[end] is not an alphanumberic character. Move pointers until you
find an alphanumeric char then check their lowercase value

[ATTEMPTED] 5/25

"""
def is_palindrome(s):

    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


def is_palindrome_pythonic(s):
    return all(a == b for a, b in zip(
        map(str.lower, filter(str.isalnum, s)),
        map(str.lower, filter(str.isalnum, reversed(s)))))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
