import functools
from collections import namedtuple
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
24.21
Design an algorithm that takes a BST as input and returns a sorted doubly
linked-list on the same elements
[ ATTEMPTED ] - 5/14
[ ATTEMPTED ] - 5/16

Time Complexity: We do a constant amount of work per tree node, so the time
complexity is O(N).

Space Complexity: O(h) where h is the height of the BST. The worst case for
height is where the height is N number of nodes
"""


def bst_to_doubly_linked_list(tree):
    HeadAndTail = namedtuple('HeadAndTail', ('head', 'tail'))

    def recur(root):
        if not root:
            return HeadAndTail(None, None)

        # Recursively build left and right lists
        left = recur(root.left)
        right = recur(root.right)

        # Root to left and right lists
        root.left = left.tail
        root.right = right.head

        # Left and right lists to root
        if left.tail:
            left.tail.right = root
        if right.head:
            right.head.left = root

        return HeadAndTail(left.head or root, right.tail or root)
    return recur(tree).head

@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_to_sorted_list.py",
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
