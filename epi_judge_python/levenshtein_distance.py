from test_framework import generic_test

"""16.2 Compute the Levenshtein Distance

Write a program that takes two strings and computes the minimum number of
edits needed to transform the first string into the second string

Leetcode: https://leetcode.com/problems/edit-distance/submissions/
~/dynammic_programming/

Attempted (6/30)

"""
def levenshtein_distance(A, B):
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
