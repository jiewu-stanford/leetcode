'''
Title     : 143. Reorder List
Problem   : https://leetcode.com/problems/reorder-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
directly adapting the 234. solution, instead of comparing the first half with the reversed second half, interlace them
Reference: https://leetcode.com/problems/reorder-list/discuss/45127/Python-solution
'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return None
        fast = slow = head
        while fast.next and fast.next.next:   # vs. while fast and fast.next in the 234. solution to ensure first half nodes is at least as many as second half nodes
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next

        first, second = head, prev
        while first and second:
            next1, next2 = first.next, second.next
            first.next, second.next = second, next1
            first, second = next1, next2