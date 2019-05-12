from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTSerializer:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def r_serialize(node):
            if node is None:
                return "None"
            else:
                L = r_serialize(node.left)
                R = r_serialize(node.right)
                return str(node.val) + "," + L + "," + R
        return r_serialize(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def r_deserialize(q):
            if q[0] == "None":
                q.popleft()
                return None
            root = TreeNode(q[0])
            q.popleft()
            root.left = r_deserialize(q)
            root.right = r_deserialize(q)
            return root

        return r_deserialize(deque(data.split(",")))

class BinaryTreeSerializerBFS:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        q = deque([root])
        ret = []
        while q:
            node = q.popleft()
            val = str(node.val) if node else 'X'
            ret.append(val)
            if node:
                q.append(node.left)
                q.append(node.right)
        return ",".join(ret)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = deque(data.split(","))
        root_node = TreeNode(int(nodes.popleft()))
        q = deque([root_node])
        while q:
            cur_node = q.popleft()
            cur_val = nodes.popleft()
            if cur_val != "X":
                cur_node.left = TreeNode(int(cur_val))
                q.append(cur_node.left)

            cur_val = nodes.popleft()
            if cur_val != "X":
                cur_node.right = TreeNode(int(cur_val))
                q.append(cur_node.right)

        return root_node
