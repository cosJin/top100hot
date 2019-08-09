# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #有两种方法：
        #方法一：两趟法：第一趟直到有多少个元素，第二趟删除
        #方法二：双指针一趟法：前指针在后指针的前n处
        h = back = ListNode(0)
        h.next = before = back.next = head
        while n-1 != 0:
            before = before.next
            n -= 1
        while before.next is not None:
            before, back = before.next, back.next
        back.next = back.next.next
        return h.next
        

        
        
