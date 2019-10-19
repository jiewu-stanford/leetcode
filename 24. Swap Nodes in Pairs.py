'''
Title     : 24. Swap Nodes in Pairs
Problem   : https://leetcode.com/problems/swap-nodes-in-pairs/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
swap first -> second -> second.next to second -> first -> second.next, and then swap the next pair second.next -> second.next.next
Reference: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby
'''
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next, second.next, first.next = second, first, second.next
            curr = curr.next.next
        return dummy.next

''' recursive solution, ibid. '''
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        next_pair = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(next_pair)
        return head