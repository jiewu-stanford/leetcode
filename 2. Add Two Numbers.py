'''
Title     : 2. Add Two Numbers
Problem   : https://leetcode.com/problems/add-two-numbers/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
add as numbers by converting to number: list -> int -> sum -> list
Reference: https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toInt(node):
            return node.val + 10*toInt(node.next) if node else 0
        
        n = toInt(l1) + toInt(l2)
        head = curr = ListNode(n % 10)
        while n > 9:
            n //= 10
            curr.next = ListNode(n % 10)
            curr = curr.next   # one-liner: curr.next = curr = ListNode(n % 10)
        return head
'''
add two lists directly and iteratively
Reference: https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return dummy.next