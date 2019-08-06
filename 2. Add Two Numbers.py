# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = now = ListNode(0)
        tag = 0
        while l1 is not None or l2 is not None:
            if l1 is None: 
                sum = l2.val + tag
                l2 = l2.next
            elif l2 is None: 
                sum = l1.val + tag
                l1 = l1.next
            else: 
                sum = l1.val + l2.val + tag
                l1, l2 = l1.next, l2.next
            tag = int(sum / 10)
            sum = int(sum % 10)
            t = ListNode(sum)
            now.next = t
            now = t
        if tag == 1:
            now.next = ListNode(1)
        return head.next
            

