# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = root.val
        def dfs(node):  #用来返回以当前节点左右支路中最常路径，并且计算左右最大路径之和。
            if not node:return 0   # 函数中定义函数时，对于函数外的变量，函数内可以读取，但是不能改变其值。需要用self.来改变其值。
            leftmax = max(0,dfs(node.left))
            rightmax = max(0,dfs(node.right))
            self.maximum = max(self.maximum,rightmax+leftmax+node.val)
            return max(leftmax,rightmax) + node.val
        dfs(root)
        return self.maximum


        

