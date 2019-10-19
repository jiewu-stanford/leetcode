'''
Title     : 82. Remove Duplicates from Sorted List II
Problem   : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = prev = ListNode(None)
        curr.next = head   # also need to check head.val thus cannot let curr = head
        dummy = curr
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next