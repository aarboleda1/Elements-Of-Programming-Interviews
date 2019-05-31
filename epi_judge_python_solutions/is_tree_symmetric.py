from test_framework import generic_test
"""9.1 Test if a binary tree is symmetric
The first thing to notice about this problem is what does it mean
to be a mirror?

We should then see there are two conditions where we can have a mirror
reflection

1. Two roots have the same value
2. The right subtree is a mirror reflection of the subtree

This leads us to the recursive solution, where we compare mirorring
subtrees

For the iterative solution, use a modified BFS. The trick here is to
place the root in the queue first. Why? Because we'll process mirroring nodes
first, extract two nodes at a time, check for equality then place the
mirroring child nodes in order in the queue

        3
  2           2
     1      1
place 3 and 3, because we've already stated we want to continue if two roots
are equal

deque 3 and 3

for 3 and 3, we need to process and make sure:
Left2.left == Right2.right AND Left2.right == Left2.left.

So, let's use the FIFO property of the queue and place in the children in that order
# these will be processed together
enque(node1.left)
enque(node2.right)

# these will be processed together
enque(node2.left)
enque(node1.right)
"""
# Iterative Solution
# O(N) time with O(N) space complexity
def is_symmetric(tree):
        if not tree:
            return True
        q = deque([tree, tree])
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.data != t2.data:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

# Recursive solution
# Time complexity : O(n). Because we traverse the entire input tree once,
# the total run time is O(n), where n is the total number of nodes in the tree.

# Space complexity: The number of recursive calls is bound by the height of the
# tree. In the worst case, the tree is linear and the height is in O(n).
# Therefore, space complexity due to recursive calls on the stack is O(n)
# in the worst case.
def is_symmetric(tree):
    def check_symmetric(t1, t2):
        if t1 is None and t2 is None:
            return True
        # one subtree is empty and the other is not
        if t1 is None or t2 is None:
            return False

        if t1.data != t2.data:
            return False

        return check_symmetric(t1.left, t2.right) and check_symmetric(t1.right, t2.left)

    return check_symmetric(tree, tree)
def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
