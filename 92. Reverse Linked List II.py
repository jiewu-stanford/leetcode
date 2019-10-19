'''
Title     : 92. Reverse Linked List II
Problem   : https://leetcode.com/problems/reverse-linked-list-ii/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
use the same one-liner from the 206. solution to reverse the segment, then connect it with the unreversed parts
Reference: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
Reference: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30681/Python-one-pass-concise-solution-with-comments
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        pre = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        curr, prev = pre.next, None
        for _ in range(n - m + 1):
            prev, curr.next, curr = curr, prev, curr.next
        pre.next.next = curr   # the reversed part reads: prev -> ... -> pre.next, to be connected with the unreversed parts head -> ... -> pre, curr -> ... -> tail
        pre.next = prev
        return dummy.next