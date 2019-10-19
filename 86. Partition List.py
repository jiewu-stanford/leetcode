'''
Title     : 86. Partition List
Problem   : https://leetcode.com/problems/partition-list/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

''' Reference: https://leetcode.com/problems/partition-list/discuss/29174/Python-concise-solution-with-dummy-nodes '''
class Solution(object):
    def partition(self, head, x):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next   # concatenate List 1 and List 2
        return h1.next