from test_framework import generic_test

"""11.4 Compute the integer square root

Write a program which takes a nonnegative integer and returns the larger integer
whose square root is less than or equal to the given integer. For example,
if the input is 16, return 4; if the input is 300, return 17, since 17^2 =
289 < 300 and 18^2 = 324 > 300

Basic Idea:
Brute force is to square each number from 1 to the key k, stopping as soon as
k is exceeded. Time complexity is O(k)

But if you look into the problem more carefully, you can see it's wasteful to take
unit-sized (incrementing by 1) increments. For example, if n^2 < k, then no number
smaller than n can be the result and if n^2 > k, then no number greater than or
equal to x can be the result


Hint: Look out for corner cases
[ ATTEMPTED ] 6/6
"""
def square_root(k):

    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


def square_root(k):
    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        squared = mid * mid
        if squared == k:
            return mid
        elif squared < k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

# Brute Force
def square_root_o_nsolution(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    ans = 1
    for n in range(1, k):
        squared = n * n
        if squared == k:
            return n
        elif squared > k:
            return n - 1
    return ans
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
