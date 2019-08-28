# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root,m,n):
            if root == None:return True
            elif m < root.val < n and helper(root.left,m,root.val) and helper(root.right,root.val,n):return True
            else:return False
        return helper(root,float("-inf"),float("inf"))
