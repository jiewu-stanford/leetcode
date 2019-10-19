'''
Title     : 206. Reverse Linked List
Problem   : https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
step-by-step iterative solution
Reference: https://www.youtube.com/watch?v=XwIivDg1BlY
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            # one-liner: prev, curr.next, curr = curr, prev, curr.next
        return prev
'''
recursive solution, without using helper function
Reference: https://leetcode.com/problems/reverse-linked-list/discuss/58338/Python-solution-Simple-Iterative
'''
class Solution:
    def reverseList(self, head: ListNode, prev: ListNode = None) -> ListNode:
        if not head: return prev
        curr = head.next
        head.next = prev
        return self.reverseList(curr, head)