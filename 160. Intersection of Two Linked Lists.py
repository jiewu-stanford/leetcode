'''
Title     : 160. Intersection of Two Linked Lists
Problem   : https://leetcode.com/problems/intersection-of-two-linked-lists/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
adapted from fast/slow two-pointer strategy, now we explore a strategy of two pointers traversing at equal velocity
idea: with equal velocity two pointers must traverse equal distance when they meet at the intersection (actually if and only if)
let len(A) = L1 + L and len(B) = L2 + L, the best candidate of such an equal distance is L1 + L + L2 = L2 + L + L1
Reference: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/249917/Python-Two-Pointers
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
'''
a generalization: suppose the two lists are allowed to touch each other at one single node instead of sharing a common segment, how to detect?
link up the two lists and convert the intersection detection into cycle detection so that we can apply the 142. solution
Reference: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        last = headA
        while last.next:
            last = last.next
        last.next = headB
        
        slow = fast = headA
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                last.next = None
                return slow
        else:
            last.next = None   # without this the OJ would produce 'linked structure was modified' arror
            return None