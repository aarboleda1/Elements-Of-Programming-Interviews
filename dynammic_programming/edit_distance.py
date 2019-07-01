"""
Given two words word1 and word2, find the minimum number of operations required
to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"

Output: 3

Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Resources:
Leetcode: https://bit.ly/2IZhFFH
Youtube: Back to Back SWE https://bit.ly/322jr0o

"""
def _minDistanceWithMemo(word1, word2, i, j, memo):
    if i == len(word1) and j == len(word2):
        return 0

    # The number of letters left
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i

    if (i, j) not in memo:
        if word1[i] == word2[j]:
            ans = _minDistanceWithMemo(word1, word2, i + 1, j + 1, memo)
        else:
            insert = 1 + _minDistanceWithMemo(word1, word2, i, j + 1, memo)
            replace = 1 + _minDistanceWithMemo(word1, word2, i + 1, j + 1, memo)
            delete = 1 + _minDistanceWithMemo(word1, word2, i + 1, j, memo)
            ans = min(insert, replace, delete)
        memo[(i, j)] = ans
    return memo[(i,j)]

def minDistanceWithMemo(word1, word2):
    return _minDistanceWithMemo(word1, word2, 0, 0, {})


# Recursive naive solution
def minDistanceRecursiveNaive(word1, word2):
    """Naive recursive solution"""
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    if word1[0] == word2[0]:
        return minDistanceRecursiveNaive(word1[1:], word2[1:])
    insert = 1 + minDistanceRecursiveNaive(word1, word2[1:])
    delete = 1 + minDistanceRecursiveNaive(word1[1:], word2)
    replace = 1 + minDistanceRecursiveNaive(word1[1:], word2[1:])
    return min(insert, replace, delete)

if __name__ == "__main__":
    ans = minDistanceRecursiveNaivie("abc", "axc")
    ans = minDistanceWithMemo("abc", "axc")
    print(ans, 'SHOULD BE 1')
    assert ans == 1
