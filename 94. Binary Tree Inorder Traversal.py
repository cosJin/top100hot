# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None: return []
        res+=self.inorderTraversal(root.left)
        res+=[root.val]
        res+=self.inorderTraversal(root.right)
        return res
a = Solution()
print(a.inorderTraversal())