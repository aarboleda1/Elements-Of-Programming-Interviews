from test_framework import generic_test

"""12.5 People do not like reading text in which a word is used multiple times
in a short paragraph. You are to write a program which helps identify such a
problem

Write a program which takes as input an array and finds the distance between
a closest pair of equal entries. For example, if s = ["All", "work", "no",
"play", "makes", "for", "no", "work", "no", "fun", "and", "no, "results"], then
the second and third occurences of "no" is the closest pair

HISTORY LOG
- [ SOLVED ] 5/16
"""

def find_nearest_repetition(paragraph):
    res, dic = float("inf"), {}
    for i, word in enumerate(paragraph):
        if word in dic:
            res = min(i - dic[word], res)
        dic[word] = i
    return res if res != float("inf") else -1


if __name__ == '__main__':
    A = ["foo", "bar", "widget", "foo", "widget", "widget", "adnan"]
    res = find_nearest_repetition(A)
    assert res == 1
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
