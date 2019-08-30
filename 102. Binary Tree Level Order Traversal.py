# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:return []
        now,nxt = [root],[]
        res = [] 
        while now != []:
            res.append([])
            for node in now:
                res[-1].append(node.val)
                if node.left is not None:nxt.append(node.left)
                if node.right is not None:nxt.append(node.right)
            now = nxt[:]
            nxt = []
        return res
