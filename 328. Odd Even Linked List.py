'''
Title     : 328. Odd Even Linked List
Problem   : https://leetcode.com/problems/odd-even-linked-list/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

''' Reference: https://leetcode.com/problems/odd-even-linked-list/discuss/78123/Python-solution-with-two-pointers-O(N) '''
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next: return head
        odd, even = head, head.next
        evenhead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head