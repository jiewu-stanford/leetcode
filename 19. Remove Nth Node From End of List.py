'''
Title     : 19. Remove Nth Node From End of List
Problem   : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
use two pointers separated by n nodes, when the fast points to the end then the slow points to the nth node from end
Reference: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/9032/Python-concise-one-pass-solution-with-dummy-head
Reference: https://buptwc.com/2018/11/13/Leetcode-19-Remove-Nth-Node-From-End-of-List/
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next