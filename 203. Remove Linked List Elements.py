'''
Title     : 203. Remove Linked List Elements
Problem   : https://leetcode.com/problems/remove-linked-list-elements/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = ListNode(None)
        curr.next = head
        dummy = curr
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next