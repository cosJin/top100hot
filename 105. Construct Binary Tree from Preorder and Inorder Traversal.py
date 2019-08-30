# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        head = TreeNode(preorder[0])

        newinorder_left = inorder[:inorder.index(preorder[0])]
        newpreorder_left = preorder[1:1+len(newinorder_left)]

        newinorder_right = inorder[inorder.index(preorder[0])+1:]
        newpreorder_right = preorder[1+len(newinorder_right):]

        head.left = self.buildTree(newpreorder_left,newinorder_left)
        head.right = self.buildTree(newpreorder_right,newinorder_right)

        return head

        
        