#! /usr/local/bin/python3.3
"""
Given a well formed binary tree, implement an iterator that iterates over
it in post-order fashion.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Iterator:
    def __init__(self, root):
        self.stack = []
        self.rightSubTreeProcessed = set()
        self.traverse_until_leaf(root)

    def traverse_until_leaf(self, node):
        if node is None:
            return
        self.stack.append(node)
        if node.left:
            self.traverse_until_leaf(node.left)
        elif node.right:
            self.rightSubTreeProcessed.add(node)
            self.traverse_until_leaf(node.right)

    def next(self):
        next_element = None
        if len(self.stack) == 0:
            return next_element

        top_element = self.stack[len(self.stack) - 1]
        if top_element in self.rightSubTreeProcessed:
            # Right sub-tree has been processed. No need to track this anymore
            self.rightSubTreeProcessed.remove(top_element)
        else:
            self.rightSubTreeProcessed.add(top_element)
            self.traverse_until_leaf(top_element.right)

        next_element = self.stack.pop()
        return next_element


## Create a tree for testing ##
root = Node(0)
l = Node(1)
r = Node(2)
ll = Node(3)
lr = Node(4)
rl = Node(5)
rr = Node(6)
lll = Node(7)
llr = Node(8)
rrl = Node(9)
rrr = Node(10)

root.left = l
root.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr
ll.left = lll
ll.right = llr
rr.left = rrl
rr.right = rrr

## Test it ##
my_iterator = Iterator(root)
while True:
    my_node = my_iterator.next()
    if my_node == None:
        break
    print(my_node.value, end="\n")


import string
import unittest
from collections import namedtuple


# -- Begin solution

Node = namedtuple("Node", ["d", "l", "r"])


class PostOrderIterator(object):
    def __init__(self, root):
        self._root = root
        self._stack = []

        if root:
            self._walk(root)

    def __iter__(self):
        return self

    def _walk(self, start_at):
        """Invariant: top of stack is always the next node"""
        n = start_at

        while n:
            self._stack.append(n)
            n = n.l if n.l else n.r

    def next(self):
        if not self._stack:
            raise StopIteration

        next_node = self._stack.pop()

        if self._stack and next_node == self._stack[-1].l and self._stack[-1].r:
            self._walk(self._stack[-1].r)

        return next_node


# -- End Solution


# Test utilities


def post_order_traversal(tree):
    return " ".join(str(x.d) for x in PostOrderIterator(tree))


def create_tree(structure):
    """Helper function to create trees
    Expects tuples of the form
    - (data, left, right) or
    - (data)
    """
    if not structure:
        return None

    if len(structure) == 1:
        return Node(structure, None, None)

    (d, l, r) = structure
    return Node(d, create_tree(l), create_tree(r))


class PostOrderIteratorTests(unittest.TestCase):
    def test_simple(self):
        """
                 A
                / \
               B   C
              / \ / \
             D   EF  G
        """
        tree = create_tree(("A", ("B", "D", "E"), ("C", "F", "G")))

        self.assertEquals("D E B F G C A", post_order_traversal(tree))

    def test_ladder(self):
        """
          A                A           A
           \              /           /
            B            B           B
             \          /             \
              C        C               C
        """
        right_tree = create_tree(("A", None, ("B", None, "C")))
        self.assertEquals("C B A", post_order_traversal(right_tree))

        left_tree = create_tree(("A", ("B", "C", None), None))
        self.assertEquals("C B A", post_order_traversal(left_tree))

        angle_tree = create_tree(("A", ("B", None, "C"), None))
        self.assertEquals("C B A", post_order_traversal(left_tree))

    def test_empty(self):
        """ """
        self.assertEquals("", post_order_traversal(None))


if __name__ == "__main__":
    unittest.main()
