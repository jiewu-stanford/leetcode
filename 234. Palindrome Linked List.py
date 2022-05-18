'''
Title     : 234. Palindrome Linked List
Problem   : https://leetcode.com/problems/palindrome-linked-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
without the O(1) space constraint, we can convert palindrome linked list checking to palindrome number checking
Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/64514/5-lines-Python-O(n)-time-and-space
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals += head.val,   # TRICK: int is mutable thus not iterable, use tuple instead 1 -> (1, )
            head = head.next
        return vals == vals[::-1]
'''
instead of converting to palindrome number checking we can convert it to palindrome node checking using deque(), albeit O(n) space is required
Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly)
'''
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = deque([])
        while head:
            queue.append(head.val)
            head = head.next
        while len(queue) >= 2:
            if queue.popleft() != queue.pop():
                return False
        return True
'''
O(1) time solution, use fast/slow two-pointer strategy to split the list into first half and second half, OK if first half is longer than second half
and then use the 206. solution to reverse the second half and compare it with the first half
Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/190622/Python-reverse-and-compare
Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/64771/One-Python-Solution
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next

        first, second = head, prev
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        return True