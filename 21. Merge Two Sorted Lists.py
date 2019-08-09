# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = now = ListNode(0)
        while l1 is not None or l2 is not None:
            if l1 is None:
                now.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                now.next = ListNode(l1.val)
                l1 = l1.next
            else:
                now.next = ListNode(min(l1.val,l2.val))
                if l1.val <= l2.val:
                    l1 = l1.next
                elif l1.val > l2.val:
                    l2 = l2.next
            now = now.next
        return head.next
