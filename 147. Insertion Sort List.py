'''
Title     : 147. Insertion Sort List
Problem   : https://leetcode.com/problems/insertion-sort-list/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

''' Reference: https://leetcode.com/problems/insertion-sort-list/discuss/190913/Java-Python-with-Explanations '''
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val > head.next.val:
                curr = head.next
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                head.next = curr.next   # FROM: prev -> head -> curr -> ...
                curr.next = prev.next   # TO:   prev -> curr -> head -> ...
                prev.next = curr
            else:
                head = head.next
        return dummy.next