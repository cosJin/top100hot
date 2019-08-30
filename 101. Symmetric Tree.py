# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        def helper(left,right):
            if left is None and right is None:return True
            elif left is not None and right is not None and left.val == right.val:
                return helper(left.right,right.left) and helper(left.left,right.right)
            else:return False
        return helper(root.left,root.right)
                