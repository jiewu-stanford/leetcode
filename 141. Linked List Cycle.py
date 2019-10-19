'''
Title     : 141. Linked List Cycle
Problem   : https://leetcode.com/problems/linked-list-cycle/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
use fast/slow two-pointer strategy
Reference: https://leetcode.com/problems/linked-list-cycle/discuss/204183/Python-solution
'''
class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next: return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False