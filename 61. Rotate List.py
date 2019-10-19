'''
Title     : 61. Rotate List
Problem   : https://leetcode.com/problems/rotate-list/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
again two-pointer strategy, separate fast and slow pointer by k, use % length to handle k > length
Reference: https://leetcode.com/problems/rotate-list/discuss/22889/An-iterative-Python-solution-O(2n)-89ms
'''
class Solution(object):
    def rotateRight(self, head, k):
        if not head or k==0: return head
        slow = fast = head
        length = 0
        while fast:
            fast = fast.next
            length += 1
            
        k %= length
        fast = head
        while k:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head   # concatenate two segments
        head = slow.next
        slow.next = None
        
        return head