from test_framework import generic_test


"""13.1 Compute the intersection of two sorted arrays

Write a program which takes as input two sorted arrays, and returns
a new array containing elements that are present in both of the input
arrays. The input arrays may have duplicate entries, but the returned
array should be free of duplicates. For example, the input is
[2,3,3,5,5,6,7,7,8,12] and [5,5,6,8,8,9,10,10], your input should be
[5,6,8]

[ SOLVED ] 6/3
"""
def intersect_two_sorted_arrays(A, B):
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else: # equal
            if not res or B[j] != res[-1]:
                res.append(B[j])
            j += 1
            i += 1
    return res

if __name__ == '__main__':
    print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]))
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
