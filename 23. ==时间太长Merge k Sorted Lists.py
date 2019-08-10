# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#该方法是两两合并，很慢
#另外讲所有头结点存在一起，从中找最小的，然后更新头节点。可以用heapq实现。
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        num = len(lists)
        if num == 0:return None
        while num > 1:
            lists.append(self.merge(lists.pop(0),lists.pop(0)))
            num -= 1
        return lists[0]

    def merge(self,list1,list2):
        if list1 is None and list2 is None:return None
        head = now = ListNode(0)
        while list1 is not None or list2 is not None:
            if list1 is None:
                now.next = ListNode(list2.val)
                now = now.next
                list2 = list2.next
            elif list2 is None:
                now.next = ListNode(list1.val)
                now = now.next
                list1 = list1.next
            else:
                now.next = ListNode(min(list1.val,list2.val))
                now = now.next
                if list1.val <= list2.val:
                    list1 = list1.next
                elif list1.val > list2.val:
                    list2 = list2.next
        return head.next


                

