import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Intution:
    1. Recursively build linked lists from the left and right subtrees.
    2. Append the current tree to the list from the left subtree
    3. Append the list from the right subtree to the current subtree
    4. Return a new linked list TUPLE
- [ ATTEMPTED ] 5/14
- [ ATTEMPTED ] 5/16
"""

def bst_to_doubly_linked_list_V2(tree):
    HeadAndTail = collections.namedtuple('HeadAndTail', ('head', 'tail'))

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

def bst_to_doubly_linked_list(tree):

    HeadAndTail = collections.namedtuple('HeadAndTail', ('head', 'tail'))

    # Transforms a BST into a sorted doubly linked list in-place,
    # and return the head and tail of the list.
    def bst_to_doubly_linked_list_helper(tree):
        # Empty subtree.
        if not tree:
            return HeadAndTail(None, None)

        # Recursively builds the list from left and right subtrees.
        left = bst_to_doubly_linked_list_helper(tree.left)
        right = bst_to_doubly_linked_list_helper(tree.right)

        # Appends tree to the list from left subtree.
        if left.tail:
            left.tail.right = tree
        tree.left = left.tail

        # Appends the list from right subtree to tree.
        tree.right = right.head
        if right.head:
            right.head.left = tree

        return HeadAndTail(left.head or tree, right.tail or tree)

    return bst_to_doubly_linked_list_helper(tree).head


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
