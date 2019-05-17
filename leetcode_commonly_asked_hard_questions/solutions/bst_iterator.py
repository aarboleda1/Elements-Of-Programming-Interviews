# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.traverseLeft(root)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.hasNext():
            return

        cur = self.stack.pop()
        if cur.right:
            self.traverseLeft(cur.right)
        return cur.val

    def traverseLeft(self, root):
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack
