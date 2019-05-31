def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return output[::-1]
