'''
Title     : 25. Reverse Nodes in k-Group
Problem   : https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
recursive solution, adapt the 206. solution to reverse the k-group
Reference: https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/172576/Python-or-Follow-up-of-LC206
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1: return head
        count, curr = 0, head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k: return head   # list shorter than k
        rem_head, prev = self.reverseList(head, k)
        head.next = self.reverseKGroup(rem_head, k)   # recursive function produces prev -> ... -> head
        return prev
    
    def reverseList(self, head, count):
        prev = None
        curr = head
        while count > 0:
            prev, curr.next, curr = curr, prev, curr.next
            count -= 1
        return (curr, prev)
'''
iterative solution
Reference: https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1: return head
        dummy = next_head = ListNode(None)
        dummy.next = head
        prev = curr = head

        while True:
            count = 0
            while curr and count < k:
                count += 1
                curr = curr.next
            if count == k:
                h, t = curr, prev   # assign the first node of next k-group and the first node of current k-group to h(ead), t(ail)
                for _ in range(k):   # note that this is NOT a standard reversing by swapping arrows between adjacent nodes
                    tmp = t.next     # instead it poplefts the nodes of current k-group successively: t, t.next, t.next.next, ... (ref. Campanula's comment)
                    t.next = h
                    h = t
                    t = tmp
                    # one-liner: t.next, t, h = h, t.next, t
                next_head.next = h   # connect the last node of the previous reversed k-group to the head of the current reversed k-group
                next_head = prev     # after reversal the first node of current k-group becomes the last node of the group, to be connected to the next k-group
                prev = curr   # head of the next yet to be reversed k-group
            else:
                return dummy.next