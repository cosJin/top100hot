# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:return None
        if root.left is None and root.right is None:return TreeNode(root.val)
        elif root.left is None : 
            root.right = self.flatten(root.right)
            return root
        elif root.right is None : 
            root.right = self.flatten(root.left)
            root.left = None
            return root

        #left to link
        leftl = self.flatten(root.left)
        #right to link
        rightl = self.flatten(root.right)

        tail = leftl
        while tail.right is not None:
            tail = tail.right
        root.right = leftl
        root.left = None
        tail.right = rightl
        return root