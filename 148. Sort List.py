'''
Title     : 148. Sort List
Problem   : https://leetcode.com/problems/sort-list/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
recursion with merge sort, use fast/slow two-pointer strategy to split the list into two halves and the 21. solution to merge, not constant space though
Reference: https://leetcode.com/problems/sort-list/discuss/46711/Python-merge-sort-with-comments
Reference (merge): https://leetcode.com/problems/sort-list/discuss/46808/My-Python-solution%3A-merge-sort
'''
class Solution(object):
    def sortList(self, head):
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None   # cut off between first and second half
        left = self.sortList(head)
        right = self.sortList(second)
        return self.merge(left, right)

    def merge(self, l1, l2):
        if None in (l1, l2): return l1 or l2
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next