'''
Title     : 369. Plus One Linked List ($$$)
Problem   : https://leetcode.com/problems/plus-one-linked-list/
          : https://www.lintcode.com/problem/plus-one-linked-list/description
'''
# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
'''
straightforward step-by-step iterative solution
Reference: https://www.cnblogs.com/lightwindy/p/9649781.html
'''
class Solution:
    def plusOne(self, head):
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr.next:
            if curr.val != 9: prev = curr   # prev stops at the node to absorb the carry
            curr = curr.next
        
        if curr.val != 9:   # the end node
            curr.val += 1
        else:
            prev.val += 1
            curr = prev.next
            while curr:
                curr.val = 0
                curr = curr.next
                
        return dummy if dummy.val else dummy.next   # dummy becomes a valid node once it absorbs the carry

''' use the 206. solution to reverse the list so that carrying over is in the same direction of the link pointer, ibid. '''
class Solution:
    def plusOne(self, head):
        if not head: return None
        rev_head = self.reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:
            curr.val += carry
            carry = curr.val // 10
            curr.val %= 10
            if carry and not curr.next:
                curr.next = ListNode(0)   # create the head node first, assign val = 1 in the next while loop iteration
            curr = curr.next
        return self.reverseList(rev_head)
        
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        return prev