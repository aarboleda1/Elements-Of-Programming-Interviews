"""
Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

HISTORY LOG
- [ SOLVED ] 5/17
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):


    def next(self) -> int:
        """
        @return the next smallest number
        """


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
