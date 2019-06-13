"""
a) recursively reverse a string.
b) print a number vertically with each digit on its own line, without converting to a string.
c) remove all prime numbers from a linked list.
i   char  alist
0    a     [cb] + [a]
1    b     [c] + [b]
2    c      [c] + []
3            []
"""

# a
def recur(s, idx, alist):
    if idx == len(s):
        return alist
    return recur(s, idx + 1, alist) + [s[idx]]
def reverse(s):
    alist = recur(s, 0, [])
    return "".join(alist)

"""
21

n = 32
nums = [1]

n = 3
nums = [1,2]

n = 0
nums = [1,2,3]
3
2
1
"""
# b
def print_num_vertically(n):
    n = abs(n)
    nums = []
    while n > 0:
        rem = n % 10
        nums.append(rem)
        n = n // 10

    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])

if __name__ == "__main__":
    print(reverse("abc"), "cba")
    print(reverse("cat"), "tac")
    print(reverse("asdfghjkl;"), ";lkjhgfdsa")
    print_num_vertically(321)
    print("-----")
    print_num_vertically(123)
