import functools
from collections import namedtuple
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Design an algorithm that takes a BST as input and returns a sorted doubly linked
list on the same elements
[ ATTEMPTED ] 5/14

"""


def bst_to_doubly_linked_list(tree):
    HeadTailNode = namedtuple('HeadTailNode', ('head', 'tail'))

    def bst_to_dll_helper(tree):
        if not tree:
            return HeadTailNode(None, None)

        left = bst_to_dll_helper(tree.left)
        right = bst_to_dll_helper(tree.right)
        print(left)
        if left.tail:
            left.tail.right = tree
        tree.left = left.tail

        tree.right = right.head
        if right.head:
            right.head.left = tree

        return HeadTailNode(left.head or tree, right.tail or tree)
    return bst_to_dll_helper(tree).head


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
