def avg(a, b):
    return (a + b) / 2.0


def median_of_two_sorted_arrays(A, B):
    if len(B) < len(A):
        return median_of_two_sorted_arrays(B, A)
    n, m = len(A), len(B)
    imin, imax = 0, n
    half_len = (n + m + 1) // 2
    while imin <= imax:
        # gen the play
        i = (imin + imax) // 2
        j = half_len - i
        if i > 0 and i < n and A[i - 1] > B[j]:
            imax = i - 1
        elif j > 0 and i < n and B[j - 1] > A[i]:
            imin = i + 1
        else:  # perfect!
            max_of_left = max(A[i - 1], B[j - 1])
            if (n + m) % 2 == 1:
                return max_of_left
            else:
                max_of_left = max(A[i - 1], B[j - 1])
                print(i,j)
                min_of_right = min(A[i], B[j]) if i < n else B[j]
                if i == n:
                    min_of_right = B[j]
                return avg(max_of_left, min_of_right)


if __name__ == "__main__":
    A = [0, 2, 4, 6]
    B = [3, 5, 7, 9, 11, 12]
    # 0,2,3,4,5,6,7,9,11,12
    # ans = median_of_two_sorted_arrays(A, B)
    # assert ans == 5.5
    # # ---------------------------------------
    # C = [0, 2, 4, 6]
    # D = [3, 5, 7, 9, 11, 12, 13, 14, 15]
    # ans = median_of_two_sorted_arrays(C, D)
    # print(ans, "123489123491827340183740197")
    # assert ans == 7
    # print("CORRECT!!!!")
    # # ---------------------------------------
    # A = [1, 2]
    # B = [3, 4, 5]
    # ans = median_of_two_sorted_arrays(A, B)
    # assert ans == 3
    # ---------------------------------------
    # A = [1, 2, 3]
    # B = [3, 4, 5]
    # ans = median_of_two_sorted_arrays(A, B)
    # assert ans == 3
    # ---------------------------------------
    A = [1, 2, 3, 4]
    B = [5, 6, 7, 8]
    ans = median_of_two_sorted_arrays(A, B)
    print(ans)
    assert ans == 4.5
    # assert ans == 5.5
"""
3 + 4 // 2 = 3
m = 4
n = 9
half_len = 6
imin | imax | i | j
  0     4     2   4
  3     4     3   3
  4     4     4   2
"""
