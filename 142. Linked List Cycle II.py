'''
Title     : 142. Linked List Cycle II
Problem   : https://leetcode.com/problems/linked-list-cycle-ii/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
again fast/slow two-pointer strategy: if fast pointer velocity is twice as slow pointer velocity then fast pointer displacement
is twice as slow pointer displacement, hence if fast pointer traverses m cycles and slow pointer traverses n cycles then m = 2n
Reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44902/Sharing-my-Python-solution
to find the start of the cycle requires a bit of math, the key is that if we let slow pointer start from beginning and slow down
fast pointer to the same speed then when they meet the second time they must meet at the start of the cycle, because
for fast pointer the total displacement is a multiple of full cycle: (H + nC + D) + (nC - D) = H + 2nC
Reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/258948/%2B-python
'''
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next: return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:   # while...else clause!
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow