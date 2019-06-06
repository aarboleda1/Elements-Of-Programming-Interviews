from test_framework import generic_test


"""11.1 Search a sorted array for first occurrence of k

A = [-14, 10, 2, 108, 108, 248, 285, 285, 285, 401]

Write a method that takes in a sorted array and a key and returns the index
of the first occurrence of that key in the array. Return -1 if the key does not
appear in the array. For example, when applied to array A in the example above
your algorithm should return 3 if the given key is 108; if it is 285, your
algorithm should return 6

[-14, 2, 108, 108, 248, 285, 285, 285, 401]

L = 2
R = 3
mid = 1
k = 108

# [ ATTEMPTED ] - 6/5, Solved, but didn't get optimal time complexity
- Hint, the O(N) is trivial, explain out loud how and why you can maintain
a log N solution
"""

def search_first_of_k(A, k):
    pass

if __name__ == "__main__":
    A = [-14, 2, 108, 108, 248, 285, 285, 285, 401]
    print(search_first_of_k(A, 285))
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
