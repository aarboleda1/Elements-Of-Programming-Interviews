from test_framework import generic_test


def has_two_sum(A, t):
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        if A[lo] + A[hi] == t:
            return True
        elif A[lo] + A[hi] < t:
            lo += 1
        else:
            hi -= 1
    return False


def has_three_sum(A, t):
    A.sort()
    for i in range(len(A)):
        if has_two_sum(A, t - A[i]):
            return True
    return False
    # Finds if the sum of two numbers in A equals to t - a.

if __name__ == "__main__":
    exit(generic_test.generic_test_main(
        "three_sum.py",
        "three_sum.tsv",
        has_three_sum)
    )
